import json
import os
import subprocess
from pathlib import Path
from .base import BaseStep, CheckResult
from .. import ui
from ..i18n.loader import t


def run_interactive(cmd: str) -> bool:
    """執行互動式 shell 指令（允許使用者在終端輸入）"""
    ui.print_command(cmd)
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0


def run_silent(cmd: str) -> tuple[int, str]:
    """靜默執行指令，回傳 (returncode, stdout)"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout.strip()


class GeminiCliVertexAuthStep(BaseStep):
    description = "step.gemini_cli_vertex_auth.desc"

    def run(self) -> bool:
        persist_to = self.params.get("persist_to", "~/.gemini/.env")
        location_default = self.params.get("location_default", "us-central1")
        check_conflicting = self.params.get("check_conflicting_keys", True)

        # 嘗試抓取目前的 gcloud project 作為預設值
        code, current_project = run_silent("gcloud config get-value project 2>/dev/null")
        project_default = current_project if (code == 0 and current_project and current_project != "(unset)") else ""

        project = ui.ask(t("run.gemini.ask_project"), default=project_default)
        if not project:
            ui.print_error(t("run.gemini.project_empty"))
            return False

        location = ui.ask(t("run.gemini.ask_location"), default=location_default)

        if check_conflicting:
            conflicting = [k for k in ["GOOGLE_API_KEY", "GEMINI_API_KEY"] if os.environ.get(k)]
            if conflicting:
                ui.print_warning(t("run.gemini.conflict_keys", keys=", ".join(conflicting)))
                ui.print_warning(t("run.gemini.conflict_detail"))
                if not ui.confirm(t("run.gemini.conflict_confirm")):
                    ui.print_warning(t("run.gemini.cancelled"))
                    return False

        env_path = Path(persist_to).expanduser()
        env_path.parent.mkdir(parents=True, exist_ok=True)

        existing_lines = []
        if env_path.exists():
            with open(env_path) as f:
                existing_lines = f.readlines()

        keys_to_set = {
            "GOOGLE_CLOUD_PROJECT": project,
            "GOOGLE_CLOUD_LOCATION": location,
        }
        new_lines = []
        written_keys: set[str] = set()

        for line in existing_lines:
            stripped = line.strip()
            replaced = False
            for key, value in keys_to_set.items():
                if stripped.startswith(f"{key}=") or stripped.startswith(f"export {key}="):
                    new_lines.append(f'{key}="{value}"\n')
                    written_keys.add(key)
                    replaced = True
                    break
            if not replaced:
                new_lines.append(line)

        for key, value in keys_to_set.items():
            if key not in written_keys:
                new_lines.append(f'{key}="{value}"\n')

        with open(env_path, "w") as f:
            f.writelines(new_lines)

        ui.print_success(t("run.gemini.written", path=env_path))
        ui.print_info(f"GOOGLE_CLOUD_PROJECT = {project}")
        ui.print_info(f"GOOGLE_CLOUD_LOCATION = {location}")

        return run_interactive("gcloud auth application-default login")

    def verify(self) -> list[CheckResult]:
        persist_to = self.params.get("persist_to", "~/.gemini/.env")
        results = []

        env_path = Path(persist_to).expanduser()
        if not env_path.exists():
            results.append(CheckResult(False, t("verify.gemini.env_not_found", path=persist_to)))
            return results
        results.append(CheckResult(True, t("verify.gemini.env_exists", path=persist_to)))

        env_vars: dict[str, str] = {}
        with open(env_path) as f:
            for line in f:
                line = line.strip().removeprefix("export").strip()
                if "=" in line and not line.startswith("#"):
                    k, _, v = line.partition("=")
                    env_vars[k.strip()] = v.strip().strip('"').strip("'")

        project = env_vars.get("GOOGLE_CLOUD_PROJECT", "")
        results.append(CheckResult(bool(project),
            t("verify.gemini.project_set") if project else t("verify.gemini.project_not_set"),
            detail=project,
        ))

        location = env_vars.get("GOOGLE_CLOUD_LOCATION", "")
        results.append(CheckResult(bool(location),
            t("verify.gemini.location_set") if location else t("verify.gemini.location_not_set"),
            detail=location,
        ))

        # 優先檢查 GOOGLE_APPLICATION_CREDENTIALS 環境變數
        adc_env = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
        if adc_env and Path(adc_env).exists():
            results.append(CheckResult(True, t("verify.gemini.adc_exists"), detail=adc_env))
        else:
            # 檢查清單：gcloud 回報的路徑、標準家目錄路徑
            possible_paths = []
            
            # 1. 使用 gcloud info 獲取配置目錄
            code, config_dir = run_silent('gcloud info --format="value(config.paths.global_config_dir)" 2>/dev/null')
            if code == 0 and config_dir:
                possible_paths.append(Path(config_dir) / "application_default_credentials.json")
            
            # 2. 標準家目錄路徑 (Fallback)
            possible_paths.append(Path("~/.config/gcloud/application_default_credentials.json").expanduser())

            # 找出第一個存在的路徑
            found_path = next((p for p in possible_paths if p.exists()), None)

            results.append(CheckResult(found_path is not None,
                t("verify.gemini.adc_exists") if found_path else t("verify.gemini.adc_not_found"),
                detail=str(found_path) if found_path else ""
            ))

        return results


class GCloudAuthStep(BaseStep):
    description = "step.gcloud_auth.desc"

    def run(self) -> bool:
        require_project = self.params.get("require_project", False)

        project = None
        if require_project:
            project = ui.ask(t("run.gcloud_auth.ask_project"))
            if not project:
                ui.print_error(t("run.gcloud_auth.project_empty"))
                return False

        if not run_interactive("gcloud auth login"):
            return False

        if not run_interactive("gcloud auth application-default login"):
            return False

        if project:
            ui.print_info(t("run.gcloud_auth.set_project", project=project))
            if not run_interactive(f"gcloud config set project {project}"):
                return False

        return True

    def verify(self) -> list[CheckResult]:
        results = []

        code, account = run_silent(
            'gcloud auth list --filter=status:ACTIVE --format="value(account)" 2>/dev/null'
        )
        results.append(CheckResult(code == 0 and bool(account),
            t("verify.gcloud_auth.logged_in") if (code == 0 and account) else t("verify.gcloud_auth.not_logged_in"),
            detail=account if account else "",
        ))

        if self.params.get("require_project"):
            code, project = run_silent("gcloud config get-value project 2>/dev/null")
            is_set = code == 0 and project and project != "(unset)"
            results.append(CheckResult(bool(is_set),
                t("verify.gcloud_auth.project_set") if is_set else t("verify.gcloud_auth.project_not_set"),
                detail=project if is_set else "",
            ))

        return results


class GCloudEnableApisStep(BaseStep):
    description = "step.gcloud_enable_apis.desc"

    def run(self) -> bool:
        apis = self.params.get("apis", [])
        if not apis:
            ui.print_warning(t("run.apis.none"))
            return True

        for api in apis:
            ui.print_info(api)

        return run_interactive("gcloud services enable " + " ".join(apis))

    def verify(self) -> list[CheckResult]:
        apis = self.params.get("apis", [])
        if not apis:
            return [CheckResult(True, t("verify.apis.none_specified"))]

        results = []
        for api in apis:
            code, output = run_silent(
                f'gcloud services list --enabled --filter="name:{api}" --format="value(name)" 2>/dev/null'
            )
            if code == 0 and api in output:
                results.append(CheckResult(True, t("verify.apis.enabled", api=api)))
            elif code != 0:
                results.append(CheckResult(False, t("verify.apis.query_failed", api=api)))
            else:
                results.append(CheckResult(False, t("verify.apis.not_enabled", api=api)))

        return results


class GcpBillingCreditStep(BaseStep):
    description = "step.gcp_billing_credit.desc"

    def run(self) -> bool:
        ui.print_info(t("run.billing.manual_info"))
        ui.print_info(t("run.billing.manual_link_label"))
        ui.print_info("https://console.cloud.google.com/billing/redeem")
        return True

    def verify(self) -> list[CheckResult]:
        project_id = self.params.get("project_id", "")
        results = []

        if not project_id:
            code, project_id = run_silent("gcloud config get-value project 2>/dev/null")
            if code != 0 or not project_id or project_id == "(unset)":
                results.append(CheckResult(False, t("verify.billing.no_project_id")))
                return results

        results.append(CheckResult(True, t("verify.billing.project"), detail=project_id))

        code, billing_json = run_silent(
            f"gcloud billing projects describe {project_id} --format=json 2>/dev/null"
        )
        if code != 0 or not billing_json:
            results.append(CheckResult(False, t("verify.billing.query_failed")))
            return results

        try:
            billing_data = json.loads(billing_json)
        except json.JSONDecodeError:
            results.append(CheckResult(False, t("verify.billing.response_error")))
            return results

        if not billing_data.get("billingEnabled"):
            results.append(CheckResult(False, t("verify.billing.not_enabled")))
            return results

        billing_account_name = billing_data.get("billingAccountName", "")
        billing_account_id = billing_account_name.replace("billingAccounts/", "")
        results.append(CheckResult(True, t("verify.billing.enabled"), detail=billing_account_id))

        code, account_json = run_silent(
            f"gcloud billing accounts describe {billing_account_id} --format=json 2>/dev/null"
        )
        if code == 0 and account_json:
            try:
                account_data = json.loads(account_json)
                display_name = account_data.get("displayName", "")
                is_open = account_data.get("open", False)
                results.append(CheckResult(bool(is_open),
                    t("verify.billing.account_active") if is_open else t("verify.billing.account_inactive"),
                    detail=display_name,
                ))
            except json.JSONDecodeError:
                pass

        console_url = f"https://console.cloud.google.com/billing/{billing_account_id}/credits"
        results.append(CheckResult(None, t("verify.billing.manual_check"), detail=console_url))

        return results

import subprocess
import sys
from pathlib import Path
from .base import BaseStep, CheckResult
from .. import ui
from ..i18n.loader import t


class PythonVenvStep(BaseStep):
    description = "step.python_venv.desc"

    def run(self) -> bool:
        venv_dir = self.params.get("venv_dir", ".venv")
        requirements = self.params.get("requirements_file", "requirements.txt")

        if Path(venv_dir).exists():
            ui.print_warning(t("run.venv.already_exists", venv_dir=venv_dir))
        else:
            ui.print_command(f"python3 -m venv {venv_dir}")
            result = subprocess.run([sys.executable, "-m", "venv", venv_dir])
            if result.returncode != 0:
                ui.print_error(t("run.venv.create_failed"))
                return False
            ui.print_success(t("run.venv.created", venv_dir=venv_dir))

        if not Path(requirements).exists():
            ui.print_error(t("run.venv.requirements_not_found", requirements=requirements))
            return False

        pip = str(Path(venv_dir) / "bin" / "pip")
        ui.print_command("pip install --upgrade pip")
        subprocess.run([pip, "install", "--upgrade", "pip", "-q"])

        ui.print_command(f"pip install -r {requirements}")
        result = subprocess.run([pip, "install", "-r", requirements])

        if result.returncode == 0:
            ui.print_success(t("run.venv.install_complete"))
        return result.returncode == 0

    def verify(self) -> list[CheckResult]:
        venv_dir = self.params.get("venv_dir", ".venv")
        requirements = self.params.get("requirements_file", "requirements.txt")
        results = []

        venv_path = Path(venv_dir)
        pip_path = venv_path / "bin" / "pip"

        if not venv_path.exists():
            results.append(CheckResult(False, t("verify.venv.not_found", venv_dir=venv_dir)))
            return results
        results.append(CheckResult(True, t("verify.venv.exists", venv_dir=venv_dir)))

        if not pip_path.exists():
            results.append(CheckResult(False, t("verify.venv.pip_not_found", pip_path=pip_path)))
            return results

        if not Path(requirements).exists():
            results.append(CheckResult(False, t("verify.venv.requirements_not_found", requirements=requirements)))
            return results

        result = subprocess.run([str(pip_path), "check"], capture_output=True, text=True)
        if result.returncode == 0:
            results.append(CheckResult(True, t("verify.venv.pip_check_passed")))
        else:
            results.append(CheckResult(False, t("verify.venv.pip_check_failed"), detail=result.stdout.strip()))

        return results

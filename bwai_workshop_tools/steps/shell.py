import subprocess
from .base import BaseStep, CheckResult
from .. import ui
from ..i18n.loader import t


class ShellStep(BaseStep):
    description = "step.shell.desc"

    def run(self) -> bool:
        command = self.params.get("command", "")
        if not command:
            ui.print_error(t("run.shell.no_command"))
            return False

        ui.print_command(command)
        result = subprocess.run(command, shell=True)

        if result.returncode == 0:
            ui.print_success(t("run.shell.complete"))
        else:
            ui.print_error(t("run.shell.failed", code=result.returncode))
        return result.returncode == 0

    def verify(self) -> list[CheckResult]:
        verify_cmd = self.params.get("verify_command", "")
        if not verify_cmd:
            return [CheckResult(None, t("verify.shell.no_command"))]

        result = subprocess.run(verify_cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return [CheckResult(True, t("verify.shell.passed"), detail=result.stdout.strip())]
        else:
            return [CheckResult(False, t("verify.shell.failed"), detail=result.stderr.strip() or result.stdout.strip())]

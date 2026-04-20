from ..i18n.loader import t


class CheckResult:
    def __init__(self, ok: bool, message: str, detail: str = ""):
        self.ok = ok
        self.message = message
        self.detail = detail


class BaseStep:
    description = ""

    def __init__(self, step_config: dict):
        self.id = step_config.get("id", "unknown")
        self.step_description = step_config.get("description", "")
        self.params = step_config.get("params", {})

    @classmethod
    def get_description(cls) -> str:
        return t(f"step.{cls.__name__.replace('Step', '').lower()}.desc") or cls.description

    def run(self) -> bool:
        raise NotImplementedError

    def verify(self) -> list[CheckResult]:
        return [CheckResult(ok=None, message=t("step.base.no_verify"))]

import json
from pathlib import Path
from rich.rule import Rule
from .steps.registry import REGISTRY
from . import ui
from .i18n.loader import t


class Runner:
    def __init__(self, step_file: str):
        path = Path(step_file)
        if not path.exists():
            ui.print_error(t("runner.file_not_found") + step_file)
            raise SystemExit(1)
        with open(path) as f:
            self.config = json.load(f)
        self.steps = self.config.get("steps", [])

    def run(self, only_ids: list[str] | None = None, dry_run: bool = False):
        name = self.config.get("name", "")
        desc = self.config.get("description", "")

        ui.print_header(name, desc)

        steps_to_run = self.steps
        if only_ids:
            steps_to_run = [s for s in self.steps if s["id"] in only_ids]

        total = len(steps_to_run)

        for idx, step_config in enumerate(steps_to_run, 1):
            step_type = step_config.get("type")
            step_id = step_config.get("id", "unknown")
            description = step_config.get("description", step_id)
            params = step_config.get("params", {})

            ui.print_step_header(idx, total, description)
            ui.print_step_info(step_type, step_id, params)

            if step_type not in REGISTRY:
                ui.print_error(t("runner.unknown_type") + step_type)
                ui.print_info(t("runner.available_types") + ", ".join(REGISTRY.keys()))
                raise SystemExit(1)

            if dry_run:
                ui.print_warning(t("runner.dry_run_skip"))
                continue

            if not ui.confirm_step():
                ui.print_warning(t("runner.step_skipped"))
                continue

            step_cls = REGISTRY[step_type]
            step = step_cls(step_config)
            success = step.run()

            if success:
                ui.print_success(t("runner.step_completed"))
            else:
                ui.print_error(t("runner.step_failed"))
                raise SystemExit(1)

        ui.console.print()
        ui.console.print(Rule(style="cyan"))

        if not dry_run:
            ui.console.print(f"\n[bold green]  {t('runner.all_done')}[/bold green]\n")
        else:
            ui.console.print(f"\n[yellow]  {t('runner.dry_run_done', total=total)}[/yellow]\n")

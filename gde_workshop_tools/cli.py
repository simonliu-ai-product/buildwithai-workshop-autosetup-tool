import json
import sys
from pathlib import Path
import click
from rich.rule import Rule
from rich.table import Table
from .steps.registry import REGISTRY
from .runner import Runner
from . import ui
from .i18n.loader import t, get_language, set_language, SUPPORTED_LANGUAGES


@click.group()
@click.version_option()
def main():
    """GDE Workshop 通用環境設定 CLI 工具"""
    pass


@main.command()
@click.option("--step", required=True, help="步驟設定檔路徑 (JSON)")
@click.option("--only", default=None, help="只執行指定的步驟 ID，多個用逗號分隔")
@click.option("--dry-run", is_flag=True, help="列出所有步驟但不實際執行")
def setup(step, only, dry_run):
    """依照步驟設定檔執行環境設定"""
    runner = Runner(step)
    only_ids = [s.strip() for s in only.split(",")] if only else None
    runner.run(only_ids=only_ids, dry_run=dry_run)


@main.command()
@click.option("--step", required=True, help="步驟設定檔路徑 (JSON)")
@click.option("--only", default=None, help="只驗證指定的步驟 ID，多個用逗號分隔")
def verify(step, only):
    """驗證步驟設定檔中的每個步驟是否已正確完成"""
    path = Path(step)
    if not path.exists():
        ui.print_error(t("cli.verify.file_not_found") + step)
        raise SystemExit(1)

    with open(path) as f:
        config = json.load(f)

    name = config.get("name", "")
    desc = config.get("description", "")
    steps_config = config.get("steps", [])

    ui.print_header(name, desc)

    only_ids = [s.strip() for s in only.split(",")] if only else None
    if only_ids:
        steps_config = [s for s in steps_config if s["id"] in only_ids]

    total = len(steps_config)
    all_passed = True
    manual_checks = []

    for idx, step_config in enumerate(steps_config, 1):
        step_type = step_config.get("type")
        step_id = step_config.get("id", "unknown")
        description = step_config.get("description", step_id)

        ui.print_step_header(idx, total, description)

        if step_type not in REGISTRY:
            ui.print_error(t("runner.unknown_type") + step_type)
            all_passed = False
            continue

        step_obj = REGISTRY[step_type](step_config)
        results = step_obj.verify()

        auto_results = [r for r in results if r.ok is not None]
        manual_results = [(description, r) for r in results if r.ok is None]
        manual_checks.extend(manual_results)

        step_ok = ui.print_verify_results(auto_results)
        if not step_ok:
            all_passed = False

    ui.console.print()
    ui.console.print(Rule(style="cyan"))

    if manual_checks:
        ui.console.print(f"\n[bold yellow]  {t('cli.verify.manual_header')}[/bold yellow]\n")
        ui.print_manual_checks(manual_checks)

    if all_passed:
        ui.console.print(f"\n[bold green]  {t('cli.verify.all_passed')}[/bold green]\n")
    else:
        ui.console.print(f"\n[bold red]  {t('cli.verify.failed')}[/bold red]\n")
        sys.exit(1)


# ── Language commands ──────────────────────────────────────────────────────────

@main.group()
def language():
    """語言設定相關指令"""
    pass


@language.command("list")
def language_list():
    """列出所有支援的語言"""
    current = get_language()

    table = Table(
        title=t("lang.list_title"),
        show_header=True,
        header_style="bold cyan",
    )
    table.add_column(t("lang.col_code"), style="cyan", no_wrap=True)
    table.add_column(t("lang.col_name"))
    table.add_column(t("lang.col_current"))

    for code, name in SUPPORTED_LANGUAGES.items():
        marker = t("lang.current_marker") if code == current else ""
        table.add_row(code, name, marker)

    ui.console.print(table)


@language.command("set")
@click.argument("lang")
def language_set(lang: str):
    """設定語言（例如：en、ja、ko、zh-tw）"""
    if lang not in SUPPORTED_LANGUAGES:
        ui.print_error(t("lang.invalid", lang=lang))
        ui.print_info(t("lang.supported", supported=", ".join(SUPPORTED_LANGUAGES.keys())))
        sys.exit(1)

    set_language(lang)
    name = SUPPORTED_LANGUAGES[lang]
    ui.print_success(t("lang.set_success", lang=lang, name=name))


@language.command("show")
def language_show():
    """顯示目前的語言設定"""
    current = get_language()
    name = SUPPORTED_LANGUAGES.get(current, current)
    ui.print_info(t("lang.current", lang=current, name=name))


# ── Steps commands ─────────────────────────────────────────────────────────────

@main.group()
def steps():
    """步驟相關指令"""
    pass


@steps.command("list")
def steps_list():
    """列出所有支援的步驟類型"""
    table = Table(title="支援的步驟類型", show_header=True, header_style="bold cyan")
    table.add_column("type", style="cyan", no_wrap=True)
    table.add_column("說明")
    for type_name, cls in REGISTRY.items():
        table.add_row(type_name, t(f"step.{type_name}.desc"))
    ui.console.print(table)

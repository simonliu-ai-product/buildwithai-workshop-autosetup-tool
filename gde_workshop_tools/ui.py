import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule
from rich.text import Text
from rich import box

console = Console()


def _t(key: str, **kwargs) -> str:
    """延遲匯入避免循環依賴"""
    from .i18n.loader import t
    return t(key, **kwargs)


def print_header(name: str, description: str):
    content = Text()
    content.append(name, style="bold white")
    if description:
        content.append(f"\n{description}", style="dim")
    console.print(Panel(content, border_style="cyan", padding=(1, 2)))


def print_step_header(idx: int, total: int, description: str):
    console.print()
    console.print(Rule(
        f"[bold cyan] [{idx}/{total}]  {description} [/bold cyan]",
        style="cyan",
        align="left",
    ))


def print_step_info(step_type: str, step_id: str, params: dict):
    table = Table(box=box.ROUNDED, border_style="dim", show_header=False, padding=(0, 1))
    table.add_column(style="dim", no_wrap=True, width=20)
    table.add_column()

    table.add_row("type", Text(step_type, style="yellow"))
    table.add_row("id", Text(step_id, style="dim"))
    for k, v in params.items():
        table.add_row(k, str(v))

    console.print(table)


def print_command(cmd: str):
    console.print(Panel(
        Text(f"$ {cmd}", style="bold green"),
        title=f"[dim]{_t('ui.command_title')}[/dim]",
        border_style="green",
        padding=(0, 1),
    ))


def print_info(message: str):
    console.print(f"  [cyan]ℹ[/cyan]  {message}")


def print_success(message: str):
    console.print(f"  [bold green]✔[/bold green]  {message}")


def print_warning(message: str):
    console.print(f"  [bold yellow]⚠[/bold yellow]  {message}")


def print_error(message: str):
    console.print(f"  [bold red]✘[/bold red]  {message}")


def ask(message: str, default: str = "") -> str:
    hint_line = f"[dim]{_t('ui.input_default_hint')}[/dim]" if default else ""
    body = f"[bold]{message}[/bold]"
    if default:
        body += f"\n{hint_line}"
    console.print(Panel(
        body,
        title=f"[dim]{_t('ui.input_title')}[/dim]",
        border_style="blue",
        padding=(0, 1),
    ))
    sys.stdout.write("  › ")
    sys.stdout.flush()
    value = sys.stdin.readline().strip()
    return value if value else default


def confirm_step() -> bool:
    from .i18n.loader import t
    sys.stdout.write(f"\n  {t('runner.confirm_step')} [Y/n]: ")
    sys.stdout.flush()
    answer = sys.stdin.readline().strip().lower()
    return answer in ("", "y", "yes")


def confirm(message: str, default: bool = False) -> bool:
    hint = "[Y/n]" if default else "[y/N]"
    sys.stdout.write(f"  {message} {hint}: ")
    sys.stdout.flush()
    answer = sys.stdin.readline().strip().lower()
    if answer == "":
        return default
    return answer in ("y", "yes")


def print_manual_checks(items: list) -> None:
    for step_desc, r in items:
        content = Text()
        content.append(f"{r.message}\n", style="bold")
        if r.detail:
            content.append(r.detail, style="cyan underline")
        console.print(Panel(
            content,
            title=f"[dim]{step_desc}[/dim]",
            border_style="yellow",
            padding=(0, 2),
        ))
    console.print()


def print_verify_results(results: list) -> bool:
    if not results:
        return True

    table = Table(box=box.ROUNDED, border_style="dim", show_header=False, padding=(0, 1))
    table.add_column(width=3, no_wrap=True)
    table.add_column()
    table.add_column(style="dim")

    all_ok = True
    for r in results:
        if r.ok is True:
            icon = "[bold green]✔[/bold green]"
        elif r.ok is False:
            icon = "[bold red]✘[/bold red]"
            all_ok = False
        else:
            icon = "[dim]–[/dim]"

        table.add_row(icon, r.message, r.detail or "")

    console.print(table)
    return all_ok

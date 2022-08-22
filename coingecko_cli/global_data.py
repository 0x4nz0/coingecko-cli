import httpx
from rich.console import Console
from typer import Typer

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def data():
    """
    Get cryptocurrency global data
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/global")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def defi():
    """
    Get cryptocurrency global decentralized finance(defi) data
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/global/decentralized_finance_defi")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


if __name__ == "__main__":
    app()

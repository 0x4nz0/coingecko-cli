import httpx
from rich.console import Console
from typer import Typer, Argument, Option
from typing import Optional

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def list(
    per_page: Optional[int] = Option(None, help="Total results per page"),
    page: Optional[int] = Option(None, help="Page through results"),
):
    """
    List all market indexes
    """
    params = {}
    if per_page is not None:
        params["per_page"] = str(per_page)
    if page is not None:
        params["page"] = str(page)
    try:
        r = httpx.get(f"{API_BASE_URL}/indexes", params=params)
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def market_index(
    market_id: str = Argument(..., help="Pass the marked id"),
    id: str = Argument(..., help="Pass the index id"),
):
    """
    Get market index by market id and index id
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/indexes/{market_id}/{id}")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def list_id_name():
    """
    List market indexes id and name
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/indexes/list")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


if __name__ == "__main__":
    app()

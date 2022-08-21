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
    r = httpx.get(f"{API_BASE_URL}/indexes", params=params).json()
    console.print_json(data=r)


@app.command()
def market_index(
    market_id: str = Argument(..., help="Pass the marked id"),
    id: str = Argument(..., help="Pass the index id"),
):
    """
    Get market index by market id and index id
    """
    r = httpx.get(f"{API_BASE_URL}/indexes/{market_id}/{id}").json()
    console.print_json(data=r)


@app.command()
def list_id_name():
    """
    List market indexes id and name
    """
    r = httpx.get(f"{API_BASE_URL}/indexes/list").json()
    console.print_json(data=r)


if __name__ == "__main__":
    app()

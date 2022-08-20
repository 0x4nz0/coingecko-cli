import httpx
from rich.console import Console
from typer import Typer, Option

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def list(per_page: int = Option(100), page: int = Option(1)):
    """
    List all market indexes
    """
    params = {"per_page": str(per_page), "page": str(page)}
    r = httpx.get(f"{API_BASE_URL}/indexes", params=params).json()
    console.print(r)


@app.command()
def market_index(market_id: str, id: str):
    """
    Get market index by market id and index id
    """
    r = httpx.get(f"{API_BASE_URL}/indexes/{market_id}/{id}").json()
    console.print(r)


if __name__ == "__main__":
    app()

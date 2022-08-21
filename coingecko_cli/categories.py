import httpx
from rich.console import Console
from typer import Typer, Option
from enum import Enum

from .utils import API_BASE_URL

console = Console()

app = Typer()


class MarketOrder(str, Enum):
    market_cap_desc = "market_cap_desc"
    market_cap_asc = "market_cap_asc"
    name_desc = "name_desc"
    name_asc = "name_asc"
    market_cap_change_24h_desc = "market_cap_change_24h_desc"
    market_cap_change_24h_asc = "market_cap_change_24h_asc"


@app.command()
def list():
    """
    List all categories
    """
    r = httpx.get(f"{API_BASE_URL}/coins/categories/list").json()
    console.print_json(data=r)


@app.command()
def market_data(
    order: MarketOrder = Option(
        MarketOrder.market_cap_desc, help="Sort results by field"
    )
):
    """
    List all categories with market data
    """
    params = {"order": order.value}
    r = httpx.get(f"{API_BASE_URL}/coins/categories", params=params).json()
    console.print_json(data=r)


if __name__ == "__main__":
    app()

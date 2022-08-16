import httpx
from rich.console import Console
from rich.table import Table
from typer import Typer
from enum import Enum

from .utils import API_BASE_URL

console = Console()

app = Typer()


class Order(str, Enum):
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
    table = Table("category_id", "name")
    for coin in r:
        category_id, name = coin.values()
        table.add_row(category_id, name)
    console.print(table)


@app.command()
def market_data(order: Order = Order.market_cap_desc):
    """
    List all categories with market data
    """
    params = {"order": order.value}
    r = httpx.get(f"{API_BASE_URL}/coins/categories", params=params).json()
    console.print(r)


if __name__ == "__main__":
    app()

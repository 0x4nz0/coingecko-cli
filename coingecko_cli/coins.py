import httpx
from rich.console import Console
from rich.table import Table
from typer import Typer, Argument, Option
from enum import Enum

from .utils import API_BASE_URL

console = Console()

app = Typer()


class Order(str, Enum):
    gecko_desc = "gecko_desc"
    gecko_asc = "gecko_asc"
    market_cap_desc = "market_cap_desc"
    market_cap_asc = "market_cap_asc"
    volume_asc = "volume_asc"
    volume_desc = "volume_desc"
    id_asc = "id_asc"
    id_desc = "id_desc"


@app.command()
def list():
    """
    List all supported coins with id, name and symbol (no pagination required)
    """
    r = httpx.get(f"{API_BASE_URL}/coins/list").json()
    table = Table("id", "symbol", "name")
    for coin in r:
        _id, symbol, name = coin.values()
        table.add_row(_id, symbol, name)
    console.print(table)


@app.command()
def markets(
    vs_currency: str,
    ids: str = Option(""),
    category: str = Option(""),
    order: Order = Argument(Order.market_cap_desc),
    per_page: int = Argument(100, min=1, max=250),
    page: int = Argument(1),
    sparkline: bool = Option(False, "--sparkline"),
    price_change_percentage: str = Option(""),
):
    """
    List all supported coins price, market cap, volume, and market related data
    """
    params = {
        "vs_currency": vs_currency,
        "ids": ids,
        "category": category,
        "order": order.value,
        "per_page": str(per_page),
        "page": str(page),
        "sparkline": sparkline,
        "price_change_percentage": price_change_percentage,
    }
    r = httpx.get(f"{API_BASE_URL}/coins/markets", params=params).json()
    console.print(r)


if __name__ == "__main__":
    app()

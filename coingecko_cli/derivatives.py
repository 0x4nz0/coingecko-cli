import httpx
from rich.console import Console
from typer import Typer, Option
from enum import Enum
from typing import Optional

from .utils import API_BASE_URL

console = Console()

app = Typer()


class TickerOption(str, Enum):
    all = "all"
    unexpired = "unexpired"


class ExchangeOrder(str, Enum):
    name_asc = "name_asc"
    name_desc = "name_desc"
    open_interest_btc_asc = "open_interest_btc_asc"
    open_interest_btc_desc = "open_interest_btc_desc"
    trade_volume_24h_btc_asc = "trade_volume_24h_btc_asc"
    trade_volume_24h_btc_desc = "trade_volume_24h_btc_desc"


@app.command()
def exchanges(
    order: ExchangeOrder = ExchangeOrder.name_desc,
    per_page: int = Option(100),
    page: int = Option(1),
):
    """
    List all derivative exchanges
    """
    params = {"order": order.value, "per_page": str(per_page), "page": str(page)}
    r = httpx.get(f"{API_BASE_URL}/derivatives/exchanges", params=params).json()
    console.print(r)


@app.command()
def exchange_data(id: str, include_tickers: Optional[TickerOption] = None):
    """
    Show derivative exchange data
    """
    params = {}
    if include_tickers is not None:
        params["include_tickers"] = include_tickers.value
    r = httpx.get(f"{API_BASE_URL}/derivatives/exchanges/{id}", params=params).json()
    console.print(r)


@app.command()
def list():
    """
    List all derivative exchanges name and identifier
    """
    r = httpx.get(f"{API_BASE_URL}/derivatives/exchanges/list").json()
    console.print(r)


if __name__ == "__main__":
    app()

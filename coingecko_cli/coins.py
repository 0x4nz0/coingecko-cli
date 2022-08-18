import httpx
from rich.console import Console
from rich.table import Table
from typer import Typer, Argument, Option
from enum import Enum
from datetime import datetime

from .utils import API_BASE_URL

console = Console()

app = Typer()


class MarketOrder(str, Enum):
    gecko_desc = "gecko_desc"
    gecko_asc = "gecko_asc"
    market_cap_desc = "market_cap_desc"
    market_cap_asc = "market_cap_asc"
    volume_asc = "volume_asc"
    volume_desc = "volume_desc"
    id_asc = "id_asc"
    id_desc = "id_desc"


class TickerOrder(str, Enum):
    trust_score_desc = "trust_score_desc"
    trust_score_asc = "trust_score_asc"
    volume_desc = "volume_desc"


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
    order: MarketOrder = Argument(MarketOrder.market_cap_desc),
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


@app.command()
def current_data(
    id: str,
    localization: bool = Option(True, "--no-localization"),
    tickers: bool = Option(True, "--no-tickers"),
    market_data: bool = Option(True, "--no-market-data"),
    community_data: bool = Option(True, "--no-community-data"),
    developer_data: bool = Option(True, "--no-developer-data"),
    sparkline: bool = Option(False, "--sparkline"),
):
    """
    Get current data (name, price, market, ... including exchange tickers)
    for a coin
    """
    params = {
        "localization": localization,
        "tickers": tickers,
        "market_data": market_data,
        "community_data": community_data,
        "developer_data": developer_data,
    }
    r = httpx.get(f"{API_BASE_URL}/coins/{id}", params=params).json()
    console.print(r)


@app.command()
def tickers(
    id: str,
    exchange_ids: str = Option(""),
    include_exchange_logo: bool = Option(False, "--include-exchange-logo"),
    page: int = Option(1),
    order: TickerOrder = Option(TickerOrder.trust_score_desc),
    depth: bool = Option(False, "--depth"),
):
    """
    Get coin tickers (paginated to 100 items)
    """
    params = {
        "exchange_ids": exchange_ids,
        "include-exchange-logo": include_exchange_logo,
        "page": str(page),
        "order": order,
        "depth": depth,
    }
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/tickers", params=params).json()
    console.print(r)


@app.command()
def historical_data(
    id: str,
    date: datetime = Argument(..., formats=["%d-%m-%Y"]),
    localization: bool = Option(True, "--no-localization"),
):
    """
    Get historical data (name, price, market, stats) at a given date for a coin
    """
    params = {"date": date.strftime("%d-%m-%Y"), "localization": localization}
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/history", params=params).json()
    console.print(r)


@app.command()
def market_chart(id: str, vs_currency: str, days: int = Argument(..., min=1, max=30)):
    """
    Get historical market data include price, market cap, and 24h volume
    (granularity auto)
    """
    params = {"vs_currency": vs_currency, "days": str(days)}
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/market_chart", params=params).json()
    console.print(r)


if __name__ == "__main__":
    app()

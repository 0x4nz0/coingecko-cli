import httpx
from rich.console import Console
from typer import Typer, Argument, Option
from enum import Enum
from typing import Optional
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
def list(
    include_platform: bool = Option(
        False,
        "--include-platform",
        help="Flag to include platform contract addresses (eg. 0x.... for Ethereum based tokens)",
    )
):
    """
    List all supported coins with id, name and symbol (no pagination required)
    """
    params = {"include_platform": str(include_platform).lower()}
    r = httpx.get(f"{API_BASE_URL}/coins/list", params=params).json()
    console.print(r)


@app.command()
def markets(
    vs_currency: str = Argument(
        ..., help="The target currency of market data (usd, eur, jpy, etc.)"
    ),
    ids: Optional[str] = Option(
        None, help="The ids of the coin, comma separated crytocurrency symbols (base)"
    ),
    category: Optional[str] = Option(None, help="Filter by coin category"),
    order: MarketOrder = Option(
        MarketOrder.market_cap_desc, help="Sort results by field"
    ),
    per_page: int = Option(100, min=1, max=250, help="Total results per page"),
    page: int = Option(1, help="Page through results"),
    sparkline: bool = Option(
        False, "--sparkline", help="Include sparkline 7 days data"
    ),
    price_change_percentage: Optional[str] = Option(
        None,
        help="Include price change percentage in 1h, 24h, 7d, 14d, 30d, 200d, 1y (eg. '1h,24h,7d' comma-separated)",
    ),
):
    """
    List all supported coins price, market cap, volume, and market related data
    """
    params = {
        "vs_currency": vs_currency,
        "order": order.value,
        "per_page": str(per_page),
        "page": str(page),
        "sparkline": sparkline,
    }
    if ids is not None:
        params["ids"] = ids
    if category is not None:
        params["category"] = category
    if price_change_percentage is not None:
        params["price_change_percentage"] = price_change_percentage
    r = httpx.get(f"{API_BASE_URL}/coins/markets", params=params).json()
    console.print(r)


@app.command()
def coin(
    id: str = Argument(..., help="Pass the coin id (eg. bitcoin)"),
    localization: bool = Option(
        True, "--no-localization", help="Include all localized languages in response"
    ),
    tickers: bool = Option(True, "--no-tickers", help="Include tickers data"),
    market_data: bool = Option(True, "--no-market-data", help="Include market_data"),
    community_data: bool = Option(
        True, "--no-community-data", help="Include community_data"
    ),
    developer_data: bool = Option(
        True, "--no-developer-data", help="Include developer_data"
    ),
    sparkline: bool = Option(
        False, "--sparkline", help="Include sparkline 7 days data"
    ),
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
    id: str = Argument(..., help="Pass the coin id (eg. bitcoin)"),
    exchange_ids: Optional[str] = Option(None, help="Filter results by exchange_ids"),
    include_exchange_logo: bool = Option(
        False, "--include-exchange-logo", help="Flag to show exchange_logo"
    ),
    page: Optional[int] = Option(None, help="Page through results"),
    order: TickerOrder = Option(TickerOrder.trust_score_desc),
    depth: bool = Option(False, "--depth", help="Flag to show 2% orderbook depth"),
):
    """
    Get coin tickers (paginated to 100 items)
    """
    params = {
        "include-exchange-logo": include_exchange_logo,
        "order": order,
        "depth": depth,
    }
    if exchange_ids is not None:
        params["exchange_ids"] = exchange_ids
    if page is not None:
        params["page"] = str(page)
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/tickers", params=params).json()
    console.print(r)


@app.command()
def history(
    id: str = Argument(..., help="Pass the coin id (eg. bitcoin)"),
    date: datetime = Argument(
        ...,
        formats=["%d-%m-%Y"],
        help="The date of data snapshot in dd-mm-yyyy eg. 30-12-2017",
    ),
    localization: bool = Option(
        True, "--no-localization", help="To include localized languages in response"
    ),
):
    """
    Get historical data (name, price, market, stats) at a given date for a coin
    """
    params = {"date": date.strftime("%d-%m-%Y"), "localization": localization}
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/history", params=params).json()
    console.print(r)


@app.command()
def market_chart(
    id: str = Argument(..., help="Pass the coin id (eg. bitcoin)"),
    vs_currency: str = Argument(
        ..., help="The target currency of market data (usd, eur, jpy, etc.)"
    ),
    days: int = Argument(
        ..., min=1, max=30, help="Data up to number of days ago (eg. 1,14,30)"
    ),
    interval: Optional[str] = Option(None, help="Data interval. Possible value: daily"),
):
    """
    Get historical market data include price, market cap, and 24h volume
    (granularity auto)
    """
    params = {"vs_currency": vs_currency, "days": str(days)}
    if interval is not None:
        params["interval"] = interval
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/market_chart", params=params).json()
    console.print(r)


@app.command()
def market_chart_range(
    id: str = Argument(..., help="Pass the coin id (eg. bitcoin)"),
    vs_currency: str = Argument(
        ..., help="The target currency of market data (usd, eur, jpy, etc.)"
    ),
    from_date: datetime = Argument(
        ...,
        formats=["%d-%m-%Y", "%d-%m-%YT%H:%M:%S"],
        help="From date (eg. 30-12-2017, 30-12-2017T00:00:00)",
    ),
    to_date: datetime = Argument(
        ...,
        formats=["%d-%m-%Y", "%d-%m-%YT%H:%M:%S"],
        help="To date (eg. 01-01-2018, 01-02-2018T00:00:00)",
    ),
):
    """
    Get historical market data include price, market cap, and 24h volume
    within a range of timestamp (granularity auto)
    """
    params = {
        "vs_currency": vs_currency,
        "from": str(datetime.timestamp(from_date)),
        "to": str(datetime.timestamp(to_date)),
    }
    r = httpx.get(
        f"{API_BASE_URL}/coins/{id}/market_chart/range",
        params=params,
    ).json()
    console.print(r)


@app.command()
def ohlc(
    id: str = Argument(..., help="Pass the coin id (eg. bitcoin)"),
    vs_currency: str = Argument(
        ..., help="The target currency of market data (usd, eur, jpy, etc.)"
    ),
    days: int = Argument(
        ..., min=1, max=365, help="Data up to number of days ago (1/7/14/30/90/180/365)"
    ),
):
    """
    Get coin's OHLC
    """
    params = {"vs_currency": vs_currency, "days": days}
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/ohlc", params=params).json()
    console.print(r)


if __name__ == "__main__":
    app()

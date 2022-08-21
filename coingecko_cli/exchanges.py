import httpx
from rich.console import Console
from typer import Typer, Argument, Option
from enum import Enum
from typing import Optional

from .utils import API_BASE_URL

console = Console()

app = Typer()


class TickerOrder(str, Enum):
    trust_score_desc = "trust_score_desc"
    trust_score_asc = "trust_score_asc"
    volume_desc = "volume_desc"


class TickerDepth(str, Enum):
    cost_to_move_up_usd = "cost_to_move_up_usd"
    cost_to_move_down_usd = "cost_to_move_down_usd"


@app.command()
def list(
    per_page: int = Option(100, min=1, max=250, help="Total results per page"),
    page: int = Option(1, help="Page through results"),
):
    """
    List all exchanges (Active with trading volumes)
    """
    params = {"per_page": str(per_page), "page": str(page)}
    r = httpx.get(f"{API_BASE_URL}/exchanges", params=params).json()
    console.print(r)


@app.command()
def markets_list():
    """
    List all supported markets id and name (no pagination required)
    """
    r = httpx.get(f"{API_BASE_URL}/exchanges/list").json()
    console.print(r)


@app.command()
def volume(id: str = Argument(..., help="Pass the exchange id (eg. binance)")):
    """
    Get exchange volume in BTC and tickers
    """
    r = httpx.get(f"{API_BASE_URL}/exchanges/{id}").json()
    console.print(r)


@app.command()
def tickers(
    id: str = Argument(..., help="Pass the exchange id (eg. binance"),
    coin_ids: Optional[str] = Option(None, help="Filter tickers by coin ids"),
    include_exchange_logo: bool = Option(
        False, "--include-exchange-logo", help="Flag to show exchange_logo"
    ),
    page: Optional[int] = Option(None, help="Page through results"),
    depth: TickerDepth = Option(
        TickerDepth.cost_to_move_up_usd, help="Flag to show 2% orderbook depth"
    ),
    order: TickerOrder = Option(
        TickerOrder.trust_score_desc, help="Sort results by field"
    ),
):
    """
    Get exchange tickers (paginated, 100 tickers per page)
    """
    params = {
        "include_exchange_logo": include_exchange_logo,
        "depth": depth.value,
        "order": order.value,
    }
    if coin_ids is not None:
        params["coin_ids"] = coin_ids
    if page is not None:
        params["page"] = str(page)
    r = httpx.get(f"{API_BASE_URL}/exchanges/{id}/tickers", params=params).json()
    console.print(r)


@app.command()
def volume_chart(
    id: str = Argument(..., help="Pass the exchange id (eg. binance"),
    days: int = Argument(
        ..., min=1, max=30, help="Data up to number of days ago (eg. 1,14,30)"
    ),
):
    """
    Get volume_chart data for a given exchange
    """
    params = {"days": str(days)}
    r = httpx.get(f"{API_BASE_URL}/exchanges/{id}/volume_chart", params=params).json()
    console.print(r)


if __name__ == "__main__":
    app()

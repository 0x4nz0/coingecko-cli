import httpx
from rich.console import Console
from typer import Typer, Argument, Option
from enum import Enum

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
def list(per_page: int = Argument(100, min=1, max=250), page: int = Argument(1)):
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
def volume(id: str):
    """
    Get exchange volume in BTC and tickers
    """
    r = httpx.get(f"{API_BASE_URL}/exchanges/{id}").json()
    console.print(r)


@app.command()
def tickers(
    id: str,
    coin_ids: str = Option(""),
    include_exchange_logo: bool = Option(False, "--include-exchange-logo"),
    page: int = Option(1),
    depth: TickerDepth = Option(TickerDepth.cost_to_move_up_usd),
    order: TickerOrder = Option(TickerOrder.trust_score_desc),
):
    """
    Get exchange tickers (paginated, 100 tickers per page)
    """
    params = {
        "coin_ids": coin_ids,
        "include_exchange_logo": include_exchange_logo,
        "page": str(page),
        "depth": depth.value,
        "order": order.value,
    }
    r = httpx.get(f"{API_BASE_URL}/exchanges/{id}/tickers", params=params).json()
    console.print(r)


if __name__ == "__main__":
    app()

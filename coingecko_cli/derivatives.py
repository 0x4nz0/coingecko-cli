import httpx
from rich.console import Console
from typer import Typer, Argument, Option
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
def tickers(
    include_tickers: TickerOption = Option(
        TickerOption.unexpired, help="To show all or unexpired tickers"
    )
):
    """
    List all derivative tickers
    """
    params = {"include_tickers": include_tickers.value}
    try:
        r = httpx.get(f"{API_BASE_URL}/derivatives", params=params)
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def exchanges(
    order: Optional[ExchangeOrder] = Option(None, help="Sort results by field"),
    per_page: Optional[int] = Option(None, help="Total results per page"),
    page: Optional[int] = Option(None, help="Page through results"),
):
    """
    List all derivative exchanges
    """
    params = {}
    if order is not None:
        params["order"] = order.value
    if per_page is not None:
        params["per_page"] = str(per_page)
    if page is not None:
        params["page"] = str(page)
    try:
        r = httpx.get(f"{API_BASE_URL}/derivatives/exchanges", params=params)
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def exchange_data(
    id: str = Argument(..., help="Pass the exchange id"),
    include_tickers: Optional[TickerOption] = Option(
        None, help="To show all or unexpired tickers"
    ),
):
    """
    Show derivative exchange data
    """
    params = {}
    if include_tickers is not None:
        params["include_tickers"] = include_tickers.value
    try:
        r = httpx.get(f"{API_BASE_URL}/derivatives/exchanges/{id}", params=params)
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def list():
    """
    List all derivative exchanges name and identifier
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/derivatives/exchanges/list")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


if __name__ == "__main__":
    app()

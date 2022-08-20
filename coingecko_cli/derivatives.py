import httpx
from rich.console import Console
from typer import Typer
from enum import Enum
from typing import Optional

from .utils import API_BASE_URL

console = Console()

app = Typer()


class TickerOption(str, Enum):
    all = "all"
    unexpired = "unexpired"


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

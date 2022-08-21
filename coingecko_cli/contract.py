import httpx
from rich.console import Console
from typer import Typer, Argument
from datetime import datetime

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def coin_info(
    id: str = Argument(..., help="Asset platform"),
    contract_address: str = Argument(..., help="Token's contract address"),
):
    """
    Get coin info from contract address
    """
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/contract/{contract_address}").json()
    console.print_json(data=r)


@app.command()
def market_chart(
    id: str = Argument(..., help="The id of the platform issuing tokens"),
    contract_address: str = Argument(..., help="Token's contract address"),
    vs_currency: str = Argument(
        ..., help="The target currency of market data (usd, eur, jpy, etc.)"
    ),
    days: int = Argument(
        ..., min=1, max=30, help="Data up to number of days ago (eg. 1,14,30,max)"
    ),
):
    """
    Get historical market data include price, market cap, and 24h volume
    (granularity auto)
    """
    params = {"vs_currency": vs_currency, "days": str(days)}
    r = httpx.get(
        f"{API_BASE_URL}/coins/{id}/contract/{contract_address}/market_chart/",
        params=params,
    ).json()
    console.print_json(data=r)


@app.command()
def market_chart_range(
    id: str = Argument(..., help="The id of the platform issuing tokens"),
    contract_address: str = Argument(..., help="Token's contract address"),
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
    Get historical market data include price, market cap, and 24h volume within
    a range of datetime (granularity auto)
    """
    params = {
        "vs_currency": vs_currency,
        "from": str(datetime.timestamp(from_date)),
        "to": str(datetime.timestamp(to_date)),
    }
    r = httpx.get(
        f"{API_BASE_URL}/coins/{id}/contract/{contract_address}/market_chart/range",
        params=params,
    ).json()
    console.print_json(data=r)


if __name__ == "__main__":
    app()

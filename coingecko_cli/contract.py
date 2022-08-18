import httpx
from rich.console import Console
from typer import Typer, Argument
from datetime import datetime

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def info(id: str, contract_address: str):
    """
    Get coin info from contract address
    """
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/contract/{contract_address}").json()
    console.print(r)


@app.command()
def market_chart(
    id: str,
    contract_address: str,
    vs_currency: str,
    days: int = Argument(..., min=1, max=30),
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
    console.print(r)


@app.command()
def market_chart_range(
    id: str,
    contract_address: str,
    vs_currency: str,
    from_date: datetime = Argument(..., formats=["%d-%m-%Y", "%d-%m-%YT%H:%M:%S"]),
    to_date: datetime = Argument(..., formats=["%d-%m-%Y", "%d-%m-%YT%H:%M:%S"]),
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
    console.print(r)


if __name__ == "__main__":
    app()

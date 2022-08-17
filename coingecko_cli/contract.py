import httpx
from rich.console import Console
from typer import Typer, Argument

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
    id: str, contract_address: str, vs_currency: str, days: int = Argument(..., min=1)
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


if __name__ == "__main__":
    app()

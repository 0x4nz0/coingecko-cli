import httpx
from rich.console import Console
from rich.columns import Columns
from typer import Typer, Option

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def price(
    ids: str,
    vs_currencies: str,
    include_market_cap: bool = Option(False, "--market-cap"),
    include_24hr_vol: bool = Option(False, "--24hr-vol"),
    include_24hr_change: bool = Option(False, "--24hr-change"),
    include_last_updated_at: bool = Option(False, "--last-updated-at"),
):
    """
    Get the current price of any cryptocurrencies in any other supported
    currencies that you need
    """
    params = {
        "ids": ids,
        "vs_currencies": vs_currencies,
        "include_market_cap": str(include_market_cap).lower(),
        "include_24hr_vol": str(include_24hr_vol).lower(),
        "include_24hr_change": str(include_24hr_change).lower(),
        "include_last_updated_at": str(include_last_updated_at).lower(),
    }
    r = httpx.get(f"{API_BASE_URL}/simple/price", params=params).json()
    console.print(r)


@app.command()
def token_price(
    id: str,
    contract_addresses: str,
    vs_currencies: str,
    include_market_cap: bool = Option(False, "--market-cap"),
    include_24hr_vol: bool = Option(False, "--24hr-vol"),
    include_24hr_change: bool = Option(False, "--24hr-change"),
    include_last_updated_at: bool = Option(False, "--last-updated-at"),
):
    """
    Get current price of tokens (using contract addresses) for a given platform
    in any other currency that you need
    """
    params = {
        "contract_addresses": contract_addresses,
        "vs_currencies": vs_currencies,
        "include_market_cap": str(include_market_cap).lower(),
        "include_24hr_vol": str(include_24hr_vol).lower(),
        "include_24hr_change": str(include_24hr_change).lower(),
        "include_last_updated_at": str(include_last_updated_at).lower(),
    }
    r = httpx.get(f"{API_BASE_URL}/simple/token_price/{id}", params=params).json()
    console.print(r)


@app.command()
def supported_vs_currencies():
    """
    List of supported_vs_currencies
    """
    r = httpx.get(f"{API_BASE_URL}/simple/supported_vs_currencies").json()
    console.print(Columns([f"- [yellow]{currency}" for currency in r]))


if __name__ == "__main__":
    app()

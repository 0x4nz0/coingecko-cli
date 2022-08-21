import httpx
from rich.console import Console
from typer import Typer, Argument, Option

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def price(
    ids: str = Argument(
        ..., help="id of coins, comma-separated if querying more than 1 coin"
    ),
    vs_currencies: str = Argument(
        ...,
        help="vs_currency of coins, comma-separated if querying more than 1 vs_currency",
    ),
    include_market_cap: bool = Option(
        False, "--market-cap", help="To include market_cap"
    ),
    include_24hr_vol: bool = Option(False, "--24hr-vol", help="To include 24hr_vol"),
    include_24hr_change: bool = Option(
        False, "--24hr-change", help="To include 24hr_change"
    ),
    include_last_updated_at: bool = Option(
        False, "--last-updated-at", help="To include last_updated_at of price"
    ),
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
    console.print_json(data=r)


@app.command()
def token_price(
    id: str = Argument(..., help="The id of the platform issuing tokens"),
    contract_addresses: str = Argument(
        ..., help="The contract address of tokens, comma separated"
    ),
    vs_currencies: str = Argument(
        ...,
        help="vs_currency of coins, comma-separated if querying more than 1 vs_currency",
    ),
    include_market_cap: bool = Option(
        False, "--market-cap", help="To include market_cap"
    ),
    include_24hr_vol: bool = Option(False, "--24hr-vol", help="To include 24hr_vol"),
    include_24hr_change: bool = Option(
        False, "--24hr-change", help="To include 24hr_change"
    ),
    include_last_updated_at: bool = Option(
        False, "--last-updated-at", help="To include last_updated_at of price"
    ),
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
    console.print_json(data=r)


@app.command()
def supported_vs_currencies():
    """
    List of supported_vs_currencies
    """
    r = httpx.get(f"{API_BASE_URL}/simple/supported_vs_currencies").json()
    console.print_json(data=r)


if __name__ == "__main__":
    app()

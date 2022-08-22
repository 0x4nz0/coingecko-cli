import httpx
from rich.console import Console
from typer import Typer, Argument

from .utils import API_BASE_URL
from . import (
    simple,
    coins,
    contract,
    categories,
    exchanges,
    indexes,
    derivatives,
    global_data,
)

console = Console()

app = Typer()
app.add_typer(simple.app, name="simple", help="Check price(s) of cryptocurrency")
app.add_typer(coins.app, name="coins", help="Check market data of cryptocurrency")
app.add_typer(
    contract.app,
    name="contract",
    help="Check cryptocurrency info from contract address",
)
app.add_typer(categories.app, name="categories", help="Check data of categories")
app.add_typer(exchanges.app, name="exchanges", help="Check market data of exchanges")
app.add_typer(indexes.app, name="indexes", help="Check info of market indexes")
app.add_typer(
    derivatives.app, name="derivatives", help="Check data of derivative exchanges"
)
app.add_typer(
    global_data.app, name="global", help="Check global data of cryptocurrency and DeFi"
)


@app.command()
def ping():
    """
    Check API server status
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/ping")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def asset_platforms():
    """
    List all asset platforms (Blockchain networks)
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/asset_platforms")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def exchange_rates():
    """
    Get BTC-to-Currency exchange rates
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/exchange_rates")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def search(query: str = Argument(..., help="Search string")):
    """
    Search for coins, categories and markets listed on CoinGecko ordered
    by largest Market Cap first
    """
    params = {"query": query}
    try:
        r = httpx.get(f"{API_BASE_URL}/search", params=params)
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def trending():
    """
    Top-7 trending coins on CoinGecko as searched by users in the last 24 hours
    (Ordered by most popular first)
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/search/trending")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


@app.command()
def companies_public_treasury(
    coin_id: str = Argument(..., help="Pass the coin id (eg. bitcoin or ethereum)")
):
    """
    Get public companies bitcoin or ethereum holdings
    (Ordered by total holdings descending)
    """
    try:
        r = httpx.get(f"{API_BASE_URL}/companies/public_treasury/{coin_id}")
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        console.print(f"[bold red]ERROR[/]: {exc}")
    else:
        console.print_json(data=r.json())


if __name__ == "__main__":
    app()

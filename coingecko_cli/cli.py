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
    companies,
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
app.add_typer(global_data.app, name="global")
app.add_typer(companies.app, name="companies")


@app.command()
def ping():
    """
    Check API server status
    """
    r = httpx.get(f"{API_BASE_URL}/ping").json()["gecko_says"]
    console.print(r)


@app.command()
def asset_platforms():
    """
    List all asset platforms (Blockchain networks)
    """
    r = httpx.get(f"{API_BASE_URL}/asset_platforms").json()
    console.print(r)


@app.command()
def exchange_rates():
    """
    Get BTC-to-Currency exchange rates
    """
    r = httpx.get(f"{API_BASE_URL}/exchange_rates").json()
    console.print(r)


@app.command()
def search(query: str = Argument(..., help="Search string")):
    """
    Search for coins, categories and markets listed on CoinGecko ordered
    by largest Market Cap first
    """
    params = {"query": query}
    r = httpx.get(f"{API_BASE_URL}/search", params=params).json()
    console.print(r)


@app.command()
def trending():
    """
    Top-7 trending coins on CoinGecko as searched by users in the last 24 hours
    (Ordered by most popular first)
    """
    r = httpx.get(f"{API_BASE_URL}/search/trending").json()
    console.print(r)


if __name__ == "__main__":
    app()

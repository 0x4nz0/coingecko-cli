import httpx
from rich.console import Console
from typer import Typer

from .utils import API_BASE_URL
from . import (
    simple,
    coins,
    search,
    categories,
    asset_platforms,
    global_data,
    contract,
    exchanges,
    exchange_rates,
    companies,
)

console = Console()

app = Typer()
app.add_typer(simple.app, name="simple")
app.add_typer(coins.app, name="coins")
app.add_typer(search.app, name="search")
app.add_typer(categories.app, name="categories")
app.add_typer(asset_platforms.app, name="asset-platforms")
app.add_typer(global_data.app, name="global")
app.add_typer(contract.app, name="contract")
app.add_typer(exchanges.app, name="exchanges")
app.add_typer(exchange_rates.app, name="exchange-rates")
app.add_typer(companies.app, name="companies")


@app.command()
def ping():
    """
    Check API server status
    """
    r = httpx.get(f"{API_BASE_URL}/ping").json()["gecko_says"]
    console.print(r)


if __name__ == "__main__":
    app()

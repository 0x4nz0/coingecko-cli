import httpx
from rich.console import Console
from typer import Typer

from .utils import API_BASE_URL
from . import simple, coins, search

console = Console()

app = Typer()
app.add_typer(simple.app, name="simple")
app.add_typer(coins.app, name="coins")
app.add_typer(search.app, name="search")


@app.command()
def ping():
    """
    Check API server status
    """
    r = httpx.get(f"{API_BASE_URL}/ping").json()["gecko_says"]
    console.print(r)


if __name__ == "__main__":
    app()

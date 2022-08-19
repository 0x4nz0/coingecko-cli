import httpx
from rich.console import Console
from typer import Typer

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def list():
    """
    Get BTC-to-Currency exchange rates
    """
    r = httpx.get(f"{API_BASE_URL}/exchange_rates").json()
    console.print(r)


if __name__ == "__main__":
    app()

import httpx
from rich.console import Console
from typer import Typer

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def list(coin_id: str):
    """
    Get public companies bitcoin or ethereum holdings
    (Ordered by total holdings descending)
    """
    r = httpx.get(f"{API_BASE_URL}/companies/public_treasury/{coin_id}").json()
    console.print(r)


if __name__ == "__main__":
    app()

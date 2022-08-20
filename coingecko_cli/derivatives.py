import httpx
from rich.console import Console
from typer import Typer
from enum import Enum

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def list():
    """
    List all derivative exchanges name and identifier
    """
    r = httpx.get(f"{API_BASE_URL}/derivatives/exchanges/list").json()
    console.print(r)


if __name__ == "__main__":
    app()

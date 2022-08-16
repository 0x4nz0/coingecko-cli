import httpx
from rich.console import Console
from rich.table import Table
from typer import Typer

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def list():
    """
    List all asset platforms (Blockchain networks)
    """
    r = httpx.get(f"{API_BASE_URL}/asset_platforms").json()
    console.print(r)


if __name__ == "__main__":
    app()

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
    List all supported coins with id, name and symbol (no pagination required)
    """
    r = httpx.get(f"{API_BASE_URL}/coins/list").json()
    table = Table("id", "symbol", "name")
    for coin in r:
        _id, symbol, name = coin.values()
        table.add_row(_id, symbol, name)
    console.print(table)


if __name__ == "__main__":
    app()

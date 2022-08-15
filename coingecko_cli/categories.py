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
    List all categories
    """
    r = httpx.get(f"{API_BASE_URL}/coins/categories/list").json()
    table = Table("category_id", "name")
    for coin in r:
        category_id, name = coin.values()
        table.add_row(category_id, name)
    console.print(table)


if __name__ == "__main__":
    app()

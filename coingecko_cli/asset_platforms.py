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
    table = Table("id", "chain_identifier", "name", "shortname")
    for platform in r:
        _id, chain_identifier, name, shortname = platform.values()
        if not chain_identifier:
            chain_identifier = "N/A"
        if not shortname:
            shortname = "N/A"
        table.add_row(_id, str(chain_identifier), name, shortname)
    console.print(table)


if __name__ == "__main__":
    app()

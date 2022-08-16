import httpx
from rich.console import Console
from typer import Typer

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def data():
    """
    Get cryptocurrency global data
    """
    r = httpx.get(f"{API_BASE_URL}/global").json()
    console.print(r)


if __name__ == "__main__":
    app()

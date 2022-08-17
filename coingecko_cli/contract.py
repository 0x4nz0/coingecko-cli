import httpx
from rich.console import Console
from typer import Typer

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def info(id: str, contract_address: str):
    """
    Get coin info from contract address
    """
    r = httpx.get(f"{API_BASE_URL}/coins/{id}/contract/{contract_address}").json()
    console.print(r)


if __name__ == "__main__":
    app()

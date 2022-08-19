import httpx
from rich.console import Console
from typer import Typer, Argument

from .utils import API_BASE_URL

console = Console()

app = Typer()


@app.command()
def list(per_page: int = Argument(100, min=1, max=250), page: int = Argument(1)):
    """
    List all exchanges (Active with trading volumes)
    """
    params = {"per_page": str(per_page), "page": str(page)}
    r = httpx.get(f"{API_BASE_URL}/exchanges", params=params).json()
    console.print(r)


if __name__ == "__main__":
    app()

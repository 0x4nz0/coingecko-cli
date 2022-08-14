import httpx
from rich.console import Console
from rich.columns import Columns
from rich.table import Table
from typer import Typer
from typer import Option

console = Console()

app = Typer()

API_BASE_URL = "https://api.coingecko.com/api/v3"


@app.command()
def ping():
    """
    Check API server status
    """
    r = httpx.get(f"{API_BASE_URL}/ping").json()["gecko_says"]
    console.print(r)


@app.command()
def price(
    ids: str,
    vs_currencies: str,
    include_market_cap: bool = Option(False, "--market-cap"),
    include_24hr_vol: bool = Option(False, "--24hr-vol"),
    include_24hr_change: bool = Option(False, "--24hr-change"),
    include_last_updated_at: bool = Option(False, "--last-updated-at"),
):
    """
    Get the current price of any cryptocurrencies in any other supported currencies that you need
    """
    params = {
        "ids": ids,
        "vs_currencies": vs_currencies,
        "include_market_cap": str(include_market_cap).lower(),
        "include_24hr_vol": str(include_24hr_vol).lower(),
        "include_24hr_change": str(include_24hr_change).lower(),
        "include_last_updated_at": str(include_last_updated_at).lower(),
    }
    r = httpx.get(f"{API_BASE_URL}/simple/price", params=params).json()
    console.print(r)


@app.command()
def supported_vs_currencies():
    """
    List of supported_vs_currencies
    """
    r = httpx.get(f"{API_BASE_URL}/simple/supported_vs_currencies").json()
    console.print(Columns([f"- [yellow]{currency}" for currency in r]))


@app.command()
def trending():
    """
    Top-7 trending coins on CoinGecko as searched by users in the last 24 hours (Ordered by most popular first)
    """
    r = httpx.get(f"{API_BASE_URL}/search/trending").json()["coins"]
    table = Table("id", "coin_id", "name", "symbol", "market_cap_rank", "price_btc")
    for coin in r:
        coin = coin["item"]
        (
            _id,
            coin_id,
            name,
            symbol,
            market_cap_rank,
            _,
            _,
            _,
            _,
            price_btc,
            _,
        ) = coin.values()
        table.add_row(
            _id, str(coin_id), name, symbol, str(market_cap_rank), str(price_btc)
        )
    console.print(table)


if __name__ == "__main__":
    app()

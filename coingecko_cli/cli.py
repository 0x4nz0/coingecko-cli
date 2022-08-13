import httpx
from rich.console import Console
from rich.table import Table
from typer import Typer


console = Console()

app = Typer()


@app.command()
def ping():
    """
    Check API server status
    """
    r = httpx.get("https://api.coingecko.com/api/v3/ping").json()["gecko_says"]
    console.print(r)


@app.command()
def trending():
    """
    Top-7 trending coins on CoinGecko as searched by users in the last 24 hours (Ordered by most popular first)
    """
    r = httpx.get("https://api.coingecko.com/api/v3/search/trending").json()["coins"]
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

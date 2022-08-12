import httpx
from rich import print
from typer import Typer

app = Typer()


@app.command()
def ping():
    """
    Check API server status
    """
    r = httpx.get("https://api.coingecko.com/api/v3/ping").json()["gecko_says"]
    print(r)


@app.command()
def trending():
    """
    Top-7 trending coins on CoinGecko as searched by users in the last 24 hours (Ordered by most popular first)
    """
    r = httpx.get("https://api.coingecko.com/api/v3/search/trending").json()["coins"]
    print(r)


if __name__ == "__main__":
    app()

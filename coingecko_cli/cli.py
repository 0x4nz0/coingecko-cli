import httpx
from rich import print
from typer import Typer

app = Typer()


@app.command()
def ping():
    r = httpx.get("https://api.coingecko.com/api/v3/ping").json()["gecko_says"]
    print(r)


if __name__ == "__main__":
    app()

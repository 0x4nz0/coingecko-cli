=============
CoinGecko CLI
=============

CLI application `Powered by CoinGecko <https://www.coingecko.com/>`_.

-----
Endpoints included
-----

* ping

  * **/ping** : Check API server status::

        coingecko-cli ping

* simple

  * **/simple/price** : Get the current price of any cryptocurrencies in any other supported currencies that you need::

        coingecko-cli simple price <ids> <vs_currencies>

  * **/simple/token_price/{id}** : Get current price of tokens (using contract addresses) for a given platform in any other currency that you need::

        coingecko-cli simple token-price <id> <contract_addresses> <vs_currencies>

  * **/simple/supported_vs_currencies** : Get list of supported_vs_currencies::

        coingecko-cli simple supported-vs-currencies

* coins

  * **/coins/list** : List all supported coins with id, name and symbol (no pagination required)::

        coingecko-cli coins list

  * **/coins/markets** : List all supported coins price, market cap, volume, and market related data::

        coingecko-cli coins markets <vs_currency>

  * **/coins/{id}** : Get current data (name, price, market, ... including exchange tickers) for a coin::

        coingecko-cli coins coin <id>

  * **/coins/{id}/tickers** : Get coin tickers (paginated to 100 items)::

        coingecko-cli coins tickers <id>

  * **/coins/{id}/history** : Get historical data (name, price, market, stats) at a given date for a coin::

      coingecko-cli coins history <id> <date>

  * **/coins/{id}/market_chart** : Get historical market data include price, market cap, and 24h volume (granularity auto)::

      coingecko-cli coins market-chart <id> <vs_currency> <days>

  * **/coins/{id}/market_chart/range** : Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)::

      coingecko-cli coins market-chart-range <id> <vs_currency> <from_date> <to_date>

  * **/coins/{id}/ohlc** : Get coin's OHLC::
    
      coingecko-cli coins ohlc <id> <vs_currency> <days>

* contract

  * **/coins/{id}/contract/{contract_address}** : Get coin info from contract address::

      coingecko-cli contract coin-info <id> <contract_address>

  * **/coins/{id}/contract/{contract_address}/market_chart** : Get historical market data include price, market cap, and 24h volume (granularity auto)::

      coingecko-cli contract market-chart <id> <contract_address> <vs_currency> <days>

  * **/coins/{id}/contract/{contract_address}/market_chart/range** : Get historical market data include price, market cap, and 24h volume within a range of datetime (granularity auto)::

      coingecko-cli contract market-chart-range <id> <contract_address> <vs_currency> <from_date> <to_date>

* asset_platforms

  * **/asset_platforms** : List all asset platforms (Blockchain networks)::

      coingecko-cli asset-platforms

* categories

  * **/coins/categories/list** : List all categories::

      coingecko-cli categories list

  * **/coins/categories** : List all categories with market data::

      coingecko-cli categories market-data

* exchanges

  * **/exchanges** : List all exchanges (Active with trading volumes)::

      coingecko-cli exchanges list

  * **/exchanges/list** : List all supported markets id and name (no pagination required)::

      coingecko-cli exchanges markets-list

  * **/exchanges/{id}** : Get exchange volume in BTC and tickers::

      coingecko-cli exchanges volume <id>

  * **/exchanges/{id}/tickers** : Get exchange tickers (paginated, 100 tickers per page)::

      coingecko-cli exchanges tickers <id>

  * **/exchanges/{id}/volume_chart** : Get volume_chart data for a given exchange::

      coingecko-cli exchange volume-chart <id> <days>

* indexes

  * **/indexes** : List all market indexes::

      coingecko-cli indexes list

  * **/indexes/{market_id}/{id}** : Get market index by market id and index id::

      coingecko-cli indexes market-index <market_id> <id>

  * **/indexes/list** : List market indexes id and name::
    
      coingecko-cli indexes list-id-name

* derivatives

  * **/derivatives** : List all derivative tickers::

      coingecko-cli derivatives tickers

  * **/derivatives/exchanges** : List all derivative exchanges::

      coingecko-cli derivatives exchanges

  * **/derivatives/exchanges/{id}** : Show derivative exchange data::

      coingecko-cli derivatives exchange-data <id>

  * **/derivatives/exchanges/list** : List all derivative exchanges name and identifier::

      coingecko-cli derivatives list

* exchange_rates

  * **/exchange_rates** : Get BTC-to-Currency exchange rates::

      coingecko-cli exchange-rates

* search

  * **/search** : Search for coins, categories and markets listed on CoinGecko ordered by largest Market Cap first::

      coingecko-cli search <query>

* trending

  * **/search/trending** : Top-7 trending coins on CoinGecko as searched by users in the last 24 hours (Ordered by most popular first)::

      coingecko-cli trending

* global

  * **/global** : Get cryptocurrency global data::

      coingecko-cli global data

  * **/global/decentralized_finance_defi** : Get cryptocurrency global decentralized finance(defi) data::

      coingecko-cli global defi

* companies

  * **/companies/public_treasury/{coin_id}** : Get public companies bitcoin or ethereum holdings (Ordered by total holdings descending)::

      coingecko-cli companies-public-treasury <coin_id>

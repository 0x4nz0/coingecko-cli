=============
CoinGecko CLI
=============

CLI application `Powered by CoinGecko <https://www.coingecko.com/>`_.

-----
Endpoints included
-----

* ping

  * **/ping**

* simple

  * **/simple/price**
  * **/simple/token_price/{id}**
  * **/simple/supported_vs_currencies**

* coins

  * **/coins/list**
  * **/coins/markets**
  * **/coins/{id}**
  * **/coins/{id}/tickers**
  * **/coins/{id}/history**
  * **/coins/{id}/market_chart**
  * **/coins/{id}/market_chart/range**
  * **/coins/{id}/ohlc**

* contract

  * **/coins/{id}/contract/{contract_address}**
  * **/coins/{id}/contract/{contract_address}/market_chart**
  * **/coins/{id}/contract/{contract_address}/market_chart/range**

* asset_platforms

  * **/asset_platforms**

* categories

  * **/coins/categories/list**
  * **/coins/categories**

* exchanges

  * **/exchanges**
  * **/exchanges/list**
  * **/exchanges/{id}**
  * **/exchanges/{id}/tickers**
  * **/exchanges/{id}/volume_chart**

* indexes

  * **/indexes**
  * **/indexes/{market_id}/{id}**
  * **/indexes/list**

* derivatives

  * **/derivatives**
  * **/derivatives/exchanges**
  * **/derivatives/exchanges/{id}**
  * **/derivatives/exchanges/list**

* exchange_rates

  * **/exchange_rates**

* search

  * **/search**

* trending

  * **/search/trending**

* global

  * **/global**
  * **/global/decentralized_finance_defi**

* companies

  * **/companies/public_treasury/{coin_id}**

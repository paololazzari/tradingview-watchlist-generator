# Tradingview watchlist generator

A Python 3 program that automates the creation of watchlists in TradingView.
This program uses:

- [selenium](https://github.com/SeleniumHQ/selenium) for opening and managing Chrome
- [autoit](https://github.com/Lonami/autoit) for automating the moving, clicking and typing within Chrome

https://user-images.githubusercontent.com/6552810/158073757-38ab5e46-bc5d-4a49-abc1-f6f4d7ddd50b.mp4

# Requirements

- Windows
- chromedriver

# Installation

```bash
git clone https://github.com/paololazzari/tradingview-watchlist-generator.git
cd tradingview-watchlist-generator
pip install -e .
```

# Usage

Before running the program, make sure that you are logged in TradingView and that you have closed all Chrome processes.

Create a watchlist for the S&P 100:

```bash
tradingview-watchlist-generator --watchlist-name sp100watchlist --index-name sp100
```

Create a watchlist with certain tickers:

```bash
tradingview-watchlist-generator --watchlist-name mywatchlist --ticker-list NASDAQ:AAPL,NYSE:BABA
```

# How it works

The program creates a text document which contains one or more tickers, and then imports it in TradingView to generate a watchlist.

When you specify an index, such as `sp100`, the program looks up the constituents of the index to find the exchange and ticker pairings, such as `NASDAQ:AAPL`.
When you specify a list of tickers, those are used as-is.

## TODOs

* [ ] Support for Linux
* [ ] Release to pypi
* [ ] Setup CI/CD for pypi
* [ ] Add more indexes
* [ ] Add support for coinmarketcap top cryptocurrencies

# Legal

This project has no affiliations with TradingView. It's an open-source tool that intends to help users in creating watchlists within TradingView.

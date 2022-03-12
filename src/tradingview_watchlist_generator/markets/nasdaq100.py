import re

import bs4
import requests

from .indexretriever import IndexRetriever


class Nasdaq100(IndexRetriever):
    _index_data_source = "https://en.wikipedia.org/wiki/Nasdaq-100"

    @property
    def index_data_source(cls):
        return cls._index_data_source

    @property
    def ticker_list(cls):
        """For each constituent of the index, look up the wikipedia
        page to extract the exchange and ticker pair, e.g. NASDAQ:AAPL
        """

        table_of_constituents = cls._table_parser_helper(
            cls.index_data_source, {"id": "id", "name": "constituents"}
        )

        tickers = []
        for row in table_of_constituents.findAll("tr")[1:]:
            partial_ticker = re.sub("\n", "", row.findAll("td")[1].text)

            # All tickers in the NASDAQ100 index are listed on the NASDAQ
            ticker = "NASDAQ:" + partial_ticker
            tickers.append(ticker)

        return ",".join(tickers)

import re

import bs4
import requests

from .indexretriever import IndexRetriever


class SP100(IndexRetriever):
    _index_data_source = "https://en.wikipedia.org/wiki/S%26P_100"

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

            if row.find("a") is None:
                # Alphabet (Class A) does not have a page
                partial_ticker = re.sub("\n", "", row.findAll("td")[0].text)
                tickers.append("NASDAQ:" + partial_ticker)
            else:
                # The tickers in the SP100 are listed on NYSE and NASDAQ
                # For each ticker, find the exchange on which it is listed

                wikipedia_link = re.findall(
                    'href="(\/wiki\/[^"]+)"', str(row.find("a"))
                )[0]
                wikipedia_page = "https://en.wikipedia.org" + wikipedia_link

                table_of_info = cls._table_parser_helper(
                    wikipedia_page, {"id": "class", "name": "infobox vcard"}
                )

                valid_exchanges = ["NYSE", "Nasdaq"]

                ticker = cls.wikipedia_infobox_table_parser(
                    table_of_info, valid_exchanges
                )

                tickers.append(ticker)

        return ",".join(tickers)

import re

import bs4
import requests

from .indexretriever import IndexRetriever


class FTSE100(IndexRetriever):
    _index_data_source = "https://en.wikipedia.org/wiki/FTSE_100_Index"

    @property
    def index_data_source(cls):
        return cls._index_data_source

    @property
    def ticker_list(cls):
        """For each constituent of the index, look up the wikipedia
        page to extract the exchange and ticker pair, e.g. LSE:AZN
        """

        table_of_constituents = cls._table_parser_helper(
            cls.index_data_source, {"id": "id", "name": "constituents"}
        )

        tickers = []
        for row in table_of_constituents.findAll("tr")[1:]:
            # All tickers in the FTSE100 index are listed on the LSE,
            # however some in the table are incorrect as they
            # are missing special characters
            wikipedia_link = re.findall('href="(\/wiki\/[^"]+)"', str(row.find("a")))[0]
            wikipedia_page = "https://en.wikipedia.org" + wikipedia_link

            table_of_info = cls._table_parser_helper(
                wikipedia_page, {"id": "class", "name": "infobox vcard"}
            )

            valid_exchanges = ["LSE"]

            ticker = cls.wikipedia_infobox_table_parser(table_of_info, valid_exchanges)

            tickers.append(ticker)

        return ",".join(tickers)

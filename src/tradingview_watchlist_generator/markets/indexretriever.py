from abc import ABC, abstractmethod

import bs4
import requests
import re


class IndexRetriever(ABC):
    @property
    @abstractmethod
    def index_data_source(self):
        pass

    @property
    @abstractmethod
    def ticker_list(self):
        pass

    def _table_parser_helper(self, url, table):
        """Given a url and a table, return the elements
        of that table
        """
        resp = requests.get(url)
        soup = bs4.BeautifulSoup(resp.text, "html.parser")
        return soup.find("table", {table["id"]: table["name"]})

    def wikipedia_infobox_table_parser(self, table_of_info, valid_exchanges):
        """Given a url, returns the properly formatted exchange
        from the infobox table
        """
        # Find the row in which the ticker symbol data is found.
        table_of_info_rows = table_of_info.findChildren("tr")
        for row in table_of_info_rows:
            if 'title="Ticker symbol"' in str(row):
                break

        li_elements = row.findAll("li")
        a_elements = row.findAll("a")

        if li_elements:
            # Find the row in which the ticker is located
            for i, li in enumerate(li_elements):
                if any(ex in li.text for ex in valid_exchanges):
                    break
            # Concatenate the exchange and the ticker, e.g. NASDAQ:AAPL
            ticker = (
                re.sub(" ?\(?Class [A-Z]:?\)?", "", re.sub("\xa0", "", li.text))
                .upper()
                .strip()
            )
            return ticker

        if a_elements:
            # Find the row in which the ticker is located
            for i, a in enumerate(a_elements):
                if any(ex in a.text for ex in valid_exchanges):
                    break
            # Concatenate the exchange and the ticker, e.g. LSE:AZN
            ticker = ":".join([a_elements[i].text, a_elements[i + 1].text]).upper()
            return ticker

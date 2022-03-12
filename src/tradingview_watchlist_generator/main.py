import argparse
import os
import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from . import validate
from . import controller
from .tradingview import TradingView
from .selenium_helper import SeleniumHelper
from .markets import indexretriever
from .markets import util


def create_watchlist_file(filename, tickers):
    # Create a properly formatted text document for TradingView import
    watchlist_directory = os.path.join(os.getcwd(), "watchlists")
    watchlist_file_path = os.path.join(watchlist_directory, filename + ".txt")
    os.makedirs(os.path.dirname(watchlist_file_path), exist_ok=True)

    try:
        with open(watchlist_file_path, "w") as f:
            f.write(tickers)
    except IOError as e:
        raise IOError(
            f"""
            Could not create watchlist file.
            Do you have write permissions in {watchlist_directory}?
            """
        )


def import_watchlist_routine(t, watchlist_name):
    # Import the watchlist in TradingView
    controller.move_to_location_pause_click(t.toolbar_position, t.menu_loading_time)
    controller.move_to_location_pause_click(t.settings_position, t.menu_loading_time)
    controller.move_to_location_pause_click(
        t.import_watchlist_position, t.menu_loading_time
    )
    controller.get_watchlist_file(watchlist_name)
    controller.move_to_location_pause_click(t.toolbar_position, t.menu_loading_time)


def main():
    validate.validate_setup()

    parser = argparse.ArgumentParser("Required arguments")
    parser.add_argument("--watchlist-name", required=True)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--index-name", choices=list(util.get_supported_indexes()))
    group.add_argument("--ticker-list")

    args = parser.parse_args()
    validate.validate_args(args)

    index_name = args.index_name
    watchlist_name = args.watchlist_name
    ticker_list = args.ticker_list

    if ticker_list is not None:
        validate.validate_ticker_list(ticker_list)
        tickers = ticker_list
    else:
        supported_indexes = util.get_supported_indexes()
        index = supported_indexes[index_name]()
        tickers = index.ticker_list

    create_watchlist_file(watchlist_name, tickers)
    s = SeleniumHelper()
    t = TradingView()
    s.setup_chrome_window()
    s.driver.get(t.homepage)
    import_watchlist_routine(t, watchlist_name)


if __name__ == "__main__":
    main()

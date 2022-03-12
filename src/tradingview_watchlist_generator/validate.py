from shutil import which
import sys
import os
import re

import psutil

from .selenium_helper import get_chrome_userdata_dir


def validate_args(args):
    # Index name or tickers must be specified
    if all(arg is None for arg in [args.index_name, args.ticker_list]):
        print("Either index name or tickers must be specified.")
        sys.exit(1)


def validate_ticker_list(ticker_list):
    # Only certain chars are allowed
    if re.search("[^A-Z:,]", ticker_list) is not None:
        print("Only alphabetical chars, colons, and commas are allowed.")
        sys.exit(1)

    # The comma separated elements must be in the form
    # exchange, ":", ticker
    split_tickers = ticker_list.split(",")
    for ticker in split_tickers:
        if re.match("^[A-Z]+:[A-Z]+$", ticker) is None:
            print(
                "The specified tickers are invalid.\n"
                "The format must be EXCHANGE:TICKER, e.g. NASDAQ:AAPL,NASDAQ:AMZN"
            )
            sys.exit(1)


def check_chrome_driver_exists():
    # If chromedriver isn't on the path, exit
    if which("chromedriver") is None:
        print("chromedriver not found on path!")
        sys.exit(1)


def check_chrome_userdata_dir_path_exists():
    # Check if chrome user data exists
    if not os.path.isdir(get_chrome_userdata_dir()):
        print("User Data folder does not exist!")
        sys.exit(1)


def check_chrome_is_closed():
    # Make sure that there are no Chrome processes running
    for proc in psutil.process_iter(["name"]):
        if proc._name == "chrome.exe":
            print("All Chrome processes must be closed!")
            sys.exit(1)


def validate_setup():
    check_chrome_driver_exists()
    check_chrome_userdata_dir_path_exists()
    check_chrome_is_closed()

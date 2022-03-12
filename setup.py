import os

from setuptools import setup, find_packages

VERSION = "0.0.1"

setup(
    name="tradingview-watchlist-generator",
    version=VERSION,
    author="Paolo Lazzari",
    author_email="lazzari.paolok@gmail.com",
    url="https://github.com/paololazzari/tradingview-watchlist-generator",
    description="Tool for automatically creating tradingview watchlists",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "selenium==4.1.2",
        "autoit==0.2.4",
        "requests==2.27.1",
        "beautifulsoup4==4.10.0",
        "psutil==5.9.0",
    ],
    entry_points={
        "console_scripts": [
            "tradingview-watchlist-generator=tradingview_watchlist_generator.main:main"
        ],
    },
    zip_safe=False,
)

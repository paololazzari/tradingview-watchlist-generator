class TradingView:
    def __init__(self):

        self.homepage = "https://www.tradingview.com"

        # Absolute positions of elements on screen for automation of clicks
        self.toolbar_position = (0.97, 0.16)
        self.settings_position = (0.935, 0.16)
        self.import_watchlist_position = (0.935, 0.35)

        # Loading time for TradingView components
        self.main_page_loading_time = 8
        self.menu_loading_time = 3

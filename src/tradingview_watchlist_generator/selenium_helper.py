import os
from shutil import which

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_chrome_userdata_dir():
    appdata_path = os.getenv("LOCALAPPDATA")
    return os.path.join(appdata_path, "Google", "Chrome", "User Data")


class SeleniumHelper:
    def __init__(self):
        chrome_options = Options()
        chrome_driver_path = which("chromedriver")
        chrome_userdata_dir_path = get_chrome_userdata_dir()
        chrome_options.add_argument("profile-directory=Default")
        chrome_options.add_argument(f"user-data-dir={chrome_userdata_dir_path}")
        self.driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)

    def setup_chrome_window(self):
        # Force Chrome window on primary monitor, and maximize it
        self.driver.set_window_position(0, 0)
        self.driver.maximize_window()

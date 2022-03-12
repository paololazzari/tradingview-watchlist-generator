import time
import os
import ait


def move_to_location_pause_click(location, pause_time):
    # Move to a certain place, wait, and click
    ait.move(*location)
    time.sleep(pause_time)
    ait.click()
    time.sleep(pause_time)


def get_watchlist_file(filename):
    # Type in and select the file with the contents of the watchlist
    working_directory = os.getcwd()
    ait.write(working_directory + "\\" + "watchlists" + "\\")
    ait.write(filename)
    ait.press("DECIMAL")
    ait.press(*"txt")
    ait.press("enter")

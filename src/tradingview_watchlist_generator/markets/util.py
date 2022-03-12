from .nasdaq100 import Nasdaq100
from .sp100 import SP100
from .ftse100 import FTSE100


def get_supported_indexes():
    return dict({"nasdaq100": Nasdaq100, "sp100": SP100, "ftse100": FTSE100})

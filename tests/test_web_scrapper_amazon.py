from collections import namedtuple
import bs4
from ..code.web.scraper.scrap.amazon import get_url_amazon, scrap_amazon
from . import setup_get_driver_details


def test_get_url_amazon():
    description = namedtuple("description", "title price")
    description.title = "2021 Apple 10.2-inch iPad (Wi-Fi 256GB) - Silver"
    description.price = "478.99"
    url = get_url_amazon(description)
    assert (url == "https://www.amazon.com/s?k=2021%20Apple%2010.2-inch%20iPad%20%28Wi-Fi%20256GB%29%20-%20Silver&ref"
                   "=nb_sb_noss")


def test_scrap_amazon():
    description = namedtuple("description", "title price")
    description.title = "2021 Apple 10.2-inch iPad (Wi-Fi 256GB) - Silver"
    description.price = "478.99"
    result = scrap_amazon(description)
    result_type = isinstance(result, bs4.element.ResultSet)
    assert result_type is True

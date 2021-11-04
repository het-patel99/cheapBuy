from collections import namedtuple
from ..code.web.scraper.scrap.ebay import get_url_ebay, scrap_ebay, extract_item_ebay
import bs4
from . import setup_get_driver_details


def test_get_url_ebay():
    description = namedtuple("description", "title price")
    description.title = 'PS5 IN HAND - NEW Playstation 5 Digital Edition White Console System LATEST'
    description.price = '899.00'
    link = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=PS5%20IN%20HAND%20-%20NEW%20Playstation%205%20Digital%20" \
           "Edition%20White%20Console%20System%20LATEST&_sacat=0&rt=nc&_udlo=0&_udhi=899.00"
    assert (get_url_ebay(description) == "https://www.ebay.com/sch/i.html?_from=R40&_nkw=PS5%20IN%20HAND%20-%20NEW%20"
                                         "Playstation%205%20Digital%20Edition%20White%20Console%20System%20LATEST"
                                         "&_sacat=0&rt=nc&_udlo=0&_udhi=899.00")


def test_scrap_ebay():
    description = namedtuple("description", "title price")
    description.title = 'PS5 IN HAND - NEW Playstation 5 Digital Edition White Console System LATEST'
    description.price = '899.00'
    result = scrap_ebay(description)
    result_type = isinstance(result, bs4.element.ResultSet)
    assert result_type is True

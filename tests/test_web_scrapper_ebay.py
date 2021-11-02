from ..code.web.scraper.scrap.ebay import get_url_ebay, scrap_ebay, extract_item_ebay
from . import setup_get_driver_details

def test_get_url_ebay_1():
    item_name = "2021 Apple 10 2 inch iPad Wi Fi"
    search_term = item_name.replace("%20", " ")
    assert get_url_ebay(item_name) == f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={search_term}"


def test_get_url_ebay_2():
    item_name = "Brita Longlast Replacement Filters Dispensers"
    search_term = item_name.replace("%20", " ")
    assert get_url_ebay(item_name) == f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={search_term}"

def test_scrap_ebay():
    item_name = "W. Trends Sunset Twin-Size Metal Bunk Bed - Black"
    results = scrap_ebay(setup_get_driver_details(), item_name)
    assert results is not None

# def test_extract_item_ebay_result_len():
#     item_name = "Brita Longlast Replacement Filters Dispensers"
#     result = extract_item_ebay(setup_get_driver_details(), item_name)
#     assert len(result) == 4
#
# def test_extract_item_ebay_result_site():
#     item_name = "Amazfit Band 5 Fitness Tracker with Alexa Built-in"
#     result = extract_item_ebay(setup_get_driver_details(), item_name)
#     assert result["site"] == "ebay"
#
# def test_extract_item_ebay_result_url():
#     item_name = "SAMSUNG Galaxy Tab A7 32GB"
#     result = extract_item_ebay(setup_get_driver_details(), item_name)
#     assert result["url"].find("https://www.ebay.com") != -1

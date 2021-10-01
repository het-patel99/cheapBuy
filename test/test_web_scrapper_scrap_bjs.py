import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper import scrapper

def test_scrapper_bjs_result():
    result = scrapper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert result is not None

def test_scrapper_bjs_result_len():
    result = scrapper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert len(result) == 4

def test_scrapper_bjs_result_description_count():
    result = scrapper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert len(result["description"]) == 2

def test_scrapper_bjs_result_site():
    result = scrapper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert result["site"] == ["amazon","ebay"]

def test_scrapper_bjs_result_url_ebay():
    result = scrapper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert result["url"][1].find("ebay") != -1

def test_scrapper_bjs_result_url_amazon():
    result = scrapper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert result["url"][0].find("amazon") != -1

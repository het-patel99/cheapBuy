import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper import scrapper

def test_scrapper_bjs_result():
    result = scrapper("https://www.bjs.com/product/apple-ipad-pro-11-3rd-generation-256gb-wi-fi---space-gray/3000000000001510763")
    assert result is not None

def test_scrapper_bjs_result_len():
    result = scrapper(
        "https://www.bjs.com/product/tide-ultra-concentrated-liquid-laundry-detergent-208-fl-oz/3000000000002203255")
    assert len(result) == 4

def test_scrapper_bjs_result_description_count():
    result = scrapper(
        "https://www.bjs.com/product/berkley-jensen-ultra-strong-bath-tissue-24-ct/3000000000001957283")
    assert len(result["description"]) == 2

def test_scrapper_bjs_result_site():
    result = scrapper(
        "https://www.bjs.com/product/samsung-55-q6da-qled-4k-smart-tv---qn55q6daafxza-with-your-choice-subscription-and-3-year-warranty/3000000000003018763")
    assert result["site"] == ["amazon","ebay"]

def test_scrapper_bjs_result_url_ebay():
    result = scrapper(
        "https://www.bjs.com/product/huggies-little-snugglers-baby-diapers/3000000000002993748")
    assert result["url"][1].find("ebay") != -1

def test_scrapper_bjs_result_url_amazon():
    result = scrapper(
        "https://www.bjs.com/product/microsoft-surface-laptop-3-intel-core-i5-processor-8gb-memory-256gb-ssd/3000000000003180287")
    assert result["url"][0].find("amazon") != -1

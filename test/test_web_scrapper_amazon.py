from code.web_scrappers import web_scrapper_amazon
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def setup_get_driver_details():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    return driver


def test_get_url_amazon_1():
    item_name = "2021 Apple 10 2 inch iPad Wi Fi"
    assert web_scrapper_amazon.get_url_amazon(item_name) == "https://www.amazon.com/s?k=2021+Apple+10+2+inch+iPad+Wi+Fi&ref=nb_sb_ss_ts-doa-p_3_5"


def test_get_url_amazon_2():
    assert web_scrapper_amazon.get_url_amazon("Brita Longlast Replacement Filters Dispensers") == "https://www.amazon.com/s?k=Brita+Longlast+Replacement+Filters+Dispensers&ref=nb_sb_ss_ts-doa-p_3_5"


def test_scrap_amazon():
    item_name = "W. Trends Sunset Twin-Size Metal Bunk Bed - Black"
    results = web_scrapper_amazon.scrap_amazon(setup_get_driver_details(), item_name)
    assert results is not None


def test_extract_item_amazon_result_len():
    item_name = "Brita Longlast Replacement Filters Dispensers"
    result = web_scrapper_amazon.extract_item_amazon(setup_get_driver_details(),item_name)
    assert len(result) == 4


def test_extract_item_amazon_result_site():
    item_name = "Amazfit Band 5 Fitness Tracker with Alexa Built-in"
    result = web_scrapper_amazon.extract_item_amazon(setup_get_driver_details(),item_name)
    assert result["site"] == "amazon"


def test_extract_item_amazon_result_url():
    item_name = "SAMSUNG Galaxy Tab A7 32GB"
    result = web_scrapper_amazon.extract_item_amazon(setup_get_driver_details(),item_name)
    assert result["url"].find("https://www.amazon.com") != -1

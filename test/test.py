from test_web_scrapper_amazon import *
from test_web_scrapper_ebay import *

def test_web_scrappers():
    test_get_url_amazon_1()
    test_get_url_amazon_2()
    test_scrap_amazon()
    test_extract_item_amazon_result_len()
    test_extract_item_amazon_result_site()
    test_extract_item_amazon_result_url()

    test_get_url_ebay_1()
    test_get_url_ebay_2()
    test_scrap_ebay()
    test_extract_item_ebay_result_len()
    test_extract_item_ebay_result_site()
    test_extract_item_ebay_result_url()

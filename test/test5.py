import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_scrap_walmart import *
from cheapBuy.test.test_web_scrapper_scrap_amazon import *
from cheapBuy.test.test_web_scrapper_scrap_ebay import *


def test_answer():
    test_scrapper_walmart_result()
    test_scrapper_walmart_result_len()
    test_scrapper_amazon_result()
    test_scrapper_amazon_result_len()
    test_scrapper_amazon_result_description_count()
    test_scrapper_amazon_result_site_ebay()
    test_scrapper_amazon_result_url_ebay()
    test_scrapper_ebay_result()
    test_scrapper_ebay_result_len()
    test_scrapper_ebay_result_description_count()
    test_scrapper_ebay_result_site_amazon()
    test_scrapper_ebay_result_url_amazon()
    
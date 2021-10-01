import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_scrap_ebay import *


def test_answer():
    test_scrapper_ebay_result()
    test_scrapper_ebay_result_len()
    test_scrapper_ebay_result_description_count()
    test_scrapper_ebay_result_site_amazon()
    test_scrapper_ebay_result_url_amazon()
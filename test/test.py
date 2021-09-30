import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_ebay import *
from cheapBuy.test.test_web_scrapper import *

def test_answer():
   # test_web_scrapper.py
   test_get_driver()

   # test_web_scrapper_ebay.py
   test_get_url_ebay_1()
   test_get_url_ebay_2()
   test_scrap_ebay()
   test_extract_item_ebay_result_len()
   test_extract_item_ebay_result_site()
   test_extract_item_ebay_result_url()
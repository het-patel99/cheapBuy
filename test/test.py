import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_ebay import *
from cheapBuy.test.test_web_scrapper import *
from cheapBuy.test.test_server_api import *

def test_answer():
   # test_web_scrapper.py
   test_get_driver()

   # test_server_api.py
   test_post_result()
   test_post_result_status()
   test_post_result_response_ebay()
   test_post_result_response_bjs()
   test_post_result_response_amazon()
   test_post_result_response_costco()
   test_post_result_response_walmart()

   # test_web_scrapper_ebay.py
   test_get_url_ebay_1()
   test_get_url_ebay_2()
   test_scrap_ebay()
   test_extract_item_ebay_result_len()
   test_extract_item_ebay_result_site()
   test_extract_item_ebay_result_url()
import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_amazon import *
from cheapBuy.test.test_web_scrapper_walmart import *
from cheapBuy.test.test_web_scrapper_bjs import *


def test_answer():
   # test_web_scrapper_amazon.py
   test_get_url_amazon_1()
   test_get_url_amazon_2()
   test_scrap_amazon()

   # test_web_scrapper_walmart.py
   test_get_url_walmart_1()
   test_get_url_walmart_2()
   test_scrap_walmart()

   # test_web_scrapper_bjs.py
   test_get_url_bjs_1()
   test_get_url_bjs_2()
   test_scrap_bjs()
import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_amazon import *

def test_answer():
   # test_web_scrapper_amazon.py
   test_get_url_amazon_1()
   test_get_url_amazon_2()
   test_scrap_amazon()
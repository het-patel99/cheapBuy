import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_fetch_description_walmart import *
from cheapBuy.test.test_fetch_description_ebay import *
from cheapBuy.test.test_fetch_description_amazon import *
from cheapBuy.test.test_fetch_description_bjs import *
from cheapBuy.test.test_fetch_description_costco import *

def test_answer():
   test_fetch_description_walmart1()
   test_fetch_description_walmart2()
   test_fetch_description_amazon1()
   test_fetch_description_amazon2()
   test_fetch_description_bjs1()
   test_fetch_description_bjs2()
   test_fetch_description_ebay_1()
   test_fetch_description_ebay_2()
   test_fetch_description_costco1()
   test_fetch_description_costco2()

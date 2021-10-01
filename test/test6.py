import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_scrap_bjs import *
from cheapBuy.test.test_web_scrapper_scrap_costco import *


def test_answer():
    test_scrapper_bjs_result()
    test_scrapper_bjs_result_len()
    test_scrapper_costco_result()
    test_scrapper_costco_result_len()
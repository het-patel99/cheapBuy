import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_scrap_walmart import *
from cheapBuy.test.test_web_scrapper_scrap_amazon import *


def test_answer():
	test_scrapper_walmart_result()
	test_scrapper_walmart_result_len()
    
    test_scrapper_amazon_result()
    test_scrapper_amazon_result_len()
    test_scrapper_amazon_result_description_count()
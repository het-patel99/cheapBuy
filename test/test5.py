import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_web_scrapper_scrap_walmart import *


def test_answer():
	test_scrapper_walmart_result()
	test_scrapper_walmart_result_len()
	test_scrapper_walmart_result_description_count()
	test_scrapper_walmart_result_site()
	test_scrapper_walmart_result_url_ebay()
	test_scrapper_walmart_result_url_amazon()
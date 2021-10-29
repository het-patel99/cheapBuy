from ..code.web.scraper.web_scraper import scraper

def test_scrapper_bjs_result():
    result = scraper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert result is not None

def test_scrapper_bjs_result_len():
    result = scraper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert len(result) == 4
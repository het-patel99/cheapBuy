from ..code.web.scraper.web_scraper import get_driver

def test_get_driver():
    assert get_driver() is not None
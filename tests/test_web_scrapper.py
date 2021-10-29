from ..code.web.scraper.web_scraper import scraper

def test_get_driver():
    assert scraper() is not None
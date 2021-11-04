from ..code.web.scraper.web_scraper import scraper


def test_scrapper_costco_result():
    result = scraper(
        "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
    )
    assert result is not None


def test_scrapper_costco_result_len():
    result = scraper(
        "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
    )
    assert len(result) == 4

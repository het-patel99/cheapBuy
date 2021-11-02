from ..code.web.scraper.web_scraper import scraper


def test_scrapper_walmart_result():
    result = scraper(
        "https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038"
    )
    assert result is not None


def test_scrapper_walmart_result_len():
    result = scraper(
        "https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038"
    )
    assert len(result) == 4

import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper import scrapper


def test_scrapper_walmart_result():
    result = scrapper("https://www.walmart.com/ip/PUMA-SAFETY-SHOES-642865-Athltc-Style-Wrk-Shoes-9-1-2C-Gry-Pnk-PR/113851508")
    assert result is not None

def test_scrapper_walmart_result_len():
    result = scrapper(
        "https://www.walmart.com/ip/Straight-Talk-Apple-iPhone-11-Pro-64GB-Midnight-Green-Prepaid-Smartphone/544554428")
    assert len(result) == 4

def test_scrapper_walmart_result_description_count():
    result = scrapper(
        "https://www.walmart.com/ip/Great-Value-Whole-Vitamin-D-Milk-Gallon-128-fl-oz/10450114?athcpid=10450114&athpgid=AthenaHomepageDesktop&athcgid=null&athznid=bs&athieid=v0&athstid=CS020&athguid=Fix4gTw_m5jcFbkeoVd_UhOcXoh9Q1uYCMfW&athancid=null&athena=true")
    assert len(result["description"]) == 2

def test_scrapper_walmart_result_site():
    result = scrapper(
        "https://www.walmart.com/ip/Lenovo-IdeaPad-1-14-0-Laptop-Intel-Pentium-Silver-N5030-Quad-Core-Processor-4GB-Memory-128GB-Solid-State-Drive-Windows-10S-Ice-Blue-81VU000JUS/198284484")
    assert result["site"] == ["amazon","ebay"]

def test_scrapper_walmart_result_url_ebay():
    result = scrapper(
        "https://www.walmart.com/ip/Great-Value-Plain-Salt-26-oz/10448311")
    assert result["url"][1].find("ebay") != -1

def test_scrapper_walmart_result_url_amazon():
    result = scrapper(
        "https://www.walmart.com/ip/M-M-s-Peanut-Milk-Chocolate-Peanut-Butter-Full-Size-Halloween-Chocolate-Candy-Bars-30-58oz-18ct-Count-Box/397639069")
    assert result["url"][0].find("amazon") != -1

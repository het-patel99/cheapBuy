import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper import scrapper


def test_scrapper_ebay_result():
    result = scrapper("https://www.ebay.com/itm/194247858048?hash=item2d3a131780:g:DWQAAOSwf7Bg9beR")
    assert result is not None

def test_scrapper_ebay_result_len():
    result = scrapper(
        "https://www.ebay.com/itm/333961459415?var=543008787203&_trkparms=%26rpp_cid%3D5cc74708067a454c1b52f1f5%26rpp_icid%3D5cc74708067a454c1b52f1f4")
    assert len(result) == 4

def test_scrapper_ebay_result_description_count():
    result = scrapper(
        "https://www.ebay.com/itm/284464988272?var=586022769402&_trkparms=ispr%3D1&hash=item423b6f4070:g:Ea8AAOSwSRxhT2N~&amdata=enc%3AAQAGAAACoPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsSwcmzw5CLtzTE60FqHcnq2KYEl5z5jIqWk%252BzS%252BcSt1fZJKwFcRzPXe26H8Hu32BrgEjJ8NGyes66oHMPipf%252FKAQXhp%252F3zlgijqE5Sa0ze2w1uGs8rzBf%252FcONaH20qXl%252FW4VdHAlO31fPj%252FYqsf1aRuCT9XuJsOSL%252F70Z7Segq%252F6QvNOYsEcVZcW9fzGkyiADfzWbwRhqJo3RRzRa6VMI3njjOIyOOYWayiegF4YPD5kLmQ95JAhCSxXB9CTzGBTfoUPPPXqq9xg7pjqLK%252F1q36FZZnc5165h1gM%252FmGu5Et1imWmH2yRpofN0JsIHSKVxSy9Lpz3mvz%252BUnhsJdqb%252BiENrrafOxLFI4qz%252F5%252BLE18LkXdYTENCBod6ZNdQuyBhnYk8HuH09g3WRfMiU6QuRkwe1CklH1vnKHWTS7HwWyg6XPWIWk6illjJQwBe21PjHfITet3r6U1CTtRZGEWxJH%252FlzmOn9If1y2PpBXAsS4dn%252FO7Rz3rwZrZ5pFMMzjNz3Ud7hoOq8CqnxgyAvMQExluTWQFdHuiKFj5GfJpH%252FHcmwMnMaR%252B%252FFCKnXbuOMwR%252FSqqiZVPtVw7CN9Cv1dV5uDIHgbZuWn6BLSYSorS3jZmZhGwmaMWXDLcFz5QgRS3szTO8M6d8dIsMmSMfpJbBARsVvFKvzqHYHCahdTieJ3YpHQuBFmnKzjioBW%252FWW7R2qdMA04cyf4pHjw6PcHV%252FG%252FNpc0l50z2fjt5OphHRMTsifuVjFH5RhJJTw60z6PNAsoJDsO7YuystgaCQzvbN1WweQbmfxCfs7tWEV5z85G85oFaL%252FUXo25PlUUmobyDie6InWliswC1tOS4PXh86xZug%253D%253D%7Campid%3APL_CLK%7Cclp%3A2334524")
    assert len(result["description"]) == 1

def test_scrapper_ebay_result_site_amazon():
    result = scrapper(
        "https://www.ebay.com/itm/124505970766?epid=2267631590&hash=item1cfd22584e:g:g1QAAOSwnRpf61AF")
    assert result["site"] == ["amazon"]

def test_scrapper_ebay_result_url_amazon():
    result = scrapper(
        "https://www.ebay.com/itm/164391405049?_trkparms=amclksrc%3DITM%26aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20180816085401%26meid%3D1c7bfba98c9b4088af22371e909970c3%26pid%3D100970%26rk%3D2%26rkt%3D9%26sd%3D124505970766%26itm%3D164391405049%26pmt%3D1%26noa%3D1%26pg%3D2380057&_trksid=p2380057.c100970.m5481&_trkparms=pageci%3A3086d43a-2216-11ec-bab2-0621da914732%7Cparentrq%3A37cf970417c0a21958a35ecafff4a07a%7Ciid%3A1")
    assert result["url"][0].find("amazon") != -1

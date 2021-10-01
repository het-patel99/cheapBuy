import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.fetch_description_costco import description_from_url_costco


def test_fetch_description_costco1():
    link = "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
    assert description_from_url_costco(link) == "brita replacement filters%2c 10 pack"


def test_fetch_description_costco2():
    link = "https://www.costco.com/tide-advanced-power-ultra-concentrated-liquid-laundry-detergent-with-oxi%2c-original%2c-81-loads%2c-150-fl-oz.product.100414600.html"
    description = description_from_url_costco(link)
    assert description == "tide advanced power ultra concentrated liquid laundry detergent with oxi%2c original%2c 81 loads%2c 150 fl oz' == 'new apple ipad pro 12.9%e2%80%9d 512gb (5th gen)"

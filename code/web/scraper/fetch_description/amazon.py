from collections import namedtuple
import requests
from typing import NamedTuple
from bs4 import BeautifulSoup


def description_from_url_amazon(link: str) -> NamedTuple:
    """
    Returns product title and price by scraping

    Parameters
    ----------
    link : str
        website url

    Returns
    -------
    description: NamedTuple
        NamedTuple named Description, contains product title and price

    Raises
    ------
    ConnectionRefusedError
        when website does not allow scraping
    """
    try:
        headers = {'Host': 'www.amazon.com',
                   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/44.0.2403.157 Safari/537.36',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1', 'TE': 'Trailers'}
        webpage = requests.get(link, headers=headers)
        if webpage.status_code == 200:
            soup = BeautifulSoup(webpage.content, "lxml")
            product_title = soup.find("span", attrs={"id": "productTitle"})
            product_title_string = product_title.string.strip().replace(',', '')
            print(F"Extracted title: {product_title_string}")
            product_price = soup.find("span", attrs={"class": "a-offscreen"})
            print(F"Extracted price: {product_price.string}")
            description = namedtuple("Description", "title price")
            return description(product_title_string, product_price.string.replace('$', ''))
        else:
            raise ConnectionRefusedError("Website does not allow scraping")
    except Exception as e:
        print(e)
        return None


from collections import namedtuple
import requests
from typing import NamedTuple
from bs4 import BeautifulSoup


def description_from_url_ebay(link: str) -> NamedTuple:
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
    """
    try:
        headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, "
                                 "like Gecko) Chrome/90.0.4430.93 Safari/537.36 "}
        html = requests.get(link, headers=headers)
        if html.status_code == 200:
            soup = BeautifulSoup(html.content, "html.parser")
            # print(soup.prettify())
            product = soup.find("div", {"class": "vi-swc-lsp"}, {"id": "itemTitle"})
            title = product.find("span", class_="u-dspn").text.strip()
            print(F"Extracted title: {title}")
            price_ = soup.find("div", {"class": "u-flL w29 vi-price"}, {"id": "vi-mskumap-none"})
            price = price_.find("span", class_="notranslate").text.strip('US $')
            print(F"Extracted price: {price}")
            description = namedtuple("Description", "title price")
            return description(title, price)
        else:
            raise ConnectionRefusedError("Website does not allow scraping")
    except Exception as e:
        print(e)
        return None

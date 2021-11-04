from collections import namedtuple
import requests
from typing import NamedTuple
from bs4 import BeautifulSoup


def description_from_url_costco(chrome, link):
    """
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
    description = ""
    try:
        chrome.get(link)
        innerHTML = chrome.page_source
        soup = BeautifulSoup(innerHTML, "html.parser")
        product_title = soup.find('meta', property="og:description").get('content')
        print(product_title)
        product_price = soup.find('span', class_="op-value")
        print(product_price.text)
        remove_initial = link.replace("https://www.costco.com/", "")
        for i in remove_initial:
            if i != ".":
                description += i
            else:
                break
        description = description.replace("-", " ")
        print(
            f"Extracted item/search_term/description to be searched:\n >>{description}<<"
        )
    except:
        print("Can't pull the description from costco url.")
        description = ""
    print("-" * 10)
    return description

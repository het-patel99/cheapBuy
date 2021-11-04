import bs4.element
import requests
from typing import NamedTuple
import urllib.parse
from bs4 import BeautifulSoup


class NoProductsFoundError(Exception):
    def __init__(self, message="No matching products found"):
        self.message = message
        super().__init__(self.message)


def get_url_ebay(search_term: NamedTuple) -> str:
    """
    Returns an ebay search url, which is built using product description like title and price

    Parameters
    ----------
    search_term: NamedTuple
        NamedTuple named Description, contains product title and price

    Returns
    -------
    template : str
        ebay search url for the selected product
    """
    modified_search_term = urllib.parse.quote(str(search_term.title))
    template = F"https://www.ebay.com/sch/i.html?_from=R40&_nkw={modified_search_term}&_sacat=0&rt=nc&_udlo=0&_udhi=" \
               F"{search_term.price}"
    print(f"Constructed Ebay URL:\n{template}")
    return template


def scrap_ebay(search_term: NamedTuple) -> bs4.element.ResultSet:
    """
    Returns search results obtained for the search url generated in ``get_url_ebay``

    Parameters
    ----------
    search_term: NamedTuple
        NamedTuple named Description, contains product title and price

    Returns
    -------
    results : bs4.element.ResultSet
        BeautifulSoup ResultSet containing the list of matching products

    Raises
    ------
    ConnectionRefusedError
        when website does not allow scraping
    """
    try:
        url = get_url_ebay(search_term)
        # driver.get(url)
        page = requests.get(url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'lxml')
            results = soup.find_all("li", attrs={"class": "s-item s-item__pl-on-bottom s-item--watch-at-corner"})
            return results
        else:
            raise ConnectionRefusedError(F"{page.status_code}: Unable to scrape the website")
    except Exception as e:
        print(e)
        return None


def extract_item_ebay(search_term: NamedTuple) -> dict:
    """
    Returns a dictionary containing product title, price, url and website

    Parameters
    ----------
    search_term: NamedTuple
        NamedTuple named Description, contains product title and price

    Returns
    -------
    result : dict
        dictionary containing product title, url, price, website
    """
    result = {}
    try:
        results = scrap_ebay(search_term)
        if results is not None:
            if len(results) != 0:
                print(F"Found {len(results)} items on the Ebay, picking the 1st one.")
                item = results[0]
                atag = item.find("a", {"class": "s-item__link"})
                result['description'] = item.find("h3", {"class": "s-item__title"}).get_text().strip()
                result['url'] = atag.get('href')
                result['price'] = item.find("span", {"class": "s-item__price"}).get_text().strip().strip('$')
                result['site'] = 'ebay'
                print(F"result: {result}")
                return result
            else:
                raise NoProductsFoundError
        else:
            raise Exception("Scraping failed on ebay")
    except Exception as e:
        print(e)
        return result


from difflib import SequenceMatcher
from collections import namedtuple
import bs4
import requests
from typing import NamedTuple
import urllib.parse
from bs4 import BeautifulSoup


class NoProductsFoundError(Exception):
    def __init__(self, message="No matching products found"):
        self.message = message
        super().__init__(self.message)


def get_url_amazon(search_term: NamedTuple) -> str:
    """
    Returns an amazon search url, which is built using product description like title and price

    Parameters
    ----------
    search_term: NamedTuple
        NamedTuple named Description, contains product title and price

    Returns
    -------
    template : str
        amazon search url for the selected product
    """
    modified_search_term = urllib.parse.quote(str(search_term.title))
    template = F"https://www.amazon.com/s?k={modified_search_term}&ref=nb_sb_noss"
    print(f"Constructed amazon URL: \n {template}")
    return template


def scrap_amazon(search_term: NamedTuple) -> bs4.element.ResultSet or None:
    """
    Returns search results obtained for the search url generated in ``get_url_amazon``

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
        url = get_url_amazon(search_term)
        # driver.get(url)
        headers = {'Host': 'www.amazon.com',
                   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/44.0.2403.157 Safari/537.36',
                   'Accept-Language': 'en-US, en;q=0.5',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br',
                   'Connection': 'keep-alive',
                   'Upgrade-Insecure-Requests': '1', 'TE': 'Trailers'}
        page = requests.get(url, headers=headers)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'lxml')
            results = soup.find_all('div', {'data-component-type': 's-search-result'})
            return results
        else:
            raise ConnectionRefusedError(F"{page.status_code}: Unable to scrape the website")
    except Exception as e:
        print(e)
        return None


def find_best_matching_product(search_term: NamedTuple, results: bs4.element.ResultSet) -> bs4.element.Tag:
    """
    The method tries to find the best matching product on amazon using longest sequence matching method
    Amazon usually places sponsored products at the beginning of search results, to circumvent this given
    product title is matched with amazon's result set, result with longest match is returned

    Parameters
    ----------
    search_term: NamedTuple
        NamedTuple named Description, contains product title and price

    results: bs4.element.ResultSet
        BeautifulSoup ResultSet containing the list of matching products

    Returns
    -------
    best_match_product: bs4.element.Tag
        BeautifulSoup element tag which contains product title, price, url
    """
    max_match_len = 0
    best_match_product = ''
    for result in results:
        sponsored = result.find("span", attrs={"class": "s-label-popover-hover"})
        if sponsored:
            continue
        else:
            desc = result.find("span", attrs={"class": "a-size-medium a-color-base a-text-normal"})
            if desc is not None:
                title = desc.text.strip()
                str_1 = search_term.title
                seq_match = SequenceMatcher(None, str_1, title)
                match = seq_match.find_longest_match(0, len(str_1), 0, len(title))
                if match.size > max_match_len:
                    max_match_len = match.size
                    best_match_product = result
    return best_match_product


def extract_item_amazon(search_term: NamedTuple) -> dict:
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
        results = scrap_amazon(search_term)
        if results is not None:
            if len(results) != 0:
                print(f'Found {len(results)} items on the amazon, picking the nearest matching one.')
                item = find_best_matching_product(search_term, results)
                result['description'] = item.find("span", attrs={"class": "a-size-medium a-color-base a-text-normal"}).text
                item_link = item.find(class_="a-link-normal s-underline-text s-underline-link-text a-text-normal", href=True)
                result['url'] = F"https://www.amazon.com/{item_link}"
                result['price'] = item.find('span', {"class": "a-offscreen"}).text.strip('$')
                result['site'] = 'amazon'
                print(result)
                return result
            else:
                raise NoProductsFoundError
        else:
            raise Exception("Scraping failed on Amazon")
    except Exception as e:
        print(e)
        return result


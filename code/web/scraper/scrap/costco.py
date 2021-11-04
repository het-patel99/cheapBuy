import requests
import urllib.parse
from bs4 import BeautifulSoup


def get_url_costco(search_term):
    """
    Parameters
    ----------
    search_term: NamedTuple
        NamedTuple named Description, contains product title and price

    Returns
    -------
    template : str
        costco search url for the selected product
    """
    modified_search_term = urllib.parse.quote(str(search_term.title))
    url = F"https://www.costco.com/CatalogSearch?dept=All&keyword={modified_search_term}"
    print(f"Constructed Costco's URL: \n {url}")
    return url


def scrap_costco(search_term):
    """

    :param driver:
    :param search_term:
    :return:
    """
    results = []
    try:
        url = get_url_costco(search_term)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        # with open(
        #     "/Users/anubhavchaudhary/Downloads/github/repos/cheapBuy/data/costco.html",
        #     "w",
        # ) as fileptr:
        #     fileptr.write(str(soup))
        results = soup.find_all("div", {"class": "product-tile-set"})

    except Exception as e:
        print(e)
        results = []
    return results


def extract_item_costco(search_term):
    """

    :param driver:
    :param search_term:
    :return:
    """
    result = {}
    try:
        results = scrap_costco(search_term)
        if len(results) == 0:
            print(
                f"For search_term: {search_term}, \n No item found scrapping Costco.")
            return result
        print(f"Found {len(results)} items on the Costco, picking the 1st one.")
        item = results[0]
        atag = item.find("a", {"automation-id": "productDescriptionLink_0"})
        result["description"] = atag.text
        result["url"] = atag.get("href")
        result["price"] = (
            item.find("div", {"class": "price"}).get_text().strip().strip("$")
        )
        result["site"] = "Costco"
    except Exception as e:
        print(F"Scraping failed for Costco due to: {e}")
        result = {}
    return result

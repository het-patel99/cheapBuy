from bs4 import BeautifulSoup


def get_url_ebay(search_term):
    """

    :param search_term:
    :return:
    """
    domain_name = "https://www.ebay.com"
    amended_search_term = "%20".join(search_term.split(" "))
    url = f"{domain_name}/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={amended_search_term}"

    print(f"Constructed Ebay URL: \n >>{url}<<")
    return url


def scrap_ebay(driver, search_term):
    """

    :param driver:
    :param search_term:
    :return:
    """
    results = []
    try:
        url = get_url_ebay(search_term)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        results = soup.find_all(
            "li", {"class": "s-item s-item__sep-on-bottom s-item--watch-at-corner"}
        )
    except:
        results = []
    return results


def extract_item_ebay(driver, search_term):
    """

    :param driver:
    :param search_term:
    :return:
    """
    result = {}
    try:
        results = scrap_ebay(driver, search_term)
        if len(results) == 0:
            print(
                f"***** For search_term: {search_term}, \n No item found scrapping Ebay."
            )
            return result
        print(f"Found {len(results)} items on the Ebay, picking the 1st one.")
        item = results[0]
        atag = item.find("a", {"class": "s-item__link"})
        result["description"] = (
            item.find("h3", {"class": "s-item__title"}).get_text().strip()
        )
        result["url"] = atag.get("href")
        result["price"] = (
            item.find("span", {"class": "s-item__price"}).get_text().strip().strip("$")
        )
        result["site"] = "ebay"
    except:
        print("Scraping failed for Ebay")
        result = {}
    return result

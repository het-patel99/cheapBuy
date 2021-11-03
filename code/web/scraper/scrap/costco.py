from bs4 import BeautifulSoup


def get_url_costco(search_term):
    """

    :param search_term:
    :return:
    """
    domain_name = "https://www.costco.com/"
    amended_search_term = "%20".join(search_term.split(" "))
    url = f"{domain_name}/CatalogSearch?dept=All&keyword={amended_search_term}"
    print(f"Constructed Costco's URL: \n {url}")
    return url


def scrap_costco(driver, search_term):
    """

    :param driver:
    :param search_term:
    :return:
    """
    results = []
    try:
        url = get_url_costco(search_term)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        with open(
            "/Users/anubhavchaudhary/Downloads/github/repos/cheapBuy/data/costco.html",
            "w",
        ) as fileptr:
            fileptr.write(str(soup))
        results = soup.find_all("div", {"class": "product-tile-set"})

    except:
        results = []
    return results


def extract_item_costco(driver, search_term):
    """

    :param driver:
    :param search_term:
    :return:
    """
    result = {}
    try:
        results = scrap_costco(driver, search_term)
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
    except:
        print("Scraping failed for Costco")
        result = {}
    return result

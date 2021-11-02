from bs4 import BeautifulSoup


def get_url_amazon(search_term):
    try:
        template = "https://www.amazon.com" + "/s?k={}&ref=nb_sb_ss_ts-doa-p_3_5"
        search_term = search_term.replace(" ", "+")
        template = template.format(search_term)
    except:
        template = ""
    print(f"Constructed amazon URL: \n {template}")
    return template


def scrap_amazon(driver, search_term):
    results = []
    try:
        url = get_url_amazon(search_term)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        results = soup.find_all("div", {"data-component-type": "s-search-result"})
    except:
        results = []
    return results


def extract_item_amazon(driver, search_term):
    result = {}
    try:
        results = scrap_amazon(driver, search_term)
        if len(results) == 0:
            print(f"For search_term: {search_term}, \n No item found scrapping Amazon.")
            return result
        print(f"Found {len(results)} items on the amazon, picking the 1st one.")
        item = results[0]
        atag = item.h2.a
        result["description"] = atag.text.strip()
        result["url"] = "https://www.amazon.com" + atag.get("href")
        price_parent = item.find("span", "a-price")
        item_price = price_parent.find("span", "a-offscreen").text.strip("$")
        print(f"Amazon {search_term} price : {item_price}")
        result["price"] = item_price
        result["site"] = "amazon"
    except:
        print("Scraping failed for amazon")
        result = {}
    return result

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from .fetch_description.amazon import description_from_url_amazon
from .fetch_description.ebay import description_from_url_ebay
from .fetch_description.walmart import description_from_url_walmart
from .fetch_description.costco import description_from_url_costco
from .fetch_description.bjs import description_from_url_bjs

from .scrap.amazon import extract_item_amazon
from .scrap.ebay import extract_item_ebay
from .scrap.walmart import extract_item_walmart
from .scrap.bjs import extract_item_bjs
from .scrap.costco import extract_item_costco


def get_driver():
    """
    :return:  instance of Chrome WebDriver.
    """
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(
        options=options, executable_path=ChromeDriverManager().install()
    )
    # driver.set_page_load_timeout(30)
    return driver


def set_results(to, from_):
    """
    sets the main results dict.
    :param to:
    :param from_:
    :return:
    """
    to["url"].append(from_["url"])
    to["description"].append(from_["description"])
    to["price"].append(from_["price"])
    to["site"].append(from_["site"])


def search_amazon(driver, description, results):
    """

    :param driver:
    :param description:
    :param results:
    :return:
    """
    result_dict_amazon = extract_item_amazon(driver, description)
    if result_dict_amazon != {}:
        print(f"Amazon price: {result_dict_amazon['price']}")
        set_results(results, result_dict_amazon)
    pass


def search_bjs(driver, description, results):
    """

    :param driver:
    :param description:
    :param results:
    :return:
    """
    print("`" * 20)
    result_dict_bjs = extract_item_bjs(driver, description)
    if result_dict_bjs != {}:
        print(f"Bjs price: {result_dict_bjs['price']}")
        set_results(results, result_dict_bjs)
    pass


def search_walmart(driver, description, results):
    """

    :param driver:
    :param description:
    :param results:
    :return:
    """
    print("`" * 20)
    result_dict_walmart = extract_item_walmart(driver, description)
    if result_dict_walmart != {}:
        print(f"Walmart price: {result_dict_walmart['price']}")
        set_results(results, result_dict_walmart)
    pass


def search_costco(driver, description, results):
    """

    :param driver:
    :param description:
    :param results:
    :return:
    """
    print("`" * 20)
    result_dict_costco = extract_item_costco(driver, description)
    if result_dict_costco != {}:
        print(f"Costco price: {result_dict_costco['price']}")
        set_results(results, result_dict_costco)
    pass


def search_ebay(driver, description, results):
    """

    :param driver:
    :param description:
    :param results:
    :return:
    """
    print("`" * 20)
    result_dict_ebay = extract_item_ebay(driver, description)
    if result_dict_ebay != {}:
        print(f"Ebay price: {result_dict_ebay['price']}")
        set_results(results, result_dict_ebay)
    pass


def scraper(link):
    """

    :param link:
    :return:
    """
    print("\n \t\t\t\t\t\t\t ****** User request Started.******\n")

    driver = get_driver()
    results = {"url": [], "description": [], "price": [], "site": []}

    if "amazon.com" in link:
        print(f"User is on amazon with URL: \n {link}")
        description = description_from_url_amazon(link)
        if description:
            print(
                f"***** Let's search \n >>{description}<< \n on Ebay, costco, bjs, walmart *****"
            )
            # searching item!
            search_ebay(driver, description, results)
            search_costco(driver, description, results)
            search_bjs(driver, description, results)
            search_walmart(driver, description, results)
            return results
        else:
            return ""

    if "ebay.com" in link:
        print(f"User is on Ebay with URL: \n {link}")
        description = description_from_url_ebay(link)
        if description:
            print(
                f"***** Let's search >>{description}<< \n on amazon, costco, bjs, walmart *****"
            )
            # searching item!
            search_amazon(driver, description, results)
            search_costco(driver, description, results)
            search_bjs(driver, description, results)
            search_walmart(driver, description, results)
            return results
        else:
            return ""

    if "walmart.com" in link:
        print(f"User is on Walmart with URL: \n {link}")
        description = description_from_url_walmart(link)
        if description:
            print(
                f"***** Let's search >>{description}<< \n on amazon, costco, bjs, ebay *****"
            )
            # searching item!
            search_amazon(driver, description, results)
            search_costco(driver, description, results)
            search_bjs(driver, description, results)
            search_ebay(driver, description, results)
            return results
        else:
            return ""

    if "costco.com" in link:
        print(f"User is on Costco with URL: \n {link}")
        description = description_from_url_costco(link)
        if description:
            print(
                f"***** Let's search >>{description}<< \n on amazon, ebay, bjs, walmart *****"
            )
            # searching item!
            search_amazon(driver, description, results)
            search_ebay(driver, description, results)
            search_bjs(driver, description, results)
            search_walmart(driver, description, results)
            return results
        else:
            return ""

    if "bjs.com" in link:
        print(f"User is on Bjs with URL: \n {link}")
        description = description_from_url_bjs(link)
        if description:
            print(
                f"***** Let's search >>{description}<< \n on amazon, ebay, costco, walmart *****"
            )
            # searching item!
            search_amazon(driver, description, results)
            search_ebay(driver, description, results)
            search_costco(driver, description, results)
            search_walmart(driver, description, results)
            return results
        else:
            return ""

    print("\n \t\t\t\t\t\t\t ****** User request finished.******")

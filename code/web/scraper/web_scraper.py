from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.firefox import GeckoDriverManager

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
    # Chrome
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    )
    chrome_browser = webdriver.Chrome(
        options=option, executable_path=ChromeDriverManager().install()
    )

    # Firefox
    useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36"

    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", useragent)
    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webnotifications.serviceworker.enabled", False)
    options.set_preference("dom.webnotifications.enabled", False)
    options.add_argument("--headless")
    firefox_browser = webdriver.Firefox(
        firefox_profile=profile,
        options=options,
        executable_path=GeckoDriverManager().install(),
    )

    return chrome_browser, firefox_browser


def get_agent():
    agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    return agent


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
	
def search_amazon(description, results):
	result_dict_amazon = extract_item_amazon(description)
	if result_dict_amazon != {}:
		print(f"Amazon price: {result_dict_amazon['price']}")
		set_results(results, result_dict_amazon)
=======
    


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



def search_ebay(description, results):
	result_dict_ebay = extract_item_ebay(description)
	if result_dict_ebay != {}:
		print(f"Ebay price: {result_dict_ebay['price']}")
		set_results(results, result_dict_ebay)


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

    chrome, firefox = get_driver()
    results = {"url": [], "description": [], "price": [], "site": []}

    if "amazon.com" in link:
        print(f"User is on amazon with URL: \n {link}")
        description = description_from_url_amazon(link)
        if description:
            print(
                f"***** Let's search \n >>{description}<< \n on Ebay, costco, bjs, walmart *****"
            )
            # searching item!
            search_ebay(chrome, description, results)
            search_costco(chrome, description, results)
            search_bjs(chrome, description, results)
            search_walmart(chrome, description, results)
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
            search_amazon(chrome, description, results)
            search_costco(chrome, description, results)
            search_bjs(chrome, description, results)
            search_walmart(chrome, description, results)
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
            search_amazon(chrome, description, results)
            search_costco(chrome, description, results)
            search_bjs(chrome, description, results)
            search_ebay(chrome, description, results)
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
            search_amazon(chrome, description, results)
            search_ebay(chrome, description, results)
            search_bjs(chrome, description, results)
            search_walmart(chrome, description, results)
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
            search_amazon(chrome, description, results)
            search_ebay(chrome, description, results)
            search_costco(chrome, description, results)
            search_walmart(chrome, description, results)
            return results
        else:
            return ""

    print("\n \t\t\t\t\t\t\t ****** User request finished.******")

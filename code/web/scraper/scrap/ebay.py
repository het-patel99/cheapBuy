import requests
from bs4 import BeautifulSoup


def get_url_ebay(search_term):

    try:
        modified_search_term = search_term.title.replace(' ', '%20')
        template = F"https://www.ebay.com/sch/i.html?_from=R40&_nkw={modified_search_term}&_sacat=0&rt=nc&_udlo=0&_udhi=" \
                   F"{search_term.price}"
    except:
        template = ''
    print(f"Constructed Ebay URL: \n {template}")
    return template


def scrap_ebay(search_term):
    results = []
    try:
        url = get_url_ebay(search_term)
        # driver.get(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        results = soup.find_all("li", attrs={"class": "s-item s-item__pl-on-bottom s-item--watch-at-corner"})
    except:
        results = []
    return results


def extract_item_ebay(search_term):
    result = {}
    try:
        results = scrap_ebay(search_term)
        if len(results) == 0:
            print(f'***** For search_term: {search_term}, \n No item found scrapping Ebay.')
            return result
        print(f'Found {len(results)} items on the Ebay, picking the 1st one.')
        item = results[0]
        atag = item.find("a", {"class": "s-item__link"})
        result['description'] = item.find("h3", {"class": "s-item__title"}).get_text().strip()
        result['url'] = atag.get('href')
        result['price'] = item.find("span", {"class": "s-item__price"}).get_text().strip().strip('$')
        result['site'] = 'ebay'
    except:
        print('Scraping failed for Ebay')
        result = {}
    return result

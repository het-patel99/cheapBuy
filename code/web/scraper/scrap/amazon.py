import requests
from bs4 import BeautifulSoup


def get_url_amazon(search_term):
    try:

        print(search_term)
        modified_search_term = search_term.replace(' ', '+')
        modified_search_term = modified_search_term.replace(',', '%2C')
        template = F"https://www.amazon.com/s?k={modified_search_term}%2C114&ref=nb_sb_noss"
    
    except:
        print("here")
        template = ''
    print(f"Constructed amazon URL: \n {template}")
    return template




def scrap_amazon(search_term):
    results = []
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
        print(page.status_code)
        soup = BeautifulSoup(page.content, 'lxml')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})
    except:
        results = []
    return results


def extract_item_amazon(search_term):
    result = {}
    try:
        results = scrap_amazon(search_term)
        if len(results) == 0:
            print(f'For search_term: {search_term}, \n No item found scrapping Amazon.')
            return result
        print(f'Found {len(results)} items on the amazon, picking the 1st one.')
        item = results[0]
        atag = item.h2.a
        result['description'] = atag.text.strip()
        result['url'] = 'https://www.amazon.com' + atag.get('href')
        price_parent = item.find('span', 'a-price')
        item_price = price_parent.find('span', 'a-offscreen').text.strip('$')
        print(f'Amazon {search_term} price : {item_price}')
        result['price'] = item_price
        result['site'] = 'amazon'
    except:
        print('Scraping failed for amazon')


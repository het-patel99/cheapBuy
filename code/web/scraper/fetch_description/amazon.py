from collections import namedtuple
import requests
from bs4 import BeautifulSoup


# def description_from_url_amazon(link):
#     description = ''
#     try:
#         print(F"amazon link: {link}")
#         link = link.replace('https://www.amazon.com/', '')
#         print(F"after link replace: {link}")
#         for ch in link:
#             if ch != '/':
#                 description += ch
#             else:
#                 break
#         description = description.replace('-', ' ')
#         print(f'Extracted item/search_term/description to be searched:\n {description}')
#     except:
#         print("Can't pull the description from amazon url.")
#         description = ''
#     print('-' * 10)
#     return description


def description_from_url_amazon(link):
    headers = {'Host': 'www.amazon.com',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/44.0.2403.157 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': '1', 'TE': 'Trailers'}
    webpage = requests.get(link, headers=headers)
    soup = BeautifulSoup(webpage.content, "lxml")
    product_title = soup.find("span", attrs={"id": "productTitle"})
    product_title_string = product_title.string.strip().replace(',', '')
    print(F"Extracted title: {product_title_string}")
    product_price = soup.find("span", attrs={"class": "a-offscreen"})
    print(F"Extracted price: {product_price.string}")
    description = namedtuple("Description", "title price")
    return description(product_title_string, product_price)

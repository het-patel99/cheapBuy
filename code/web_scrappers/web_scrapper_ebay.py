from bs4 import BeautifulSoup

def get_url_ebay(search_term):
  template="https://www.ebay.com"+"/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}"
  return template.format(search_term)

def scrap_ebay(driver, search_term):
  url = get_url_ebay(search_term)
  driver.get(url)
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  results = soup.find_all("li",{"class":"s-item s-item__sep-on-bottom s-item--watch-at-corner"})
  return results

def extract_item_ebay(driver, search_term):
  result={}
  results = scrap_ebay(driver, search_term)
  if len(results) == 0:
    return result 
  item=results[0]
  atag = item.find("a",{"class":"s-item__link"})
  result['description'] = item.find("h3",{"class":"s-item__title"}).get_text().strip()
  result['url'] = atag.get('href')
  result['price'] = item.find("span",{"class":"s-item__price"}).get_text().strip().strip('$')
  result['site'] = 'ebay'
  return result
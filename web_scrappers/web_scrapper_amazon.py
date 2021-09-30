from bs4 import BeautifulSoup

def get_url_amazon(search_term):
	template = 'https://www.amazon.com'+'/s?k={}&ref=nb_sb_ss_ts-doa-p_3_5'
	search_term = search_term.replace(' ','+')
	return template.format(search_term)

def scrap_amazon(driver, search_term):
	url = get_url_amazon(search_term)
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	results = soup.find_all('div',{'data-component-type': 's-search-result'})
	return results


def extract_item_amazon(driver, search_term):
	result={}
	results = scrap_amazon(driver, search_term)
	if len(results) == 0:
		return result 
	item=results[0]
	atag = item.h2.a
	result['description'] = atag.text.strip()
	result['url'] = 'https://www.amazon.com'+atag.get('href')
	price_parent = item.find('span', 'a-price')
	result['price'] = price_parent.find('span', 'a-offscreen').text.strip('$')
	result['site'] = 'Amazon'
	return result


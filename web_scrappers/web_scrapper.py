from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from web_scrapper_amazon import extract_item_amazon
from web_scrapper_ebay import extract_item_ebay
from web_scrapper_walmart import extract_item_walmart
from fetch_description_amazon import description_from_url_amazon
from fetch_description_ebay import description_from_url_ebay
from fetch_description_walmart import description_from_url_walmart
from fetch_description_costco import description_from_url_costco
from fetch_description_bjs import description_from_url_bjs

def get_driver():
	options = webdriver.ChromeOptions()
	options.headless = True
	driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
	return driver

def scrapper(link):
	driver = get_driver()
	results = {'url':[],'description':[],'price':[],'site':[]}
	if 'amazon' in link:
		description = description_from_url_amazon(link)
		result_dict_ebay = extract_item_ebay(driver, description)
		results['url'].append(result_dict_ebay['url'])
		results['description'].append(result_dict_ebay['description'])
		results['price'].append(result_dict_ebay['price'])
		results['site'].append(result_dict_ebay['site'])
	elif 'ebay' in link:
		description = description_from_url_ebay(link)
		result_dict_amazon = extract_item_amazon(driver, description)
		results['url'].append(result_dict_amazon['url'])
		results['description'].append(result_dict_amazon['description'])
		results['price'].append(result_dict_amazon['price'])
		results['site'].append(result_dict_amazon['site'])
	elif 'walmart' in link:
		description = description_from_url_walmart(link)
		result_dict_amazon = extract_item_amazon(driver, description)
		result_dict_ebay = extract_item_ebay(driver, description)
		results['url'].append(result_dict_amazon['url'])
		results['url'].append(result_dict_ebay['url'])
		results['description'].append(result_dict_amazon['description'])
		results['description'].append(result_dict_ebay['description'])
		results['price'].append(result_dict_amazon['price'])
		results['price'].append(result_dict_ebay['price'])
		results['site'].append(result_dict_amazon['site'])
		results['site'].append(result_dict_ebay['site'])
	elif 'costco' in link:
		description = description_from_url_costco(link)
		result_dict_amazon = extract_item_amazon(driver, description)
		result_dict_ebay = extract_item_ebay(driver, description)
		results['url'].append(result_dict_amazon['url'])
		results['url'].append(result_dict_ebay['url'])
		results['description'].append(result_dict_amazon['description'])
		results['description'].append(result_dict_ebay['description'])
		results['price'].append(result_dict_amazon['price'])
		results['price'].append(result_dict_ebay['price'])
		results['site'].append(result_dict_amazon['site'])
		results['site'].append(result_dict_ebay['site'])
	else:
		description = description_from_url_bjs(link)
		result_dict_amazon = extract_item_amazon(driver, description)
		result_dict_ebay = extract_item_ebay(driver, description)
		results['url'].append(result_dict_amazon['url'])
		results['url'].append(result_dict_ebay['url'])
		results['description'].append(result_dict_amazon['description'])
		results['description'].append(result_dict_ebay['description'])
		results['price'].append(result_dict_amazon['price'])
		results['price'].append(result_dict_ebay['price'])
		results['site'].append(result_dict_amazon['site'])
		results['site'].append(result_dict_ebay['site'])

	return results
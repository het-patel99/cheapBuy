
# from webdriver_manager import driver
import re
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

def get_driver():
	options = webdriver.ChromeOptions()
	options.headless = True
	driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
	return driver

def set_results(to, from_):
	to['url'].append(from_['url'])
	to['description'].append(from_['description'])
	to['price'].append(from_['price'])
	to['site'].append(from_['site'])
	
def search_amazon(driver, description, results):
	result_dict_amazon = extract_item_amazon(driver, description)
	if result_dict_amazon != {}:
		print(f"Amazon price: {result_dict_amazon['price']}")
		set_results(results, result_dict_amazon)

def search_bjs(driver, description, results):
	result_dict_amazon = extract_item_bjs(driver, description)
	if result_dict_amazon != {}:
		print(f"Amazon price: {result_dict_amazon['price']}")
		set_results(results, result_dict_amazon)

def search_walmart(driver, description, results):
	result_dict_amazon = extract_item_walmart(driver, description)
	if result_dict_amazon != {}:
		print(f"Amazon price: {result_dict_amazon['price']}")
		set_results(results, result_dict_amazon)

def search_costco(driver, description, results):
	pass

def search_ebay(driver, description, results):
	result_dict_ebay = extract_item_ebay(driver, description)
	if result_dict_ebay != {}:
		print(f"Ebay price: {result_dict_ebay['price']}")
		set_results(results, result_dict_ebay)


def scraper(link):
	print('\n \t\t\t\t\t\t\t ****** User request Started.******\n')

	driver = get_driver()

	print(f'User selected url: \n {link}')
	print('-'*10)	
	
	results = {'url':[],'description':[],'price':[],'site':[]}
	
	if 'amazon.com' in link:
		print('User selected amazon')
		description = description_from_url_amazon(link)
		if description:
			print(f"***** Let's search >>{description}<< \n on Ebay *****")
			print('-'*5)
			# search item on Ebay!
			search_ebay(driver, description, results)
			return results
		else:
			return ''

	if 'ebay.com' in link:
		print('User selected ebay')
		description = description_from_url_ebay(link)
		if description:	
			print(f"***** Let's search >>{description}<< \n on amazon *****")
			print('-'*5)
			# search item on amazon!
			search_amazon(driver, description, results)
			return results
		else:
			return ''

	if 'walmart.com' in link:
		print('User selected Walmart')
		description = description_from_url_walmart(link)
		if description:
			print(f"***** Let's search >>{description}<< \n on amazon and ebay *****")
			print('-'*5)
			# search item on amazon!
			search_amazon(driver, description, results)
			print('-'*5)
			# search item on ebay!
			search_ebay(driver, description, results)
			return results
		else:
			return ''

	if 'costco.com' in link:
		print('User selected costco')	
		description = description_from_url_costco(link)
		if description:
			print(f"***** Let's search >>{description}<< \n on amazon and ebay *****")
			print('-'*5)
			# search item on amazon!
			search_amazon(driver, description, results)
			print('-'*5)
			# search item on ebay!
			search_ebay(driver, description, results)
			return results
		else:
			return ''
			
	if 'bjs.com' in link:
		print('User selected bjs')
		description = description_from_url_bjs(link)
		if description:
			print(f"***** Let's search >>{description}<< \n on amazon and ebay *****")
			print('-'*5)
			# search item on amazon!
			search_amazon(driver, description, results)
			print('-'*5)
			# search item on ebay!
			search_ebay(driver, description, results)
			return results	
		else:
			return ''		
	print('\n \t\t\t\t\t\t\t ****** User request finished.******')


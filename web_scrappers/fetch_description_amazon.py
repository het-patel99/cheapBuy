def description_from_url_amazon(link):
	link = link.replace('https://www.amazon.com/','')
	description = ''
	for ch in link:
		if ch!='/':
			description+=ch
		else:
			break
	description = description.replace('-', ' ')
	return description
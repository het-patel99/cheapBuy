def description_from_url_costco(link):
    remove_initial = link.replace("https://www.costco.com/","")
    description = ''
    for i in remove_initial:
        if(i!="."):
            description += i
        else:
            break
    description  = description.replace('-',' ')
    return description

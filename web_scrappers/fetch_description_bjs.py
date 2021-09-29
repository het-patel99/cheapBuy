def description_from_url_bjs(link):
    remove_initial = link.strip("https://www.bjs.com/product/")
    description = ''
    for i in remove_initial:
        if(i!="/"):
            description += i
        else:
            break
    description  = description.replace('-',' ')
    return description
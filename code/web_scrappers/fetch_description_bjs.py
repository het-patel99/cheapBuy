def description_from_url_bjs(link):
    remove_initial = link.replace("https://www.bjs.com/product/","")
    description = ''
    print(remove_initial)
    for i in remove_initial:
        if(i!="/"):
            description += i
        else:
            break
    description  = description.replace('-',' ')
    return description

def description_from_url_walmart(link):
    remove_initial = link.replace("https://www.walmart.com/ip/","")
    description = ''
    for i in remove_initial:
        if(i!="/"):
            description += i
        else:
            break
    description  = description.replace('-',' ')
    return description

def description_from_url_walmart(link):
<<<<<<< HEAD:code/web_scrappers/fetch_description_walmart.py
    remove_initial = link.replace("https://www.walmart.com/ip/","")
=======
    remove_initial = link.replace("https://walmart.com/ip/","")
>>>>>>> 8e51b91814cfe2848f8a68d0e55ca83b876b5521:web_scrappers/fetch_description_walmart.py
    description = ''
    for i in remove_initial:
        if(i!="/"):
            description += i
        else:
            break
    description  = description.replace('-',' ')
    return description
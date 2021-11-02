def description_from_url_amazon(link):
    """

    :param link:
    :return:
    """
    description = ""
    try:
        link = link.replace("https://www.amazon.com/", "")
        for ch in link:
            if ch != "/":
                description += ch
            else:
                break
        description = description.replace("-", " ")
        print(
            f"Extracted item/search_term/description to be searched: \n >>{description}<<"
        )
    except:
        print("Can't pull the description from amazon url.")
        description = ""
    print("-" * 10)
    return description

def get_url(url: str):
    """
        Method get url from pagination

        :param url: url of next or previous
        :type url: str
        :return: url
    """
    count = 0
    position = 0
    # capture position of chart /
    for i, chart in enumerate(url):
        if "/" == chart:
            position = i
            count = count + 1
        if count > 2:
            break
    # get temporal url
    temporal_url = url[position:]
    return temporal_url

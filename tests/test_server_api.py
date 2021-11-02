import requests


def test_post_result():
    """
    Need to run the server code before running this test case.
    :return:
    """
    server = "0.0.0.0"  # '3.89.74.154'
    port = 8080
    domain = "https://www.bjs.com"
    search_term = "brita-pour-through-pitcher-replacement-filter-6-pk"
    result = requests.post(
        f"http://{server}:{port}/scrap?link={domain}/product/{search_term}/23538"
    )
    assert result is not None

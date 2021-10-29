import requests

def test_post_result():
    server='0.0.0.0' # '3.89.74.154'
    port=8080
    result = requests.post(f"http://{server}:{port}/scrap?link=https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-6-pk/23538")
    assert result is not None

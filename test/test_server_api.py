import requests


def test_post_result():
    result = requests.post("http://18.233.163.121:8080/scrap?link=https://www.amazon.com/2021-Apple-10-2-inch-iPad-Wi-Fi/dp/B09G9FPHY6/ref=sr_1_3?dchild=1&keywords=ipad&qid=1632940310&sr=8-3")
    assert result is not None


def test_post_result_status():
    result = requests.post("http://18.233.163.121:8080/scrap?link=https://www.amazon.com/2021-Apple-10-2-inch-iPad-Wi-Fi/dp/B09G9FPHY6/ref=sr_1_3?dchild=1&keywords=ipad&qid=1632940310&sr=8-3")
    assert result.status_code == 200


def test_post_result_response_ebay():
    response = requests.post("http://18.233.163.121:8080/scrap?link=https://www.ebay.com/itm/154529733835?_trkparms=amclksrc%3DITM%26aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20180816085401%26meid%3D9b423a8b0ea04935ad0501c5f532ebad%26pid%3D100970%26rk%3D1%26rkt%3D2%26sd%3D154529733835%26itm%3D154529733835%26pmt%3D1%26noa%3D1%26pg%3D2380057%26brand%3DApple&_trksid=p2380057.c100970.m5481&_trkparms=pageci%3A4e49dd80-2204-11ec-b2df-5ee8de9052b5%7Cparentrq%3A375a630b17c0a6e784fc6ef0fff45dfc%7Ciid%3A1").json()
    assert len(response["description"]) == 1

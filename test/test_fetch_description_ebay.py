import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.fetch_description_ebay import description_from_url_ebay


def test_fetch_description_ebay_1():
    link = "https://www.ebay.com/itm/393519397796?_trkparms=%26rpp_cid%3D6126793c53c5f7913b0d74e3%26rpp_icid%3D6126793c53c5f7913b0d74e2&_trkparms=pageci%3A3ac38985-2156-11ec-a266-a2130cc87e42%7Cparentrq%3A32e58f7d17c0aaf50aecf96afff75412%7Ciid%3A1"
    assert description_from_url_ebay(link) == "AKG by Harman N60NC Wireless Noise-cancelling Headphones, Black"


def test_fetch_description_ebay_2():
    link = "https://www.ebay.com/itm/154529733835?epid=25034208652&_trkparms=ispr%3D1&hash=item23fab09ccb:g:77wAAOSwVe9hO8Kg&amdata=enc%3AAQAGAAACkPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsStEKTPzZMfQmny3knR97t0D49zgtRr%252FmkDOj5xka02OoEnKbVzDathPeh4pIL1djCuDYy%252FCukb591Bt2yV9ORNBECq7d1MqvZJP8wYRKk82QhkJN1YtDzekvtEHjLiS6dNwSFAs0XaWo%252BmngO74p%252BmO2QbCDk%252FBWRjddWF0uN7NhXE8sCG9Ga93G01ZdHOQEsS3GuIr19i7T%252BYa61NlWRZMG5cJns21%252FWnWASOBfZFspqQAdxngJYZiFzqH4QtYFS8WXB%252BN610lbQfn9bR2vAjXVMm5zP5f1J8UVjuxm2BVzc%252FSHbJUDsFzNE73qbGKigB%252BI1SbvPnE2PmT1TSw5nKGVbk1f3L1vcgcq9Tj6RhN14aQrHUsX23AIKKeG%252FxEuuI5Mc1%252FoMYoNn8urjBOrvcuinpyRPvMFHvCOcyxarJO0KPOyD4MoPWdiEm5UjbEpeRwBhzOlrsdGUUhysaDgeoLy93upwKWALa5YxpiTRu6%252FxAjg0NhFGWCpCGlaWYfK0OUA4EVP3YVZ2f94wRgvDD5ZOXn%252BoYMirOs8kN25ApizemeswjYCXNk6DXw5QW48DlOOsfz%252F%252BYJIMIipwzCxILZvk2W1U1UKEp2huIjx0hZydPjuUpNL8k8fC%252Fp%252FQSyeuGeCinCKhIsj0vi7%252FPalBkyuXltg25mqoVRUSDK9%252FP92GBxtI49Mz5IS2PrK611cIJi%252BOaN04c8aH5HU%252BD5tMup%252BaHu%252B2IhXADcnrXVgQIi2AaoE4E%252Fp%252Bg895JxtAhAjO75JOlu%252B17lMfnL%252FEfc%252FVdTuMPUeUGdkDuKl%252Fb%252FUXuvpO4AscUf2Blp%252F%252BpZROrggE%7Campid%3APL_CLK%7Cclp%3A2334524"
    description = description_from_url_ebay(link)
    assert description == "Apple  iPhone 11 64GB Verizon TMobile AT&T UNLOCKED A2111"

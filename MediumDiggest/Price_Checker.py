import json

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Bose-QuietComfort-Wireless-Headphones-Cancelling/dp/B079NM341X/ref=sr_1_16?" \
      "crid=1OOBXSPHV23NB&dchild=1&keywords=bose+headphones&qid=1586027433&sprefix=Bose+%2Caps%2C187&sr=8-16"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/80.0.3987.149 Safari/537.36"
headers = {"User-agent": user_agent}

URL_2 = "http://www.johnlewis.com/toms-berkley-slipper-grey/p3061099"

page = requests.get(URL_2)
soup = BeautifulSoup(page.content, 'html.parser')
product_content = json.dumps(page.text)

element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = (element.get_text(strip=True).lstrip("£"))
print(float(string_price))



for title in soup.find_all('span'):
    if 'Bose QuietComfort 35' in title:
        pass

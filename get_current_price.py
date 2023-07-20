import requests
from bs4 import BeautifulSoup
from pprint import pprint
import warnings
import sqlite3
from datetime import datetime
warnings.filterwarnings("ignore", message="Unverified HTTPS request")
url = "https://www.latamairlines.com/bff/air-offers/v2/offers/search?redemption=false&adult=1&inOfferId=null&sort=PRICE%2Casc&inFrom=null&destination=CPH&cabinType=Economy&inFlightDate=null&origin=CWB&outOfferId=null&outFrom=2024-05-04&outFlightDate=null&child=0&infant=0"

payload = {}
headers = {
  'X-latam-Action-Name': 'search-result.flightselection.offers-search',
  'X-latam-App-Session-Id': 'abb8c089-6e7a-4258-81e0-008d1bf747f5',
  'X-latam-Application-Country': 'BR',
  'X-latam-Application-Lang': 'pt',
  'X-latam-Application-Name': 'web-air-offers',
  'X-latam-Application-Oc': 'br',
  'X-latam-Client-Name': 'web-air-offers',
  'X-latam-Request-Id': '01c68057-db56-4e6f-bba6-f84126b1d4ca',
  'X-latam-Track-Id': 'c82f2186-4961-4ff3-86f7-008ff0fb53d6',
  'x-latam-captcha-token': '',
  'x-latam-search-token': ''
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

json_prices = response.json()

current_price = json_prices['content'][0]['summary']['brands'][0]['price']['amount']

connection_obj = sqlite3.connect('latam.db')

# cursor object
cursor_obj = connection_obj.cursor()

now = datetime.now()
# Creating table
insert = f"""INSERT INTO pricesLatam (day, price, cia)
          VALUES ('{now.strftime("%Y-%m-%d %H:%M")}', {current_price}, 'LATAM')"""

cursor_obj.execute(insert)


connection_obj.commit()


connection_obj.close()



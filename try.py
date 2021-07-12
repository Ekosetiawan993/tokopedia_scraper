from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

url = 'https://www.newegg.com/p/pl?N=100023083%20600481395&cm_sp=Cat_Home-Audio_6-_-VisNav-_-Bluetooth-Speakers_1'
session = HTMLSession()
page = session.get(url)

body_page = bs(page.content, 'html.parser')
product_containers = body_page.find_all('div', class_="item-cell")
print(len(product_containers))
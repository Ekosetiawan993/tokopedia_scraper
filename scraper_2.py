from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

BASE_URL = "https://www.tokopedia.com/gramedia-store/etalase/buku-remaja-dan-anak"
session = HTMLSession()

page = session.get(BASE_URL)
bs_page = bs(page.content, "html.parser")

#block = page.html.find('div.css-tjjb18', first=True)
#products = block.find('div.css-1sn1xa2')
block = bs_page.find('div', class_='css-tjjb18')
products = block.find_all('div', class_='css-1sn1xa2')

print(len(products))


from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

BASE_URL = "https://www.tokopedia.com/gramedia-store/etalase/buku-remaja-dan-anak"
url = "https://www.tokopedia.com/gramedia-store/etalase/buku-remaja-dan-anak?perpage=20"
session = HTMLSession()

page = session.get(url)
bs_page = bs(page.content, "html.parser")

#block = page.html.find('div.css-tjjb18', first=True)
#products = block.find('div.css-1sn1xa2')
block = bs_page.find('div', class_='css-tjjb18')
products = block.find_all('div', class_='css-1sn1xa2')

juduls = page.html.find('div.css-1f4mp12')

#print(len(products))
print(len(juduls))
for judul in juduls:
    print(judul.text)

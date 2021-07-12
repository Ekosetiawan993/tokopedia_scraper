from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession

BASE_URL = "https://www.tokopedia.com/gramedia-store/etalase/buku-remaja-dan-anak"
url = "https://realpython.com/beautiful-soup-web-scraper-python/"
session = HTMLSession()

r = session.get(BASE_URL)
block = r.html.find('div.unf-card.css-e66myc-unf-card.e1ukdezh0', first=True)
#title_ = section_1.find('h1', first=True)
#r.html.render()
#print(page)
#all_div = about.find('div')
#print(all_div[10])
judul = block.find('.css-18c4yhp', first=True)
harga = block.find('div.css-rhd610', first=True)
terjual = block.find('span.css-1kgbcz0', first=True)

print(judul.text, harga.text, terjual.text)
print(terjual.html)

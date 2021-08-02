import numpy as np
import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = "https://www.newegg.com/p/pl?d=graphics+cards"

# opening the connection

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
print(page_soup.body.span)

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})
print(len(containers))
#print(containers[0].a.img["title"])
print(containers[0].div.div)

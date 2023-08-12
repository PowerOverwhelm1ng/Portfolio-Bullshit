from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https.www. com/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.find_all("div",{"class":"_3O0U0u"})
print(len(containers))
print(soup.prettify(containers[0]))

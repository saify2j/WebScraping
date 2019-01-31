import requests
from bs4 import BeautifulSoup

mainPage=requests.get("https://www.startech.com.bd/component/motherboard")
soup=BeautifulSoup(mainPage.content,'html.parser')

product_names=[]
product_links=[]
product_prices=[]
stock_info=[]

names=soup.findAll(attrs={"class":"product-name"})
for i in range (0,len(names)):
    product_names.append(names[i].get_text()[1:-1])

for a in soup.select('.product-name a'):
    product_links.append(a['href'])

prices=soup.findAll(attrs={"class":"price space-between"})
for i in range (0,len(prices)):
    product_prices.append(prices[i].get_text()[1:-4])

stocks=soup.findAll(attrs={"class":"cart-btn"})
for i in range(0,len(stocks)):
    print(stocks[0].get_text())
    #stock_info.append()
#print(prices[0].get_text())
#print(soup.prettify())
#print(product_names)
print(product_prices)
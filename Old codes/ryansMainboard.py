import requests,time
import csv
from bs4 import BeautifulSoup
x=time.time()
wr = open('ryansMainboard.csv', 'a', newline='')
writer = csv.writer(wr)
header = ['Product Name', 'Link', 'Price']
writer.writerow(header)

mainPage=requests.get("https://ryanscomputers.com/components/mainboard.html")
soup=BeautifulSoup(mainPage.content,'html.parser')

page = soup.find_all(attrs={"class": "pages"})
numberOfPages=[]

#print(page)
for a in soup.select('.pages li a'):
    numberOfPages.append(a.get_text())

print(int(numberOfPages[-2]))
lastPage=int(numberOfPages[-2])

for i in range (1, lastPage+1):
    number = i
    y = "https://ryanscomputers.com/components/mainboard.html?p=" + str(number)
    page = requests.get(y)
    soup = BeautifulSoup(page.content, 'html.parser')

    names = []
    links = []
    prices = []


    for a in soup.select('.container h2 a'):
        links.append(a['href'])
        names.append(a.get_text(strip=True))

    price_list=soup.find_all('p',attrs={"class":"special-price"})

    for i in price_list:
        prices.append(i.get_text()[18:])

    #print(names[0]+" : "+links[0]+" : "+prices[0])

    rows=zip(names,links,prices)
    wr=open('ryansMainboard.csv','a',newline='')
    writer=csv.writer(wr)
    
    for row in rows:
        writer.writerow(row)
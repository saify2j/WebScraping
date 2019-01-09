import requests
from bs4 import BeautifulSoup
def loadData(component):
    mainPage = requests.get("https://www.startech.com.bd/component/"+component)

    soup = BeautifulSoup(mainPage.content, 'html.parser')
    pageList = soup.findAll(attrs={"class": "pagination"})
    #print(list(pageList))
    # print(pageList)

    numberOfPages = []
    for a in soup.select('.pagination li a'):
        numberOfPages.append(a.get_text())
    lastPage=numberOfPages[-2]
    print(lastPage)
#loadData("motherboard")
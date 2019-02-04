import requests
page=requests.get('http://bsse09.tk/')
#print(page)

from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')

div=soup.findAll('div',{'class':'gallery'})
#print(div)
for text in div :
    download = text.find_all('a')


# print(type(download))
#x=download[0]
#print(type(x))
#print(str(x))
#print(list(x))
# x=soup.findAll(name='a')
# print(soup.prettify())
# #x=soup.find_all('a')
# print(x)
y=soup.find_all(attrs={"data-title":True})
#print(y[0])
output=y[0]

print(type(output))
print(output)

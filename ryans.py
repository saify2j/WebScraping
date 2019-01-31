from bs4 import BeautifulSoup
import requests


def get_last_page(url, component):
    main_page = requests.get(url + component)
    soup = BeautifulSoup(main_page.content, 'html.parser')
    #print(soup.prettify())
    page_list=[]
    for a in soup.select('.pager'):
       # page_list.append(a.get_text())
        print(a.get_text())
#    page_list = soup.findAll(attrs={"class": "pager"})

    # print(page_list)


def main():
    url = "https://ryanscomputers.com/components/"
    component = "processor"
    get_last_page(url, component)


if __name__ == '__main__':
    main()

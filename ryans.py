from bs4 import BeautifulSoup
import requests


def get_last_page(url, component):
    main_page = requests.get(url + component+".html")
    soup = BeautifulSoup(main_page.content, 'html.parser')
    # print(soup.prettify())
    number_of_pages = []
    for a in soup.select('.pages li a'):
        number_of_pages.append(a.get_text())

    last_page = int(number_of_pages[-2])
    return last_page


def load_data(url,component,last_page):
    page = requests.get(url+component+"html?p="")

def main():
    url = "https://ryanscomputers.com/components/"
    component = "processor"
    last_page = get_last_page(url, component)


if __name__ == '__main__':
    main()

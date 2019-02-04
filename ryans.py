from bs4 import BeautifulSoup
import requests
import csv


def get_last_page(url, component):
    main_page = requests.get(url + component+".html")
    soup = BeautifulSoup(main_page.content, 'html.parser')
    # print(soup.prettify())
    number_of_pages = []
    for a in soup.select('.pages li a'):
        number_of_pages.append(a.get_text())

    last_page = int(number_of_pages[-2])
    return last_page


def load_data(url, component, last_page):

    for i in range(1, last_page + 1):
        number = i
        page = requests.get(url + component + ".html?p=" + str(number))
        soup = BeautifulSoup(page.content, 'html.parser')

        names = []
        links = []
        prices = []

        for a in soup.select('.container h2 a'):
            links.append(a['href'])
            names.append(a.get_text(strip=True))

        price_list = soup.find_all('p', attrs={"class": "special-price"})

        for j in price_list:
            prices.append(j.get_text()[18:])

        # print(names[0]+" : "+links[0]+" : "+prices[0])

        rows = zip(names, links, prices)
        wr = open('ryans-'+component+'.csv', 'a', newline='')
        writer = csv.writer(wr)

        for row in rows:
            writer.writerow(row)
    print("Writing to file done...")


def main():
    url = "https://ryanscomputers.com/components/"
    component = ["processor",
                 "desktop-ram",
                 "mainboard",
                 "graphics-card"]
                 
    last_page = get_last_page(url, component)
    print(last_page)
    load_data(url, component, last_page)


if __name__ == '__main__':
    main()

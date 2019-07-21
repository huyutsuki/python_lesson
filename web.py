#coding: UTF-8
from urllib import request
from bs4 import BeautifulSoup

def main():
    print("This script is a web scraping test.")

def web():
    url = "https://www.yomiuri.co.jp/"
    html = request.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")

    mainNewsIndex = soup.find("ul", attrs={"class", "p-category-latest-sec-list p-list p-list-col2"})
    headlines = mainNewsIndex.find_all("li", attrs={"class", "p-list-item"})

    #print headlines
    for headline in headlines:
        print(headline.find("a").string)


if __name__ == "__main__":
    web()

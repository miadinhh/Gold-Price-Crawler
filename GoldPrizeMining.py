import requests
import sys
from bs4 import BeautifulSoup as bs
import csv

def craw(url):
    # url = "https://giavangsjc.net/widgets/giavangfull/dat-gia-vang"
    res = requests.get(url)
#convert res.text to csv table using BeautifulSoup
    soup = bs(res.text, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
#using unicode charmap to convert to excel format
    with open("gold.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            if len(cols) < 1:
                continue
            writer.writerow(cols)
            # print(cols)

if __name__ == "__main__":
    #get url from parameters and pass to craw function
    url = input("Enter url: ")
    craw(url)
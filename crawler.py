from bs4 import BeautifulSoup
import requests


def crawl():
    result = requests.get("https://www.logting.fo/casenormal/view.gebs?menuChanged=16&type=0&caseNormal.id=4546")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    print(soup)
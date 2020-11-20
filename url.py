from bs4 import BeautifulSoup
import requests
import time

def makeRequest(url: str):
    print(url)
    time.sleep(2)
    result = requests.get(url)
    src = result.content
    return BeautifulSoup(src, 'lxml')
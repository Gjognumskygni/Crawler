from bs4 import BeautifulSoup
from url import Url
from typing import List

class Link():
    def __init__(self,
    number: str,
    title: str,
    committeeName: str,
    status: str):
        self.number = number
        self.title = title
        self.committeeName = committeeName
        self.status = status
        self.urls: List[Url] = []

    @staticmethod
    def getUrl(a: BeautifulSoup):
        return "https://www.logting.fo" + a["href"]

    @staticmethod
    def populateLinkObj(td: BeautifulSoup, link):
        a: BeautifulSoup = td[0].find("a")
        link.number = a.get_text()
        link.proposalUrl = Link.getUrl(a)
        link.urls.append(Url.createURLObj(link.proposalUrl, "proposal"))
        link.title = td[1].get_text()
        committeeA: BeautifulSoup = td[2].find("a")
        if "Ikki brúkt" in link.title:
            link.committeeName = td[2].get_text()
        elif committeeA is None:
            link.committeeName = ""
        else:
            link.committeeName = committeeA.get_text()
            url = Link.getUrl(committeeA)
            link.urls.append(Url.createURLObj(url,"committee"))
        link.status = td[3].get_text()
        return link
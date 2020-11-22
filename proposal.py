from bs4 import BeautifulSoup
from typing import List
from vote import Vote
from url import makeRequest
import requests
import time

class Proposal():
    def __init__(self, title: str, type: str):
        self.title = title
        self.type = type
        self.proposers: List[str] = []
        self.votes: List[Vote] = []

    @staticmethod
    def getProposer(soup: BeautifulSoup) -> str:
        return soup.find('span', class_='green').get_text()

    @staticmethod
    def getTitle(soup: BeautifulSoup) -> str:
        return soup.find('h5', class_="pb-5 pt-3").get_text()

    @staticmethod
    def getVotes(soup: BeautifulSoup, url: str) -> Vote:
        newSoup: BeautifulSoup = soup
        process: str = ""
        for tr in soup.find_all("tr"):
            th: str = (tr.find("th")).get_text()
            if "Skjal" in th:
                a: BeautifulSoup = tr.find('a', href=True)
                newSoup: BeautifulSoup = makeRequest(a['data-url'])
            elif "Atkvøða greidd í" in th:
                process = (tr.find("td")).get_text()
        return Vote.createVoteObj(newSoup, process)
    
    @staticmethod
    def createProposalObj(soup: BeautifulSoup, title):
        returnObj: Proposal = Proposal(title, "uppskot")
        table: BeautifulSoup = soup.find('table', class_="table")
        for tr in table.find_all("tr"):
            th: str = (tr.find("th")).get_text()
            if "Slag" in th:
                returnObj.type = (tr.find("td")).get_text()
            elif "Uppskotssetari" in th:
                for div in tr.find_all('div'):
                    returnObj.proposers.append(div.get_text())
            elif "Atkvøðugreiðslur" in th:
                for a in tr.find_all('a', href=True):
                    url: str = "https://www.logting.fo" + a['href']
                    newSoup: BeautifulSoup = makeRequest(url)
                    for link in newSoup.find_all('div', class_='macroContainer'):
                        if 'GetVoteDetail' in link['data-url']:
                            voteUrl: str = "https://www.logting.fo" + link['data-url']
                            returnObj.votes.append(Proposal.getVotes(makeRequest(voteUrl), voteUrl))
        return returnObj

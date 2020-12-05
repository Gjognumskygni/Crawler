from bs4 import BeautifulSoup
from typing import List
from vote import Vote
from url import Url
from link import Link
import requests
import time

class Proposal():
    def __init__(self, number: str, title: str, type: str, link: Link):
        self.number = number
        self.title = title
        self.type = type
        self.link = link
        self.proposers: List[str] = []
        self.votes: List[Vote] = []
        self.tags: List[str] = []

    @staticmethod
    def getVotes(soup: BeautifulSoup) -> Vote:
        newSoup: BeautifulSoup = soup
        process: str = ""
        for tr in soup.find_all("tr"):
            th: str = (tr.find("th")).get_text()
            if "Skjal" in th:
                a: BeautifulSoup = tr.find('a', href=True)
                newSoup: BeautifulSoup = Url.makeRequest(a['data-url'])
            elif "Atkvøða greidd í" in th:
                process: str = (tr.find("td")).get_text()
            elif "Úrslit" in th:
                votestring: str = ((tr.find("div")).get_text()).replace('(', ' ').replace(')', ' ')
                votesList: List[int] = [int(s) for s in votestring.split() if s.isdigit()]
        return Vote.createVoteObj(newSoup, process, votesList)
    
    @staticmethod
    def populateProposalObj(soup: BeautifulSoup, proposal):
        proposal.number = proposal.link.number
        proposal.title = proposal.link.title
        table: BeautifulSoup = soup.find('table', class_="table")
        for tr in table.find_all("tr"):
            th: str = (tr.find("th")).get_text()
            if "Slag" in th:
                proposal.type: str = (tr.find("td")).get_text()
            elif "Uppskotssetari" in th:
                for div in tr.find_all('div'):
                    proposal.proposers.append(div.get_text())
            elif "Atkvøðugreiðslur" in th:
                for a in tr.find_all('a', href=True):
                    url: str = "https://www.logting.fo" + a['href']
                    proposal.link.urls.append(Url.createURLObj(url,"votePage"))
                    newSoup: BeautifulSoup = Url.makeRequest(url)
                    for link in newSoup.find_all('div', class_='macroContainer'):
                        if 'GetVoteDetail' in link['data-url']:
                            votesoup = Url.makeRequest("https://www.logting.fo" + link['data-url'])
                            a: BeautifulSoup = votesoup.find('a', href=True)
                            if "pdf" in a['data-title']:
                                proposal.link.urls.append(Url.createURLObj(a['data-url'],"votePDF"))
                            elif "html" in a['data-title']:
                                proposal.link.urls.append(Url.createURLObj(a['data-url'],"voteHTML"))
                            proposal.votes.append(Proposal.getVotes(votesoup))
        return proposal

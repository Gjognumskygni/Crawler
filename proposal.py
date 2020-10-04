from crawler import makeRequest
from bs4 import BeautifulSoup
from typing import List
from vote import Vote

class Process():
    def __init__(self, number: int, vote: Vote):
        self.number = number
        self.vote = vote
    
    @staticmethod
    def getVotes(soup: BeautifulSoup):
        pass

    @staticmethod
    def getProcess(soup: BeautifulSoup):
        process_list: List[Process] = []
        for a in soup.find_all('a', class_="txt_type"):
            if "2. viðgerð" in a.get_text() or "3. viðgerð" in a.get_text():
                if len(process_list) == 0:
                    newSoup = makeRequest("https://www.logting.fo/" + a['href'])
                    process_list.append(Process(1,Process.getVotes(newSoup)))
                else:
                    newSoup = makeRequest("https://www.logting.fo/" + a['href'])
                    process_list.append(Process(2,Process.getVotes(newSoup)))

class Proposal():
    def __init__(self, title: str, proposers: str):
        self.title = title
        self.proposers = proposers
        self.processes: List[Process] = []

    @staticmethod
    def getProposer(soup: BeautifulSoup):
        return soup.find('span', class_='green').get_text()

    @staticmethod
    def getTitle(soup: BeautifulSoup):
        return soup.find('h4', class_='up').get_text()
    
    @staticmethod
    def createProposalObj(soup: BeautifulSoup):
        return Proposal(Proposal.getTitle(soup), Proposal.getProposer(soup))

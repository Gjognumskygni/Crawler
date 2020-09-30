from bs4 import BeautifulSoup
from typing import List
from vote import Vote

class Process():
    def __init__(self, number: int, vote: Vote):
        self.number = number
        self.vote = vote

class Proposer():
    def __init__(self, name: str):
        self.name = name
    
    @staticmethod
    def createProposerObj(soup: BeautifulSoup):
        return Proposer(soup.find('span', class_='green').get_text())

class Proposal():
    def __init__(self, title: str):
        self.title = title
        self.proposers: List[Proposer] = []
        self.processes: List[Process] = []
    
    @staticmethod
    def getTitle(soup: BeautifulSoup):
        return soup.find('h4', class_='up').get_text()

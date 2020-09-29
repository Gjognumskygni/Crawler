from bs4 import BeautifulSoup
from typing import List

def getMetaData(soup: BeautifulSoup):
    strong_list = soup.find_all('strong')
    return strong_list[2].get_text(), strong_list[4].get_text(), strong_list[6].get_text(), strong_list[8].get_text() 

class Vote():
    def __init__(self, present: int, yes: int, no: int, blank: int, yes_list: List[str], no_list: List[str], blank_list: List[str]):
        self.present = present
        self.yes = yes
        self.no = no
        self.blank = blank
        self.yes_list = yes_list
        self.no_list = no_list
        self.blank_list = blank_list 

    @staticmethod
    def createVoteObj(soup: BeautifulSoup):
        present, yes, no, blank = getMetaData(soup)
        yes_list = []
        no_list = []
        blank_list = []
        isYes = False
        isNo = False
        isBlank = False
        for td in soup.find_all('td'):
            if len(td.get_text()) > 1:
                if "JA:" in td.get_text():
                    isYes = True
                    isNo = False
                    isBlank = False
                elif "NEI:" in td.get_text():
                    isNo = True
                    isYes = False
                    isBlank = False
                elif "BLANK:" in td.get_text():
                    isBlank = True
                    isYes = False
                    isNo = False
                elif isYes == True:
                    yes_list.append(td.get_text().split('. ')[1])
                elif isNo == True:
                    no_list.append(td.get_text().split('. ')[1])
                elif isBlank == True:
                    blank_list.append(td.get_text().split('. ')[1])
        return Vote(present, yes, no, blank, yes_list, no_list, blank_list)

from bs4 import BeautifulSoup
from typing import List

class Vote():
    def __init__(self, title: str, process: str, present: int, yes: int, no: int, blank: int, yes_list: List[str], no_list: List[str], blank_list: List[str]):
        self.title = title
        self.process = process
        self.present = present
        self.yes = yes
        self.no = no
        self.blank = blank
        self.yes_list = yes_list
        self.no_list = no_list
        self.blank_list = blank_list
        self.absent_list: List[str] = []

    @staticmethod
    def createVoteObj(soup: BeautifulSoup, process: str, votesList):
        b: BeautifulSoup = soup.find('b')
        span: BeautifulSoup = soup.find('span')
        if b is None:
            title: str = ""
        elif span is not None:
            title: str = span.get_text()
        else:
            title: str = b.get_text()
        yes_list: List[str] = []
        no_list: List[str] = []
        blank_list: List[str] = []
        isYes: bool = False
        isNo: bool = False
        isBlank: bool = False
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
                    if ". " in td.get_text():
                        yes_list.append(td.get_text().split('. ')[1])
                    else:
                        yes_list.append(td.get_text().split('.')[1])
                elif isNo == True:
                    if ". " in td.get_text():
                        no_list.append(td.get_text().split('. ')[1])
                    else:
                        no_list.append(td.get_text().split('.')[1])
                elif isBlank == True:
                    if ". " in td.get_text():
                        blank_list.append(td.get_text().split('. ')[1])
                    else:
                        blank_list.append(td.get_text().split('.')[1])
        return Vote(title, process, (len(yes_list) + len(no_list) + len(blank_list)), votesList[0], votesList[2], votesList[1], yes_list, no_list, blank_list)

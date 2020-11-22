from bs4 import BeautifulSoup

class Link():
    def __init__(self,
    number: str,
    proposalUrl: str,
    title: str,
    committeeName: str,
    committeeUrl: str,
    status: str):
        self.number = number
        self.proposalUrl = proposalUrl
        self.title = title
        self.committeeName = committeeName
        self.committeeUrl = committeeUrl
        self.status = status

    @staticmethod
    def getUrl(a: BeautifulSoup):
        return "https://www.logting.fo" + a["href"]

    @staticmethod
    def createLinkObj(td: BeautifulSoup):
        a = td[0].find("a")
        number: str = a.get_text()
        print(number)
        proposalUrl: str = Link.getUrl(a)
        title: str = td[1].get_text()
        committeeA = td[2].find("a")
        if "Ikki brúkt" in title:
            committeeName: str = td[2].get_text()
            committeeUrl: str = ""
        elif committeeA is None:
            committeeName: str = ""
            committeeUrl: str = ""
        else:
            committeeName: str = committeeA.get_text()
            committeeUrl: str = Link.getUrl(committeeA)
        status:str = td[3].get_text()
        return Link(number, proposalUrl, title, committeeName, committeeUrl, status)
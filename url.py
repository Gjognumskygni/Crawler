from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import time
import enum

class URLType(enum.Enum):
    proposal = 1
    votePage = 2
    voteHTML = 3
    votePDF = 4
    committee = 5


class Url():
    def __init__(self, scheme: str, netloc: str, path: str, params: str, query: str, fragment: str, iscrawled: bool, urlType: URLType ):
        self.scheme = scheme
        self.netloc = netloc
        self.path = path
        self.params = params
        self.query = query
        self.fragment = fragment
        self.iscrawled = iscrawled
        self.urlType = urlType

    @staticmethod
    def makeRequest(url: str):
        print(url)
        time.sleep(2)
        result = requests.get(url)
        src = result.content
        return BeautifulSoup(src, 'lxml')

    @staticmethod
    def _getURLType(urlType):
        print(urlType)
        if "proposal" in urlType:
            return URLType.proposal
        elif "votePage" in urlType:
            return URLType.votePage
        elif "voteHTML" in urlType:
            return URLType.voteHTML
        elif "votePDF" in urlType:
            return URLType.votePDF
        else:
            return URLType.committee

    @staticmethod
    def createURLObj(url: str, urlType):
        urlobj = urlparse(url)
        newUrlType = Url._getURLType(urlType)
        return Url(urlobj.scheme, urlobj.netloc,urlobj.path,urlobj.params,urlobj.query,urlobj.fragment,False, newUrlType)

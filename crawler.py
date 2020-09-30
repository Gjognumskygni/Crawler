from bs4 import BeautifulSoup
import requests
from vote import Vote
from proposal import Proposer

def crawl():
    result = requests.get("https://www.logting.fo/casenormal/viewState.gebs?caseState.id=28251&menuChanged=16")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    Proposer.createProposerObj(soup)
    """ Vote.createVoteObj(soup) """
    
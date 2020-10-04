from proposal import Process, Proposal
from bs4 import BeautifulSoup
from vote import Vote
import requests
import time

def printProposal(proposalObj: Proposal):
    print("Title:", proposalObj.title)
    print("Proposers:", proposalObj.proposers)

def isProposal(soup: BeautifulSoup):
    title = Proposal.getTitle(soup)
    if "Uppskot til løgtingslóg" in title:
        return True
    return False

def scrapeProposal(soup: BeautifulSoup):
    proposalObj = Proposal.createProposalObj(soup)
    printProposal(proposalObj)
    
def makeRequest(url: str):
    time.sleep(2)
    result = requests.get(url)
    src = result.content
    return BeautifulSoup(src, 'lxml')

def crawl():
    soup = makeRequest("https://www.logting.fo/casenormal/view.gebs?menuChanged=16&type=0&caseNormal.id=4708")
    if isProposal(soup) == True:
        Process.getProcess(soup)
        ''' scrapeProposal(soup) '''
    """ Vote.createVoteObj(soup) """
    
from proposal import Proposal
from link import Link
from bs4 import BeautifulSoup
from vote import Vote
from fm import ProposalToFile, ProposalFromFile
from url import Url
from typing import List

def crawlProposalLinks() -> List[Proposal]:
    url: str = "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2019&X-Requested-With=XMLHttpRequest&_=1606593520654"
    proposals: List[Proposal] = []
    soup = Url.makeRequest(url)
    tbody: BeautifulSoup = soup.find('tbody')
    i = 0
    for tr in tbody.find_all("tr"):
        if i < 1:
            td = tr.find_all("td")
            link = Link("","","","")
            proposals.append(Proposal("", "", "", Link.populateLinkObj(td,link)))
            i = i+1
    return proposals

def crawl():
    Proposals: List[Proposal] = crawlProposalLinks()
    length = len(Proposals)
    index = 1
    for proposal in Proposals:
        print("----- crawling new url -----")
        print(index)
        print(length)
        print(proposal.link.number)
        soup = Url.makeRequest(proposal.link.proposalUrl)
        proposal = Proposal.populateProposalObj(soup, proposal)
        index += 1
    ProposalToFile(Proposals)

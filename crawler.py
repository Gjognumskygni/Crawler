from proposal import Proposal
from link import Link
from bs4 import BeautifulSoup
from vote import Vote
from fm import ProposalToFile, linksToFile, ProposalFromFile
from url import makeRequest
from typing import List

def crawlProposalLinks() -> List[Link]:
    url: str = "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2018&X-Requested-With=XMLHttpRequest&_=1606033985196"
    links: List[Link] = []
    soup = makeRequest(url)
    tbody: BeautifulSoup = soup.find('tbody')
    for tr in tbody.find_all("tr"):
        td = tr.find_all("td")
        links.append(Link.createLinkObj(td))
    return links

def crawl():
    proposal_list: List[Proposal] = []
    links: List[Link] = crawlProposalLinks()
    length = len(links)
    index = 1
    for url in links:
        print("----- crawling new url -----")
        print(index)
        print(length)
        print(url.number)
        soup = makeRequest(url.proposalUrl)
        proposal_list.append(Proposal.createProposalObj(soup, url.title))
        index += 1
    ProposalToFile(proposal_list)

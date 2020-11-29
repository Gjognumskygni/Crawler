from proposal import Proposal
from link import Link
from bs4 import BeautifulSoup
from vote import Vote
from fm import *
from url import makeRequest
from typing import List
from print import *

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
    proposals = ProposalFromFile()
    party = PartiesFromFile()
    politicians = PoliticiansIncludingTimespansFromFile()

    #print(party)
    print("Parties")
    for i in party:
        printParty(i)

    #print(politicians)
    print("Politicians")
    for i in politicians:
        printPolitician(i)


    # print(proposals)

    # name_occurrance = []
    

    # # Extract all persons

    # for i in proposals: 
    #     name_occurrance.append(i.getVotes().blank_list)
    #     name_occurrance.append(i.getVotes().no_list)
    #     name_occurrance.append(i.getVotes().yes_list)

    # print(name_occurrance.count())
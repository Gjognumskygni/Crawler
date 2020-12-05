from proposal import Proposal
from link import Link
from bs4 import BeautifulSoup
from vote import Vote
from fm import ProposalToFile, ProposalFromFile
from url import Url
from typing import List



def crawlProposalLinks() -> List[Proposal]:
    urls = ["https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2019&X-Requested-With=XMLHttpRequest&_=1607020162247",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2018&X-Requested-With=XMLHttpRequest&_=1607020162246",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2017&X-Requested-With=XMLHttpRequest&_=1607020162245",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2016&X-Requested-With=XMLHttpRequest&_=1607020162244",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2015&X-Requested-With=XMLHttpRequest&_=1607020162243",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2014&X-Requested-With=XMLHttpRequest&_=1607020162242",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2013&X-Requested-With=XMLHttpRequest&_=1607020162241",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2012&X-Requested-With=XMLHttpRequest&_=1607020162240",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2011&X-Requested-With=XMLHttpRequest&_=1607020162239",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2010&X-Requested-With=XMLHttpRequest&_=1607020162238",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2009&X-Requested-With=XMLHttpRequest&_=1607020162237",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2008&X-Requested-With=XMLHttpRequest&_=1607020162236",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2007&X-Requested-With=XMLHttpRequest&_=1607020162235",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2006&X-Requested-With=XMLHttpRequest&_=1607020162234",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2005&X-Requested-With=XMLHttpRequest&_=1607020162233",
    "https://www.logting.fo/umbraco/Surface/MacroSurface/GetCasesByYearAndType?SelectedType=1&SelectedYear=2004&X-Requested-With=XMLHttpRequest&_=1607020162232"]
    proposals: List[Proposal] = []
    for url in urls:
        soup = Url.makeRequest(url)
        tbody: BeautifulSoup = soup.find('tbody')
        for tr in tbody.find_all("tr"):
            td = tr.find_all("td")
            link = Link("","","","")
            proposals.append(Proposal("", "", "", Link.populateLinkObj(td,link)))
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

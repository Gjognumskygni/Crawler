from proposal import Proposal
from vote import Vote
from bs4 import BeautifulSoup
from vote import Vote
from fm import dataToFile
from url import makeRequest
from typing import List

def crawl():
    urls: List[Vote] = ["https://www.logting.fo/mal/mal/?id=8673", "https://www.logting.fo/mal/mal/?id=8338", "https://www.logting.fo/mal/mal/?id=5422"]
    proposal_list: List[Proposal] = []
    for url in urls:
        soup = makeRequest(url)
        proposal_list.append(Proposal.createProposalObj(soup))
        dataToFile(proposal_list)
        
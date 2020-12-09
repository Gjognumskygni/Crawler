from typing import List, Dict
import json
from proposal import Proposal
from vote import Vote
from link import Link
from url import Url, URLType

def _urlEncoder(urlObj: Url):
    return {"scheme": urlObj.scheme,
            "netloc": urlObj.netloc,
            "path": urlObj.path,
            "params": urlObj.params,
            "query": urlObj.query,
            "fragment": urlObj.fragment,
            "iscrawled": urlObj.iscrawled,
            "urlType": urlObj.urlType.value}

def _linkEncoder(linkObj: Link):
    urlList = []
    for url in linkObj.urls:
        urlList.append(_urlEncoder(url)) 
    return {"number": linkObj.number,
            "title": linkObj.title,
            "committeeName": linkObj.committeeName,
            "status": linkObj.status,
            "urls": urlList}

def _voteEncoder(voteObj: Vote):
    newprocess = voteObj.process.strip("\n")
    return {"title": voteObj.title,
            "process": newprocess,
            "present": voteObj.present,
            "yes": voteObj.yes,
            "no": voteObj.no,
            "blank": voteObj.blank,
            "yes_list": voteObj.yes_list,
            "no_list": voteObj.no_list,
            "blank_list": voteObj.blank_list,
            "absent_list": voteObj.absent_list}

def _proposalEncoder(proposalObj: Proposal):
    striptTitile = proposalObj.type.strip("\r\n                                                ")
    newProposers = []
    newVote = []
    link = _linkEncoder(proposalObj.link)
    for proposer in proposalObj.proposers:
        newProposer = proposer.strip("\r\n")
        newProposer = newProposer.strip("                                                    ")
        newProposers.append(newProposer)
    for vote in proposalObj.votes:
        newVote.append(_voteEncoder(vote))
    return {"number": proposalObj.number,
            "title": proposalObj.title,
            "type": striptTitile,
            "proposers": newProposers,
            "tags": proposalObj.tags,
            "link": link,
            "votes": newVote}

def ProposalToFile(objList):
    dataList = []
    for proposalObj in objList:
        dataList.append(_proposalEncoder(proposalObj)) 
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False, indent=4)

def _voteDecoder(voteDict):
    yes_list: List[str] = []
    no_list: List[str] = []
    blank_list: List[str] = []
    for voter in voteDict["yes_list"]:
        yes_list.append(voter)
    for voter in voteDict["no_list"]:
        no_list.append(voter)
    for voter in voteDict["blank_list"]:
        blank_list.append(voter)
    returnObj: Vote = Vote(voteDict["title"], voteDict["process"], voteDict["present"], voteDict["yes"], voteDict["no"], voteDict["blank"], yes_list, no_list, blank_list)
    for absent in voteDict["absent_list"]:
        returnObj.absent_list.append(absent)
    return returnObj

def _urlDecoder(urlDict):
    return Url(urlDict["scheme"],urlDict["netloc"],urlDict["path"],urlDict["params"], urlDict["query"], urlDict["fragment"], urlDict["iscrawled"], urlDict["urlType"])

def _linkDecoder(linkDict):
    returnLink = Link(linkDict["number"], linkDict["title"], linkDict["committeeName"], linkDict["status"])
    for url in linkDict["urls"]:
        returnLink.urls.append(_urlDecoder(url))
    return returnLink

def _proposalDecoder(proposalDict):
    returnObj: Proposal = Proposal(proposalDict["number"], proposalDict["title"], proposalDict["type"], _linkDecoder(proposalDict["link"]))
    for proposer in proposalDict["proposers"]:
        returnObj.proposers.append(proposer)
    for vote in proposalDict["votes"]:
        returnObj.votes.append(_voteDecoder(vote))
    for tag in proposalDict["tags"]:
        returnObj.tags.append(tag)
    return returnObj

def ProposalFromFile():
    proposals: List[Proposal] = []
    with open('1998-2019data.json') as json_file:
        proposalList = json.load(json_file)
        for proposalDict in proposalList:
            proposals.append(_proposalDecoder(proposalDict))
    return proposals

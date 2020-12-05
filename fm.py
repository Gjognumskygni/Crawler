from typing import List, Dict
import json
from proposal import Proposal
from vote import Vote
from link import Link
from url import Url

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
    returnObj: Vote = Vote("", "", 0, 0, 0, 0, [], [], [])
    for key, value in voteDict.items():
        if key == "title":
            returnObj.title = value
        elif key == "process":
            returnObj.process = value
        elif key == "present":
            returnObj.present = int(value)
        elif key == "yes":
            returnObj.yes = int(value)
        elif key == "no":
            returnObj.no = int(value)
        elif key == "blank":
            returnObj.blank = int(value)
        elif key == "yes_list":
            if len(value) != 0:
                for voter in value:
                    returnObj.yes_list.append(voter)
        elif key == "no_list":
            if len(value) != 0:
                for voter in value:
                    returnObj.no_list.append(voter)
        elif key == "blank_list":
            if len(value) != 0:
                for voter in value:
                    returnObj.blank_list.append(voter)
        elif key == "absent_list":
            if len(value) != 0:
                for absent in value:
                    returnObj.blank_list.append(absent)
    return returnObj

def _urlDecoder(urlDict):
    returnLink = Url("","","","","","", False,"")
    for key, value in urlDict.items():
        if key == "scheme":
            returnLink.scheme = value
        elif key == "netloc":
            returnLink.netloc = value
        elif key == "path":
            returnLink.path = value
        elif key == "params":
            returnLink.params = value
        elif key == "query":
            returnLink.query = value
        elif key == "fragment":
            returnLink.fragment = value
        elif key == "iscrawled":
            returnLink.iscrawled = value
        else:
            returnLink.urlType = value
    return returnLink

def _linkDecoder(linkDict):
    returnLink = Link("","","","")
    for key, value in linkDict.items():
        if key == "number":
            returnLink.number = value
        elif key == "title":
            returnLink.title = value
        elif key == "committeeName":
            returnLink.committeeName = value
        elif key == "status":
            returnLink.status
        else:
            for url in value:
                returnLink.urls.append(_urlDecoder(url))
    return returnLink

def _proposalDecoder(proposalDict):
    returnObj: Proposal = Proposal("","","", Link("","","",""))
    for key, value in proposalDict.items():
        if key == "number":
            returnObj.number = value
        if key == "title":
            returnObj.title = value
        elif key == "type":
            returnObj.type = value
        elif key == "link":
            returnObj.link = _linkDecoder(value)
        elif key == "proposers":
            for proposer in value:
                returnObj.proposers.append(proposer)
        elif key == "votes":
            if len(value) != 0:
                for vote in value:
                    returnObj.votes.append(_voteDecoder(vote))
        else:
            returnObj.tags = value
    return returnObj

def ProposalFromFile():
    proposals: List[Proposal] = []
    with open('data.json') as json_file:
        proposalList = json.load(json_file)
        for proposalDict in proposalList:
            proposals.append(_proposalDecoder(proposalDict))
    return proposals

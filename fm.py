from typing import List, Dict
import json
from proposal import Proposal
from vote import Vote

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
            "blank_list": voteObj.blank_list}

def _proposalEncoder(proposalObj: Proposal):
    striptTitile = proposalObj.type.strip("\r\n                                                ")
    newProposers = []
    newVote = []
    for proposer in proposalObj.proposers:
        newProposer = proposer.strip("\r\n")
        newProposer = newProposer.strip("                                                    ")
        newProposers.append(newProposer)
    for vote in proposalObj.votes:
        newVote.append(_voteEncoder(vote))
    return {"title": proposalObj.title, "type": striptTitile, "proposers": newProposers, "votes": newVote}

def ProposalToFile(objList):
    dataList = []
    for proposalObj in objList:
        dataList.append(_proposalEncoder(proposalObj)) 
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False, indent=4)

def _linkEncoder(linkObj):
    return {"number": linkObj.number, "proposalUrl": linkObj.proposalUrl, "title": linkObj.title, "committeeName": linkObj.committeeName, "committeeUrl": linkObj.committeeUrl, "status": linkObj.status}

def linksToFile(objList):
    linkList = []
    for linkobj in objList:
        linkList.append(_linkEncoder(linkobj)) 
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(linkList, f, ensure_ascii=False, indent=4)

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
    return returnObj

def _proposalDecoder(proposalDict):
    returnObj: Proposal = Proposal("","")
    for key, value in proposalDict.items(): 
        if key == "title":
            returnObj.title = value
        elif key == "type":
            returnObj.type = value
        elif key == "proposers":
            for proposer in value:
                returnObj.proposers.append(proposer)
        else:
            if len(value) != 0:
                for vote in value:
                    returnObj.votes.append(_voteDecoder(vote))
    return returnObj

def ProposalFromFile():
    proposals: List[Proposal] = []
    with open('2014-2019data.json') as json_file:
        proposalList = json.load(json_file)
        for proposalDict in proposalList:
            proposals.append(_proposalDecoder(proposalDict))
    return proposals

from typing import List, Dict
import json
from proposal import Proposal
from vote import Vote

def voteEncoder(voteObj: Vote):
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

def proposalEncoder(proposalObj: Proposal):
    striptTitile = proposalObj.type.strip("\r\n                                                ")
    newProposers = []
    newVote = []
    for proposer in proposalObj.proposers:
        newProposer = proposer.strip("\r\n")
        newProposer = newProposer.strip("                                                    ")
        newProposers.append(newProposer)
    for vote in proposalObj.votes:
        newVote.append(voteEncoder(vote))
    return {"title": proposalObj.title, "type": striptTitile, "proposers": newProposers, "votes": newVote}

def dataToFile(objList):
    dataList = []
    for proposalObj in objList:
        dataList.append(proposalEncoder(proposalObj)) 
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False, indent=4)

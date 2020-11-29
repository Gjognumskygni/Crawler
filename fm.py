from typing import List, Dict
import json
from proposal import Proposal
from vote import Vote
from politician import Politician, Timespan, Role, Party

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
    with open('data/2014-2019data.json') as json_file:
        proposalList = json.load(json_file)
        for proposalDict in proposalList:
            proposals.append(_proposalDecoder(proposalDict))
    return proposals

def _partyDecoder(partyDict):
    returnObj: Party = Party("","","")
    for key, value in partyDict.items(): 
        if key == "name":
            returnObj.name = value
        elif key == "letter":
            returnObj.letter = value
        elif key == "guid":
            returnObj.guid = value
    return returnObj

def PartiesFromFile():
    parties: List[Party] = []
    with open('data/parties.json') as json_file:
        partyList = json.load(json_file)
        for partyDict in partyList:
            parties.append(_partyDecoder(partyDict))
    return parties

def _politicianDecoder(politicianDict):
    returnObj: Politician = Politician("","",[])
    for key, value in politicianDict.items(): 
        if key == "name":
            returnObj.name = value
        elif key == "guid":
            returnObj.guid = value
    return returnObj

def _politicianTimespanDecoder(politicianDict, parties, politicians):
    returnObj: Politician = Politician("","",[])
    for key, value in politicianDict.items(): 
        if key == "name":
            returnObj.name = value
        elif key == "guid":
            returnObj.guid = value
        elif key == "timespans":
            for timespan in value:
                returnObj.timespans.append(_timespanDecoder(timespan, parties, politicians))
    return returnObj

def _timespanDecoder(timespanDict, parties, politicians):
    returnObj: Timespan = Timespan("","","","","")
    for key, value in timespanDict.items(): 
        if key == "party":
            returnObj.party = [x for x in parties if x.guid == value][0]
        elif key == "role":
            returnObj.role = Role[value]
        elif key == "start":
            returnObj.start = value
        elif key == "end":
            returnObj.end = value
        elif key == "substituteFor":
            returnObj.substituteFor = None if value == None else [x for x in politicians if x.guid == value][0].guid
    return returnObj

def PoliticiansWithoutTimespansFromFile():
    allPoliticians: List[Politician] = []
    politicians: List[Politician] = []
    with open('data/politicians.json') as json_file:
        politicianList = json.load(json_file)
        for politicianDict in politicianList:
            politicians.append(_politicianDecoder(politicianDict))
    return politicians

def PoliticiansIncludingTimespansFromFile():
    parties: List[Party] = PartiesFromFile()
    politicians: List[Politician] = PoliticiansWithoutTimespansFromFile()

    # Load politicians' timespans
    politicians: List[Politician] = []
    with open('data/politicians.json') as json_file:
        politicianList = json.load(json_file)
        for politicianDict in politicianList:
            politicians.append(_politicianTimespanDecoder(politicianDict, parties, politicians))
    return politicians


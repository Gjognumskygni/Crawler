from proposal import Proposal
from vote import Vote
def printProposal(proposalObj: Proposal):
    print("Title:", proposalObj.title)
    print("Proposers:", proposalObj.proposers)
    for vote in proposalObj.votes:
        print("title:", vote.title)
        print("process:", vote.process)
        print("present:", vote.present)
        print("yes:", vote.yes)
        print("no:", vote.no)
        print("blank:", vote.blank)
        print("---yes list---")
        for yes in vote.yes_list:
            print(yes)
        print("---no list---")
        for no in vote.no_list:
            print(no)
        print("---blank list---")
        for blank in vote.blank_list:
            print(blank)

def printVote(vote: Vote):
    print("title:", vote.name)
    print("present:", vote.present)
    print("yes:", vote.yes)
    print("no:", vote.no)
    print("blank:", vote.blank)
    print("---yes list---")
    for yes in vote.yes_list:
        print(yes)
    print("---no list---")
    for no in vote.no_list:
        print(no)
    print("---blank list---")
    for blank in vote.blank_list:
        print(blank)
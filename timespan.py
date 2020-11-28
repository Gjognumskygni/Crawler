from party import Party
from enum import Enum
import datetime

class Role(Enum):
    Unassigned = 1
    PrimeMinister = 2
    Minister = 3
    Legislator = 4
    

class Timespan():
    def __init__(self, party: Party, start: datetime, end: datetime, role: Role):
        self.party = party
        self.start = start
        self.end = end
        self.role = role
        
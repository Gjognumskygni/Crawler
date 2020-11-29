from typing import List
import datetime
from enum import Enum

class Party():
    def __init__(self, name: str, letter: str, guid: str):
        self.name = name
        self.letter = letter
        self.guid = guid

class Role(Enum):
    Running = 1
    Unassigned = 2
    Legislator = 3
    Minister = 4
    PrimeMinister = 5
    Substitute = 6

class Timespan():
    def __init__(self, party: Party, start: datetime, end: datetime, role: Role, substituteFor: str):
        self.party = party
        self.start = start
        self.end = end
        self.role = role
        self.substituteFor = substituteFor

class Politician():
    def __init__(self, name: str, guid: str, timespans: List[Timespan]):
        self.name = name
        self.guid = guid
        self.timespans = timespans
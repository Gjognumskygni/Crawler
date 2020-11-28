from party import Party
from timespan import Timespan
from typing import List

class Politician():
    def __init__(self, name: str, guid: str, timespans: List[Timespan]):
        self.name = name
        self.guid = guid
        self.timespans = timespans

from MediaEntry import MediaEntry
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Amenities:
    # Is this supposed to be a dict?
    # amenities: List[MediaEntry]
    amenities: Dict

    def __init__(self, li: List):
        self.amenities = {'general': li, 'room': []}

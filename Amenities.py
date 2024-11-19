from MediaEntry import MediaEntry
from typing import List, Dict
from dataclasses import dataclass
from utils import decide_attr

@dataclass
class Amenities:
    general: List 
    room: List 

    @classmethod
    def from_list( cls, li: List):
        amenities = {'general': li, 'room': []}

        return cls(**amenities)
    
    def merge(self, other):

        amenities = Amenities([], [])

        for key in [key for key in dir(other) if not key.startswith('__') and not callable(getattr(other, key))]:

            setattr(amenities, key, decide_attr(getattr(other, key), getattr(self, key)))

        

        return amenities

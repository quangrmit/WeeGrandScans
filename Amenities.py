from typing import List
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

          # Loop through attributes of an object
        for attribute in [key for key in dir(other) if not key.startswith('__') and not callable(getattr(other, key))]:

            # Get values of the attribute from 2 objects
            self_attribute = getattr(self, attribute)
            other_attribute = getattr(other, attribute)

            # Decide on which value to take
            decision = decide_attr(other_attribute, self_attribute)

            # Set the attribute to the better value
            setattr(amenities, attribute, decision)
        

        return amenities

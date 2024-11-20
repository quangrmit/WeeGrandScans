from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional
from utils import decide_attr


@dataclass_json
@dataclass
class Location:
    lat: Optional[int] = None
    lng: Optional[int] = None
    address: Optional[str] = None
    city: str = None
    country: str = None

    def merge(self, other):

        location = Location()

        # Loop through attributes of an object
        for attribute in [key for key in dir(other) if not key.startswith('__') and not callable(getattr(other, key))]:

            # Get values of the attribute from 2 objects
            self_attribute = getattr(self, attribute)
            other_attribute = getattr(other, attribute)

            # Decide on which value to take
            decision = decide_attr(other_attribute, self_attribute)

            # Set the attribute to the better value
            setattr(location, attribute, decision)
        return location

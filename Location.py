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

        for key in [key for key in dir(other) if not key.startswith('__') and not callable(getattr(other, key))]:

            setattr(location, key, decide_attr(getattr(other, key), getattr(self, key)))
        return location




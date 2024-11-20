from MediaEntry import MediaEntry
from dataclasses import dataclass, field
from typing import List, Optional, Union
from utils import decide_attr


@dataclass
class Images:
    rooms: Optional[List[MediaEntry]] = field(default_factory=list)
    site: Union[List[MediaEntry]] = field(default_factory=list)
    amenities: Optional[List[MediaEntry]] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def merge(self, other):

        images = Images()

           # Loop through attributes of an object
        for attribute in [key for key in dir(other) if not key.startswith('__') and not callable(getattr(other, key))]:

            # Get values of the attribute from 2 objects
            self_attribute = getattr(self, attribute)
            other_attribute = getattr(other, attribute)

            # Decide on which value to take
            decision = decide_attr(other_attribute, self_attribute)

            # Set the attribute to the better value
            setattr(images, attribute, decision)

        return images

    @classmethod
    def from_list(cls, li):
        images = {'rooms': li, 'site': [], 'amenities': []}
        return cls(**images)

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

        for key in [key for key in dir(other) if not key.startswith('__') and not callable(getattr(other, key))]:

            setattr(images, key, decide_attr(
                getattr(other, key), getattr(self, key)))

        return images

    @classmethod
    def from_list(cls, li):
        images = {'rooms': li, 'site': [], 'amenities': []}
        return cls(**images)

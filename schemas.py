from typing import Union, List, Dict
from Location import Location
from Amenities import Amenities
from Images import Images
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from utils import decide_attr
from abc import ABC, abstractmethod


class BaseSupplierSchema(ABC):

    @abstractmethod
    def adapt(self, other):
        pass

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass
@dataclass_json
class Hotel():
    id: str
    destination_id: str
    name: str
    description: str
    location: Location
    amenities: Amenities
    images: Images
    booking_conditions: List[str]
    
    def merge(self, other):
        result = Hotel()
        result.id = self.id
        result.destination_id = self.destination_id
        
        self_len = len(self.name) if self.name else 0
        other_len = len(other.name) if other.name else 0
        result.name = self.name if self_len >= other_len else other.name

        self_len = len(self.description) if self.description else 0
        other_len = len(other.description) if other.description else 0
        result.description = self.description if self_len >= other_len else other.description

        result.location = self.location.merge(other.location)
        result.amenities = self.amenities.merge(other.amenities)
        result.images = self.images.merge(other.images)


        result.booking_conditions = self.booking_conditions if len(self.booking_conditions) >= len(other.booking_conditions) else other.booking_conditions
        return result


@dataclass
class Acme(BaseSupplierSchema):
    Id: str
    DestinationId: str
    Name: str
    Latitude: Union[str, float, None]
    Longitude: Union[str, float, None]
    Address: str
    City: str
    Country: str
    PostalCode: str
    Description: str
    Facilities: List[str]

    
    @staticmethod
    def adapt(ins) -> Hotel:
        hotel = Hotel()
        hotel.id = ins.Id
        hotel.destination_id = ins.DestinationId
        hotel.name = ins.Name
        hotel.description = ins.Description
        hotel.location = Location(ins.Latitude, ins.Longitude, ins.Address, ins.City, ins.Country)
        hotel.amenities = Amenities.from_list(ins.Facilities)
        hotel.booking_conditions = []
        hotel.images = Images.from_list([])

        return hotel
        
    

@dataclass
class Patagonia(BaseSupplierSchema):
    id: str
    destination: int
    name: str
    lat: Union[float, None]
    lng: Union[float, None]
    address: Union[str, None]
    info: Union[str, None]
    amenities: Union[List[str], None]
    images: Dict

    
    @staticmethod
    def adapt(ins) -> Hotel:
        hotel = Hotel()
        hotel.id = ins.id
        hotel.destination_id = ins.destination
        hotel.name = ins.name
        hotel.description = ins.info
        hotel.location = Location(ins.lat, ins.lng, ins.address, None, None)
        hotel.amenities = Amenities.from_list(ins.amenities)

        hotel.images = Images.from_dict(ins.images)
        hotel.booking_conditions = []

        return hotel

@dataclass
class Paperflies(BaseSupplierSchema):
    hotel_id: str
    destination_id: str
    hotel_name: str
    location: Dict
    details: str
    amenities: Dict
    images: Dict
    booking_conditions: List[str]



    @staticmethod
    def adapt(ins) -> Hotel:
        hotel = Hotel()
        hotel.id = ins.hotel_id
        hotel.destination_id = ins.destination_id
        hotel.name = ins.hotel_name
        hotel.description = ins.details
        hotel.location = Location(None, None,  ins.location['address'], None, ins.location['country'])
        hotel.amenities = Amenities(ins.amenities['general'], ins.amenities['room'])
        hotel.images = Images.from_dict(ins.images)
        hotel.booking_conditions = ins.booking_conditions

        return hotel

from typing import Union, List, Dict
from Location import Location
from Amenities import Amenities
from Images import Images
from dataclasses import dataclass

# @dataclass
class Hotel:
    id: str
    destination_id: str
    name: str
    description: str
    location: Location
    amenities: Amenities
    images: Images
    booking_conditions: list[str]

    def __repr__(self) -> str:
        return str({'id': self.id, 'destination_id': self.destination_id, 'name': self.name, 'description': self.description, 'location': self.location, 'amenities': self.amenities, 'images': self.images, 'booking_conditions': self.booking_conditions})


@dataclass
class Acme:
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

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
    
    @staticmethod
    def adapt(ins) -> Hotel:
        hotel = Hotel()
        hotel.id = ins.Id
        hotel.destination_id = ins.DestinationId
        hotel.name = ins.Name
        hotel.description = ins.Description
        hotel.location = Location(ins.Latitude, ins.Longitude, ins.Address, ins.City, ins.Country)
        hotel.amenities = Amenities(ins.Facilities)
        hotel.booking_conditions = []
        hotel.images = []

        return hotel
        
    

@dataclass
class Patagonia:
    id: str
    destination: int
    name: str
    lat: Union[float, None]
    lng: Union[float, None]
    address: Union[str, None]
    info: Union[str, None]
    amenities: Union[List[str], None]
    images: Dict

    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    @staticmethod
    def adapt(ins) -> Hotel:
        hotel = Hotel()
        hotel.id = ins.id
        hotel.destination_id = ins.destination
        hotel.name = ins.name
        hotel.description = ins.info
        # hotel.location = Location(ins.lat, ins.lng, ins.address, ins.city, ins.country)
        hotel.location = Location(ins.lat, ins.lng, ins.address, None, None)
        hotel.amenities = Amenities(ins.amenities)
        hotel.images = ins.images
        hotel.booking_conditions = []

        return hotel

@dataclass
class Paperflies:
    hotel_id: str
    destination_id: str
    hotel_name: str
    location: Location
    details: str
    amenities: Dict
    images: Dict
    booking_conditions: List[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    @staticmethod
    def adapt(ins) -> Hotel:
        hotel = Hotel()
        hotel.id = ins.hotel_id
        hotel.destination_id = ins.destination_id
        hotel.name = ins.hotel_name
        hotel.description = ins.details
        # hotel.location = Location(ins.lat, ins.lng, ins.address, ins.city, ins.country)
        hotel.location = ins.location
        hotel.amenities = Amenities(ins.amenities)
        hotel.images = ins.images
        hotel.booking_conditions = []

        return hotel

from typing import Union, List, Dict
from Location import Location
from Amenities import Amenities
from Images import Images
from dataclasses import dataclass

@dataclass
class Hotel:
    id: str
    destination_id: str
    name: str
    description: str
    location: Location
    amenities: Amenities
    images: Images
    booking_conditions: list[str]

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
    
    def adapt(self) -> Hotel:
        hotel = Hotel()
        hotel.id = self.Id
        hotel.destination_id = self.DestinationId
        hotel.name = self.Name
        hotel.description = self.Description
        hotel.location = Location(self.Latitude, self.Longitude, self.Address, self.City, self.Country)
        hotel.amenities = Amenities(self.Facilities)

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



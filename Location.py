from dataclasses import dataclass

@dataclass
class Location:
    lat: int
    lng: int
    address: str
    city: str
    country: str


    def validate(self):
        #validate some of the fields (maybe)
        pass



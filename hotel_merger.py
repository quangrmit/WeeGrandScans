import argparse
from dataclasses import dataclass
import requests
import json
from typing import List, Union, Dict
from Location import Location
from Amenities import Amenities
from Images import Images
from schemas import Acme, Hotel, Paperflies, Patagonia
from fetchers import AcmeFetcher, PaperfliesFetcher, PatagoniaFetcher


# create a mutual parent class (for fetching first of all)


class HotelsInstance:

    hotels = []
    def __init__(self):
        pass
    
    def merge(cls):
        # merge hotels in self.hotels
        # First we need to adapt each hotel to a mutual schema. Where to do that?

        '''
            we have the hotels fetcher, 
            so first we must fetch the hotels
            then adapt the the schema
            then concatenate them

        '''

    @classmethod
    def create_hotel_fetcher(cls, hotel_name):
        if hotel_name == 'acme':
            # (DONE) also makclse sure that each hotel is created once (Singleton)
            hotel = AcmeFetcher()
            cls.hotels.append(hotel)
            return hotel

        elif hotel_name == 'patagonia':
            hotel = PatagoniaFetcher()
            cls.hotels.append(hotel)
            return hotel
        elif hotel_name == 'paperflies':
            hotel = PaperfliesFetcher()
            cls.hotels.append(hotel)
            return hotel
        else:
            raise Exception('Invalid hotel name')


class HotelMerger:
    def merge(self, hotel_names: List[str]):
        pass
        
        

def hotel_merger(hotel_ids, destination_ids):
    pass


def main():
    parser = argparse.ArgumentParser(description="Merge hotel information based on hotel and destination IDs.")

    parser.add_argument('hotel_ids', type=str, help="Comma-separated list of hotel IDs or 'none'")
    parser.add_argument('destination_ids', type=str, help="Comma-separated list of destination IDs or 'none'")

    args = parser.parse_args()

    hotel_merger(args.hotel_ids, args.destination_ids)

if __name__ == "__main__":
    
    
    patagonia = HotelsInstance.create_hotel_fetcher('paperflies')
    hotels = patagonia.fetch()
    for indi in hotels:
        tmp = Paperflies.from_dict(indi)
        print(tmp)
        print('\n')
    
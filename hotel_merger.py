import argparse
from dataclasses import dataclass
import requests
import json
from typing import List, Union, Dict
from Location import Location
from Amenities import Amenities
from Images import Images
from schemas import Acme, Hotel, Paperflies, Patagonia
from fetchers import AcmeFetcher, PaperfliesFetcher, PatagoniaFetcher, Fetcher

class HotelsInstance:

    hotels = []
    merged = []
    def __init__(self):
        pass
    
    @classmethod
    def merge(cls):

        '''
            we have the hotels fetcher, 
            so first we must fetch the hotels
            then adapt the the schema
            then concatenate them

        '''
        for h in cls.hotels:
            print(h.url)
            data = h.fetch()
            for i in range(len(data)):
                tmp = h.cl.from_dict(data[i])
                data[i] = h.cl.adapt(tmp)
                cls.merged.append(data[i])
                print(data[i])
            print(data)
        

    @classmethod
    def create_hotel_fetcher(cls, hotel_name):
        cl = None
        if hotel_name == 'acme':
            cl = Acme
        elif hotel_name == 'patagonia':
            cl = Patagonia
        elif hotel_name == 'paperflies':
            cl = Paperflies
        else:
            raise Exception('Invalid hotel name')
        f = Fetcher(hotel_name, cl)
        cls.hotels.append(f)
        return f


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
    
    HotelsInstance.create_hotel_fetcher('acme')
    HotelsInstance.create_hotel_fetcher('patagonia')
    HotelsInstance.create_hotel_fetcher('paperflies')

    HotelsInstance.merge()
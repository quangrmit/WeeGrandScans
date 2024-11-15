import requests
import json 
from typing import List


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

# @singleton
class Fetcher:
    base_url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/"
    def __init__(self, hotel_name, cl):
        self.url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/" + hotel_name
        self.data = None
        self.cl = cl

    
    def fetch(self):
        res = requests.get(self.url)
        response = json.loads(res.text)
        self.data = response
        return response

    def adapt(self):
        for i in range(len(self.data)):
            one = self.data[i]
            self.data[i] = self.cl.adapt(one)
        return self.data


@singleton
class AcmeFetcher:
    def __init__(self) -> None:
        self.url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"
        self.data = None
    
    def fetch(self) -> List[dict]:
        res = requests.get(self.url)
        response = json.loads(res.text)
        self.data = response
        return response



        
@singleton        
class PatagoniaFetcher:
    def __init__(self) -> None:
     self.url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"

    def fetch(self) -> List[dict]:
        res = requests.get(self.url)
        response = json.loads(res.text)
        return response
    
@singleton
class PaperfliesFetcher:
    def __init__(self) -> None:
     self.url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"

    def fetch(self) -> List[dict]:
        res = requests.get(self.url)
        response = json.loads(res.text)
        return response
    

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

class Fetcher:
    def __init__(self):
        self.base_url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/"
    def fetch(self):
        pass

    def adapt(self):
        pass

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
    

import requests
import json 
from typing import List



class Fetcher:
    def __init__(self, hotel_name, hotel_classname):
        self.base_url = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/"
        self.url = self.base_url + hotel_name
        self.hotel_classname = hotel_classname

    
    def fetch(self):
        res = requests.get(self.url)
        response = json.loads(res.text)
        self.data = response
        return response

    def adapt(self):
        for i in range(len(self.data)):
            one = self.data[i]
            self.data[i] = self.hotel_classname.adapt(one)
        return self.data


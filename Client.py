import requests
from flask import json


class Client:
    def __init__(self, adress, requests_count=1000):
        self.adress = adress
        self.requests_count = requests_count
        self.stats = {}
        self.free_node = ""
        self.loaded_node = ""
        self.count = 0

    def update_stats(self):
        if self.count == 0:
            stats = json.loads(requests.get(self.adress + "/getstats").text)
            self.loaded_node = max(stats, key=lambda adress: stats[adress])
            self.free_node = max(stats, key=lambda adress: stats[adress])
        self.count = (self.count + 1) % self.requests_count

    def read(self):
        self.update_stats()
        return json.loads(requests.get(self.loaded_node + "/readmessage").text)

    def write(self, message):
        self.update_stats()
        requests.post(self.free_node + '/writemessage', data=json.dumps(message))
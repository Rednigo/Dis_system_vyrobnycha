import DataNode
import json


class ControlNode:
    def __init__(self, adress):
        self.adress = adress
        self.stats = []

    def get_stats(self):
        to_json = {}
        for i in self.stats():
            to_json[i] = DataNode.get_stats()
        return json.dumps(to_json)

    def add_node(self, getted_json):
        ip_dic = json.loads(getted_json)
        to_add = ip_dic["ip"]
        self.stats.append(to_add)

    def remove_node(self, getted_json):
        ip_dic = json.loads(getted_json)
        to_add = ip_dic["ip"]
        self.stats.remove(to_add)

    def save_stats(self):
        with open(str(self.adress)+".txt", 'w') as node:
            node.write(self.stats)

    def read_stats(self):
        with open(str(self.adress)+".txt", 'r') as node:
            node.read(self.stats)

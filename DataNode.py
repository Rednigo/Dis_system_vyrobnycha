import json

class DataNode:
    def __init__(self, adress):
        self.adress = adress
        self.messages = []

    def get_stats(self):
        return {self.adress: len(self.messages)}

    def read(self):
        return json.dumps(self.messages[0])

    def write(self, message):
        ip_dic = json.loads(message)
        to_add = ip_dic["data"]
        self.stats.append(to_add)
        with open(str(self.adress)+".txt", 'a') as node:
            node.write(to_add)

    def resend(self):
        pass




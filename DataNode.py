
class DataNode:
    def __init__(self, adress):
        self.adress=adress
        self.messages=[]

    def get_stats(self):
        return {self.adress: len(self.messages)}


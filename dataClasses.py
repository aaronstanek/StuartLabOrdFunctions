class data_event:
    def __init__(self):
        self.meta = dict()
        self.data = dict()
    def fromDict(self,d):
        self.meta = d["EV_META"]
        self.data = d["EV_DATA"]

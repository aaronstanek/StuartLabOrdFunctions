class data_event:
    def __init__(self):
        self.meta = dict()
        self.data = dict()
    def fromDict(self,d):
        self.meta = d["EV_META"]
        self.data = d["DATA"]
    def getMaxes(self):
        u = list(self.data)
        ou = dict()
        for chan in u:
            ou[chan] = max(self.data[chan])
        return ou

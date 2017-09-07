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
    def getIntegral(self):
        ou = dict()
        for chan in self.data:
            spot = int(float(len(self.data[chan]))/float(8))
            cal = 0
            for i in range(0,spot):
                cal = cal+self.data[chan][i]
            val = 0
            for i in range(spot,len(self.data[chan])):
                val = val+self.data[chan][i]
            ave_value = float(val)/float(len(self.data[chan])-spot) - float(cal)/float(spot)
            total_value = ave_value*float(self.meta["DISPLAY_TIMEDIVISION"])
            ou[chan] = total_value
        return ou

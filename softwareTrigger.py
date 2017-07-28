def scanChannel(data,lev,direction):
    #data is a list of floats
    #lev is a float
    #direction is a string ("above","below")
    if dir=="above":
        for x in data:
            if x>=lev:
                return True
        return False
    elif dir=="below":
        for x in data:
            if x<=lev:
                return True
        return False
    else:
        raise Exception("incorrect argument to scanChannel dir: "+str(direction))

class softwareTrigger:
    def __init__(self):
        self.lev = dict()
        self.direction = ""
    def setLevel(self,channel,level):
        self.lev[str(channel)] = float(level)
    def setDirection(self,direction):
        self.direction = direction
    def scan(self,ev):
        #ev is a data_event object
        for x in self.lev:
            good = scanChannel(ev.data[x],lev[x],self.direction)
            if good==False:
                return False
        return True

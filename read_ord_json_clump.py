import json
import dataClasses

def readRaw(filename):
    infile = open(filename,"r")
    indata = infile.read()
    infile.close()
    return indata

def makeEvents(rawdata):
    ou = []
    for x in rawdata["EVENTS"]:
        #x is an event structure
        ev = dataClasses.data_event()
        ev.fromDict(x)
        ou.append(ev)
    return ou

def read(filename):
    raw = readRaw(filename)
    st = json.loads(raw)
    del(raw)
    ev_list = makeEvents(st)
    del(st)
    return ev_list

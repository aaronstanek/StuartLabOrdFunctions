import json

def makeStructure(osc_meta,ev_list):
    events = []
    for x in ev_list:
        ev = dict()
        ev["EV_META"] = x.meta
        ev["DATA"] = x.data
        events.append(ev)
    st = dict()
    st["OSC_META"] = osc_meta
    st["EVENTS"] = events
    return st

def encode(st):
    ou = json.dumps(st)
    return ou

def save(filename,osc_meta,ev_list):
    ou = encode(makeStructure(osc_meta,ev_list))
    outfile = open(filename,"w")
    outfile.truncate(0)
    outfile.seek(0,0)
    outfile.write(ou)
    outfile.close()

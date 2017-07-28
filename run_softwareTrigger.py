import os

import read_ord_json_clump as clread
import write_ord_json_clump as clwrite
import softwareTrigger

def getInputFiles(path):
    raw = os.listdir(path)
    ou = []
    for x in raw:
        if os.path.isfile(path+x):
            ou.append(x)
    return ou

def main(inpath,outpath,lev,direction):
    #lev is a dict
    #direction is a string
    #see softwareTrigger.py::softwareTrigger for more information
    st = softwareTrigger.softwareTrigger()
    st.lev = lev
    st.direction = direction
    files = getInputFiles(inpath)
    for f in files:
        [osc_meta,ev_list] = clread.read(inpath+f)
        ev_list_scanned = st.scanList(ev_list)
        clwrite(outpath,osc_meta,ev_list_scanned)
        del(osc_meta)
        del(ev_list)
        del(ev_list_scanned)

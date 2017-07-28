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

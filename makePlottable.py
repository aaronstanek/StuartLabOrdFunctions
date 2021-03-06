import run_softwareTrigger
import read_ord_json_clump
import histplotlib

def plotChop(xval,yval,**options):
    if "chopxmax" in options:
        if xval>options["chopxmax"]:
            return True
    if "chopymax" in options:
        if yval>options["chopymax"]:
            return True
    if "chopxmin" in options:
        if xval<options["chopxmin"]:
            return True
    if "chopymin" in options:
        if yval<options["chopymin"]:
            return True
    return False

def makePlottable(data,get1,get2,**options):
    #data is a list of dict (str->float)
    #get1 and get2 are str, specifying keys in the dicts of data
    useIntegral = False
    if "useIntegral" in options:
        if options["useIntegral"]==True:
            useIntegral = True
    if len(data)==0:
        raise Exception("This is an empty dataset.")
    ran = dict()
    if useIntegral:
        w = data[0].getIntegral()
    else:
        w = data[0].getMaxes()
    xVal = w[get1]
    yVal = w[get2]
    ran["xmin"] = xVal
    ran["xmax"] = xVal
    ran["ymin"] = yVal
    ran["ymax"] = yVal
    ou = []
    for x in data:
        if useIntegral:
            w = x.getIntegral()
        else:
            w = x.getMaxes()
        xVal = w[get1]
        yVal = w[get2]
        if xVal<ran["xmin"]:
            ran["xmin"] = xVal
        if xVal>ran["xmax"]:
            ran["xmax"] = xVal
        if yVal<ran["ymin"]:
            ran["ymin"] = yVal
        if yVal>ran["ymax"]:
            ran["ymax"] = yVal
        if plotChop(xVal,yVal,**options)==False:
            ou.append([xVal,yVal])
    return ou,ran

def plotChop_single(xval,**options):
    if "chopxmax" in options:
        if xval>options["chopxmax"]:
            return True
    if "chopxmin" in options:
        if xval<options["chopxmin"]:
            return True
    return False

def makePlottable_single(data,get1,**options):
    #data is a list of dict (str->float)
    #get1 and get2 are str, specifying keys in the dicts of data
    useIntegral = False
    if "useIntegral" in options:
        if options["useIntegral"]==True:
            useIntegral = True
    if len(data)==0:
        raise Exception("This is an empty dataset.")
    ran = dict()
    if useIntegral:
        w = data[0].getIntegral()
    else:
        w = data[0].getMaxes()
    xVal = w[get1]
    ran["xmin"] = xVal
    ran["xmax"] = xVal
    ou = []
    for x in data:
        if useIntegral:
            w = x.getIntegral()
        else:
            w = x.getMaxes()
        xVal = w[get1]
        if xVal<ran["xmin"]:
            ran["xmin"] = xVal
        if xVal>ran["xmax"]:
            ran["xmax"] = xVal
        if plotChop_single(xVal,**options)==False:
            ou.append(xVal)
    return ou,ran

def joinPlottable(ou1,ran1,ou2,ran2):
    for x in ou2:
        ou1.append(x)
    ran = dict()
    ran["xmin"] = min(ran1["xmin"],ran2["xmin"])
    ran["xmax"] = max(ran1["xmax"],ran2["xmax"])
    ran["ymin"] = min(ran1["ymin"],ran2["ymin"])
    ran["ymax"] = max(ran1["ymax"],ran2["ymax"])
    return ou1,ran

def joinPlottable_single(ou1,ran1,ou2,ran2):
    for x in ou2:
        ou1.append(x)
    ran = dict()
    ran["xmin"] = min(ran1["xmin"],ran2["xmin"])
    ran["xmax"] = max(ran1["xmax"],ran2["xmax"])
    return ou1,ran

def plotDir(dirpath,savepath,get1,get2,**options):
    fileList = run_softwareTrigger.getInputFiles(dirpath)
    pl_hold = []
    pl_ran = []
    for f in fileList:
        [osc_meta,ev_list] = read_ord_json_clump.read(dirpath+f)
        del(osc_meta)
        try:
            mp_ou,mp_ran = makePlottable(ev_list,get1,get2,**options)
        except:
            continue
        del(ev_list)
        if len(pl_ran)==0:
            pl_hold = mp_ou
            pl_ran = mp_ran
        else:
            pl_hold,pl_ran = joinPlottable(pl_hold,pl_ran,mp_ou,mp_ran)
        del(mp_ou)
        del(mp_ran)
    for f in pl_ran:
        options[f] = pl_ran[f]
    histplotlib.twoAxis(pl_hold,savepath,**options)

def plotDir_single(dirpath,savepath,get1,**options):
    fileList = run_softwareTrigger.getInputFiles(dirpath)
    pl_hold = []
    pl_ran = []
    for f in fileList:
        [osc_meta,ev_list] = read_ord_json_clump.read(dirpath+f)
        del(osc_meta)
        try:
            mp_ou,mp_ran = makePlottable_single(ev_list,get1,**options)
        except:
            continue
        del(ev_list)
        if len(pl_ran)==0:
            pl_hold = mp_ou
            pl_ran = mp_ran
        else:
            pl_hold,pl_ran = joinPlottable_single(pl_hold,pl_ran,mp_ou,mp_ran)
        del(mp_ou)
        del(mp_ran)
    for f in pl_ran:
        options[f] = pl_ran[f]
    histplotlib.histogram(pl_hold,savepath,**options)

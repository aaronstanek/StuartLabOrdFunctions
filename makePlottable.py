def makePlottable(data,get1,get2):
    #data is a list of dict (str->float)
    #get1 and get2 are str, specifying keys in the dicts of data
    if len(data)==0:
        raise Exception("This is an empty dataset.")
    ran = dict()
    ran["xmin"] = data[0][get1]
    ran["xmax"] = data[0][get1]
    ran["ymin"] = data[0][get2]
    ran["ymax"] = data[0][get2]
    ou = []
    for x in data:
        xVal = x[get1]
        if xVal<ran["xmin"]:
            ran["xmin"] = xVal
        if xVal>ran["xmax"]:
            ran["xmax"] = xVal
        yVal = x[get2]
        if yVal<ran["ymin"]:
            ran["ymin"] = yVal
        if yVal>ran["ymax"]:
            ran["ymax"] = yVal
        ou.append([xVal,yVal])
    return ou,ran

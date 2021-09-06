
def getKeywordList(objList, var):
    keywordList = list()

    for obj in objList:
        keywordList.append(getattr(obj, var))

    return keywordList
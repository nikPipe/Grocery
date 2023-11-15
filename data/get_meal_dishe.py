
#GET ALL THE RECPIE DATA
from dishe.india import lunch
from meal import india
import os, json





def getFileNameFromImportedModule(module):
    return os.path.dirname(module.__file__)

def readjsonFile(file):
    with open(file) as f:
        data = json.load(f)
    return data


def getIndiameal():
    file = getFileNameFromImportedModule(india)
    dishesList = []
    for each in os.listdir(file):
        if each.endswith('.json'):
            data = readjsonFile(file+'/'+each)
            dishesList.append(data)

    return dishesList


def getIndiaLunchdish():
    file = getFileNameFromImportedModule(lunch)
    luchDataList = []
    for each in os.listdir(file):
        if each.endswith('.json'):
            data = readjsonFile(file+'/'+each)
            luchDataList.append(data)

    return luchDataList




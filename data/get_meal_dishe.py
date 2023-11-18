
#GET ALL THE RECPIE DATA
from dishe.india import lunch
from meal import india
import meal
from data import mealClass
import os, json

from meal import india



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


def getAllMeal():
    file = getFileNameFromImportedModule(india)
    mealList = []
    for each in os.listdir(file):
        if each.endswith('.json'):
            data = readjsonFile(file+'/'+each)
            mealList.append(data)
    return mealList


def getAlldietTypes():
    file = getFileNameFromImportedModule(meal)
    dietTypeList = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = readjsonFile(root+'/'+each)
                mealClass_ = mealClass.mealClass(data)
                for eachDieType in mealClass_.dietTypes:
                    if eachDieType not in dietTypeList:
                        dietTypeList.append(eachDieType)

    return dietTypeList


def getmealtime():
    file = getFileNameFromImportedModule(meal)
    mealtimeList = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = readjsonFile(root+'/'+each)
                mealClass_ = mealClass.mealClass(data)
                for eachmealtime in mealClass_.mealtime:
                    if eachmealtime not in mealtimeList:
                        mealtimeList.append(eachmealtime)

    return mealtimeList


def getListJsonFromCatagory(catagory):
    file = getFileNameFromImportedModule(meal)
    mealList = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = readjsonFile(root+'/'+each)
                mealClass_ = mealClass.mealClass(data)
                if catagory in mealClass_.dietTypes or catagory in mealClass_.mealtime:
                    mealList.append(data)
    return mealList


def getDic():
    file = getFileNameFromImportedModule(meal)
    mealDic = {}
    list_val = []
    get_dieType = getAlldietTypes()
    get_meal = getmealtime()
    list_val.extend(get_dieType)
    list_val.extend(get_meal)
    for each in list_val:
        mealDic[each] = getListJsonFromCatagory(each)

    return mealDic







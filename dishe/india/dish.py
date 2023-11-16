from dishe.india import lunch
from meal import india
import json


import os
jsonFile = os.listdir(os.path.dirname(lunch.__file__))
indiaFile = os.listdir(os.path.dirname(india.__file__))

def getDishList():
    dishList = []
    for eachJson in indiaFile:
        if '.json' in eachJson:
            path = os.path.join(os.path.dirname(india.__file__), eachJson)
            json_data = open(path).read()
            data = json.loads(json_data)
            dishList.append(data)
    return dishList


def getIdFromDishList(name):
    '''

    :param name:
    :return:
    '''
    dishList = getDishList()
    for each in dishList:
        if name in each['id']:
            return True

    return False



for eachJson in jsonFile:
    disList = getDishList()

    if '.json' in eachJson:
        not_in_list = []
        if '9' in eachJson:
            path = os.path.join(os.path.dirname(lunch.__file__), eachJson)
            json_data = open(path).read()
            data = json.loads(json_data)
            for key, value in data.items():
                if key == 'menu':
                    for eachKey, eachValue in value.items():
                        for eacheachkey, eacheachvalue in eachValue.items():
                            if eacheachkey == 'default':
                                if getIdFromDishList(eacheachvalue['id']) == False:
                                    print(eacheachvalue)
                                pass
                            else:
                                for each in eacheachvalue:
                                    if getIdFromDishList(eacheachvalue[each]) == False:
                                        print(each, '>>>', eacheachvalue[each])
                                    pass










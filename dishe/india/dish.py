from dishe.india import lunch
from dishe.india import breakfast
from meal import india
import json


import os
jsonFile = os.listdir(os.path.dirname(lunch.__file__))
indiaFile = os.listdir(os.path.dirname(india.__file__))
indiaBreakfastFile = os.listdir(os.path.dirname(breakfast.__file__))


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


def printNot(importName, val=12):
    file = os.listdir(os.path.dirname(importName.__file__))
    list_recepie = []
    for eachJson in file:

        if '.json' in eachJson:
            not_in_list = []
            if str(val) in eachJson:
                path = os.path.join(os.path.dirname(importName.__file__), eachJson)


                json_data = open(path).read()
                data = json.loads(json_data)
                for key, value in data.items():
                    if key == 'menu':
                        for eachKey, eachValue in value.items():
                            for eacheachkey, eacheachvalue in eachValue.items():
                                if eacheachkey == 'default':
                                    if getIdFromDishList(str(eacheachvalue['id'])) == False:
                                        list_recepie.append(eacheachvalue['name'])
                                        #print(eacheachvalue)
                                    pass
                                else:
                                    for each in eacheachvalue:
                                        if getIdFromDishList(str(eacheachvalue[each])) == False:
                                            #print(each, '>>>', str(eacheachvalue[each]))
                                            list_recepie.append(each)
                                        pass

    #print(list_recepie)
    return list_recepie

def findRecipe(name):
    filePath = os.path.join(os.path.dirname(india.__file__))
    #walk through all the files in the directory
    find_val = False
    for root, dirs, files in os.walk(filePath):

        for eachFile in files:
            if '.json' in eachFile:
                path = os.path.join(root, eachFile)
                #path = os.path.join(os.path.dirname(root), eachFile)
                json_data = open(path).read()
                data = json.loads(json_data)
                if name in data['name']:
                    print(data['id'])
                    print(data['name'])
                    find_val = True

    return find_val









list_recepie = printNot(breakfast, 1)
for each in list_recepie:
    print(each)

#print('Lunch')
#for each in list_recepie:
#    if findRecipe(each) == False:
#        print(each)








'''



for eachJson in jsonFile:
    disList = getDishList()

    if '.json' in eachJson:
        not_in_list = []
        if '12' in eachJson:
            path = os.path.join(os.path.dirname(lunch.__file__), eachJson)

            json_data = open(path).read()
            data = json.loads(json_data)
            for key, value in data.items():
                if key == 'menu':
                    for eachKey, eachValue in value.items():
                        for eacheachkey, eacheachvalue in eachValue.items():
                            if eacheachkey == 'default':
                                if getIdFromDishList(str(eacheachvalue['id'])) == False:
                                    print(eacheachvalue)
                                pass
                            else:
                                for each in eacheachvalue:
                                    if getIdFromDishList(str(eacheachvalue[each])) == False:
                                        print(each, '>>>', str(eacheachvalue[each]))
                                    pass

'''








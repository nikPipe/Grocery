
from meal import india as meal_india
from dishe import india as dish_india
import json
import Levenshtein


import os
meal_indiaFile = os.listdir(os.path.dirname(meal_india.__file__))
dish_indiaFile = os.listdir(os.path.dirname(dish_india.__file__))


def getDishList():
    dishList = []
    for eachJson in meal_indiaFile:
        if '.json' in eachJson:
            path = os.path.join(os.path.dirname(meal_india.__file__), eachJson)
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
        id = each['id'].lower()
        name = name.lower()
        levenshtein_distance = Levenshtein.distance(name, id)
        max_length = max(len(name), len(id))
        similarity = 1 - (levenshtein_distance / max_length)
        threshold = 0.8
        if similarity > threshold:
            return True


        #if name.lower() in str(each['id'].lower()):
            #return True

    return False


def printNot(importName, val=1):

    file = os.listdir(os.path.dirname(importName.__file__))
    list_recepie = []
    list_id = []
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
                                        list_id.append(eacheachvalue['id'])
                                        #print(eacheachvalue)
                                else:
                                    for each in eacheachvalue:
                                        if getIdFromDishList(str(eacheachvalue[each])) == False:
                                            #print(each, '>>>', str(eacheachvalue[each]))
                                            list_recepie.append(each)
                                            list_id.append(str(eacheachvalue[each]))
                                        pass

                '''
                for key, value in data.items():
                    if key == 'menu':
                        for eachKey, eachValue in value.items():
                            for eacheachkey, eacheachvalue in eachValue.items():
                                if eacheachkey == 'default':
                                    if getIdFromDishList(str(eacheachvalue['id'])) == False:
                                        list_recepie.append(eacheachvalue['name'])
                                        list_id.append(eacheachvalue['id'])
                                        #print(eacheachvalue)
                                    pass
                                else:
                                    for each in eacheachvalue:
                                        if getIdFromDishList(str(eacheachvalue[each])) == False:
                                            #print(each, '>>>', str(eacheachvalue[each]))
                                            list_recepie.append(each)
                                            list_id.append(str(eacheachvalue[each]))
                                        pass
                '''
    #print(list_recepie)
    return list_recepie, list_id

def findRecipe(name):
    filePath = os.path.join(os.path.dirname(india.__file__))
    #walk through all the files in the directory
    find_val = False
    for root, dirs, files in os.walk(filePath):

        for eachFile in files:
            if '.json' in eachFile:
                path = os.path.join(root, eachFile)
                json_data = open(path).read()
                data = json.loads(json_data)
                if data['id'].lower() == name.lower():
                    pass

    return find_val


def getmealType():
    mealType = []
    for eachJson in dish_indiaFile:
        if '.json' in eachJson:
            path = os.path.join(os.path.dirname(dish_india.__file__), eachJson)
            json_data = open(path).read()
            data = json.loads(json_data)
            for each in data['mealtimes']:
                if each not in mealType:
                    mealType.append(each)
    return mealType


def getDishListFromMealType(mealType):
    dishList = []
    for eachJson in dish_indiaFile:
        if '.json' in eachJson:
            path = os.path.join(os.path.dirname(dish_india.__file__), eachJson)
            json_data = open(path).read()
            data = json.loads(json_data)
            for each in data['mealtimes']:
                if each == mealType:
                    dishList.append(data)
    return dishList

def getAllMealTypeDic():
    mealType = getmealType()
    mealTypeDic = {}
    for each in mealType:
        mealTypeDic[each] = getDishListFromMealType(each)
    return mealTypeDic


list_recepie, list_id = printNot(dish_india, 1)


for each in list_id:
    print(each)

mealType = getmealType()
mealTypeDic = getAllMealTypeDic()


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








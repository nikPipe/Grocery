
#GET ALL THE RECPIE DATA
from data.old.dishOld import lunch
import meal
from data import mealClass
import os, json

import dishe

from meal import india

from data import help
help_ = help.Help()


#MELA DATA


#RECEPIE DATA

def getIndiameal():

    file = help_.getFileNameFromImportedModule(india)
    dishesList = []
    for each in os.listdir(file):
        if each.endswith('.json'):
            data = help_.readjsonFile(file+'/'+each)
            dishesList.append(data)
    return dishesList

def getIndiaLunchdish():
    file = help_.getFileNameFromImportedModule(lunch)
    luchDataList = []
    for each in os.listdir(file):
        if each.endswith('.json'):
            data = help_.readjsonFile(file+'/'+each)
            luchDataList.append(data)

    return luchDataList


def getAllMeal():

    file = help_.getFileNameFromImportedModule(india)

    file = help_.getFileNameFromImportedModule(meal)
    mealList = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                data['images']['main'] = '/'.join([root, data['id'] + '.jpg']).replace('\\', '/')
                mealList.append(data)



    '''
    mealList = []
    for each in os.listdir(file):
        if each.endswith('.json'):
            data = help_.readjsonFile(file+'/'+each)
            data['images']['main'] = '/'.join([file, data['id'] + '.jpg']).replace('\\', '/')
            mealList.append(data)
    '''
    return mealList


def getAlldietTypes():
    file = help_.getFileNameFromImportedModule(meal)
    dietTypeList = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                mealClass_ = mealClass.mealClass(data)
                for eachDieType in mealClass_.dietTypes:
                    if eachDieType not in dietTypeList:
                        dietTypeList.append(eachDieType)

    return dietTypeList


def getmealtime():
    file = help_.getFileNameFromImportedModule(meal)
    mealtimeList = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                mealClass_ = mealClass.mealClass(data)
                for eachmealtime in mealClass_.mealtime:
                    if eachmealtime not in mealtimeList:
                        mealtimeList.append(eachmealtime)

    return mealtimeList


def getListJsonFromCatagory(catagory):
    file = help_.getFileNameFromImportedModule(meal)
    mealList = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                data['images']['main'] = '/'.join([root, data['id'] + '.jpg']).replace('\\', '/')
                mealClass_ = mealClass.mealClass(data)
                if catagory in mealClass_.dietTypes or catagory in mealClass_.mealtime:
                    mealList.append(data)
    return mealList


def getListJsonFromCatagoryRecepie(catagory, country):
    file = help_.getFileNameFromImportedModule(dishe)
    mealList = {}
    mealList[country] = {}
    catagory_list = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                if data['origin'].lower() == country.lower():
                    if catagory in data['mealtimes']:
                        catagory_list.append(data)

    mealList[country][catagory] = catagory_list
    return mealList




def getDic():
    file = help_.getFileNameFromImportedModule(meal)
    mealDic = {}
    list_val = []
    get_dieType = getAlldietTypes()
    get_meal = getmealtime()
    list_val.extend(get_dieType)
    list_val.extend(get_meal)
    for each in list_val:
        val = getListJsonFromCatagory(each)


        mealDic[each] = getListJsonFromCatagory(each)



    return mealDic

def getRecepieMealtimes():
    file = help_.getFileNameFromImportedModule(dishe)
    mealtimes = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                mealtime = data['mealtimes']
                for each in mealtime:
                    if each not in mealtimes:
                        mealtimes.append(each)

    return mealtimes


def getRecepieCountryList():
    file = help_.getFileNameFromImportedModule(dishe)
    countryList = []
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                country = data['origin']
                if country not in countryList:
                    countryList.append(country)

    return countryList



'''
from data import mealClass
getAllMeal_ = getAllMeal()
ingredientList = []
for each in getAllMeal_:
    mealClass_ = mealClass.mealClass(each)
    ingredient = mealClass_.getIngredientsItem()
    for each_ingredient in ingredient:
        if ' ' in each_ingredient:
            each_ingredient = each_ingredient.replace(' ', '_')
            if '-' in each_ingredient:
                each_ingredient = each_ingredient.replace('-', '_')

        if each_ingredient not in ingredientList:
            path = 'C:/Users/Admin/Desktop/Nikheel/GroceryMain/Grocery/groceryData/groeceryImage'
            if os.path.exists(path+'/'+each_ingredient+'.jpg'):
                pass
            else:
                ingredientList.append(each_ingredient)

        if 'asafoetida' == each_ingredient:
            print(each['name'])
            print('-------------------------')




ingredientList = sorted(ingredientList)
for each in ingredientList:
    print(each)
    pass
'''

'''

crushed_baati

fruits

ground_spices_(coriander_powder,_cumin_powder,_red_chili_powder,_turmeric_powder,_garam_masala)


mixed_nuts_(almonds,_cashews,_pistachios),_chopped

silver_leaf
spices_(garam_masala,_cumin_powder,_red_chili_powder)
spices_(garam_masala,_red_chili_powder,_turmeric_powder,_coriander_powder)
tomatoe
warm_water
water
whole_spices_(cardamom,_cloves,_bay_leaves)
whole_spices_(cardamom,_cloves,_cinnamon,_bay_leaves)
whole_spices_(cardamom,_cloves,_cinnamon_stick,_bay_leaves)
whole_spices_(cinnamon,_cloves,_cardamom)

'''


















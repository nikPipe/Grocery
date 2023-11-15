


from data import get_meal_dishe, mealClass


#GET THE DATA FROM JSON
getLunchData = get_meal_dishe.getIndiaLunchdish()
getMealData = get_meal_dishe.getIndiameal()

for each_LunchData in getLunchData:

    mealClass_ = mealClass.mealClass(each_LunchData)
    disDic = mealClass_.getDishes()
    print(mealClass_.name)
    print('-' * 20)
    for eachdish in disDic:
        name = disDic[eachdish]['name']
        id = disDic[eachdish]['id']


        print(name)
        print(id)
        for eachMealData in getMealData:
            if eachMealData['id'] == id:
                print(eachMealData)
                print('________________')









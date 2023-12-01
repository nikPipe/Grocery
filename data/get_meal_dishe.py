
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
            ingredientList.append(each_ingredient)

        if 'asafoetida' == each_ingredient:
            print(each['name'])
            print('-------------------------')




ingredientList = sorted(ingredientList)
for each in ingredientList:
    print(each)
    pass

'''

bay_leaf
bay_leaves
beef
bell_pepper
bell_pepper,_chopped
bell_peppers
biryani_masala
bisi_bele_bath_masala
black_cardamom_pods
black_chickpeas
black_mustard_seeds
black_pepper
black_peppercorns
black_salt
black_salt_(kala_namak)
black_tea_leaves
boondi
bottle_gourd
bread
butter
cabbage
capsicum
cardamom_pods
cardamom_powder
carom_seeds
carrot
carrots
carrots,_chopped
cashew
cashew_nut_paste
cashew_nuts
cashew_paste
cashews
cauliflower
chaat_masala
chana_dal
cheese
chicken
chickpea_flour
chickpeas
chili_powder
cilantro
cilantro_
cinnamon_stick
cloves
coconut
coconut_milk
coffee_powder
coriander
coriander_leaves
coriander_powder
coriander_seeds
cornflour
cornstarch
cream
crushed_baati
cucumber
cucumbers
cumin_powder
cumin_seeds
curd
curry_leaves
curry_leaves,_chopped
curry_powder
dal
dill
dosa_podi
dried_apricots
dried_figs
dried_red_chilies
drumstick
drumsticks
dry_red_chilies
dry_yeast
edible_food_color
edible_silver_leaf
egg
eggplant
eggplants
eggs
fennel_powder
fennel_seeds
fenugreek
fenugreek_leaves
fenugreek_seeds
filling:_mixed_dried_fruits_(raisins,_apricots,_etc.)
filling:_nuts_(almonds,_cashews,_etc.),_chopped
fish_fillets
flattened_rice
fresh_cilantro,_chopped
fresh_coriander_leaves,_chopped
fresh_cream
frozen_peas
fruits
garam_masala
garam_masala_powder
garlic
garlic_cloves
ghee
ghee_or_butter,_melted
ghee_or_oil
ginger
ginger,_chopped
ginger_garlic_paste
ginger_green_chili_paste
ginger_paste
ginger_powder
gram_flour
gram_flour)
grapes
grated_coconut
grated_cucumber
green_bean
green_beans
green_beans,_chopped
green_bell_pepper
green_cardamom
green_cardamom_pods
green_chili
green_chili_ginger_paste
green_chili_paste
green_chilies
green_onions
green_peas
green_tea_leaves
ground_almonds
ground_coriander
ground_cumin
ground_spices_(coriander_powder,_cumin_powder,_red_chili_powder,_turmeric_powder,_garam_masala)
heavy_cream
hing
honey
hot_water
ice_cubes
ice_water
idli_rice
jaggery
jaggery_or_brown_sugar
jowar_flour
kasuri_methi
ker_berries
ker_sangri
khoya
kidney_beans
kokum
kolhapuri_masala
lamb
lemon
lemon_and_mint_leaves
lemon_juice
lemons
lettuce
lime
limes
maize_flour
mango
mangodi
mangoes
masoor_dal
matki
milk
milk_powder
minced_meat
minced_meat_(lamb_or_beef)
mint_chutney
mint_leaves
mixed_nuts_(almonds,_cashews,_pistachios),_chopped
moong
moong_dal
moong_dal_(split_green_gram)
mushroom
mushrooms
mustard_greens
mustard_oil
mustard_seeds
mutton
nannari_syrup
nuts
nuts_and_raisins
oil
okra
olive_oil
onion
onions
orange
orange_juice
paneer
papads
papadums
paprika
parboiled_rice
parsley
pav
peanuts
peas
pepper
pineapple
pineapple_juice
pistachios
plain_yogurt
poha
pomegranate
pomegranate_seeds
poppy_seeds
pork
potato
potatoe
potatoes
powdered_sugar
prawns
puliyogare_masala
pumpkin
radish
ragi_flour
raisins
rasam_powder
raw_banana
raw_mango
raw_mangoes
red_bell_pepper
red_chili_flakes
red_chili_powder
red_chili_sauce
red_chilies
red_chilies,_dry
red_kidney_beans
reduced_milk_ice_cream
rice
ripe_mangoes
roasted_cumin_powder
rose_syrup
rose_water
sabudana
saffron
saffron_strands
salt
sambar_powder
sangri_beans
sarsaparilla_syrup
sattu
semolina
sesame_oil
sesame_seeds
sev
sevai
silver_leaf
slivered_almonds
snake_gourd
sour_yogurt
soy_sauce
sparkling_water
spices_(garam_masala,_cumin_powder,_red_chili_powder)
spices_(garam_masala,_red_chili_powder,_turmeric_powder,_coriander_powder)
spinach
spring_onions
strawberries
sugar
sugarcane_stalks
sun_dried_vegetables
tamarind_chutney
tamarind_paste
tamarind_pulp
tandoori_masala
tea_bag
tender_coconut
tomato
tomato_ketchup
tomato_puree
tomatoe
tomatoes
toor_dal
turmeric_powder
urad_dal
urad_dal_flour
vinegar
warm_milk
warm_water
water
watermelon
wheat_flour
white_chickpeas
white_fish
whole_spices_(cardamom,_cloves,_bay_leaves)
whole_spices_(cardamom,_cloves,_cinnamon,_bay_leaves)
whole_spices_(cardamom,_cloves,_cinnamon_stick,_bay_leaves)
whole_spices_(cinnamon,_cloves,_cardamom)
whole_wheat_flour
yam
yeast
yellow_bell_pepper
yogurt
'''
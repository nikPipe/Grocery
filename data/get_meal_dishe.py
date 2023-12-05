
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
    mealList = {}
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                data['images']['main'] = '/'.join([root, data['id'] + '.jpg']).replace('\\', '/')
                mealList[data['id']] = data

    return mealList


def getAlldietTypes(allmeal={}):
    dietTypeList = []
    for each in allmeal:
        mealClass_ = mealClass.mealClass(allmeal[each])
        dietType_ = mealClass_.dietTypes
        for each_dietType in dietType_:
            if each_dietType not in dietTypeList:
                dietTypeList.append(each_dietType)

    return dietTypeList



    '''
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
    '''
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
    mealDic = {}

    
    file = help_.getFileNameFromImportedModule(meal)
    
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



def dietType_Dic():
    '''

    :return:
    '''
    dietTypeDic = {}
    dietTypeDic['Vegetarian'] = ['Achari_Salad_Recipe', 'Akki_Roti_Recipe', 'Aloo_Gobi_Recipe', 'Aloo_Mangodi_Recipe', 'Aloo_Mutter_Recipe', 'Aloo_Palak_Recipe', 'Aloo_Paratha_Recipe', 'Aloo_Sabzi_Recipe', 'Appam_Recipe', 'Avial_Recipe', 'Badam_Milk_Recipe', 'Baingan_Bharta_Recipe', 'Bajra_Roti_Recipe', 'Barfi_Recipe', 'Basic_Cooked_Rice_Recipe', 'Basmati_Rice_Recipe', 'Batata_Vada_Recipe', 'Bejad_Roti_Recipe', 'Besan_Chilla_Recipe', 'Besan_Ladoo_Recipe', 'Bhakri_Recipe', 'Bhatura_Recipe', 'Bhindi_Masala_Recipe', 'Bisi_Bele_Bath_Recipe', 'Black_Tea_Recipe', 'Boondi_Raita_Recipe', 'Bread_Pakora_Recipe', 'Buttermilk_Recipe', 'Butter_Naan_Recipe', 'Cabbage_Curry_Recipe', 'Carrot_Halwa_Recipe', 'Chana_Dal_Vada_Recipe', 'Chana_Masala_Recipe', 'Chana_Salad_Recipe', 'Chapati_Recipe', 'Cheese_Naan_Recipe', 'Chole_Bhature_Recipe', 'Chole_Recipe', 'Coconut_Barfi_Recipe', 'Coconut_Chutney_Recipe', 'Coconut_Rice_Recipe', 'Cucumber_Raita_Recipe', 'Cucumber_Salad_Recipe', 'Curd_Recipe', 'Curd_Rice_Recipe', 'Curd_Rice_Thayir_Sadam_Recipe', 'Curry_Leaf_Rice_Recipe', 'Curry_Rice_Recipe', 'Dahi_Bhalla_Recipe', 'Dal_Baati_Churma_Recipe', 'Dal_Makhani_Recipe', 'Dal_Tadka_Recipe', 'Dhebra_Recipe', 'Dhokla_Recipe', 'Dosa_Recipe', 'Dum_Aloo_Recipe', 'Egg_Curry_Recipe', 'Fafda_Recipe', 'Filter_Coffee_Recipe', 'Fruit_Punch_Recipe', 'Fruit_Salad_Recipe', 'Garlic_Naan_Recipe', 'Gatte_Ka_Pulao_Recipe', 'Gatte_Ki_Sabzi_Recipe', 'Ghee_Rice_Recipe', 'Ghee_Roast_Dosa_Recipe', 'Ghevar_Recipe', 'Ginger_Tea_Recipe', 'Gobi_Manchurian_Recipe', 'Gobi_Paratha_Recipe', 'Govind_Gatte_Recipe', 'Green_Chilli_Pickle_Recipe', 'Green_Chutney_Recipe', 'Green_Salad_Recipe', 'Green_Tea_Recipe', 'Gulab_Jamun_Recipe', 'Halwa_Recipe', 'Hot_Lemon_Tea_Recipe', 'Idli_Recipe', 'Jalebi_Recipe', 'Jal_Jeera_Recipe', 'Jeera_Aloo_Recipe', 'Jeera_Rice_Recipe', 'Jigarthanda_Recipe', 'Jowar_Roti_Recipe', 'Kabuli_Recipe', 'Kachori_Recipe', 'Kachumber_Salad_Recipe', 'Kadai_Paneer_Recipe', 'Kadhi_Pakora_Recipe', 'Kadhi_Recipe', 'Kala_Chana_Curry_Recipe', 'Kanda_Poha_Recipe', 'Karnataka_Style_Bisi_Bele_Bath_Recipe', 'Kashmiri_Pulao_Recipe', 'Ker_Sangri_Paratha_Recipe', 'Ker_Sangri_Recipe', 'Kesar_Badam_Milk_Recipe', 'Kesar_Lassi_Recipe', 'Kesar_Milk_Recipe', 'Khaman_Recipe', 'Kheer_Recipe', 'Khichdi_Recipe', 'Kokum_Sherbet_Recipe', 'Kulcha_Recipe', 'Kulfi_Recipe', 'Laccha_Paratha_Recipe', 'Ladoo_Recipe', 'Lemon_Pickle_Recipe', 'Lemon_Rice_Recipe', 'Lime_Pickle_Recipe', 'Maddur_Vada_Recipe', 'Makki_Ki_Roti_Recipe', 'Malai_Kofta_Recipe', 'Mangodi_Ki_Sabzi_Recipe', 'Mango_Ice_Cream_Recipe', 'Mango_Lassi_Recipe', 'Mango_Pickle_Recipe', 'Mango_Shake_Recipe', 'Masala_Chaas_Recipe', 'Masala_Chai_Recipe', 'Masala_Dosa_Recipe', 'Masala_Papad_Recipe', 'Masala_Puri_Recipe', 'Masoor_Dal_Recipe', 'Matar_Paneer_Recipe', 'Matar_Pulao_Recipe', 'Methi_Paratha_Recipe', 'Methi_Thepla_Recipe', 'Mint_Chutney_Recipe', 'Mirchi_Bada_Recipe', 'Misal_Pav_Recipe', 'Missi_Roti_Recipe', 'Mixed_Dal_Recipe', 'Mixed_Pickle_Recipe', 'Moong_Dal_Chilla_Recipe', 'Moong_Dal_Halwa_Recipe', 'Mor_Kuzhambu_Recipe', 'Mushroom_Biryani_Recipe', 'Mushroom_Masala_Recipe', 'Mushroom_Matar_Recipe', 'Mushroom_Rice_Recipe', 'Mysore_Masala_Dosa_Recipe', 'Mysore_Pak_Recipe', 'Naan_Recipe', 'Navratan_Korma_Recipe', 'Neer_Dosa_Recipe', 'Nimbu_Pani_Recipe', 'Onion_Dosa_Recipe', 'Onion_Kulcha_Recipe', 'Onion_Rava_Dosa_Recipe', 'Onion_Rings_Recipe', 'Onion_Salad_Recipe', 'Palak_Paneer_Recipe', 'Panchmel_Dal_Recipe', 'Panchmel_Dal_Recipe', 'Paneer_Bhurji_Recipe', 'Paneer_Butter_Masala_Recipe', 'Paneer_Kulcha_Recipe', 'Paneer_Lababdar_Recipe', 'Paneer_Makhani_Recipe', 'Paneer_Naan_Recipe', 'Paneer_Paratha_Recipe', 'Paneer_Pulao_Recipe', 'Paneer_Rice_Recipe', 'Paneer_Tikka_Masala_Recipe', 'Papad_Ki_Sabzi_Recipe', 'Papad_Recipe', 'Paper_Dosa_Recipe', 'Paratha_Recipe', 'Pathiri_Recipe', 'Peas_Pulao_Recipe', 'Peda_Recipe', 'Peshawari_Naan_Recipe', 'Phulka_Recipe', 'Plain_Dosa_Recipe', 'Podi_Dosa_Recipe', 'Poha_Recipe', 'Pudina_Chutney_Recipe', 'Pudina_Paratha_Recipe', 'Puri_Bhaji_Recipe', 'Puri_Recipe', 'Pyaaz_Kachori_Recipe', 'Ragi_Dosa_Recipe', 'Ragi_Idli_Recipe', 'Ragi_Roti_Recipe', 'Raita_Recipe', 'Rajasthani_Kadhi_Recipe', 'Rajma_Masala_Recipe', 'Rasgulla_Recipe', 'Rasmalai_Recipe', 'Rava_Dosa_Recipe', 'Rava_Idli_Recipe', 'Rose_Milk_Recipe', 'Roti_Recipe', 'Rumali_Roti_Recipe', 'Sabudana_Khichdi_Recipe', 'Saffron_Rice_Recipe', 'Samosa_Recipe', 'Sattu_Paratha_Recipe', 'Set_Dosa_Recipe', 'Sevai_Recipe', 'Shahi_Paneer_Recipe', 'Sheermal_Recipe', 'Shrikhand_Recipe', 'Stuffed_Naan_Recipe', 'Stuffed_Paratha_Recipe', 'Sugarcane_Juice_Recipe', 'Sweet_Lassi_Recipe', 'Tamarind_Chutney_Recipe', 'Tamarind_Rice_Puliyodarai_Recipe', 'Tamarind_Rice_Recipe', 'Tandoori_Roti_Recipe', 'Thepla_Recipe', 'Tomato_Rice_Recipe', 'Upma_Recipe', 'Uttapam_Recipe', 'Vada_Recipe', 'Vegetable_Biryani_Recipe', 'Vegetable_Fried_Rice_Recipe', 'Vegetable_Jalfrezi_Recipe', 'Vegetable_Kadai_Recipe', 'Vegetable_Kofta_Curry_Recipe', 'Vegetable_Kolhapuri_Recipe', 'Vegetable_Korma_Recipe', 'Vegetable_Pulao_Recipe', 'Veg_Handi_Recipe', 'Yogurt_Chutney_Recipe']
    dietTypeDic['Vegan'] = ['Achari_Salad_Recipe', 'Aloo_Sabzi_Recipe', 'Basic_Cooked_Rice_Recipe', 'Basmati_Rice_Recipe', 'Besan_Chilla_Recipe', 'Bhakri_Recipe', 'Black_Tea_Recipe', 'Chana_Masala_Recipe', 'Chana_Salad_Recipe', 'Chole_Recipe', 'Coconut_Chutney_Recipe', 'Coconut_Water_Recipe', 'Coriander_Chutney_Recipe', 'Cucumber_Salad_Recipe', 'Curry_Leaf_Rice_Recipe', 'Dal_Tadka_Recipe', 'Dosa_Recipe', 'Elaneer_Recipe', 'Elaneer_Recipe', 'Ennai_Kathirikai_Recipe', 'Fruit_Punch_Recipe', 'Fruit_Salad_Recipe', 'Garlic_Chutney_Recipe', 'Ginger_Chutney_Recipe', 'Ginger_Tea_Recipe', 'Green_Chutney_Recipe', 'Green_Salad_Recipe', 'Green_Tea_Recipe', 'Hot_Lemon_Tea_Recipe', 'Idli_Recipe', 'Jal_Jeera_Recipe', 'Jeera_Aloo_Recipe', 'Kala_Chana_Curry_Recipe', 'Kanda_Poha_Recipe', 'Kokum_Sherbet_Recipe', 'Kootu_Recipe', 'Lemonade_Recipe', 'Lemon_Pickle_Recipe', 'Mango_Chutney_Recipe', 'Mango_Rice_Recipe', 'Masala_Dosa_Recipe', 'Masala_Papad_Recipe', 'Mint_Chutney_Recipe', 'Mint_Lemonade_Recipe', 'Nannari_Sarbath_Recipe', 'Nimbu_Pani_Recipe', 'Onion_Chutney_Recipe', 'Onion_Salad_Recipe', 'Orange_Juice_Recipe', 'Papad_Recipe', 'Peanut_Chutney_Recipe', 'Pudina_Chutney_Recipe', 'Puliyogare_Recipe', 'Puli_Kuzhambu_Recipe', 'Ragi_Dosa_Recipe', 'Rasam_Recipe', 'Rava_Dosa_Recipe', 'Red_Chilli_Chutney_Recipe', 'Rose_Sherbet_Recipe', 'Roti_Recipe', 'Saffron_Rice_Recipe', 'Sambar_Recipe', 'Sesame_Rice_Recipe', 'Sugarcane_Juice_Recipe', 'Tamarind_Chutney_Recipe', 'Tamarind_Rice_Recipe', 'Tomato_Chutney_Recipe', 'Tomato_Gothsu_Recipe', 'Tomato_Salad_Recipe', 'Vada_Recipe', 'Vatha_Kuzhambu_Recipe', 'Vegetable_Stew_Recipe', 'Watermelon_Juice_Recipe']
    dietTypeDic['Gluten Free'] = ['Achari_Salad_Recipe', 'Akki_Roti_Recipe', 'Aloo_Sabzi_Recipe', 'Appam_Recipe', 'Avial_Recipe', 'Bajra_Roti_Recipe', 'Basic_Cooked_Rice_Recipe', 'Basmati_Rice_Recipe', 'Besan_Chilla_Recipe', 'Bhakri_Recipe', 'Black_Tea_Recipe', 'Chana_Salad_Recipe', 'Coconut_Chutney_Recipe', 'Coconut_Water_Recipe', 'Coriander_Chutney_Recipe', 'Cucumber_Raita_Recipe', 'Cucumber_Salad_Recipe', 'Curry_Leaf_Rice_Recipe', 'Dhokla_Recipe', 'Dosa_Recipe', 'Elaneer_Recipe', 'Elaneer_Recipe', 'Ennai_Kathirikai_Recipe', 'Fish_Curry_Recipe', 'Fruit_Punch_Recipe', 'Fruit_Salad_Recipe', 'Garlic_Chutney_Recipe', 'Ginger_Chutney_Recipe', 'Ginger_Tea_Recipe', 'Green_Salad_Recipe', 'Green_Tea_Recipe', 'Idli_Recipe', 'Jowar_Roti_Recipe', 'Kokum_Sherbet_Recipe', 'Kootu_Recipe', 'Lemonade_Recipe', 'Lemon_Pickle_Recipe', 'Makki_Ki_Roti_Recipe', 'Mango_Chutney_Recipe', 'Mango_Rice_Recipe', 'Masala_Chaas_Recipe', 'Masala_Papad_Recipe', 'Mint_Chutney_Recipe', 'Mint_Lemonade_Recipe', 'Mor_Kuzhambu_Recipe', 'Nannari_Sarbath_Recipe', 'Neer_Dosa_Recipe', 'Onion_Chutney_Recipe', 'Onion_Salad_Recipe', 'Orange_Juice_Recipe', 'Papad_Recipe', 'Pathiri_Recipe', 'Peanut_Chutney_Recipe', 'Poha_Recipe', 'Pudina_Chutney_Recipe', 'Puliyogare_Recipe', 'Puli_Kuzhambu_Recipe', 'Ragi_Dosa_Recipe', 'Ragi_Idli_Recipe', 'Ragi_Roti_Recipe', 'Rasam_Recipe', 'Red_Chilli_Chutney_Recipe', 'Rose_Sherbet_Recipe', 'Sabudana_Khichdi_Recipe', 'Saffron_Rice_Recipe', 'Sambar_Recipe', 'Sesame_Rice_Recipe', 'Tomato_Chutney_Recipe', 'Tomato_Gothsu_Recipe', 'Tomato_Salad_Recipe', 'Vatha_Kuzhambu_Recipe', 'Vegetable_Stew_Recipe', 'Watermelon_Juice_Recipe', 'Yogurt_Chutney_Recipe']
    dietTypeDic['Non-Vegetarian'] = ['Andhra_Chicken_Curry_Recipe', 'Balti_Chicken_Recipe', 'Beef_Vindaloo_Recipe', 'Butter_Chicken_Recipe', 'Chicken_Chettinad_Recipe', 'Chicken_Curry_Recipe', 'Chicken_Dopiaza_Recipe', 'Chicken_Korma_Recipe', 'Chicken_Pulao_Recipe', 'Chicken_Saagwala_Recipe', 'Chicken_Tikka_Masala_Recipe', 'Chicken_Vindaloo_Recipe', 'Chicken_Xacuti_Recipe', 'Coconut_Chicken_Curry_Recipe', 'Fish_Curry_Recipe', 'Goan_Beef_Curry_Recipe', 'Goan_Pork_Vindaloo_Recipe', 'Hyderabadi_Dum_Biryani_Recipe', 'Kadai_Chicken_Recipe', 'Kashmiri_Chicken_Recipe', 'Keema_Curry_Recipe', 'Keema_Naan_Recipe', 'Keema_Pav_Recipe', 'Lamb_Korma_Recipe', 'Lamb_Madras_Recipe', 'Lamb_Rogan_Josh_Recipe', 'Mango_Chicken_Curry_Recipe', 'Nihari_Recipe', 'Patiala_Chicken_Recipe', 'Rogan_Josh_Recipe', 'Saag_Meat_Recipe']
    dietTypeDic['Paleo'] = ['Elaneer_Recipe']
    dietTypeDic['Keto'] = ['Elaneer_Recipe']
    dietTypeDic['Pescatarian'] = ['Fish_Molee_Recipe', 'Goan_Fish_Curry_Recipe', 'Prawn_Curry_Recipe']
    dietTypeDic['Gluten-free'] = ['Mango_Ice_Cream_Recipe']
    return dietTypeDic

def getMealType_Dic():
    '''

    :return:
    '''
    mealTypeDic = {}
    mealTypeDic['Any'] = ['Achari_Salad_Recipe', 'Badam_Milk_Recipe', 'Basmati_Rice_Recipe', 'Boondi_Raita_Recipe', 'Buttermilk_Recipe', 'Butter_Naan_Recipe', 'Chapati_Recipe', 'Coconut_Chutney_Recipe', 'Coconut_Water_Recipe', 'Cucumber_Raita_Recipe', 'Cucumber_Salad_Recipe', 'Curd_Recipe', 'Fruit_Salad_Recipe', 'Green_Chilli_Pickle_Recipe', 'Green_Chutney_Recipe', 'Green_Tea_Recipe', 'Hot_Lemon_Tea_Recipe', 'Jal_Jeera_Recipe', 'Jowar_Roti_Recipe', 'Kesar_Badam_Milk_Recipe', 'Kesar_Lassi_Recipe', 'Kulcha_Recipe', 'Laccha_Paratha_Recipe', 'Lemonade_Recipe', 'Lemon_Pickle_Recipe', 'Lime_Pickle_Recipe', 'Mango_Chutney_Recipe', 'Mango_Lassi_Recipe', 'Mango_Pickle_Recipe', 'Mango_Shake_Recipe', 'Masala_Chai_Recipe', 'Mint_Chutney_Recipe', 'Mint_Lemonade_Recipe', 'Missi_Roti_Recipe', 'Mixed_Pickle_Recipe', 'Nimbu_Pani_Recipe', 'Onion_Kulcha_Recipe', 'Onion_Salad_Recipe', 'Orange_Juice_Recipe', 'Papad_Recipe', 'Phulka_Recipe', 'Pudina_Chutney_Recipe', 'Rose_Milk_Recipe', 'Rose_Sherbet_Recipe', 'Stuffed_Naan_Recipe', 'Sugarcane_Juice_Recipe', 'Sweet_Lassi_Recipe', 'Tamarind_Chutney_Recipe', 'Thepla_Recipe', 'Watermelon_Juice_Recipe']
    mealTypeDic['Breakfast'] = ['Akki_Roti_Recipe', 'Aloo_Paratha_Recipe', 'Appam_Recipe', 'Bajra_Roti_Recipe', 'Bejad_Roti_Recipe', 'Besan_Chilla_Recipe', 'Bhakri_Recipe', 'Bhatura_Recipe', 'Chole_Bhature_Recipe', 'Coriander_Chutney_Recipe', 'Dhebra_Recipe', 'Dhokla_Recipe', 'Dosa_Recipe', 'Filter_Coffee_Recipe', 'Garlic_Chutney_Recipe', 'Ghee_Roast_Dosa_Recipe', 'Ginger_Chutney_Recipe', 'Gobi_Paratha_Recipe', 'Idli_Recipe', 'Kanda_Poha_Recipe', 'Keema_Pav_Recipe', 'Ker_Sangri_Paratha_Recipe', 'Khaman_Recipe', 'Masala_Dosa_Recipe', 'Methi_Paratha_Recipe', 'Methi_Thepla_Recipe', 'Misal_Pav_Recipe', 'Moong_Dal_Chilla_Recipe', 'Mysore_Masala_Dosa_Recipe', 'Neer_Dosa_Recipe', 'Nihari_Recipe', 'Onion_Chutney_Recipe', 'Onion_Dosa_Recipe', 'Onion_Rava_Dosa_Recipe', 'Paneer_Bhurji_Recipe', 'Paneer_Kulcha_Recipe', 'Paneer_Paratha_Recipe', 'Paper_Dosa_Recipe', 'Paratha_Recipe', 'Peanut_Chutney_Recipe', 'Plain_Dosa_Recipe', 'Podi_Dosa_Recipe', 'Poha_Recipe', 'Pudina_Paratha_Recipe', 'Puri_Bhaji_Recipe', 'Puri_Recipe', 'Ragi_Dosa_Recipe', 'Ragi_Idli_Recipe', 'Ragi_Roti_Recipe', 'Rava_Dosa_Recipe', 'Rava_Idli_Recipe', 'Red_Chilli_Chutney_Recipe', 'Roti_Recipe', 'Sabudana_Khichdi_Recipe', 'Sattu_Paratha_Recipe', 'Set_Dosa_Recipe', 'Sevai_Recipe', 'Sheermal_Recipe', 'Stuffed_Paratha_Recipe', 'Tomato_Chutney_Recipe', 'Tomato_Gothsu_Recipe', 'Upma_Recipe', 'Uttapam_Recipe', 'Vada_Recipe']
    mealTypeDic['Lunch'] = ['Akki_Roti_Recipe', 'Aloo_Gobi_Recipe', 'Aloo_Mangodi_Recipe', 'Aloo_Mutter_Recipe', 'Aloo_Palak_Recipe', 'Aloo_Paratha_Recipe', 'Aloo_Sabzi_Recipe', 'Andhra_Chicken_Curry_Recipe', 'Avial_Recipe', 'Baingan_Bharta_Recipe', 'Bajra_Roti_Recipe', 'Balti_Chicken_Recipe', 'Basic_Cooked_Rice_Recipe', 'Beef_Vindaloo_Recipe', 'Bejad_Roti_Recipe', 'Bhakri_Recipe', 'Bhatura_Recipe', 'Bhindi_Masala_Recipe', 'Bisi_Bele_Bath_Recipe', 'Butter_Chicken_Recipe', 'Cabbage_Curry_Recipe', 'Chana_Masala_Recipe', 'Chana_Salad_Recipe', 'Cheese_Naan_Recipe', 'Chicken_Chettinad_Recipe', 'Chicken_Curry_Recipe', 'Chicken_Dopiaza_Recipe', 'Chicken_Korma_Recipe', 'Chicken_Pulao_Recipe', 'Chicken_Saagwala_Recipe', 'Chicken_Tikka_Masala_Recipe', 'Chicken_Vindaloo_Recipe', 'Chicken_Xacuti_Recipe', 'Chole_Bhature_Recipe', 'Chole_Recipe', 'Coconut_Chicken_Curry_Recipe', 'Coconut_Rice_Recipe', 'Coriander_Chutney_Recipe', 'Curd_Rice_Recipe', 'Curd_Rice_Thayir_Sadam_Recipe', 'Curry_Leaf_Rice_Recipe', 'Curry_Rice_Recipe', 'Dal_Baati_Churma_Recipe', 'Dal_Makhani_Recipe', 'Dal_Tadka_Recipe', 'Dosa_Recipe', 'Dum_Aloo_Recipe', 'Egg_Curry_Recipe', 'Ennai_Kathirikai_Recipe', 'Fish_Curry_Recipe', 'Fish_Molee_Recipe', 'Garlic_Chutney_Recipe', 'Garlic_Naan_Recipe', 'Gatte_Ka_Pulao_Recipe', 'Gatte_Ki_Sabzi_Recipe', 'Ghee_Rice_Recipe', 'Ginger_Chutney_Recipe', 'Goan_Beef_Curry_Recipe', 'Goan_Fish_Curry_Recipe', 'Goan_Pork_Vindaloo_Recipe', 'Gobi_Manchurian_Recipe', 'Gobi_Paratha_Recipe', 'Govind_Gatte_Recipe', 'Green_Salad_Recipe', 'Hyderabadi_Dum_Biryani_Recipe', 'Jeera_Aloo_Recipe', 'Jeera_Rice_Recipe', 'Kabuli_Recipe', 'Kachumber_Salad_Recipe', 'Kadai_Chicken_Recipe', 'Kadai_Paneer_Recipe', 'Kadhi_Pakora_Recipe', 'Kadhi_Recipe', 'Kala_Chana_Curry_Recipe', 'Karnataka_Style_Bisi_Bele_Bath_Recipe', 'Kashmiri_Chicken_Recipe', 'Kashmiri_Pulao_Recipe', 'Keema_Curry_Recipe', 'Keema_Naan_Recipe', 'Ker_Sangri_Paratha_Recipe', 'Ker_Sangri_Recipe', 'Khichdi_Recipe', 'Kootu_Recipe', 'Lamb_Korma_Recipe', 'Lamb_Madras_Recipe', 'Lamb_Rogan_Josh_Recipe', 'Lemon_Rice_Recipe', 'Makki_Ki_Roti_Recipe', 'Malai_Kofta_Recipe', 'Mangodi_Ki_Sabzi_Recipe', 'Mango_Chicken_Curry_Recipe', 'Mango_Rice_Recipe', 'Masala_Dosa_Recipe', 'Masoor_Dal_Recipe', 'Matar_Paneer_Recipe', 'Matar_Pulao_Recipe', 'Methi_Paratha_Recipe', 'Methi_Thepla_Recipe', 'Misal_Pav_Recipe', 'Mixed_Dal_Recipe', 'Mor_Kuzhambu_Recipe', 'Mushroom_Biryani_Recipe', 'Mushroom_Masala_Recipe', 'Mushroom_Matar_Recipe', 'Mushroom_Rice_Recipe', 'Mysore_Masala_Dosa_Recipe', 'Naan_Recipe', 'Navratan_Korma_Recipe', 'Onion_Chutney_Recipe', 'Palak_Paneer_Recipe', 'Panchmel_Dal_Recipe', 'Panchmel_Dal_Recipe', 'Paneer_Bhurji_Recipe', 'Paneer_Butter_Masala_Recipe', 'Paneer_Kulcha_Recipe', 'Paneer_Lababdar_Recipe', 'Paneer_Makhani_Recipe', 'Paneer_Naan_Recipe', 'Paneer_Paratha_Recipe', 'Paneer_Pulao_Recipe', 'Paneer_Rice_Recipe', 'Paneer_Tikka_Masala_Recipe', 'Papad_Ki_Sabzi_Recipe', 'Paratha_Recipe', 'Pathiri_Recipe', 'Patiala_Chicken_Recipe', 'Peanut_Chutney_Recipe', 'Peas_Pulao_Recipe', 'Peshawari_Naan_Recipe', 'Prawn_Curry_Recipe', 'Pudina_Paratha_Recipe', 'Puliyogare_Recipe', 'Puli_Kuzhambu_Recipe', 'Puri_Recipe', 'Ragi_Dosa_Recipe', 'Ragi_Roti_Recipe', 'Raita_Recipe', 'Rajasthani_Kadhi_Recipe', 'Rajma_Masala_Recipe', 'Rasam_Recipe', 'Red_Chilli_Chutney_Recipe', 'Rogan_Josh_Recipe', 'Roti_Recipe', 'Rumali_Roti_Recipe', 'Saag_Meat_Recipe', 'Saffron_Rice_Recipe', 'Sambar_Recipe', 'Sattu_Paratha_Recipe', 'Sesame_Rice_Recipe', 'Shahi_Paneer_Recipe', 'Stuffed_Paratha_Recipe', 'Tamarind_Rice_Puliyodarai_Recipe', 'Tamarind_Rice_Recipe', 'Tandoori_Roti_Recipe', 'Tomato_Chutney_Recipe', 'Tomato_Gothsu_Recipe', 'Tomato_Rice_Recipe', 'Tomato_Salad_Recipe', 'Vatha_Kuzhambu_Recipe', 'Vegetable_Biryani_Recipe', 'Vegetable_Fried_Rice_Recipe', 'Vegetable_Jalfrezi_Recipe', 'Vegetable_Kadai_Recipe', 'Vegetable_Kofta_Curry_Recipe', 'Vegetable_Kolhapuri_Recipe', 'Vegetable_Korma_Recipe', 'Vegetable_Pulao_Recipe', 'Vegetable_Stew_Recipe', 'Veg_Handi_Recipe', 'Yogurt_Chutney_Recipe']
    mealTypeDic['Dinner'] = ['Aloo_Gobi_Recipe', 'Aloo_Mangodi_Recipe', 'Aloo_Mutter_Recipe', 'Aloo_Palak_Recipe', 'Aloo_Sabzi_Recipe', 'Andhra_Chicken_Curry_Recipe', 'Appam_Recipe', 'Avial_Recipe', 'Baingan_Bharta_Recipe', 'Bajra_Roti_Recipe', 'Balti_Chicken_Recipe', 'Basic_Cooked_Rice_Recipe', 'Beef_Vindaloo_Recipe', 'Bejad_Roti_Recipe', 'Bhakri_Recipe', 'Bhatura_Recipe', 'Bhindi_Masala_Recipe', 'Bisi_Bele_Bath_Recipe', 'Butter_Chicken_Recipe', 'Cabbage_Curry_Recipe', 'Chana_Masala_Recipe', 'Chana_Salad_Recipe', 'Cheese_Naan_Recipe', 'Chicken_Chettinad_Recipe', 'Chicken_Curry_Recipe', 'Chicken_Dopiaza_Recipe', 'Chicken_Korma_Recipe', 'Chicken_Pulao_Recipe', 'Chicken_Saagwala_Recipe', 'Chicken_Tikka_Masala_Recipe', 'Chicken_Vindaloo_Recipe', 'Chicken_Xacuti_Recipe', 'Chole_Bhature_Recipe', 'Chole_Recipe', 'Coconut_Chicken_Curry_Recipe', 'Coconut_Rice_Recipe', 'Coriander_Chutney_Recipe', 'Curd_Rice_Recipe', 'Curd_Rice_Thayir_Sadam_Recipe', 'Curry_Leaf_Rice_Recipe', 'Curry_Rice_Recipe', 'Dal_Baati_Churma_Recipe', 'Dal_Makhani_Recipe', 'Dal_Tadka_Recipe', 'Dosa_Recipe', 'Dum_Aloo_Recipe', 'Egg_Curry_Recipe', 'Ennai_Kathirikai_Recipe', 'Fish_Curry_Recipe', 'Fish_Molee_Recipe', 'Garlic_Chutney_Recipe', 'Garlic_Naan_Recipe', 'Gatte_Ka_Pulao_Recipe', 'Gatte_Ki_Sabzi_Recipe', 'Ghee_Rice_Recipe', 'Ghee_Roast_Dosa_Recipe', 'Ginger_Chutney_Recipe', 'Goan_Beef_Curry_Recipe', 'Goan_Fish_Curry_Recipe', 'Goan_Pork_Vindaloo_Recipe', 'Gobi_Manchurian_Recipe', 'Gobi_Paratha_Recipe', 'Govind_Gatte_Recipe', 'Green_Salad_Recipe', 'Hyderabadi_Dum_Biryani_Recipe', 'Jeera_Aloo_Recipe', 'Jeera_Rice_Recipe', 'Kabuli_Recipe', 'Kachumber_Salad_Recipe', 'Kadai_Chicken_Recipe', 'Kadai_Paneer_Recipe', 'Kadhi_Pakora_Recipe', 'Kadhi_Recipe', 'Kala_Chana_Curry_Recipe', 'Karnataka_Style_Bisi_Bele_Bath_Recipe', 'Kashmiri_Chicken_Recipe', 'Kashmiri_Pulao_Recipe', 'Keema_Curry_Recipe', 'Keema_Naan_Recipe', 'Keema_Pav_Recipe', 'Ker_Sangri_Paratha_Recipe', 'Ker_Sangri_Recipe', 'Khichdi_Recipe', 'Kootu_Recipe', 'Lamb_Korma_Recipe', 'Lamb_Madras_Recipe', 'Lamb_Rogan_Josh_Recipe', 'Lemon_Rice_Recipe', 'Makki_Ki_Roti_Recipe', 'Malai_Kofta_Recipe', 'Mangodi_Ki_Sabzi_Recipe', 'Mango_Chicken_Curry_Recipe', 'Mango_Rice_Recipe', 'Masala_Dosa_Recipe', 'Masoor_Dal_Recipe', 'Matar_Paneer_Recipe', 'Matar_Pulao_Recipe', 'Methi_Paratha_Recipe', 'Methi_Thepla_Recipe', 'Mixed_Dal_Recipe', 'Mor_Kuzhambu_Recipe', 'Mushroom_Biryani_Recipe', 'Mushroom_Masala_Recipe', 'Mushroom_Matar_Recipe', 'Mushroom_Rice_Recipe', 'Naan_Recipe', 'Navratan_Korma_Recipe', 'Neer_Dosa_Recipe', 'Nihari_Recipe', 'Onion_Chutney_Recipe', 'Onion_Rava_Dosa_Recipe', 'Palak_Paneer_Recipe', 'Panchmel_Dal_Recipe', 'Panchmel_Dal_Recipe', 'Paneer_Bhurji_Recipe', 'Paneer_Butter_Masala_Recipe', 'Paneer_Kulcha_Recipe', 'Paneer_Lababdar_Recipe', 'Paneer_Makhani_Recipe', 'Paneer_Naan_Recipe', 'Paneer_Paratha_Recipe', 'Paneer_Pulao_Recipe', 'Paneer_Rice_Recipe', 'Paneer_Tikka_Masala_Recipe', 'Papad_Ki_Sabzi_Recipe', 'Paper_Dosa_Recipe', 'Paratha_Recipe', 'Pathiri_Recipe', 'Patiala_Chicken_Recipe', 'Peanut_Chutney_Recipe', 'Peas_Pulao_Recipe', 'Peshawari_Naan_Recipe', 'Plain_Dosa_Recipe', 'Podi_Dosa_Recipe', 'Prawn_Curry_Recipe', 'Pudina_Paratha_Recipe', 'Puliyogare_Recipe', 'Puli_Kuzhambu_Recipe', 'Puri_Recipe', 'Ragi_Dosa_Recipe', 'Ragi_Roti_Recipe', 'Raita_Recipe', 'Rajasthani_Kadhi_Recipe', 'Rajma_Masala_Recipe', 'Rasam_Recipe', 'Rava_Dosa_Recipe', 'Rava_Idli_Recipe', 'Red_Chilli_Chutney_Recipe', 'Rogan_Josh_Recipe', 'Roti_Recipe', 'Rumali_Roti_Recipe', 'Saag_Meat_Recipe', 'Saffron_Rice_Recipe', 'Sambar_Recipe', 'Sattu_Paratha_Recipe', 'Sesame_Rice_Recipe', 'Set_Dosa_Recipe', 'Shahi_Paneer_Recipe', 'Sheermal_Recipe', 'Stuffed_Paratha_Recipe', 'Tamarind_Rice_Puliyodarai_Recipe', 'Tamarind_Rice_Recipe', 'Tandoori_Roti_Recipe', 'Tomato_Chutney_Recipe', 'Tomato_Rice_Recipe', 'Tomato_Salad_Recipe', 'Vatha_Kuzhambu_Recipe', 'Vegetable_Biryani_Recipe', 'Vegetable_Fried_Rice_Recipe', 'Vegetable_Jalfrezi_Recipe', 'Vegetable_Kadai_Recipe', 'Vegetable_Kofta_Curry_Recipe', 'Vegetable_Kolhapuri_Recipe', 'Vegetable_Korma_Recipe', 'Vegetable_Pulao_Recipe', 'Vegetable_Stew_Recipe', 'Veg_Handi_Recipe', 'Yogurt_Chutney_Recipe']
    mealTypeDic['Dessert'] = ['Barfi_Recipe', 'Besan_Ladoo_Recipe', 'Carrot_Halwa_Recipe', 'Coconut_Barfi_Recipe', 'Ghevar_Recipe', 'Gulab_Jamun_Recipe', 'Halwa_Recipe', 'Jalebi_Recipe', 'Kheer_Recipe', 'Kulfi_Recipe', 'Ladoo_Recipe', 'Mango_Ice_Cream_Recipe', 'Moong_Dal_Halwa_Recipe', 'Mysore_Pak_Recipe', 'Peda_Recipe', 'Rasgulla_Recipe', 'Rasmalai_Recipe', 'Shrikhand_Recipe']
    mealTypeDic['Snack'] = ['Batata_Vada_Recipe', 'Besan_Chilla_Recipe', 'Besan_Ladoo_Recipe', 'Bread_Pakora_Recipe', 'Chana_Dal_Vada_Recipe', 'Chana_Salad_Recipe', 'Coriander_Chutney_Recipe', 'Dahi_Bhalla_Recipe', 'Dhebra_Recipe', 'Dhokla_Recipe', 'Fafda_Recipe', 'Filter_Coffee_Recipe', 'Garlic_Chutney_Recipe', 'Ginger_Chutney_Recipe', 'Idli_Recipe', 'Jalebi_Recipe', 'Kachori_Recipe', 'Kanda_Poha_Recipe', 'Keema_Pav_Recipe', 'Khaman_Recipe', 'Maddur_Vada_Recipe', 'Masala_Papad_Recipe', 'Masala_Puri_Recipe', 'Methi_Thepla_Recipe', 'Mirchi_Bada_Recipe', 'Misal_Pav_Recipe', 'Moong_Dal_Chilla_Recipe', 'Onion_Chutney_Recipe', 'Onion_Dosa_Recipe', 'Onion_Rings_Recipe', 'Paneer_Kulcha_Recipe', 'Peanut_Chutney_Recipe', 'Puri_Bhaji_Recipe', 'Pyaaz_Kachori_Recipe', 'Red_Chilli_Chutney_Recipe', 'Sabudana_Khichdi_Recipe', 'Samosa_Recipe', 'Sevai_Recipe', 'Tomato_Chutney_Recipe', 'Upma_Recipe', 'Vada_Recipe', 'Yogurt_Chutney_Recipe']
    mealTypeDic['Anytime'] = ['Black_Tea_Recipe', 'Elaneer_Recipe', 'Elaneer_Recipe', 'Fruit_Punch_Recipe', 'Ginger_Tea_Recipe', 'Jigarthanda_Recipe', 'Kesar_Milk_Recipe', 'Kokum_Sherbet_Recipe', 'Masala_Chaas_Recipe', 'Nannari_Sarbath_Recipe']
    mealTypeDic['Appetizer'] = ['Chana_Dal_Vada_Recipe', 'Dahi_Bhalla_Recipe', 'Masala_Papad_Recipe']
    mealTypeDic['Side Dish'] = ['Onion_Rings_Recipe']

    return mealTypeDic

def allMealType():
    '''

    :return:
    '''

    getMealType_Dic_ = getMealType_Dic()
    dietType_Dic_ = dietType_Dic()



    getMealType_Dic_.update(dietType_Dic_)

    return getMealType_Dic_




def getMealType():
    mealType = []
    file = help_.getFileNameFromImportedModule(meal)
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                mealClass_ = mealClass.mealClass(data)
                for each in mealClass_.mealtime:
                    if each not in mealType:
                        mealType.append(each)

    return mealType


def getMealTypeList(name):
    '''

    :return:
    '''
    mealTypeList = []
    file = help_.getFileNameFromImportedModule(meal)
    for root, dirs, files in os.walk(file):
        for each in files:
            if each.endswith('.json'):
                data = help_.readjsonFile(root+'/'+each)
                mealClass_ = mealClass.mealClass(data)
                if name in mealClass_.mealtime:
                    mealTypeList.append(data['id'])

    return mealTypeList


'''

getAllMeal_ = getAllMeal()
getAlldietTypes_ = getAlldietTypes(getAllMeal_)

for each in getMealType():
    print(each)
    print(getMealTypeList(each))
    print('-------------------------')

'''

'''
getAlldietTypes_ = getAlldietTypes()
for each_DietType in getAlldietTypes_:
    dietType = []
    print(each_DietType)
    for each_Meal in getAllMeal_:

        mealClass_ = mealClass.mealClass(getAllMeal_[each_Meal])
        if each_DietType in mealClass_.dietTypes:
            dietType.append(getAllMeal_[each_Meal]['id'])
    print(dietType)
    print('-------------------------')

'''



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
            path = 'C:/Users/Admin/Desktop/Nikheel/GroceryMain/Grocery/groceryData/groceryImage'
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


















import traceback

path = 'C:/Users/Admin/Desktop/Nikheel/Grocery/meal/India/meal'
import sys, os, json

from ui_old.import_module import *
from ui_old.sampleWidget import sample_widget_template





list_dir = os.listdir(path)
jsonList = [jsonFile for jsonFile in list_dir if jsonFile.endswith('.json')]

def standardize_ingredient_names(json_data):
    # Define a dictionary to map variations to their standardized names
    list = ['cucumbers, diced', 'tomato', 'onion', 'green chili', 'carrot', 'red bell pepper', 'radish', 'fresh coriander leaves, chopped', 'mint leaves', 'lemon', 'achari masala', 'salt', 'chaat masala (optional)', 'olive oil', 'rice', 'coriander leaves', 'cumin seeds', 'water', 'oil', 'potatoes', 'cauliflower, cut into florets', 'ginger-garlic paste', 'turmeric powder', 'coriander powder', 'garam masala', 'chili powder', 'green peas', 'spinach (palak), chopped', 'garlic', 'ginger', 'whole wheat flour', 'chicken, cut into pieces', 'curry leaves', 'poppy seeds, ground', 'grated coconut', 'sugar', 'dry yeast', 'warm water', 'milk', 'almonds (badam), blanched and peeled', 'cardamom powder', 'saffron strands', 'chopped nuts (pistachios, almonds) for garnish', 'large eggplant', 'bajra flour', 'ghee or butter', 'bell peppers, chopped', 'mustard seeds', 'chickpea flour', 'baking soda', 'beef, cut into cubes', 'dried red chilies', 'vinegar', 'tamarind paste', 'jaggery or sugar', 'whole wheat flour (or millet/rice flour for gluten-free option)', 'all-purpose flour', 'yogurt', 'baking powder', 'okra (bhindi), trimmed and sliced', 'boondi (fried chickpea flour balls)', 'chaat masala', 'black salt', 'mint leaves, chopped (optional)', 'bread', 'carom seeds', 'cold water', 'mint leaves (optional)', 'black salt (optional)', 'ice cubes (optional)', 'chicken, boneless and skinless', 'garam masala powder', 'cream', 'butter', 'honey or sugar', 'fenugreek leaves (kasuri methi), crushed', 'green cardamom pods', 'cinnamon stick', 'cloves', 'cabbage, finely chopped', 'urad dal', 'chana dal (split bengal gram)', 'curry leaves, chopped', 'asafoetida', 'white chickpeas (chana)', 'amchur', 'yeast or baking powder', 'shredded cheese (mozzarella or cheddar)', 'butter or ghee, for brushing', 'garlic, minced (optional)', 'fresh coriander, chopped (optional)', 'coriander seeds', 'fennel seeds', 'black peppercorns', 'ground almonds', 'cardamom pods', 'whole spices (cardamom, cloves, cinnamon stick, bay leaves)', 'spinach, blanched and pureed', 'fresh cream', 'boneless chicken, cut into cubes', 'tandoori masala', 'heavy cream', 'poppy seeds', 'chickpeas', 'chickpeas (soaked overnight)', 'coconut milk', 'roasted chana dal (bengal gram)', 'dal', 'dry red chilies', 'cashew nuts', 'vegetable oil or ghee', 'young green coconut', 'cucumber, grated', 'black pepper, freshly ground', 'cucumbers, thinly sliced', 'red onion, thinly sliced', 'fresh dill, chopped', 'vinegar (white or apple cider)', 'sugar (optional)', 'curd culture or existing plain yogurt', 'plain yogurt (curd)', 'pomegranate seeds (optional)', 'grated cucumber (optional)', 'cashews or peanuts (optional)', 'tamarind paste (optional)', 'urad dal (split black gram), soaked for 4-6 hours', 'plain yogurt, whisked', 'tamarind chutney', 'mint chutney', 'kidney beans (rajma)', 'finely chopped garlic', 'chopped tomatoes', 'green chili-ginger paste', 'sesame seeds', 'fenugreek seeds', 'cashew nut paste', 'eggs', 'gram flour', 'fish fillets (like salmon, cod, or tilapia)', 'coconut milk or cream (optional)', 'firm white fish (like cod or halibut), cut into pieces', 'garlic cloves, finely chopped', 'black mustard seeds', 'apple, diced', 'orange, segmented', 'grapes, halved', 'strawberries, sliced', 'banana, sliced', 'honey or maple syrup (optional)', 'mint leaves, for garnish', 'ghee (clarified butter)', 'bay leaf', 'cashew nuts (optional)', 'raisins (optional)', 'dosa batter', 'ghee', 'ice water', 'water (for sugar syrup)', 'pistachios, chopped', 'silver leaf (optional)', 'edible food color (optional)', 'firm white fish (like cod or tilapia), cut into pieces', 'garlic cloves', 'ginger, chopped', 'pork, cut into cubes', 'ground coriander', 'cornstarch', 'soy sauce', 'spring onions, chopped', 'red chili sauce', 'tomato ketchup', 'pepper', 'cauliflower', 'green chilies, slit lengthwise', 'mustard seeds, powdered', 'fenugreek seeds, powdered', 'mustard oil', 'fresh cilantro (coriander leaves)', 'roasted cumin powder (optional)', 'lettuce, torn', 'spinach, chopped', 'arugula, chopped', 'cucumber, sliced', 'green bell pepper, sliced', 'fresh parsley or cilantro, chopped', 'green tea leaves or a green tea bag', 'honey or lemon (optional)', 'fresh water', 'fried onions', 'biryani masala', 'saffron strands, soaked in milk', 'bay leaves', 'cumin seeds (jeera)', 'tamarind pulp', 'black salt (kala namak)', 'ice cubes', 'boondi (optional, for garnish)', 'potatoes, boiled and cubed', 'jowar flour (sorghum flour)', 'cucumbers, finely chopped', 'green bell pepper, cubed', 'paneer (indian cottage cheese), cubed', 'onions, chopped', 'bell peppers (red & green), chopped', 'kadai masala (blend of coriander seeds, cumin seeds, fennel seeds, and dry red chilies)', 'fresh cilantro (coriander leaves), chopped', 'potato, finely chopped', 'coriander seeds, crushed', 'poha', 'onions, finely sliced', 'fennel powder', 'whole spices (cinnamon stick, bay leaf, cardamom pods, cloves)', 'saffron strands, soaked in warm milk', 'mixed dry fruits (almonds, cashews, raisins)', 'fresh fruits (apple cubes, pomegranate seeds)', 'minced meat (lamb or beef)', 'frozen peas', 'minced meat (lamb or chicken)', 'spices (garam masala, cumin powder, red chili powder)', 'minced meat', 'pav', 'almonds (badam)', 'saffron strands (kesar)', 'chopped nuts for garnishing', 'chopped nuts (almonds, pistachios) for garnish', 'ginger-green chili paste', 'fruit salt or baking soda', 'lamb, cut into cubes', 'ground cumin', 'slivered almonds', 'lamb, cut into pieces', 'tomato puree', 'whole spices (cardamom, cloves, cinnamon, bay leaves)', 'ground spices (coriander powder, cumin powder, red chili powder, turmeric powder, garam masala)', 'saffron strands (optional)', 'fresh lemons', 'mint leaves or lemon slices, for garnish', 'lemons', 'mustard seeds, coarsely ground', 'fenugreek seeds, coarsely ground', 'peanuts', 'limes, quartered', 'semolina', 'hot water', 'maize flour', 'paneer (indian cottage cheese), grated', 'green peas, boiled', 'cashew nuts, chopped', 'raisins', 'cornflour', 'ripe mangoes, pureed', 'ripe mangoes, peeled and chopped', 'apple cider vinegar', 'red chili flakes', 'milk or water', 'sugar or honey', 'cardamom powder (optional)', 'raw mangoes, diced', 'cold milk', 'sugar, or to taste', 'chopped mango or mint leaves, for garnish', 'black tea leaves', 'cardamom pods, crushed', 'fresh ginger, grated', 'black peppercorns, crushed', 'papads', 'sev (optional)', 'masoor dal (red lentils)', 'whole spices (bay leaf, cinnamon stick, cloves, green cardamoms)', 'fresh methi (fenugreek) leaves, chopped', 'fenugreek leaves', 'fresh coriander (cilantro) leaves', 'sliced lemon and mint leaves, for garnish', 'moong sprouts', 'matki sprouts', 'farsan or sev', 'fresh cilantro, finely chopped', 'onion, finely chopped (optional)', 'toor dal (split pigeon peas)', 'moong dal (split mung beans)', 'raw mango, diced', 'carrots, diced', 'lemons, diced', 'moong dal (split green gram), soaked for 4 hours', 'mushrooms, sliced', 'cream (optional)', 'cream or coconut milk (optional)', 'fresh cilantro (coriander), chopped', 'fresh mushrooms, sliced', 'vegetable stock or water', 'butter or olive oil', 'fresh thyme or parsley, chopped', 'red chili', 'fresh cilantro, chopped (optional)', 'paneer, cubed', 'carrots, chopped', 'peas', 'green beans, chopped', 'cauliflower florets', 'potatoes, cubed', 'pineapple, chopped', 'beef or lamb shank', 'whole spices (cardamom, cloves, bay leaves)', 'ginger, julienned', 'green chilies, sliced', 'black pepper', 'large onions', 'paprika', 'egg', 'red onions, thinly sliced', 'lemon juice or vinegar', 'green chilies, finely chopped (optional)', 'cumin powder (optional)', 'fresh oranges', 'sugar or honey (optional)', 'spinach (palak)', 'paneer (indian cottage cheese)', 'paneer (indian cottage cheese), crumbled', 'kasuri methi (dried fenugreek leaves)', 'water, warm', 'paneer, crumbled or grated', 'spices (garam masala, red chili powder, turmeric powder, coriander powder)', 'instant yeast', 'paneer, crumbled', 'oil or ghee for brushing', 'fresh coriander or mint leaves, chopped', 'paneer (indian cottage cheese), cut into cubes', 'urad dal flour (split black gram flour)', 'optional fillings', 'coconut oil', 'butter or ghee, melted', 'filling: mixed dried fruits (raisins, apricots, etc.) and nuts (almonds, cashews, etc.), chopped', 'coconut, desiccated', 'flattened rice', 'prawns, cleaned and deveined', 'fresh mint leaves (pudina)', 'fresh coriander leaves (cilantro)', 'garlic cloves (optional)', 'fresh mint leaves, finely chopped', 'ragi flour', 'idli rice', 'rajma (red kidney beans)', 'lamb or goat meat, cut into pieces', 'black cardamom pods', 'chilled milk', 'rose syrup', 'chilled water or soda', 'oil or ghee (optional)', 'mutton or lamb, cut into pieces', 'mustard greens, chopped', 'sabudana', 'saffron threads', 'sattu (roasted gram flour)', 'sevai (indian vermicelli)', 'warm milk', 'active dry yeast', 'potato filling', 'fresh sugarcane stalks, peeled', 'ginger, peeled', 'water or milk', 'rose water (optional)', 'jaggery (or sugar)', 'ginger powder', 'sesame oil', 'jaggery (optional)', 'basmati rice or short-grain rice', 'jaggery or sugar (optional)', 'yogurt (optional)', 'fresh fenugreek leaves (methi), chopped', 'ripe tomatoes, finely chopped', 'ripe tomatoes, sliced or chopped', 'fresh basil leaves, chopped', 'extra-virgin olive oil', 'balsamic vinegar or lemon juice', 'carrots', 'green beans', 'capsicum', 'idli or dosa batter', 'cooked rice, preferably chilled', 'carrots, finely chopped', 'bell pepper, finely chopped', 'green peas, frozen or fresh', 'green onions, chopped', 'bell peppers (red, green, yellow), chopped', 'carrots, julienned', 'mixed vegetables (carrots, bell peppers, cauliflower, peas)', 'peas, boiled', 'paneer, grated', 'mixed vegetables (carrots, peas, bell peppers, cauliflower, beans), chopped', 'kolhapuri masala', 'grated coconut (optional)', 'potato, cubed', 'yogurt or coconut milk', 'onion, sliced', 'mixed vegetables (carrots, peas, bell peppers, cauliflower)', 'cream or coconut milk', 'watermelon, seedless and cubed', 'lime juice (optional)']

    ingredient_mapping = {
        # Variations of 'onion'
        "onion, finely chopped": "onion",
        "onions, finely chopped": "onion",
        "onion, thinly sliced": "onion",
        "onions, sliced": "onion",
        "onions, thinly sliced": "onion",
        "chopped onions": "onion",

        # Variations of 'tomato'
        "tomatoes, diced": "tomato",
        "tomatoes, chopped": "tomato",
        "tomatoes, pureed": "tomato",
        "tomatoes, finely chopped": "tomato",

        # Variations of 'carrot'
        "carrot, grated": "carrot",
        "carrots, grated": "carrot",
        "carrot, diced": "carrot",

        # Variations of 'green chili'
        "green chilies, finely chopped": "green chili",
        "chopped green chilies": "green chili",
        "green chili, finely chopped": "green chili",
        "green chilies, slit": "green chili",
        "green chilies": "green chili",

        # Variations of 'coriander leaves'
        "coriander leaves, chopped": "coriander leaves",
        "chopped coriander leaves": "coriander leaves",
        "fresh coriander, chopped": "coriander leaves",
        "chopped coriander": "coriander leaves",

        # Variations of 'potatoes'
        "boiled potatoes": "potatoes",
        "potatoes, boiled and mashed": "potatoes",
        "potatoes, peeled and cubed": "potatoes",
        "potatoes (aloo), cubed": "potatoes",
        "baby potatoes": "potatoes",
        "potato": "potatoes",

        # Variations of 'cumin'
        "cumin powder": "cumin seeds",
        "roasted cumin powder": "cumin seeds",

        # Variations of 'rice'
        "parboiled rice": "rice",
        "raw rice": "rice",
        "basmati rice": "rice",
        "cooked rice": "rice",
        "rice flour": "rice",

        # Variations of 'chili powder'
        "red chili powder": "chili powder",
        "kashmiri red chili powder": "chili powder",

        # Variations of 'flour'
        "maida (refined flour)": "all-purpose flour",
        "whole wheat flour": "whole wheat flour",
        "bajra (pearl millet) flour": "bajra flour",
        "maize flour (makki ka atta)": "maize flour",
        "ragi flour": "ragi flour",

        # Variations of 'dal'
        "urad dal (split black gram)": "urad dal",
        "whole black lentils (urad dal)": "urad dal",
        "chana dal (split chickpeas)": "dal",
        "toor dal (split pigeon peas) or moong dal": "dal",

        # Variations of 'yogurt'
        "plain yogurt": "yogurt",
        "curd (yogurt)": "yogurt",
        "yogurt, whisked": "yogurt",
        "yogurt, sour": "yogurt",

        # Variations of 'oil'
        "oil or ghee": "oil",
        "vegetable oil": "oil",
        "ghee or oil": "oil",
        "butter or ghee": "oil",
        "oil or butter (optional)": "oil",
        "ghee or oil (optional)": "oil",

        # Other ingredients
        "salt": "salt",
        "water": "water",
        "sugar": "sugar",
        "sesame seeds": "sesame seeds",
        "baking soda": "baking soda",
        "baking powder": "baking powder",
        "gram flour (besan)": "gram flour",
        "mustard seeds": "mustard seeds",
        "curry leaves": "curry leaves",
        "turmeric powder": "turmeric powder",
        "coriander powder": "coriander powder",
        "garam masala": "garam masala",
        "ginger-garlic paste": "ginger-garlic paste",
        "lemon juice": "lemon juice",
        "green chili-ginger paste": "green chili-ginger paste",
        "amchur (dry mango powder)": "amchur",
        "asafoetida (hing)": "asafoetida",
        "poha (flattened rice)": "poha",
        "minced meat (mutton or lamb)": "minced meat",
        "pav (indian bread rolls)": "pav",
        "butter": "butter",
        "fresh fenugreek leaves (methi)": "fenugreek leaves",
        "carom seeds (ajwain)": "carom seeds",
        "moong sprouts": "moong sprouts",
        "matki sprouts": "matki sprouts",
        "farsan or sev": "farsan or sev",
        "lemon wedges": "lemon",
        "optional fillings (potato, paneer, cauliflower, etc.)": "optional fillings",
        "flattened rice": "flattened rice",
        "idli rice or parboiled rice": "idli rice",
        "fenugreek seeds (methi seeds)": "fenugreek seeds",
        "semolina (rava)": "semolina",
        "black pepper, crushed": "black pepper",
        "curry leaves, finely chopped": "curry leaves",
        "cashews": "cashews",
        "sabudana (tapioca pearls)": "sabudana",
        "peanuts": "peanuts",
        "green peas": "green peas",
        "carrots": "carrots",
        "peas": "peas",
        "green beans": "green beans",
        "idli or dosa batter": "idli or dosa batter",
        "capsicum, finely chopped": "capsicum",
        "black pepper": "black pepper",
        # Add any additional mappings as needed

    }



    # Loop through the JSON data and standardize ingredient names
    for ingredient in json_data["ingredients"]:
        original_name = ingredient["item"]
        standardized_name = ingredient_mapping.get(original_name, original_name)
        ingredient["item"] = standardized_name

    return json_data
def dumpException(e):
    print('Exception: %s' % e)
    traceback.print_tb(e.__traceback__)
def setLowerItem(json_data):
    '''

    :return:
    '''
    for ingredient in json_data["ingredients"]:
        ingredient["item"] = ingredient["item"].lower()

    return json_data

def getJsonData(jsonFile):
    try:
        jsonFile = path + '/' + jsonFile
        with open(jsonFile, 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        dumpException(e)

def setCommonName():
    for jsonFile in jsonList:
        jsonFile = path + '/' + jsonFile
        with open(jsonFile, 'r') as f:
            try:
                data = json.load(f)
                data = standardize_ingredient_names(data)
                data = setLowerItem(data)
                with open(jsonFile, 'w') as f:
                    json.dump(data, f, indent=4)
            except Exception as e:
                dumpException(e)
                print('Exception in file: %s' % jsonFile)

def getListItem():
    itemList = []
    for jsonFile in jsonList:
        #jsonFile = path + '/' + jsonFile
        data = getJsonData(jsonFile)
        for each in data['ingredients']:
            if each['item'] not in itemList:
                itemList.append(each['item'])
    return itemList

def getRecipeList():
    recipeList = []
    for jsonFile in jsonList:
        if 'json' in jsonFile:
            data = getJsonData(jsonFile)
            recipeList.append(data['name'])
    return recipeList

def getDietType():
    dietTypeList = []
    for jsonFile in jsonList:
        if 'json' in jsonFile:
            data = getJsonData(jsonFile)
            for each in data['dietTypes']:
                if each not in dietTypeList:
                    dietTypeList.append(each)
    return dietTypeList

def mealtime():
    mealtimeList = []
    for jsonFile in jsonList:
        if 'json' in jsonFile:
            data = getJsonData(jsonFile)
            for each in data['mealtime']:
                if each not in mealtimeList:
                    mealtimeList.append(each)
    return mealtimeList

def categorize_ingredients(ingredient_list):
    categories = {
        "Grains and Flours": ['rice flour', 'whole wheat flour', 'all-purpose flour', 'gram flour', 'ragi flour', 'semolina', 'parboiled rice', 'raw rice', 'cooked rice', 'poha', 'flattened rice', 'idli rice'],
        "Vegetables": ['onion', 'carrot', 'tomato', 'potatoes', 'capsicum', 'green chilies', 'red chilies', 'green beans', 'green peas', 'carrots'],
        "Fruits and Nuts": ['lemon', 'cashews', 'peanuts'],
        "Legumes and Pulses": ['chickpeas', 'urad dal', 'dal', 'moong sprouts', 'matki sprouts', 'urad dal (split black lentils)'],
        "Spices and Herbs": ['cumin seeds', 'mustard seeds', 'curry leaves', 'turmeric powder', 'coriander powder', 'coriander leaves', 'fenugreek seeds', 'fenugreek leaves', 'fennel seeds', 'asafoetida', 'amchur', 'carom seeds', 'black pepper', 'red chili powder', 'chili powder', 'garam masala', 'sesame seeds', 'tamarind paste'],
        "Dairy and Eggs": ['yogurt', 'butter'],
        "Baking and Cooking Essentials": ['salt', 'sugar', 'oil', 'baking soda', 'baking powder', 'dry yeast', 'warm water', 'grated coconut'],
        "Meat and Poultry": ['minced meat'],
        "Bread and Bakery": ['bread', 'pav'],
        "Condiments and Pastes": ['ginger-garlic paste', 'green chili-ginger paste', 'tamarind paste', 'garlic cloves'],
        "Prepared Mixes": ['dosa batter', 'idli or dosa batter'],
        "Optional Fillings": ['optional fillings']
    }

    categorized = {category: [] for category in categories.keys()}
    uncategorized = []

    for ingredient in ingredient_list:
        found = False
        for category, items in categories.items():
            if ingredient in items:
                categorized[category].append(ingredient)
                found = True
                break
        if not found:
            uncategorized.append(ingredient)

    return categorized, uncategorized

def getSpecificMealTime(mealtime):
    mealtimeList = []
    for jsonFile in jsonList:
        if 'json' in jsonFile:
            data = getJsonData(jsonFile)
            for each in data['mealtime']:
                data['mealtime'] = [x.lower() for x in data['mealtime']]

            if mealtime.lower() in data['mealtime']:
                mealtimeList.append(data['name'])
    return mealtimeList

class getMealData():
    def __init__(self, jsonFile):
        '''

        :param jsonFile:
        '''
        self.jsonFile = jsonFile
        self.initUI()

    def initUI(self):
        '''

        :return:
        '''
        print(self.jsonFile)



def getMealDataFromMealJsonData():
    mealPath = 'C:/Users/Admin/Desktop/Nikheel/Grocery/meal/India/meal/recepie/lunch'
    jsonList = os.listdir(mealPath)
    for eachJson in jsonList:
        if 'json' in eachJson:
            try:
                jsonFile = mealPath + '/' + eachJson
                with open(jsonFile, 'r') as f:
                    data = json.load(f)
                    getMealData(data)






            except Exception as e:
                dumpException(e)
        break


getMealDataFromMealJsonData()


class checkJsonFile:
    def __init__(self, jsonFile):
        self.jsonFile = getJsonData(jsonFile)

        self.initUI()

    def initUI(self):
        print('\n\n')
        print('id: %s' % self.getId())
        print('name: %s' % self.getName())
        print('origin: %s' % self.getorigin())
        print('history: %s' % self.getHistory())
        print('description: %s' % self.getDesc())
        print('servings: %s' % self.getServing())
        print('dietTypes: %s' % self.getdietTypes())
        print('preparationTime: %s' % self.getTime()[0])
        print('cookingTime: %s' % self.getTime()[1])
        print('totalTime: %s' % self.getTime()[2])
        print('mealtime: %s' % self.getMealTime())

        print('\n\n')
        print('This is equipment')
        for each in self.equipment():
            print(each)

        print('\n\n')
        print('This is ingredients')
        for each in self.getingredients():
            print(each)

        print('\n\n')
        print('This is instructions')
        for each in self.getInstructions():
            print(each)

        print('\n\n')
        print('This is nutrition')
        for each in self.getNutrition():
            print(each)

        print('\n\n')
        print('This is tips')
        for each in self.gettips():
            print(each)

        print('\n\n')
        print('This is variations')
        for each in self.getVariations():
            print(each)

        print('\n\n')
        print('This is images')
        for each in self.getimages():
            print(each)

        print('\n\n')
        print('This is storage')
        for each in self.getStorage():
            print(each)

        print('\n\n')
        print('This is reheatingInstructions')
        for each in self.getreheatingInstructions():
            print(each)

        print('\n\n')
        print('This is presentationTips')
        for each in self.getpresentationTips():
            print(each)

        print('\n\n')
        print('This is keywords')
        for each in self.getKeywords():
            print(each)

        print('\n\n')
        print('This is allergens')
        for each in self.getallergens():
            print(each)

        print('\n\n')


        #prepationTime, cookingTime, totalTime = self.checkTime()
        #mealtime = self.mealTime()

    def getId(self):
        return self.jsonFile['id']

    def getName(self):
        return self.jsonFile['name']

    def getorigin(self):
        return self.jsonFile['origin']

    def getHistory(self):
        return self.jsonFile['history']

    def getDesc(self):
        return self.jsonFile['description']

    def getIngredients(self):
        return self.jsonFile['ingredients']

    def getServing(self):
        if self.jsonFile['servings'] != '1':
            RuntimeError('Serving is not 1')
        return self.jsonFile['servings']

    def getdietTypes(self):
        return  self.jsonFile['dietTypes']

    def getTime(self):
        prepationTime = self.jsonFile['time']['preparationTime']['value'] + ' ' + self.jsonFile['time']['preparationTime']['unit']
        cookingTime = self.jsonFile['time']['cookingTime']['value'] + ' ' + self.jsonFile['time']['cookingTime']['unit']
        totalTime = self.jsonFile['time']['totalTime']['value'] + ' ' + self.jsonFile['time']['totalTime']['unit']
        return prepationTime, cookingTime, totalTime

    def getMealTime(self):
        return self.jsonFile['mealtime']

    def checkTime(self):
        prepationTime = self.jsonFile['time']['preparationTime']['value'] + ' ' + self.jsonFile['time']['preparationTime']['unit']
        cookingTime = self.jsonFile['time']['cookingTime']['value'] + ' ' + self.jsonFile['time']['cookingTime']['unit']
        totalTime = self.jsonFile['time']['totalTime']['value'] + ' ' + self.jsonFile['time']['totalTime']['unit']
        return prepationTime, cookingTime, totalTime

    def mealTime(self):
        mealtime = self.jsonFile['mealtime']
        return mealtime

    def equipment(self):
        equipmentList = []
        for each in self.jsonFile['equipment']:

            if 'name' not in each:
                raise RuntimeError('name not in equipment')
            if 'imageURL' not in each:
                raise RuntimeError('imageURL not in equipment')
            if 'description' not in each:
                raise RuntimeError('description not in equipment')
            one = each['name'] + ' ' + each['imageURL'] + ' ' + each['description']
            equipmentList.append(one)

        return equipmentList
    def getingredients(self):
        ingredientList = []
        for each_ing in self.jsonFile['ingredients']:
            if 'item' not in each_ing:
                raise RuntimeError('item not in ingredients')
            if 'quantity' not in each_ing:
                raise RuntimeError('quantity not in ingredients')
            if 'weight' not in each_ing:
                raise RuntimeError('weight not in ingredients')
            weight = each_ing['weight']['value'] + ' ' + each_ing['weight']['unit']
            one = each_ing['item'] + ' ' + each_ing['quantity'] + ' ' + weight
            ingredientList.append(one)
        return ingredientList

    def getInstructions(self):
        '''

        :return:
        '''
        instructionList = []
        for each in self.jsonFile['instructions']:

            if 'step' not in each:
                raise RuntimeError('step not in instructions')
            if 'title' not in each:
                raise RuntimeError('title not in instructions')
            if 'description' not in each:
                raise RuntimeError('description not in instructions')
            one = each['step'] + ' ' + each['title'] + ' ' + each['description']
            instructionList.append(one)
        return instructionList

    def getNutrition(self):
        '''

        :return:
        '''
        nutritionList = []
        for key, value in self.jsonFile['nutrition'].items():
            one = str(key) + ' ' + str(value)
            nutritionList.append(one)

        return nutritionList

    def gettips(self):
        '''

        :return:
        '''
        tipsList = []
        for each in self.jsonFile['tips']:
            tipsList.append(each)

        return tipsList

    def getVariations(self):
        '''

        :return:
        '''
        variationsList = []
        for each in self.jsonFile['variations']:
           variationsList.append(each)

        return variationsList

    def getimages(self):
        '''

        :return:
        '''
        imagesList = []
        for key, value in self.jsonFile['images'].items():
            one = str(key) + ' ' + str(value)
            imagesList.append(one)

        return imagesList

    def getStorage(self):
        '''

        :return:
        '''
        storageList = []
        for key, value in self.jsonFile['storage'].items():
            one = str(key) + ' ' + str(value)
            storageList.append(one)

        return storageList

    def getreheatingInstructions(self):
        '''

        :return:
        '''
        reheatingInstructionsList = []

        for each in self.jsonFile['reheatingInstructions']:
            reheatingInstructionsList.append(each)

        return reheatingInstructionsList

    def getpresentationTips(self):
        '''

        :return:
        '''
        presentationTipsList = []
        for each in self.jsonFile['presentationTips']:
            presentationTipsList.append(each)

        return presentationTipsList

    def getKeywords(self):
        '''

        :return:
        '''
        keywordsList = []
        for each in self.jsonFile['keywords']:
            keywordsList.append(each)

        return keywordsList

    def getallergens(self):
        '''

        :return:
        '''
        allergensList = []
        for each in self.jsonFile['allergens']:
            allergensList.append(each)

        return allergensList


'''

for each in jsonList:
    jsonPath = path + '/' + each
    jsonFile = getJsonData(each)
    equipment = jsonFile['equipment']
    for each in equipment:
        if 'imageURL' not in each:
            each['imageURL'] = ''

    with open(jsonPath, 'w') as f:
        json.dump(jsonFile, f, indent=4)



for each in jsonList:
    print(each)
    checkJsonFile(each)

'''







#one
#setCommonName()
#itemList = getListItem()
#categorized_ingredients, uncategorized_ingredients = categorize_ingredients(itemList)
#print(itemList)
'''
print(categorized_ingredients)
print(uncategorized_ingredients)

#GET ALL THE RECIPES
recipeList = getRecipeList()
print(recipeList)

#GET dietTypes
dietTypeList = getDietType()
print(dietTypeList)

mealtimeList = mealtime()
print(mealtimeList)

for each in ['Breakfast', 'Lunch', 'Dinner', 'Snack', 'Appetizer', 'Dessert']:
    print(each)
    print(getSpecificMealTime(each))

'''
















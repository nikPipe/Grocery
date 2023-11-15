import traceback

from meal import india
import os, json
path = os.path.dirname(os.path.abspath(india.__file__))

list_dir = os.listdir(path)
def dumpException(e):
    print('Exception: %s' % e)
    traceback.print_tb(e.__traceback__)


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

class mealClass():
    def __init__(self, json):
        self.json = json
        self.id = self.getId()
        self.name = self.getName()
        self.origin = self.getorigin()
        self.history = self.gethistory()
        self.description = self.getdescription()
        self.servings = self.getservings()
        self.dietTypes = self.getdietTypes()
        self.time = self.getTime()
        self.mealtime = self.getmealtime()
        self.equipment = self.getequipment()
        self.ingredients = self.getingredients()
        self.instructions = self.getinstructions()
        self.nutrition = self.getnutrition()
        self.tips = self.gettips()
        self.variations = self.getvariations()
        self.images = self.getimages()
        self.storage = self.getstorage()
        self.reheatingInstructions = self.getreheatingInstructions()
        self.presentationTips = self.getpresentationTips()
        self.keywords = self.keywords()
        self.allergens = self.getallergens()






    def getId(self):
        return self.json['id']

    def getName(self):
        return self.json['name']

    def getorigin(self):
        return self.json['origin']

    def gethistory(self):
        return self.json['history']

    def getdescription(self):
        return self.json['description']

    def getservings(self):
        return self.json['servings']

    def getdietTypes(self):
        return self.json['dietTypes']

    def getTime(self):
        string_val = ''
        preperationTime = self.json['time']['preparationTime']['value'] + ' ' + self.json['time']['preparationTime']['unit']
        cookingTime = self.json['time']['cookingTime']['value'] + ' ' + self.json['time']['cookingTime']['unit']
        totalTime = self.json['time']['totalTime']['value'] + ' ' + self.json['time']['totalTime']['unit']

        string_val = f"Preperation Time: {preperationTime}\nCooking Time: {cookingTime}\nTotal Time: {totalTime}"
        return string_val

    def getmealtime(self):
        return self.json['mealtime']

    def getequipment(self):
        string_val = 'THIS IS EQUIPMENT: \n'
        for each in self.json['equipment']:
            for key, value in each.items():
                string_val += f"{key}: {value}\n"
        return string_val

    def getingredients(self):
        string_val = 'THIS IS INGREDIENTS: \n'
        for each in self.json['ingredients']:
            for key, value in each.items():
                string_val += f"{key}: {value}\n"
            string_val += f"-" * 50 + '\n'
        return string_val

    def getinstructions(self):
        string_val = 'THIS IS INSTRUCTIONS: \n'
        for each in self.json['instructions']:
            for key, value in each.items():
                string_val += f"{key}: {value}\n"
            string_val += f"-" * 50 + '\n'
        return string_val

    def getnutrition(self):
        string_val = 'THIS IS NUTRITION: \n'
        for key, value in self.json['nutrition'].items():
            string_val += f"{key}: {value}\n"
        return string_val

    def gettips(self):
        string_val = 'THIS IS TIPS: \n'
        for each in self.json['tips']:
            string_val += f"{each}\n"
        return string_val

    def getvariations(self):
        string_val = 'THIS IS VARIATIONS: \n'
        for each in self.json['variations']:
            string_val += f"{each}\n"
        return string_val

    def getimages(self):
        string_val = 'THIS IS IMAGES: \n'
        for key, value in self.json['images'].items():
            string_val += f"{key}: {value}\n"
        return string_val

    def getstorage(self):
        string_val = 'THIS IS STORAGE: \n'
        for key, value in self.json['storage'].items():
            string_val += f"{key}: {value}\n"
        return string_val

    def getreheatingInstructions(self):
        string_val = 'THIS IS REHEATING INSTRUCTIONS: \n'
        for each in self.json['reheatingInstructions']:
            string_val += f"{each}\n"
        return string_val

    def getpresentationTips(self):
        string_val = 'THIS IS PRESENTATION TIPS: \n'
        for each in self.json['presentationTips']:
            string_val += f"{each}\n"
        return string_val

    def keywords(self):
        string_val = 'THIS IS KEYWORDS: \n'
        for each in self.json['keywords']:
            string_val += f"{each}\n"
        return string_val

    def getallergens(self):
        string_val = 'THIS IS ALLERGENS: \n'
        for each in self.json['allergens']:
            string_val += f"{each}\n"
        return string_val

    def getingredientsitem(self):
        list_item = []
        for each in self.json['ingredients']:
            for key, value in each.items():
                if key == 'item':
                    list_item.append(value)
        return list_item


    def prinCommand(self):
        print(f"this is id: {self.id}")
        print('-' * 50)
        print(f"THIS IS NAME: {self.name}")
        print(f"THIS IS ORIGIN: {self.origin}")
        print(f"THIS IS HISTORY: {self.history}")
        print(f"THIS IS DESCRIPTION: {self.description}")
        print(f"THIS IS SERVINGS: {self.servings}")
        for each in self.dietTypes:
            print(f"THIS IS DIET TYPES: {each}")

        print(f"{self.time}")
        print(f"THIS IS MEALTIME : {self.mealtime}")
        print('-' * 50)
        print(f"{self.equipment}")
        print('-' * 50)
        print(f"{self.ingredients}")
        print('-' * 50)
        print(f"{self.instructions}")
        print('-' * 50)
        print(f"{self.nutrition}")
        print('-' * 50)
        print(f"{self.tips}")
        print('-' * 50)
        print(f"{self.variations}")
        print('-' * 50)
        print(f"{self.images}")
        print('-' * 50)
        print(f"{self.storage}")
        print('-' * 50)
        print(f"{self.reheatingInstructions}")
        print('-' * 50)
        print(f"{self.presentationTips}")
        print('-' * 50)
        print(f"{self.keywords}")
        print('-' * 50)
        print(f"{self.allergens}")




def getItemList():
    list_item = []
    for each in list_dir:
        if '.json' in each:
            data = read_json_file(path + '/' + each)
            mealClass_ = mealClass(data)
            itemList = mealClass_.getingredientsitem()
            for eachItem in itemList:
                if eachItem not in list_item:
                    list_item.append(eachItem)
    return list_item








def printJsonData():
    list_item = []
    for each in list_dir:
        if '.json' in each:
            data = read_json_file(path + '/' + each)
            mealClass_ = mealClass(data)
            mealClass_.prinCommand()
            print('\n\n\n')


itemList = getItemList()
from collections import defaultdict

def consolidate_ingredients(ingredients_list):
    # Dictionary to store the consolidated ingredients
    consolidated = defaultdict(list)

    # Keywords to identify similar ingredients
    keywords = ['cucumber', 'tomato', 'onion', 'chili', 'carrot', 'bell pepper', 'radish',
                'coriander', 'mint', 'lemon', 'masala', 'salt', 'oil', 'potato', 'cauliflower',
                'ginger', 'garlic', 'turmeric', 'chili powder', 'peas', 'spinach', 'flour',
                'chicken', 'coconut', 'sugar', 'yeast', 'water', 'nuts', 'eggplant', 'ghee',
                'butter', 'mustard', 'beef', 'vinegar', 'tamarind', 'jaggery', 'yogurt', 'okra',
                'dal', 'asafoetida', 'cheese', 'fenugreek', 'cabbage', 'chana', 'cardamom',
                'saffron', 'baking soda', 'cream', 'cumin', 'fish', 'paneer', 'lentils',
                'mutton', 'lamb', 'tea', 'milk', 'poppy', 'papad', 'sev', 'lime', 'semolina',
                'prawn', 'ragi', 'idli', 'sambar', 'methi', 'sabudana', 'sattu', 'sevai',
                'sugarcane', 'rose', 'watermelon', 'pomegranate', 'capsicum', 'pepper',
                'biryani', 'pav', 'pistachio', 'masoor', 'moong', 'rajma', 'puliyogare',
                'dosa', 'poha', 'fennel', 'vathal', 'kolhapuri', 'kadai']

    # Loop through each ingredient
    for ingredient in ingredients_list:
        # Check if the ingredient contains any of the keywords
        for keyword in keywords:
            if keyword in ingredient:
                consolidated[keyword].append(ingredient)
                break
        else:
            # If no keyword is found, add it to a 'miscellaneous' group
            consolidated["miscellaneous"].append(ingredient)

    return consolidated

# Example usage
consolidated_ingredients = consolidate_ingredients(itemList)
for key, value in consolidated_ingredients.items():
    print(f"{key}: {value}")
    print('-' * 50)




import dishe
import os, json
import tempfile
from datetime import datetime, timedelta
class Help():

    def __init__(self):
        self.tempFileName = 'mealPlanner'

    def find_folders_in_directory(self, directory_path):
        # List to store the names of folders
        folders = []

        # Iterate over all the items in the directory
        for item in os.listdir(directory_path):
            # Create the full path to the item
            item_path = os.path.join(directory_path, item)

            # Check if the item is a directory
            if os.path.isdir(item_path):
                folders.append(item)

        return folders


    def getDishList(self, Country):
        '''

        :param Country:
        :return:
        '''
        country = Country.lower()
        dishFilePath = os.path.dirname(dishe.__file__)
        listDish = os.listdir(dishFilePath)
        folder = self.find_folders_in_directory(dishFilePath)
        dishList = []
        for each in folder:
            if country in each.lower():
                dishFilePath = os.path.join(dishFilePath, each)
                dishFolder = self.find_folders_in_directory(dishFilePath)
                for each in dishFolder:
                    if '__' not in each:
                        dishList.append(each)

                break

        return dishList

    def getListOfDish(self, Country, dish):
        '''

        :param Country:
        :param dish:
        :return:
        '''
        country = Country.lower()
        dish = dish.lower()

        dishFilePath = os.path.dirname(dishe.__file__)
        listDish = os.listdir(dishFilePath)
        folder = self.find_folders_in_directory(dishFilePath)
        dishList = []
        for each in folder:
            if country in each.lower():
                dishFilePath = os.path.join(dishFilePath, each)
                dishFolder = self.find_folders_in_directory(dishFilePath)
                for each in dishFolder:
                    if '__' not in each:
                        if dish in each.lower():
                            dishListDir = os.path.join(dishFilePath, each)
                            for eachDish in os.listdir(dishListDir):
                                if '.json' in eachDish:
                                    jsonRead = open(os.path.join(dishListDir, eachDish), 'r')
                                    jsonLoad = json.load(jsonRead)
                                    dishList.append(jsonLoad)

                break

        return dishList


    def totalCountry(self):
        '''

        :return:
        '''
        # Creating a Python list of all the countries in the world
        countries = [
            "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
            "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
            "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
            "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
            "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
            "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
            "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the",
            "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic",
            "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
            "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia",
            "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
            "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
            "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
            "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
            "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
            "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
            "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
            "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia",
            "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal",
            "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia",
            "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay",
            "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
            "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
            "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
            "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
            "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
            "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
            "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
            "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
            "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela",
            "Vietnam", "Yemen", "Zambia", "Zimbabwe"
        ]

        return countries

    def clearLayout(self, layout):
        # Remove all child widgets from the layout
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()  # Remove and delete the widget_old


    def getFileNameFromImportedModule(self, module):
        return os.path.dirname(module.__file__)

    def readjsonFile(self, file):
        with open(file) as f:
            data = json.load(f)
        return data


    def getTempFile(self, name):
        '''

        :return:
        '''
        tempFile = tempfile.gettempdir()
        file = os.path.join(tempFile, name + '.json')
        if os.path.exists(file):
            return file
        else:
            return False


    def createTempFile(self, name):
        '''

        :param name:
        :return:
        '''
        tempFile = tempfile.gettempdir()
        file = os.path.join(tempFile, name + '.json')
        if os.path.exists(file):
            return file
        else:
            with open(file, 'w') as f:
                json.dump({}, f)
            return file

    def get_allergies(self):
        '''

        :return:
        '''
        list = ['Dairy', 'Egg', 'Gluten', 'Grain', 'Peanut', 'Seafood', 'Sesame', 'Shellfish', 'Soy', 'Sulfite', 'Tree Nut',
         'Wheat']

        return list

    def getDiet(self):
        '''

        :return:
        '''
        list = ['Vegetarian', 'Vegan', 'Gluten-Free', 'Non-Vegetarian', 'Paleo', 'Keto', 'Pescatarian']

        return list

    def getingredientNotInclude(self):
        '''

        :return:
        '''
        list = ['Alcohol', 'Alcohol-Free', 'Celery', 'Crustacean', 'Dairy', 'Eggs', 'Fish', 'Gluten',
                          'Kidney friendly', 'Kosher', 'Low potassium', 'Lupine', 'Mustard', 'No oil added', 'No sugar',
                          'Paleo', 'Peanuts', 'Pescatarian', 'Pork', 'Red meat', 'Sesame', 'Shellfish', 'Soy',
                          'Sugar-Conscious', 'Tree Nuts', 'Vegan', 'Vegetarian', 'Wheat']

        return list


    def getcookingSkill(self):
        '''

        :return:
        '''
        list = ['Beginner', 'Intermediate', 'Advance']

        return list


    def get_set_TempFileName(self, data=''):
        '''

        :return:
        '''
        tempFile_ = self.getTempFile(self.tempFileName)

        if tempFile_:
            tempFileData = tempFile_
        else:
            tempFileData = self.createTempFile(self.tempFileName)

        with open(tempFileData, 'w') as f:
            json.dump(data, f, indent=4)

    def getTempJsonFile(self):
        tempFile_ = self.getTempFile(self.tempFileName)
        if tempFile_:
            with open(tempFile_, 'r') as f:
                data = json.load(f)
            return data


    def get_TempFileData(self):
        '''

        :return:
        '''
        tempFile_ = self.getTempFile(self.tempFileName)
        if tempFile_:
            with open(tempFile_, 'r') as f:
                data = json.load(f)
            return data
        else:
            return False

    def removeAllChildWidgets(self, widget):

        layout = widget.layout()

        if layout:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()


    def converDateToString(self, date):
        '''

        :param date:
        :return:
        '''
        date_object = datetime.strptime(date, "%d.%m.%Y")
        formatted_date = date_object.strftime("%d %B %Y")

        return formatted_date

    def getDay(self, date):
        '''

        :param date:
        :return:
        '''
        date_object = datetime.strptime(date, "%d.%m.%Y")
        day_of_week = date_object.strftime("%A")

        return day_of_week

    def getWeek(self, date):
        '''

        :param date:
        :return:
        '''
        date_object = datetime.strptime(date, "%d.%m.%Y")
        closest_previous_sunday = date_object - timedelta(days=date_object.weekday())
        end_of_week = closest_previous_sunday + timedelta(days=6)

        closest_previous_sunday = closest_previous_sunday.strftime("%d.%m.%Y")
        end_of_week = end_of_week.strftime("%d.%m.%Y")

        return closest_previous_sunday, end_of_week

    def getMonth(self, date):
        '''

        :param date:
        :return:
        '''
        date_object = datetime.strptime(date, "%d.%m.%Y")
        month = date_object.month

        return month

    def getYear(self, date):
        '''

        :param date:
        :return:
        '''
        date_object = datetime.strptime(date, "%d.%m.%Y")
        year = date_object.year
        return year






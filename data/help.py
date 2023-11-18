import dishe
import os, json

class Help():

    def __init__(self):
        pass

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
                widget.deleteLater()  # Remove and delete the widget
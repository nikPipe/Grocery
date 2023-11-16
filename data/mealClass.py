
class mealClass():
    def __init__(self, json):
        self.json = json

        self.initUI()


    def initUI(self):
        '''

        :return:
        '''
        self.name = self.getName()
        self.menu = self.getMenu()
        self.dishDic = self.getDishes()


    def getName(self):
        return self.json['name']

    def getMenu(self):
        key = []
        val = []
        for eachkey, value in self.json['menu'].items():
            key.append(eachkey)
            val.append(value)


        return key, val

    def getDishes(self):
        dishDict = {}
        key, val = self.getMenu()
        for eachkey in key:
            dishDict[eachkey] = {}
            dishDict[eachkey]['name'] = self.json['menu'][eachkey]['default']['name']
            dishDict[eachkey]['id'] = self.json['menu'][eachkey]['default']['id']

        return dishDict







class RecepieClass():
    def __init__(self, json):
        self.json = json
        self.name = self.getNames()
        self.id = self.getid()
        self.origin = self.getorigin()


    def getNames(self):
        '''

        :return:
        '''
        name = self.json['name']
        return name

    def getid(self):
        '''

        :return:
        '''
        id = self.json['id']
        return id

    def getorigin(self):
        '''

        :return:
        '''
        origin = self.json['origin']
        return origin
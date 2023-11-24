import json
from functools import partial

from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template

from ui_old__.widget_old import anotherWindow
from data import help


'''
Questions List


1 - what is your Name?
2 - what is your Email?
3 - where are you from?
3 - Do you Have any Allergies?
allerigeLis = ['Dairy', 'Egg', 'Gluten', 'Grain', 'Peanut', 'Seafood', 'Sesame', 'Shellfish', 'Soy', 'Sulfite', 'Tree Nut', 'Wheat']
4 - Do you have any Diet?
dietList = ['Gluten Free', 'Ketogenic', 'Vegetarian', 'Lacto-Vegetarian', 'Ovo-Vegetarian', 'Vegan', 'Pescetarian', 'Paleo', 'Primal', 'Whole30']
5 - any Ingredient you don't like?
ingredientList = ['Alcohol', 'Alcohol-Free', 'Celery', 'Crustacean', 'Dairy', 'Eggs', 'Fish', 'Gluten', 'Kidney friendly', 'Kosher', 'Low potassium', 'Lupine', 'Mustard', 'No oil added', 'No sugar', 'Paleo', 'Peanuts', 'Pescatarian', 'Pork', 'Red meat', 'Sesame', 'Shellfish', 'Soy', 'Sugar-Conscious', 'Tree Nuts', 'Vegan', 'Vegetarian', 'Wheat']
6 - how you describe your cooking skills?
7 - how many people you want to cook for?
8 - how much you spend on on weekly for grocery?
9 - help me out finding your favorite meal? based on this will recommend you meal

'''

class mainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.help = help.Help()
        self.userData = {}


        self.initUI()

    def initUI(self):
        # Set window size.
        self.resize(800, 800)

        # Set window title
        self.setWindowTitle('Introduction Window')

        widget = self.uiWidget()
        self.setCentralWidget(widget)

        # Show window
        self.show()

    def uiWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        self.stakewidget = QStackedWidget()
        verticalLayout.addWidget(self.stakewidget)

        self.stakewidget.addWidget(self.welcomeWidget())
        self.stakewidget.addWidget(self.getNameEmailIdWidget())
        self.stakewidget.addWidget(self.get_allergies())
        self.stakewidget.addWidget(self.get_diet())
        self.stakewidget.addWidget(self.ingredientNotInclude())
        self.stakewidget.addWidget(self.cookingSkill())
        self.stakewidget.addWidget(self.peopleToCook())
        self.stakewidget.addWidget(self.groceryBudget())
        self.stakewidget.addWidget(self.thankYoudef())

        return widget

    def welcomeWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = self.sample_widget.label(set_text='Welcome to Meal Planner', set_alighment=self.sample_widget.center_alignment)
        verticalLayout.addWidget(label)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        button = self.sample_widget.pushButton(set_text='Next', connect=partial(self.stakewidget.setCurrentIndex, 1))
        verticalLayout.addWidget(button)


        return widget

    def getNameEmailIdWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = self.sample_widget.label(set_text='let us get to know you', set_alighment=self.sample_widget.center_alignment)
        verticalLayout.addWidget(label)

        new_widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=new_widget)

        first_name_Label = self.sample_widget.label(set_text='First Name')
        gridLayout.addWidget(first_name_Label, 0, 0)

        first_name_LineEdit = self.sample_widget.line_edit(set_PlaceholderText='First Name')
        first_name_LineEdit.setAlignment(Qt.AlignCenter)
        gridLayout.addWidget(first_name_LineEdit, 0, 1)

        last_name_Label = self.sample_widget.label(set_text='Last Name')
        gridLayout.addWidget(last_name_Label, 1, 0)

        last_name_LineEdit = self.sample_widget.line_edit(set_PlaceholderText='Last Name')
        last_name_LineEdit.setAlignment(Qt.AlignCenter)
        gridLayout.addWidget(last_name_LineEdit, 1, 1)

        email_Label = self.sample_widget.label(set_text='Email')
        gridLayout.addWidget(email_Label, 2, 0)

        email_LineEdit = self.sample_widget.line_edit(set_PlaceholderText='Email')
        email_LineEdit.setAlignment(Qt.AlignCenter)
        gridLayout.addWidget(email_LineEdit, 2, 1)

        country_Label = self.sample_widget.label(set_text='Country')
        gridLayout.addWidget(country_Label, 3, 0)

        country_comboBox = self.sample_widget.comboBox(addItems=self.help.totalCountry(), setEditable=True)
        gridLayout.addWidget(country_comboBox, 3, 1)
        verticalLayout.addWidget(new_widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        button = self.sample_widget.pushButton(set_text='Next', connect=partial(self.nameEmailId_def, [first_name_LineEdit, last_name_LineEdit, email_LineEdit, country_comboBox]))
        verticalLayout.addWidget(button)

        return widget

    def nameEmailId_def(self, val):
        '''

        :return:
        '''

        nameDetail = {}
        nameDetail['first_name'] = val[0].text()
        nameDetail['last_name'] = val[1].text()
        nameDetail['email'] = val[2].text()
        nameDetail['country'] = val[3].currentText()


        for each in nameDetail:
            if nameDetail[each] == '' or '@' not in nameDetail['email']:
                display = self.sample_widget.displayMessage(text='Please fill the details')
                display.exec_()
                return False
        self.stakewidget.setCurrentIndex(2)
        self.userData['nameDetail'] = nameDetail


    def get_allergies(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


        label = self.sample_widget.label(set_text='Do you have any Allergies?', set_alighment=self.sample_widget.center_alignment)
        verticalLayout.addWidget(label)


        list_ =  self.help.get_allergies()
        new_widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=new_widget)
        buttonList = []
        for a in range(len(list_)):
            pushButton = self.sample_widget.pushButton(set_text=list_[a])
            pushButton.setCheckable(True)
            horizontalLayout.addWidget(pushButton)
            buttonList.append(pushButton)

        verticalLayout.addWidget(new_widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        pushButton = self.sample_widget.pushButton(set_text='Next', connect=partial(self.get_allergies_def, buttonList))
        verticalLayout.addWidget(pushButton)

        return widget

    def get_allergies_def(self, buttonList):
        '''

        :return:
        '''
        allergies = []
        for eachButton in buttonList:
            if eachButton.isChecked():
                allergies.append(eachButton.text())

        self.userData['allergies'] = allergies
        self.stakewidget.setCurrentIndex(3)



    def get_diet(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = self.sample_widget.label(set_text='Do you have any Diet?', set_alighment=self.sample_widget.center_alignment)
        verticalLayout.addWidget(label)

        dietList = self.help.getDiet()

        new_widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=new_widget)
        buttonList = []
        for a in range(len(dietList)):
            pushButton = self.sample_widget.pushButton(set_text=dietList[a])
            pushButton.setCheckable(True)
            horizontalLayout.addWidget(pushButton)
            buttonList.append(pushButton)
        verticalLayout.addWidget(new_widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        pushButton = self.sample_widget.pushButton(set_text='Next', connect=partial(self.get_diet_def, buttonList))
        verticalLayout.addWidget(pushButton)

        return widget

    def get_diet_def(self, buttonList):
        '''

        :param buttonList:
        :return:
        '''
        diet = []
        for eachButton in buttonList:
            if eachButton.isChecked():
                diet.append(eachButton.text())

        self.userData['diet'] = diet
        self.stakewidget.setCurrentIndex(4)

    def ingredientNotInclude(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = self.sample_widget.label(set_text='Any Ingredient you don\'t like?', set_alighment=self.sample_widget.center_alignment)
        verticalLayout.addWidget(label)


        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = self.sample_widget.widget_def()
        scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 380))
        scrollArea.setWidget(scrollAreaWidgetContents)
        verticalLayout.addWidget(scrollArea)
        horizontalLayout_2 = self.sample_widget.horizontal_layout(parent_self=scrollAreaWidgetContents)


        ingredientList = self.help.getingredientNotInclude()

        new_widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=new_widget)

        buttonList = []
        for a in range(len(ingredientList)):
            pushButton = self.sample_widget.pushButton(set_text=ingredientList[a])
            pushButton.setCheckable(True)
            horizontalLayout.addWidget(pushButton)
            buttonList.append(pushButton)
        horizontalLayout_2.addWidget(new_widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        pushButton = self.sample_widget.pushButton(set_text='Next', connect=partial(self.ingredientNotInclude_def, buttonList))
        verticalLayout.addWidget(pushButton)

        return widget

    def ingredientNotInclude_def(self, buttonList):
        '''

        :param buttonList:
        :return:
        '''
        ingredient = []
        for eachButton in buttonList:
            if eachButton.isChecked():
                ingredient.append(eachButton.text())

        self.userData['ingredientNotInclude'] = ingredient
        self.stakewidget.setCurrentIndex(5)


    def cookingSkill(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        widgetOne = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widgetOne)

        list = self.help.getcookingSkill()
        buttonList = []
        for a in range(len(list)):
            pushButton = self.sample_widget.pushButton(set_text=list[a])
            pushButton.setCheckable(True)
            horizontalLayout.addWidget(pushButton)
            buttonList.append(pushButton)

        verticalLayout.addWidget(widgetOne)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        pushButton = self.sample_widget.pushButton(set_text='Next', connect=partial(self.cookingSkill_def, buttonList))
        verticalLayout.addWidget(pushButton)

        return widget

    def cookingSkill_def(self, buttonList):
        '''

        :param buttonList:
        :return:
        '''
        skill = []
        for eachButton in buttonList:
            if eachButton.isChecked():
                skill.append(eachButton.text())

        self.userData['cookingSkill'] = skill
        self.stakewidget.setCurrentIndex(6)


    def peopleToCook(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        widgetOne = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widgetOne)

        label = self.sample_widget.label(set_text='How many people you want to cook for?', set_alighment=self.sample_widget.center_alignment)
        gridLayout.addWidget(label, 0, 0)

        lineEdit = self.sample_widget.line_edit(set_PlaceholderText='Number of people', set_text='1')
        lineEdit.setValidator(QIntValidator())
        gridLayout.addWidget(lineEdit, 0, 1)

        verticalLayout.addWidget(widgetOne)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        pushButton = self.sample_widget.pushButton(set_text='Next', connect=partial(self.peopleToCook_def, lineEdit))
        verticalLayout.addWidget(pushButton)

        return widget

    def peopleToCook_def(self, val):
        '''

        :param val:
        :return:
        '''
        val = val.text()
        int_val = int(val)
        if int_val < 1:
            display = self.sample_widget.displayMessage(text='Please enter the valid number')
            display.exec_()
            return False

        self.userData['people'] = val
        self.stakewidget.setCurrentIndex(7)

    def groceryBudget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        widgetOne = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widgetOne)

        label = self.sample_widget.label(set_text='How much you spend on on weekly for grocery?')
        gridLayout.addWidget(label, 0, 0)

        lineEdit = self.sample_widget.line_edit(set_PlaceholderText='value in $', set_text='0')
        lineEdit.setValidator(QIntValidator())
        gridLayout.addWidget(lineEdit, 0, 1)

        verticalLayout.addWidget(widgetOne)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        pushButton = self.sample_widget.pushButton(set_text='Next', connect=partial(self.groceryBudget_def, lineEdit))
        verticalLayout.addWidget(pushButton)

        return widget

    def groceryBudget_def(self, val):
        '''

        :param val:
        :return:
        '''
        val = val.text()
        int_val = int(val)
        self.userData['currentSpend'] = val
        self.stakewidget.setCurrentIndex(8)
        self.help.get_set_TempFileName(self.userData)
        self.close()

    def thankYoudef(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label = self.sample_widget.label(set_text='Thank You You can re open the script', set_alighment=self.sample_widget.center_alignment)
        verticalLayout.addWidget(label)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        pushButton = self.sample_widget.pushButton(set_text='Next', connect=partial(self.stakewidget.setCurrentIndex, 1))
        verticalLayout.addWidget(pushButton)

        return widget









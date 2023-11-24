

import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help

from ui.introduction_widget import welcomeWidget, getNameEmailWidget, getAllerygyWidget, getDietWidget, getingredientWidget, getcookingSkilWidget, getnoOfPeopleWIdget, getGroceryBudgetWidget, thankyouWidget



class mainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.welcomeWidget = welcomeWidget
        self.getNameEmailWidget = getNameEmailWidget
        self.getAllerygyWidget = getAllerygyWidget
        self.getDietWidget = getDietWidget
        self.getingredientWidget = getingredientWidget
        self.getcookingSkilWidget = getcookingSkilWidget
        self.getnoOfPeopleWIdget = getnoOfPeopleWIdget
        self.getGroceryBudgetWidget = getGroceryBudgetWidget
        self.thankyouWidget = thankyouWidget


        self.styleSheet = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.colorChild_class = sample_color_variable.COLOR_VARIABLE_CHILD(value=[0, 0, 0])




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
        '''

        :return:
        '''

        select_all_object = 'mainWidget'
        color = self.color_class.setColorVal(r=36, g=36, b=36)
        select_all_styleSheet = self.sample_widget.styleSheet_def(obj_name=select_all_object,
                                                                           background_color=color.get_value())
        #background-color: rgb(36, 36, 36);
        widget = self.sample_widget.widget_def(set_object_name=select_all_object,set_styleSheet=select_all_styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        self.stakeWidget = QStackedWidget()
        verticalLayout.addWidget(self.stakeWidget)

        #WELCOME WIDGET
        welcomeWidget = self.welcomeWidget.welcomeWidget(self)
        self.stakeWidget.addWidget(welcomeWidget)

        #GET NAME EMAIL WIDGET
        getNameEmailWidget = self.getNameEmailWidget.getNameEmailWidget(self)
        self.stakeWidget.addWidget(getNameEmailWidget)

        #GET ALLERGY WIDGET
        getAllerygyWidget = self.getAllerygyWidget.AllerygyWidget(self)
        self.stakeWidget.addWidget(getAllerygyWidget)

        #GET DIET WIDGET
        getDietWidget = self.getDietWidget.dietWidget(self)
        self.stakeWidget.addWidget(getDietWidget)

        #GET INGREDIENT WIDGET
        getingredientWidget = self.getingredientWidget.getingredientWidget(self)
        self.stakeWidget.addWidget(getingredientWidget)

        #GET COOKING SKILL WIDGET
        getcookingSkilWidget = self.getcookingSkilWidget.getcookingSkillWidget(self)
        self.stakeWidget.addWidget(getcookingSkilWidget)

        #GET NO OF PEOPLE WIDGET
        getnoOfPeopleWIdget = self.getnoOfPeopleWIdget.getnoOfPeopleWidget(self)
        self.stakeWidget.addWidget(getnoOfPeopleWIdget)

        #GET GROCERY BUDGET WIDGET
        getGroceryBudgetWidget = self.getGroceryBudgetWidget.getGroceryBudgetWidget(self)
        self.stakeWidget.addWidget(getGroceryBudgetWidget)

        #THANK YOU WIDGET
        thankyouWidget = self.thankyouWidget.thankyouWidget(self)
        self.stakeWidget.addWidget(thankyouWidget)

        return widget


    def set_stakeWidget_def(self, val):
        '''

        :param val:
        :return:
        '''
        self.stakeWidget.setCurrentIndex(val)






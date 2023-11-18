import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template

from data import get_meal_dishe
from data import help



class midWidget_MealWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.meal_dishe = get_meal_dishe
        self.help = help.Help()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

        self.update_()

    def initUI(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.filterWidget())
        verticalLayout.addWidget(self.mealWidget())



        return widget



    def filterWidget(self):
        '''

        :return:
        '''
        height = 50
        widget = self.sample_widget.widget_def(min_size=(0, height), max_size=(16777215, height))
        horizontalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = self.sample_widget.widget_def()
        scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 380))
        scrollArea.setWidget(scrollAreaWidgetContents)
        horizontalLayout.addWidget(scrollArea)

        horizontalLayout_2 = self.sample_widget.horizontal_layout(parent_self=scrollAreaWidgetContents)

        get_dieType = self.meal_dishe.getAlldietTypes()
        get_meal = self.meal_dishe.getmealtime()
        self.getMealDic = self.meal_dishe.getDic()

        catgory = []
        catgory.extend(get_dieType)
        catgory.extend(get_meal)
        self.radioButtons = []
        for each in catgory:
            radioButton = QRadioButton(scrollAreaWidgetContents)
            radioButton.setText(each)

            radioButton.toggled.connect(partial(self.radio_def, radioButton))
            self.radioButtons.append(radioButton)

            horizontalLayout_2.addWidget(radioButton)



        return widget

    def mealWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = self.sample_widget.widget_def()
        scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 380))
        scrollArea.setWidget(scrollAreaWidgetContents)
        verticalLayout.addWidget(scrollArea)

        self.mealGridLayout = self.sample_widget.grid_layout(parent_self=scrollAreaWidgetContents)

        a = 0
        while a < 10:
            button = self.sample_widget.pushButton(parent_self=scrollAreaWidgetContents)
            button.setText('test')
            self.mealGridLayout.addWidget(button, a, 0)


            a+=1



        return widget


    def update_(self):

        self.radioButtons[0].setChecked(True)


    def radio_def(self, val):
        '''

        :param val:
        :return:
        '''

        if val.isChecked():
            self.help.clearLayout(self.mealGridLayout)
            getDic = self.getMealDic[val.text()]
            a = 0
            while a < len(getDic):
                button = self.sample_widget.pushButton(parent_self=self.mealGridLayout.parentWidget())
                text_val = getDic[a]['name'] + ' total time : ' + str(getDic[a]['time']['totalTime']['value']) + ' min'
                button.setText(text_val)
                button.clicked.connect(partial(self.button_def, getDic[a]))

                self.mealGridLayout.addWidget(button, a, 0, 1, 1)
                a += 1


    def button_def(self, val):
        '''

        :param val:
        :return:
        '''
        print(json.dumps(val, indent=4))
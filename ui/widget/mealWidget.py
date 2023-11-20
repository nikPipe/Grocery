from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template


from ui.widget import leftWidget
from data import get_meal_dishe
from data import help


class MealWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.leftWidget_ = leftWidget.lefWidget()
        self.meal_dishe = get_meal_dishe
        self.help = help.Help()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)
        self.update_()


    def initUI(self):
        '''


        :return:
        '''

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.mealFilter_def())

        verticalLayout.addWidget(self.mealGridLayout_def())



        return widget


    def mealFilter_def(self):
        '''
        :return:
        '''
        widget = self.sample_widget.widget_def(min_size=[0, 50], max_size=[16777215, 50])
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = self.sample_widget.widget_def()
        scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 380))
        scrollArea.setWidget(scrollAreaWidgetContents)
        verticalLayout.addWidget(scrollArea)
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

    def radio_def(self, val):
        '''

        :param val:
        :return:
        '''

        if val.isChecked():
            self.help.clearLayout(self.mealGridLayout)
            getDic = self.getMealDic[val.text()]
            a = 0
            val = 500
            while a < len(getDic):
                button = self.mealWidget_(getDic[a])
                row = a // 5  # Calculate the row (every 5 items, start a new row)
                col = a % 5  # Calculate the column
                self.mealGridLayout.addWidget(button, row, col)
                a += 1


    def mealWidget_(self, data):
        '''

        :return:
        '''
        val= 200
        widget = self.sample_widget.widget_def(min_size=(val, val), max_size=(val, val))
        margin = 5
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(margin, margin, margin, margin))

        #CREATE MEAL PUSHBUTTON
        pushButton = self.sample_widget.pushButton()
        pushButton.setIcon(QIcon(data['images']['main']))
        pushButton.setIconSize(QSize(val, val))
        verticalLayout.addWidget(pushButton)


        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        label = self.sample_widget.label(set_text=data['name'], set_alighment=self.sample_widget.center_alignment)
        label.setFont(font)
        verticalLayout.addWidget(label)

        return widget




    def mealGridLayout_def(self):
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
        return widget



    def update_(self):

        self.radioButtons[0].setChecked(True)
















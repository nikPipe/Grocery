import json
from functools import partial

from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template


from data import get_meal_dishe
from data import help
from data import mealClass

class MealDetailWidget(QWidget):
    def __init__(self, data):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.meal_dishe = get_meal_dishe
        self.help = help.Help()
        self.data = data
        self.meal_dishe = mealClass.mealClass(self.data)


        print(self.meal_dishe.getName())

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)


    def initUI(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget)

        gridLayout.addWidget(self.groceryList_addMeal_favoriteWidget(), 0, 0, 1, 2)

        gridLayout.addWidget(self.nameWidget_def(), 1, 0, 1, 1)

        gridLayout.addWidget(self.origin_dietType_mealTime_widget(), 2, 0, 1, 1)

        gridLayout.addWidget(self.totalTime_calories_ingredients_widget_def(), 3, 0, 1, 1)

        gridLayout.addWidget(self.imageWidget(), 1, 1, 3, 1)

        gridLayout.addWidget(self.nutrition_widget(), 4, 0, 1, 2)

        gridLayout.addWidget(self.otherTabWidget(), 5, 0, 1, 2)


        '''

        #NAME WIDGET
        gridLayout.addWidget(self.nameWidget_def(), 0, 0, 1, 1)

        gridLayout.addWidget(self.imageWidget(), 0, 1, 3, 1)

        #ORIGIN DIETTYPE MEALTIME WIDGET
        gridLayout.addWidget(self.origin_dietType_mealTime_widget(), 1, 0, 1, 1)

        #TOTALTIME CALORIES INGREDIENTS WIDGET
        gridLayout.addWidget(self.totalTime_calories_ingredients_widget_def(), 2, 0, 1, 1)

        gridLayout.addWidget(self.nutrition_widget(), 3, 0, 1, 2)

        gridLayout.addWidget(self.otherTabWidget(), 4, 0, 1, 2)
        '''
        return widget

    def groceryList_addMeal_favoriteWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='Add To Grocery List')
        horizontalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Add Meal')
        horizontalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Add To Favorite')
        horizontalLayout.addWidget(button)

        return widget


    def nameWidget_def(self):
        '''
        :return:
        '''
        widget = self.sample_widget.widget_def(min_size=[0, 50], max_size=[16777215, 50])
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        label = self.sample_widget.label(set_text=self.meal_dishe.getName(), set_alighment=self.sample_widget.center_alignment)
        horizontalLayout.addWidget(label)

        return widget


    def origin_dietType_mealTime_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget)


        originLabel = self.sample_widget.label(set_text=self.meal_dishe.getorigin())
        gridLayout.addWidget(originLabel, 0, 0, 1, 1)


        #conver list to string
        dietType = ''
        for each in self.meal_dishe.getdietTypes():
            dietType += each + '\n'

        dietTypeLabel = self.sample_widget.label(set_text=dietType)
        gridLayout.addWidget(dietTypeLabel, 0, 1, 1, 1)

        mealTime = ''
        for each in self.meal_dishe.getmealtime():
            mealTime += each + '\n'
        mealTimeLabel = self.sample_widget.label(set_text=mealTime)
        gridLayout.addWidget(mealTimeLabel, 0, 2, 1, 1)


        return widget


    def totalTime_calories_ingredients_widget_def(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget)


        totalTimeLabel = self.sample_widget.label(set_text=self.meal_dishe.getTime())
        gridLayout.addWidget(totalTimeLabel, 0, 0, 1, 1)


        caloriesLabel = self.sample_widget.label(set_text=self.data['nutrition']['calories'])
        gridLayout.addWidget(caloriesLabel, 0, 1, 1, 1)

        ingredientsLabel = self.sample_widget.label(set_text=self.meal_dishe.getingredients())
        gridLayout.addWidget(ingredientsLabel, 0, 2, 2, 1)

        return widget

    def imageWidget(self):
        '''

        :return:
        '''
        val = 350
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='', min_size=[val, val], max_size=[val, val])
        button.setIcon(QIcon(self.data['images']['main']))
        button.setIconSize(QSize(val, val))

        verticalLayout.addWidget(button)

        return widget

    def nutrition_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        for each in self.data['nutrition']:
            string_val = f"{each}: {self.data['nutrition'][each]}"
            pushButton = self.sample_widget.pushButton(set_text=string_val)
            horizontalLayout.addWidget(pushButton)

        return widget

    def otherTabWidget(self):
        '''

        :return:
        '''
        val = 400
        widget = self.sample_widget.widget_def(min_size=[0, val], max_size=[16777215, val])
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        tabWidget = self.sample_widget.tab_widget(parent_self=widget)
        verticalLayout.addWidget(tabWidget)

        tabWidget.addTab(self.historyWidget(), 'History')
        tabWidget.addTab(self.descriptionsWidget(), 'Descriptions')
        tabWidget.addTab(self.equipmentWidget(), 'Equipment')
        tabWidget.addTab(self.instructionsWidget(), 'Instructions')
        tabWidget.addTab(self.getInstruction(), 'Instruction')
        tabWidget.addTab(self.tipsWidget(), 'Tips')
        tabWidget.addTab(self.variationsWidget(), 'Variations')
        tabWidget.addTab(self.storageWidget(), 'Storage')
        tabWidget.addTab(self.reheatingInstructionsWidget(), 'Reheating Instructions')
        tabWidget.addTab(self.allergyWidget(), 'Allergy')


        return widget


    def historyWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(self.meal_dishe.gethistory())
        verticalLayout.addWidget(plainTextEdit)

        return widget

    def descriptionsWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(self.meal_dishe.getdescription())
        verticalLayout.addWidget(plainTextEdit)

        return widget


    def equipmentWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(self.meal_dishe.getequipment())
        verticalLayout.addWidget(plainTextEdit)

        return widget



    def instructionsWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(self.meal_dishe.getinstructions())
        verticalLayout.addWidget(plainTextEdit)

        return widget

    def getInstruction(self):
        '''

        :return:
        '''
        string_val = ''
        for each in self.data['instructions']:
            for key, value in each.items():
                string_val += f"{key}: {value}\n"
            string_val += f"-" * 50 + '\n'

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(string_val)
        verticalLayout.addWidget(plainTextEdit)

        return widget

    def tipsWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(self.meal_dishe.gettips())
        verticalLayout.addWidget(plainTextEdit)

        return widget

    def variationsWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(self.meal_dishe.getvariations())
        verticalLayout.addWidget(plainTextEdit)

        return widget


    def storageWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(self.meal_dishe.getstorage())
        verticalLayout.addWidget(plainTextEdit)

        return widget

    def reheatingInstructionsWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(self.meal_dishe.getreheatingInstructions())
        verticalLayout.addWidget(plainTextEdit)

        return widget

    def allergyWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(self.meal_dishe.getallergens())
        verticalLayout.addWidget(plainTextEdit)

        return widget
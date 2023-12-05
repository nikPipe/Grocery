from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from data import get_meal_dishe
from ui.mainWidget.centerWidget.centerMainWidget import mealWidget_sample



class savedMealLeft_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()

        self.parent = parent
        self.mainWidget = self.parent.parent.parent.parent
        self.getCookingSkillList = []

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)
        self.sampleObjectNmae = 'labelStyleSheet'
        self.labelStyleSheet = self.sample_widget.styleSheet_def(obj_name=self.sampleObjectNmae,
                                                                 color=self.color_class.white_color.get_value())

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        '''

        :return:
        '''
        height = 1000
        width = 200
        widget = self.sample_widget.widget_def(min_size=(width, height), max_size=(width, height))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        verticalLayout.addWidget(self.name_button())

        verticalLayout.addWidget(self.savedRecepieTreeWidget())

        return widget

    def name_button(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        label_objectName = 'label'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=label_objectName, color=self.color_class.white_color.get_value())

        label = self.sample_widget.label(set_text='Saved Meal', set_object_name=label_objectName, set_styleSheet=styleSheet_,
                                         set_alighment=self.sample_widget.center_alignment)
        label.setFont(self.font)
        horizontalLayout.addWidget(label)

        button = self.sample_widget.pushButton(set_text='', min_size=(30, 30), max_size=(30, 30))
        horizontalLayout.addWidget(button)

        return widget

    def savedRecepieTreeWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        self.saveMealleft_MaintreeWidget = self.sample_widget.treeWidget(setHeaderHidden=True)
        self.saveMealleft_MaintreeWidget.selectionModel().selectionChanged.connect(partial(self.savedRecepieTreeWidget_, self.saveMealleft_MaintreeWidget))
        verticalLayout.addWidget(self.saveMealleft_MaintreeWidget)

        json_data = self.help_class.get_TempFileData()
        if 'savedMeal' in json_data:
            for meal in json_data['savedMeal']:
                meal_item = QTreeWidgetItem(self.saveMealleft_MaintreeWidget)
                meal_item.setText(0, meal)
                self.saveMealleft_MaintreeWidget.addTopLevelItem(meal_item)

        if 'forYouMeal' in json_data:
            item = QTreeWidgetItem(self.saveMealleft_MaintreeWidget)
            item.setText(0, 'For You')
            item.setExpanded(True)
            self.saveMealleft_MaintreeWidget.addTopLevelItem(item)


        return widget

    def savedRecepieTreeWidget_(self, treeWidget):
        '''

        :param treeWidget:
        :return:
        '''
        try:

            item = treeWidget.selectedItems()[0]

            verticalLayout = self.parent.saveRecepieRightWidget.verticalLayout
            self.help_class.clearLayout(verticalLayout)
            getAllMeal = self.mainWidget.getAllMeal
            readJsonFile = self.help_class.getTempJsonFile()
            mealnameList = readJsonFile['savedMeal']
            for eachMeal in mealnameList:
                if eachMeal == item.text(0):
                    for eachMeal_ in mealnameList[eachMeal]:
                        for eachMealData in getAllMeal:
                            eachMealData = getAllMeal[eachMealData]
                            if eachMeal_ == eachMealData['id']:
                                widget__ = mealWidget_sample.mealWidgetSample(parent=self.mainWidget, data=eachMealData)
                                verticalLayout.addWidget(widget__)
        except:
            import traceback
            traceback.print_exc()

    def leftTreeUpdate(self):
        '''

        :return:
        '''
        self.saveMealleft_MaintreeWidget.clear()

        json_data = self.help_class.get_TempFileData()
        if 'savedMeal' in json_data:
            for meal in json_data['savedMeal']:
                meal_item = QTreeWidgetItem(self.saveMealleft_MaintreeWidget)
                meal_item.setText(0, meal)
                self.saveMealleft_MaintreeWidget.addTopLevelItem(meal_item)

        if 'forYouMeal' in json_data:
            item = QTreeWidgetItem(self.saveMealleft_MaintreeWidget)
            item.setText(0, 'For You')
            item.setExpanded(True)
            self.saveMealleft_MaintreeWidget.addTopLevelItem(item)


    def updata_(self):
        '''

        :return:
        '''
        self.leftTreeUpdate()
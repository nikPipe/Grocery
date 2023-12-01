from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
from data import get_meal_dishe
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui import commonButtonWidget
from ui.mainWidget.centerWidget.centerMainWidget import mealWidget_sample

class commonAllSearch_Widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.mainWidget = self.parent.parent.parent.parent
        self.getCookingSkillList = []

        self.allMealList = get_meal_dishe.getAllMeal()

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        '''

        :return:
        '''
        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        verticalLayout.addWidget(self.searchWidget())
        verticalLayout.addWidget(self.mealViewWidget())

        #verticalLayout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        return widget

    def searchWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        lineEdit_object = 'lineEdit_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=lineEdit_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        self.lineEdit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet)
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setMaximumSize(QSize(16777215, 40))
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText('Search the Meal')
        self.lineEdit.textChanged.connect(partial(self.mealViewWidget_update, self.lineEdit))
        verticalLayout.addWidget(self.lineEdit)


        return widget


    def mealViewWidget(self):
        '''

        :return:
        '''
        height = 180
        widget_object = 'mealViewWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                         border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        verticalLayout.addWidget(scrollArea)
        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        scrollArea.setWidget(scrollAreaWidgetContents)

        self.search_meal_gridLayout = self.sample_widget.grid_layout(parent_self=scrollAreaWidgetContents, set_spacing=15)
        width = 250
        height = 150
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)

        return widget

    def mealViewWidget_update(self, lineedit):
        '''

        :return:
        '''
        text = lineedit.text()
        mealList = []
        for each in self.allMealList:
            name = each['name']
            if text.lower() in name.lower():
                mealList.append(each)
        a = 0
        width = 250
        height = 150
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        try:

            self.help_class.clearLayout(self.search_meal_gridLayout)
        except:
            import traceback
            traceback.print_exc()
        num_columns = 5
        a = 0
        try:

            for each in mealList:

                widget__ = mealWidget_sample.mealWidgetSample(parent=self.mainWidget, data=each)
                self.search_meal_gridLayout.addWidget(widget__, a, 0)
                a+=1
        except:
            import traceback
            traceback.print_exc()
    def pushClick(self, data):

        self.parent.mainCenterWidget.centerMainWidget.stackedWidget.setCurrentIndex(1)
        self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.stakeWidget.setCurrentIndex(1)

        self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.mealMain_widget.mealbutton_def(data)

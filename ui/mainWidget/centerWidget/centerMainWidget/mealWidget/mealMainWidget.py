from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


from ui.mainWidget.centerWidget.centerMainWidget.mealWidget import mealMain_widget
from ui.mainWidget.centerWidget.centerMainWidget.mealWidget import mealDetail_widget
from ui.mainWidget.centerWidget.centerMainWidget.mealWidget import mealSearch_widget
from ui.mainWidget.centerWidget.centerMainWidget import mealWidget_sample

from data import get_meal_dishe

class mealMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        self.mealMain_widget = mealMain_widget.mealMain_Widget(self.parent)
        self.mealDetailWidet = mealDetail_widget.mealDetail_Widget(self.parent)
        self.mealSearchWidget = mealSearch_widget.mealSearch_Widget(self.parent)

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

        self.stakeWidget = QStackedWidget(widget)
        verticalLayout.addWidget(self.stakeWidget)

        self.stakeWidget.addWidget(self.mealMain_widget)
        self.stakeWidget.addWidget(self.mealDetailWidet)
        self.stakeWidget.addWidget(self.mealSearchWidget)

        return widget



    def searchWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        lineEdit_object = 'lineEdit_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=lineEdit_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        lineEdit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet)
        lineEdit.setMinimumSize(QSize(0, 40))
        lineEdit.setMaximumSize(QSize(16777215, 40))
        lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        lineEdit.setFont(font)
        lineEdit.setPlaceholderText('Search the Meal')
        lineEdit.textChanged.connect(partial(self.lineEditTextChanged, lineEdit))
        verticalLayout.addWidget(lineEdit)

        return widget

    def lineEditTextChanged(self, lineedit):
        '''

        :param text:
        :return:
        '''
        self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.stakeWidget.setCurrentIndex(2)

        lineedit_text = lineedit.text()
        getAllMeal = get_meal_dishe.getAllMeal()
        mealList = []
        for each in getAllMeal:
            if lineedit_text.lower() in each['name'].lower():
                mealList.append(each)

        verticalLayout = self.mealSearchWidget.mealSearch_widget_verticalLayout
        self.help_class.clearLayout(verticalLayout)

        for eachMeal in mealList:
            try:

                widget__ = mealWidget_sample.mealWidgetSample(parent=self.parent, data=eachMeal)
                #widget = self.mealSearchWidget.update_Widget(eachMeal)
                verticalLayout.addWidget(widget__)
            except Exception as e:
                import traceback
                traceback.print_exc()



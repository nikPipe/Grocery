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
        self.mainWidget = self.parent.parent.parent
        self.getCookingSkillList = []
        self.mealMain_widget = mealMain_widget.mealMain_Widget(self.mainWidget)
        self.mealDetailWidet = mealDetail_widget.mealDetail_Widget(self.mainWidget)
        self.mealSearchWidget = mealSearch_widget.mealSearch_Widget(self.mainWidget)

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
        self.mealMain_lineEdit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet)
        self.mealMain_lineEdit.setMinimumSize(QSize(0, 40))
        self.mealMain_lineEdit.setMaximumSize(QSize(16777215, 40))
        self.mealMain_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.mealMain_lineEdit.setFont(font)
        self.mealMain_lineEdit.setPlaceholderText('Search the Meal')
        self.mealMain_lineEdit.textChanged.connect(partial(self.lineEditTextChanged, self.mealMain_lineEdit))
        verticalLayout.addWidget(self.mealMain_lineEdit)

        return widget

    def lineEditTextChanged(self, lineedit):
        '''

        :param text:
        :return:
        '''
        try:

            self.mainWidget.mainCenterWidget.centerMainWidget.mealMainWidget.stakeWidget.setCurrentIndex(2)
            lineedit_text = lineedit.text()
            getAllMeal = self.mainWidget.getAllMeal
            mealList = []
            for each in getAllMeal:
                if lineedit_text.lower() in getAllMeal[each]['name'].lower():
                    mealList.append(getAllMeal[each])

            verticalLayout = self.mealSearchWidget.mealSearch_widget_verticalLayout
            self.help_class.clearLayout(verticalLayout)

            for eachMeal in mealList:
                widget__ = mealWidget_sample.mealWidgetSample(parent=self.mainWidget, data=eachMeal)
                #widget = self.mealSearchWidget.update_Widget(eachMeal)
                verticalLayout.addWidget(widget__)


        except Exception as e:
            import traceback
            traceback.print_exc()

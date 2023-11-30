from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from data import get_meal_dishe

from ui.mainWidget.centerWidget.centerMainWidget.savedMealWidget import savedMealLeft_widget
from ui.mainWidget.centerWidget.centerMainWidget.savedMealWidget import savedMealRight_widget

class savedMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)

        self.saveRecepieLeftWidget = savedMealLeft_widget.savedMealLeft_widget(self)
        self.saveRecepieRightWidget = savedMealRight_widget.savedMealRight_widget(self)


        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        '''


        :return:
        '''

        widget = self.sample_widget.widget_def()
        self.verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        self.splitter = self.sample_widget.splitter_def(parent_self=widget, set_orientation=self.sample_widget.horizonatal)
        self.verticalLayout.addWidget(self.splitter)

        self.splitter.addWidget(self.saveRecepieLeftWidget)
        self.splitter.addWidget(self.saveRecepieRightWidget)

        self.splitter.setSizes([200, 850])

        return widget


    def update_(self):
        print(self.saveRecepieLeftWidget)
        self.saveRecepieLeftWidget.updata_()
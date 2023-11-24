from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))

from ui.mainWidget.centerWidget.centerMainWidget.savedGroceryWidget import savedGroceryLeft_widget
from ui.mainWidget.centerWidget.centerMainWidget.savedGroceryWidget import savedGroceryRight_widget

class savedGroceryMainWidget(QWidget):
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

        self.saveGroceryLeftWidget = savedGroceryLeft_widget.savedGroceryLeft_widget(self.parent)
        self.saveGroceryRightWidget = savedGroceryRight_widget.savedGroceryRight_widget(self.parent)


        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        '''


        :return:
        '''

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        splitter = self.sample_widget.splitter_def(parent_self=widget, set_orientation=self.sample_widget.horizonatal)
        verticalLayout.addWidget(splitter)


        splitter.addWidget(self.saveGroceryLeftWidget)
        splitter.addWidget(self.saveGroceryRightWidget)



        return widget
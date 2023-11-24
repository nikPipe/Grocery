

import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
from ui.mainWidget.topWidget import topWidgetMain
from ui.mainWidget.centerWidget import mainCenterWidget




class mainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.color_variable = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.topWidgetMain = topWidgetMain.topMainWidget(self)
        self.mainCenterWidget = mainCenterWidget.centerMainWidget(self)

        self.initUI()

    def initUI(self):
        # Set window size.
        self.resize(1200, 800)

        # Set window title
        self.setWindowTitle('Meal Planner Window')

        widget = self.uiWidget()
        self.setCentralWidget(widget)

        # Show window
        self.show()


    def uiWidget(self):
        '''
        :return: QWidget
        '''
        # Create widget
        select_all_object = 'mainWidget'
        color = self.color_variable.setColorVal(r=36, g=36, b=36)
        select_all_styleSheet = self.sample_widget.styleSheet_def(obj_name=select_all_object,
                                                                  background_color=color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=select_all_object, set_styleSheet=select_all_styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #TOP WIDGET
        verticalLayout.addWidget(self.topWidgetMain)

        #CENTER WIDGET
        verticalLayout.addWidget(self.mainCenterWidget)







        return widget
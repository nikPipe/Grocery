import json
from functools import partial

from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template

from ui_old__.widget_old import anotherWindow
from ui_old__.widget_old import topWidget, midWidget
from data import help


class mainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.help = help.Help()
        self.top_widget = topWidget.topWidget()
        self.mid_widget = midWidget.midWidget()



        self.initUI()

    def initUI(self):
        # Set window size.
        self.resize(1600, 800)

        # Set window title
        self.setWindowTitle('Meal Planner')

        widget = self.uiWidget()
        self.setCentralWidget(widget)

        # Show window
        self.show()

    def uiWidget(self):

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #verticalLayout.addWidget(self.top_widget)
        verticalLayout.addWidget(self.mid_widget)

        return widget



















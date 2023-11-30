import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderCenterMonth_widget

class AddToCalender(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.data = data

        self.calenderCenterMonth_widget = calenderCenterMonth_widget.calenderCenterMonth_widget(self.parent)


        name = 'Add to Calender: ' + str(self.data['name'])
        self.setWindowTitle(name)
        self.setModal(True)  # Set the dialog as modal

        layout = QVBoxLayout(self)
        label = QLabel("This is a modal popup dialog.", self)

        layout.addWidget(self.initUI())


    def initUI(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.calenderCenterMonth_widget)


        return widget

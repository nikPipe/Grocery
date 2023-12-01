import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderCenterMonth_widget
from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderMainWidget

class AddToCalender(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.data = data
        self.mainWidget = self.parent.parent.parent
        print(self.mainWidget)
        self.calenderMainWidget = calenderMainWidget.calenderMainWidget(self.mainWidget)
        self.calenderMainWidget.calenderCenter_widget.calenderCenterDay_widget.shoppingListHide = True
        self.calenderMainWidget.calenderCenter_widget.calenderCenterWeek_widget.shoppingListHide = True


        name = 'Add to Calender: ' + str(self.data['name'])
        self.currentDay = self.parent.calenderMainWidget.currentDay
        self.setWindowTitle(name)
        self.setModal(True)  # Set the dialog as modal

        self.setMinimumSize(1000, 700)


        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)
        self.sampleObjectNmae = 'labelStyleSheet'
        self.labelStyleSheet = self.sample_widget.styleSheet_def(obj_name=self.sampleObjectNmae,
                                                                 color=self.color_class.white_color.get_value())



        layout = QVBoxLayout(self)


        layout.addWidget(self.initUI())

    def initUI(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        comboBox = self.calenderMainWidget.findChildren(QComboBox)
        if comboBox:
            comboBox = comboBox[0]
            comboBox.setCurrentIndex(2)

        verticalLayout.addWidget(self.calenderMainWidget)



        return widget



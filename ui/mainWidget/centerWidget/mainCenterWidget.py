from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os

from ui.mainWidget.centerWidget.leftWidget import leftmainWidget
from ui.mainWidget.centerWidget.centerMainWidget import centerMainWidget_

file =  os.path.dirname(os.path.realpath(ui.__file__))

class centerMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent

        self.leftmainWidget = leftmainWidget.leftMainWidget(self)
        self.centerMainWidget = centerMainWidget_.centerMainWidget(self)



        self.getCookingSkillList = []
        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)
        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def initUI(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def(min_size=(0, 800), max_size=(self.sample_widget.max_size, self.sample_widget.max_size))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        split_def = self.sample_widget.splitter_def(parent_self=widget)
        split_def.setOrientation(Qt.Horizontal)

        horizontalLayout.addWidget(split_def)

        split_def.addWidget(self.leftmainWidget)
        split_def.addWidget(self.centerMainWidget)
        split_def.setSizes([1, 600])


        return widget
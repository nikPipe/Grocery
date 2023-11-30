import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os, traceback
file =  os.path.dirname(os.path.realpath(ui.__file__))
from data import get_meal_dishe

from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget.old import recepieDetail_widget
from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget import recepieLeft_TreeWidget
from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget import recepieRight_menuWidget
from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget import recepieRight_menuDetailWidget


class recepieCenter_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.recepieDict = {}
        #self.recepieDetail_widget = recepieDetail_widget.recepieDetail_widget(self.parent)

        self.recepie_treeWidget = recepieLeft_TreeWidget.recepieTree_widget(self.parent)
        self.recepieRightMenu_widget = recepieRight_menuWidget.recepieRightMenu_widget(self.parent)
        self.recepieRightMenuDetail_widget = recepieRight_menuDetailWidget.recepieRightMenuDetail_widget(self.parent)

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)
        self.sampleObjectNmae = 'labelStyleSheet'
        self.labelStyleSheet = self.sample_widget.styleSheet_def(obj_name=self.sampleObjectNmae,
                                                                 color=self.color_class.white_color.get_value())

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

        splitter.addWidget(self.recepie_treeWidget)
        splitter.addWidget(self.recepieDetail_widget())

        splitter.setSizes([10, 700])

        return widget



    def recepieDetail_widget(self):
        '''
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        splitter = self.sample_widget.splitter_def(parent_self=widget, set_orientation=self.sample_widget.vertical)
        verticalLayout.addWidget(splitter)

        splitter.addWidget(self.recepieRightMenu_widget)
        splitter.addWidget(self.recepieRightMenuDetail_widget)

        splitter.setSizes([100, 500])


        return widget














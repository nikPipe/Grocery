from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))




class recepieDetailMenuDetail_widget(QWidget):
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
        height = 1000
        widget = self.sample_widget.widget_def(min_size=(0, height), max_size=(16777215, height))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        verticalLayout.addWidget(self.menuTabWidget())

        return widget


    def menuTabWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        tabWidget_objName = 'tabWidget'
        tabWidget_styleSheet = self.sample_widget.styleSheet_def(obj_name=tabWidget_objName, color=self.backgroundColor.get_value(),
                                                                 background=self.color.get_value(),
                                                                 border_radius=5)
        tabWidget = self.sample_widget.tab_widget(parent_self=widget, set_styleSheet=tabWidget_styleSheet, set_object_name=tabWidget_objName)
        verticalLayout.addWidget(tabWidget)

        tabWidget.addTab(self.menuDetailWidget(), 'Menu Detail')
        tabWidget.addTab(self.recepieDetail(), 'Recepie Detail')

        tabWidget.setCurrentIndex(1)

        return widget



    def menuDetailWidget(self):
        '''

        :return:
        '''
        widget_objName = 'menuDetailWidget'
        widget_styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_objName, color=self.color_class.white_color.get_value(),
                                                              background=self.color_class.black_color.get_value(),
                                                              border_radius=5)
        widget = self.sample_widget.widget_def(set_object_name=widget_objName, set_styleSheet=widget_styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        return widget

    def recepieDetail(self):
        '''

        :return:
        '''
        widget_objName = 'recepieDetail'
        widget_styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_objName, color=self.color_class.white_color.get_value(),
                                                              background=self.color_class.black_color.get_value(),
                                                              border_radius=5)
        widget = self.sample_widget.widget_def(set_object_name=widget_objName, set_styleSheet=widget_styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        treeWidget_objName = 'treeWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=treeWidget_objName, color=self.color_class.white_color.get_value(),
                                                        background=self.color_class.black_color.get_value(),
                                                        border_radius=5)
        self.recepieDetail_treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        self.recepieDetail_treeWidget.setObjectName(treeWidget_objName)
        verticalLayout.addWidget(self.recepieDetail_treeWidget)


        return widget











from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))




class recepieDetailMenu_widget(QWidget):
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


        #verticalLayout.addWidget(self.menuCheckboxWidget())

        verticalLayout.addWidget(self.recepieDetailMenuTreeWidget())




        return widget

    def recepieDetailMenuTreeWidget(self):
        '''
        Recepie menu detail widget
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        treeWidget_objName = 'treeWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=treeWidget_objName, color=self.color_class.white_color.get_value(),
                                                        background=self.color_class.black_color.get_value(),
                                                        border_radius=5)
        treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        treeWidget.setObjectName(treeWidget_objName)
        treeWidget.setStyleSheet(styleSheet_)
        verticalLayout.addWidget(treeWidget)

        treeItem = QTreeWidgetItem(treeWidget)
        treeItem.setText(0, 'Test')
        treeItem.setCheckState(0, Qt.Checked)



        return widget









    def menuCheckboxWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def(min_size=(0, 50), max_size=(16777215, 50))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        for each in range(5):
            checkbox_objName = 'checkbox'
            styleSheet_ = self.sample_widget.styleSheet_def(obj_name=checkbox_objName, color=self.color_class.white_color.get_value())
            checkBox = self.sample_widget.checkbox(set_text='Test', set_object_name=checkbox_objName, set_styleSheet=styleSheet_)
            horizontalLayout.addWidget(checkBox)

        return widget















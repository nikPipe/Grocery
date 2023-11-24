from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))

from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget import recepieDetail_widget


class recepieCenter_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.recepieDetail_widget = recepieDetail_widget.recepieDetail_widget(self.parent)


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
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        spitter = self.sample_widget.splitter_def(parent_self=widget)
        spitter.setOrientation(Qt.Horizontal)
        horizontalLayout.addWidget(spitter)

        spitter.addWidget(self.recepieTreeWidget())
        spitter.addWidget(self.recepieDetail_widget)


        return widget


    def recepieTreeWidget(self):
        '''
        Recepie Tree Widget
        :return:
        '''
        widget = self.sample_widget.widget_def()
        widget.setFixedWidth(300)

        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        treeWidget_objName = 'treeWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=treeWidget_objName, color=self.color_class.white_color.get_value(),
                                                        background=self.color_class.black_color.get_value(),
                                                        border_radius=5)
        treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        treeWidget.setObjectName(treeWidget_objName)
        treeWidget.setStyleSheet(styleSheet_)
        verticalLayout.addWidget(treeWidget)

        return widget


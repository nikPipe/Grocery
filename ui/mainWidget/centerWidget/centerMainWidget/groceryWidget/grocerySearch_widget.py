from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


class grocerySearch_widget(QWidget):
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

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        lineEdit_object = 'lineEdit_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=lineEdit_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        self.grocerySearch_lineEdit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet,
                                                set_PlaceholderText='Search The Product Name')
        self.grocerySearch_lineEdit.setMinimumSize(QSize(0, 40))
        self.grocerySearch_lineEdit.setMaximumSize(QSize(16777215, 40))
        self.grocerySearch_lineEdit.setAlignment(Qt.AlignCenter)
        self.grocerySearch_lineEdit.textChanged.connect(partial(self.grocerySearch, self.grocerySearch_lineEdit))

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.grocerySearch_lineEdit.setFont(font)

        verticalLayout.addWidget(self.grocerySearch_lineEdit)

        return widget


    def grocerySearch(self, lineedit):
        '''

        :return:
        '''
        text = lineedit.text()

        self.parent.stakeWidget.setCurrentIndex(1)
        self.parent.grocerySearchSecound_widget.setLineeditText(text)
















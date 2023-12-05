from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget.groceryWidget import groceryItem_widget

class grocerySearchSecound_widget(QWidget):
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

        #GROCERY SEARCH LINEEDIT
        verticalLayout.addWidget(self.searchLinedit())

        verticalLayout.addWidget(self.groceryWidget())

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


        return widget


    def searchLinedit(self):
        '''

        :return:
        '''

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        lineEdit_object = 'lineEdit_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=lineEdit_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        self.grocerySearchLineedit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet,
                                                set_PlaceholderText='Search The Product Name')
        self.grocerySearchLineedit.setMinimumSize(QSize(0, 40))
        self.grocerySearchLineedit.setMaximumSize(QSize(16777215, 40))
        self.grocerySearchLineedit.setAlignment(Qt.AlignCenter)
        self.grocerySearchLineedit.textChanged.connect(partial(self.grocerySearch, self.grocerySearchLineedit))

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.grocerySearchLineedit.setFont(font)

        verticalLayout.addWidget(self.grocerySearchLineedit)

        return widget


    def grocerySearch(self, lineedit):
        '''

        :return:
        '''
        text = lineedit.text()
        if text == '':
            self.parent.grocerySearchMain_widget.grocerySearch_lineEdit.setText('')
            self.parent.stakeWidget.setCurrentIndex(0)



    def setLineeditText(self, text):
        '''

        :param text:
        :return:
        '''
        self.grocerySearchLineedit.setText(text)


    def groceryWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        object_name = 'add to cart button'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object_name, background_color=self.color_class.red_color.get_value(),
                                                       border_radius=20)
        pushButton = self.sample_widget.pushButton(set_text='Add To Cart', set_object_name=object_name,
                                                   set_styleSheet=styleSheet, min_size=(0, 40), max_size=(16777215, 40))
        verticalLayout.addWidget(pushButton)


        widget__ = self.sample_widget.widget_def()
        verticalLayout_ = self.sample_widget.vertical_layout(parent_self=widget__, set_contents_margins=(0, 0, 0, 0))
        widget_ = self.groceryItem_widget = groceryItem_widget.groceryItem_widget(self, addItemButton=widget)
        verticalLayout_.addWidget(widget_)



        return widget__




















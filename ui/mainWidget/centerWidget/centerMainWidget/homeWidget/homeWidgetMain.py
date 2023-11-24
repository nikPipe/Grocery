from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget.homeWidget import commonAllSearch_widget

class homwMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.commonAllSearch_widget = commonAllSearch_widget.commonAllSearch_Widget(self)


        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)
    def initUI(self):
        '''


        :return:
        '''
        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)


        self.stakeWidget = QStackedWidget(widget)
        verticalLayout.addWidget(self.stakeWidget)

        self.stakeWidget.addWidget(self.stakeOne())
        self.stakeWidget.addWidget(self.commonAllSearch_widget)

        return widget


    def stakeOne(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)


        verticalLayout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        verticalLayout.addWidget(self.homeMealSuggestions())

        verticalLayout.addWidget(self.searchWidget())

        verticalLayout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))


        return widget


    def homeMealSuggestions(self):
        '''
        This function is used to get the meal suggestions from the database
        '''
        widget_object = 'homeMealSuggestions'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(min_size=(0, 200), max_size=(self.sample_widget.max_size, 200),
                                               set_object_name=widget_object, set_styleSheet=styleSheet)
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        horizontalLayout.addWidget(scrollArea)
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        scrollArea.setWidget(scrollAreaWidgetContents)

        horizontalLayout_ = self.sample_widget.horizontal_layout(parent_self=scrollAreaWidgetContents, set_spacing=10,)

        width = 250
        height = 150
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        for each in  range(0, 4):
            pushButton_object = 'pushButton_object'
            styleSheet = self.sample_widget.styleSheet_def(obj_name=pushButton_object, background_color=self.backgroundColor.get_value(),
                                                           border_radius=20)

            pushButton = self.sample_widget.pushButton(set_text='Meal', min_size=(width, height), max_size=(width, height),
                                                       set_styleSheet=styleSheet, set_object_name=pushButton_object )
            pushButton.setFont(font)

            horizontalLayout_.addWidget(pushButton)

        return widget



    def searchWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)


        lineEdit_object = 'lineEdit_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=lineEdit_object, background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        lineEdit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet)
        lineEdit.setMinimumSize(QSize(0, 40))
        lineEdit.setMaximumSize(QSize(16777215, 40))
        lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        lineEdit.setFont(font)
        lineEdit.setPlaceholderText('Search the Product')
        lineEdit.textChanged.connect(partial(self.lineEditTextChanged, lineEdit))
        verticalLayout.addWidget(lineEdit)

        return widget

    def lineEditTextChanged(self, lineedit):
        '''

        :param text:
        :return:
        '''
        self.getCookingSkillList = []
        text = lineedit.text()
        if text != '':
            self.stakeWidget.setCurrentIndex(1)
            self.commonAllSearch_widget.lineEdit.setText(text)


        '''
        if text != '':
            self.stakeWidget.setCurrentIndex(1)
        '''

    def searchWidget_2(self):
        '''

        :return:
        '''



        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        pushButton = self.sample_widget.pushButton(set_text='Search')
        verticalLayout.addWidget(pushButton)

        return widget
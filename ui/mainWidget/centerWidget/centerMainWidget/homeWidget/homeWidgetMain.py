from functools import partial
import random

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import traceback
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget.homeWidget import commonAllSearch_widget
from ui.mainWidget.centerWidget.centerMainWidget import popup_detailMeal

from ui import commonButtonWidget

class homwMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.mainWindow = self.parent.parent.parent
        self.getCookingSkillList = []
        self.get_all_meal = self.mainWindow.getAllMeal
        self.mealDic = self.mainWindow.mealDic
        self.tempFile_ = self.help_class.getTempFile(self.help_class.tempFileName)

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
        try:
            verticalLayout.addWidget(self.searchWidget())
        except Exception as e:
            traceback.print_exc()


        verticalLayout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))


        return widget


    def homeMealSuggestions(self):
        '''
        This function is used to get the meal suggestions from the database
        '''
        widget_object = 'homeMealSuggestions'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        height = 250
        widget = self.sample_widget.widget_def(min_size=(0, height), max_size=(self.sample_widget.max_size, height),
                                               set_object_name=widget_object, set_styleSheet=styleSheet)
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        horizontalLayout.addWidget(scrollArea)
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        scrollArea.setWidget(scrollAreaWidgetContents)

        self.horizontalLayout_ = self.sample_widget.horizontal_layout(parent_self=scrollAreaWidgetContents, set_spacing=10,)

        self.update_horizontalLayout_()

        return widget

    def update_horizontalLayout_(self):

        self.help_class.clearLayout(self.horizontalLayout_)

        json_data = self.help_class.readjsonFile(self.tempFile_)
        diet = json_data['diet']
        dietlist = []
        for each in diet:
            if each in self.mealDic:
                dietlist.extend(self.mealDic[each])

        random_ = random.sample(dietlist, 30)
        for each in random_:
            widget_ = self.homeMealSuggestions_widget(self.get_all_meal[each])
            self.horizontalLayout_.addWidget(widget_)

    def homeMealSuggestions_widget(self, data):
        '''

        :return:
        '''

        widget_ = commonButtonWidget.commonWidget(data)
        pushButton = widget_.findChild(QPushButton)
        pushButton.clicked.connect(partial(self.pushClick, data))

        pushButtonList = widget_.findChildren(QPushButton)
        for each_pushButton in pushButtonList:
            if 'addToCalender'.lower() in each_pushButton.objectName().lower():
                each_pushButton.clicked.connect(partial(self.addToCalender, data))

        return widget_

    def searchWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)


        lineEdit_object = 'lineEdit_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=lineEdit_object, background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        self.homeWidgetMain_lineEdit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet)
        self.homeWidgetMain_lineEdit.setMinimumSize(QSize(0, 40))
        self.homeWidgetMain_lineEdit.setMaximumSize(QSize(16777215, 40))
        self.homeWidgetMain_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.homeWidgetMain_lineEdit.setFont(font)
        self.homeWidgetMain_lineEdit.setPlaceholderText('Search the Product')
        self.homeWidgetMain_lineEdit.textChanged.connect(partial(self.lineEditTextChanged, self.homeWidgetMain_lineEdit))
        verticalLayout.addWidget(self.homeWidgetMain_lineEdit)

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



    def searchWidget_2(self):
        '''

        :return:
        '''

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        pushButton = self.sample_widget.pushButton(set_text='Search')
        verticalLayout.addWidget(pushButton)

        return widget

    def pushClick(self, data):

        try:
            popup = popup_detailMeal.mealDeatail(self.mainWindow, data)
            result = popup.exec_()  # This makes the dialog modal
        except Exception as e:
            import traceback
            traceback.print_exc()

    def addToCalender(self, data):

        try:
            popup = self.mainWindow.popup_calender.AddToCalender(self.mainWindow, data)
            #popup = self.parent.popup_calender.AddToCalender(self.parent, data)
            result = popup.exec_()
        except Exception as e:
            import traceback
            traceback.print_exc()

        #self.parent.mainCenterWidget.centerMainWidget.calenderMainWidget.calenderTop_widget_def(data=data)
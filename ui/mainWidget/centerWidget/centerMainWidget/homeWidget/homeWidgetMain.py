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

from data import get_meal_dishe

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
        self.get_all_meal = get_meal_dishe.getAllMeal()
        self.mealDic = get_meal_dishe.getDic()
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
        json_data = self.help_class.readjsonFile(self.tempFile_)
        diet = json_data['diet']

        dic_val =[]
        for eachDiet in diet:
            if eachDiet in self.mealDic:
                random_ = random.sample(self.mealDic[eachDiet], 10)
                dic_val.extend(random_)

        for each in dic_val:

            widget_ = commonButtonWidget.commonWidget(each)
            pushButton = widget_.findChild(QPushButton)
            pushButton.clicked.connect(partial(self.pushClick, each))

            pushButtonList = widget_.findChildren(QPushButton)
            for each_pushButton in pushButtonList:
                if 'addToCalender'.lower() in each_pushButton.objectName().lower():
                    each_pushButton.clicked.connect(partial(self.addToCalender, each))


            horizontalLayout_.addWidget(widget_)

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

    def pushClick(self, data):

        #self.parent.mainCenterWidget.centerMainWidget.stackedWidget.setCurrentIndex(1)
        #self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.stakeWidget.setCurrentIndex(1)
        #self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.mealMain_widget.mealbutton_def(data)

        popup = popup_detailMeal.mealDeatail(self.parent, data)
        result = popup.exec_()  # This makes the dialog modal


    def addToCalender(self, data):

        try:

            popup = self.mainWindow.popup_calender.AddToCalender(self.parent, data)

            #popup = self.parent.popup_calender.AddToCalender(self.parent, data)
            result = popup.exec_()
        except Exception as e:
            import traceback
            traceback.print_exc()

        #self.parent.mainCenterWidget.centerMainWidget.calenderMainWidget.calenderTop_widget_def(data=data)
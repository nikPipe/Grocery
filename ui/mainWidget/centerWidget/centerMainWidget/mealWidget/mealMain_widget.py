from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from data import mealClass
from ui import commonButtonWidget

class mealMain_Widget(QWidget):
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


        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

        self.update_()
    def initUI(self):
        '''


        :return:
        '''
        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        self.verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        self.verticalLayout.addWidget(scrollArea)
        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        scrollArea.setWidget(scrollAreaWidgetContents)

        self.verticalLayout = self.sample_widget.vertical_layout(parent_self=scrollAreaWidgetContents, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        #verticalLayout.addWidget(self.searchWidget())
        #self.verticalLayout.addWidget(self.mealViewWidget())

        self.verticalLayout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        return widget

    def searchWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        lineEdit_object = 'lineEdit_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=lineEdit_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        lineEdit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet)
        lineEdit.setMinimumSize(QSize(0, 40))
        lineEdit.setMaximumSize(QSize(16777215, 40))
        lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        lineEdit.setFont(font)
        lineEdit.setPlaceholderText('Search the Meal')
        #lineEdit.textChanged.connect(self.lineEditTextChanged)
        verticalLayout.addWidget(lineEdit)

        return widget

    def mealViewWidget(self, buttonDic, value):
        '''

        :return:
        '''
        height = 300
        widget_object = 'mealViewWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                         border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(min_size=(0, height), max_size=(self.sample_widget.max_size, height),
                                               set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)


        label_object = 'label_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=label_object,
                                                         color=self.color_class.white_color.get_value(),
                                                            border_radius=20)
        label = self.sample_widget.label(set_text=value, set_object_name=label_object, set_styleSheet=styleSheet)
        font = QFont()
        font.setBold(True)
        font.setPointSize(15)
        label.setFont(font)
        verticalLayout.addWidget(label)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        verticalLayout.addWidget(scrollArea)
        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        scrollArea.setWidget(scrollAreaWidgetContents)

        horizontalLayout_ = self.sample_widget.horizontal_layout(parent_self=scrollAreaWidgetContents, set_spacing=10,)
        width = 250
        height = 150
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)

        for eachButton in buttonDic:
            widget_ = commonButtonWidget.commonWidget(dict=eachButton)
            widget_.findChild(QPushButton).clicked.connect(partial(self.mealbutton_def, eachButton))

            pushButtonList = widget_.findChildren(QPushButton)
            for each_pushButton in pushButtonList:
                if 'addToCalender'.lower() in each_pushButton.objectName().lower():
                    each_pushButton.clicked.connect(
                        partial(self.newButton_def, eachButton))
            horizontalLayout_.addWidget(widget_)
        

        return widget


    def update_(self):
        '''

        :return:
        '''

        mealDic = self.parent.getAllMeal
        self.mealDic_ = {}
        dietType_Dic = self.parent.mealDic
        for eachDietType_Dic in dietType_Dic:
            self.mealDic_[eachDietType_Dic] = []
            for eachDiet in dietType_Dic[eachDietType_Dic]:
                self.mealDic_[eachDietType_Dic].append(mealDic[eachDiet])



        '''
        

        getAllMeal = self.parent.getAllMeal

        for each in dietType_Dic:
            list_val = dietType_Dic[each]
            for eachList in list_val:
                if eachList not in self.mealDic:
                    dic_val = getAllMeal[eachList]
                    self.mealDic[eachList] = dic_val
        
        '''
        for eachDic in self.mealDic_:
            self.verticalLayout.addWidget(self.mealViewWidget(buttonDic=self.mealDic_[eachDic], value=eachDic))


    def newButton_def(self, buttonDic):
        '''

        :param buttonDic:
        :return:
        '''
        popup = self.parent.popup_calender.AddToCalender(parent=self.parent, data=buttonDic)
        result = popup.exec_()


        print(self.parent.mainCenterWidget.centerMainWidget.homeWidgetMain)
        #self.parent.mainCenterWidget.centerMainWidget.homeWidgetMain.addToCalender(data=buttonDic)

    def mealbutton_def(self, buttonDic, treacback=None):
        '''

        :param buttonDic:
        :return:
        '''
        print('thi sis working')
        try:
            print(self.parent)
            popUpDetail = self.parent.popup_detailMeal
            print(popUpDetail)
            pop = self.parent.popup_detailMeal.mealDeatail(parent=self.parent, data=buttonDic)
            result = pop.exec_()
        except Exception as e:
            treacback.print_exc()

        '''
        
        
        self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.stakeWidget.setCurrentIndex(1)
        mealDetailWidget = self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.mealDetailWidet

        mealClass_ = mealClass.mealClass(json=buttonDic)

        #CHANGE THE NAME
        mealDetailWidget.mealNameLabel.setText(mealClass_.name)

        #CHANGE HISTORY
        mealDetailWidget.historyTextEdit.setText(mealClass_.history)

        #ingrediant
        text = 'Ingredients'
        text += '\n' +  str(mealClass_.noOfIngredient())
        mealDetailWidget.ingredientLabel.setText(text)

        #miniuteLabel
        text = 'Miniute'
        text += '\n' + str(mealClass_.gettotalTime())
        mealDetailWidget.miniuteLabel.setText(text)

        #Calories
        text = 'Calories'
        text += '\n' + str(mealClass_.getCalaory())
        mealDetailWidget.caloriesLabel.setText(text)

        #Description
        mealDetailWidget.descriptionTextEdit.setText(mealClass_.description)

        #NUTRITION
        print(mealDetailWidget)
        mealDetailWidget.update_(dic_val=buttonDic)

        #mealDetailWidget.ingredientLabel.setText(mealClass_.getIngredient())

        #IMAGE BUTTON
        imageButton = mealDetailWidget.recepieImageButton
        image = mealClass_.getimages()
        icon = QIcon()
        icon.addPixmap(QPixmap(image), QIcon.Normal, QIcon.Off)
        imageButton.setIcon(icon)
        imageButton.setIconSize(QSize(300, 300))

        '''

























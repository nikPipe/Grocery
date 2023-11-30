import json
import traceback

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
from ui import commonButton




class getGroceryBudgetWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        width = 800

        verticalLayout.addWidget(widget)


    def initUI(self):
        '''

        :return:
        '''
        font = QFont()
        font.setBold(True)
        font.setPointSize(20)


        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget)

        gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0, 1, 1)

        howMuchYouHaveBugetForGroceryInaMonthLabel = commonButton.label_def(objName='howMuchYouHaveBugetForGroceryInaMonthLabel',
                                                    color=self.color_class.white_color.get_value(),
                                                    val=20,
                                                    name='How much you have buget for grocery ina Month?')

        howMuchYouHaveBugetForGroceryInaMonthLabel.setFont(font)
        gridLayout.addWidget(howMuchYouHaveBugetForGroceryInaMonthLabel, 1, 0, 1, 1)

        spinBox_object = 'spinBox_object'
        spinBox_styleSheet = self.sample_widget.styleSheet_def(obj_name=spinBox_object,
                                                                color=self.color_class.black_color.get_value(),
                                                                font_size=20)
        self.spinBox = QSpinBox()
        self.spinBox.setObjectName(spinBox_object)
        self.spinBox.setStyleSheet(spinBox_styleSheet)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(1)
        self.spinBox.setMinimumSize(QSize(400, 54))
        self.spinBox.setAlignment(Qt.AlignCenter)

        gridLayout.addWidget(self.spinBox, 2, 0, 1, 1)

        label = commonButton.label_def(objName='label',
                                       color=self.color_class.white_color.get_value(),
                                       val=20,
                                       name='$')
        label.setFont(font)
        label.setMinimumSize(QSize(50, 54))
        gridLayout.addWidget(label, 2, 1, 1, 1)


        nextButton = commonButton.button_def(objName='next',
                                                color=self.color_class.white_color.get_value(),
                                                backgroundColor=self.color_class.setColorVal(r=141, g=141, b=141).get_value(),
                                                val=15, name='Next'
                                                , connect=self.setValue)
        nextButton.setMinimumSize(QSize(350, 54))
        gridLayout.addWidget(nextButton, 3, 0, 1, 2)
        '''
        
        

        appName_object = 'appName'
        appName_styleSheet = self.sample_widget.styleSheet_def(obj_name=appName_object,
                                                               color=self.color_class.white_color.get_value(),
                                                               font_size=20)

        appName = self.sample_widget.label(set_object_name=appName_object,
                                                    set_styleSheet=appName_styleSheet,
                                                    set_text='How much you have buget for grocery ina Month?', set_alighment=self.sample_widget.center_alignment)
        appName.setFont(font)
        gridLayout.addWidget(appName, 2, 0, 1, 2)


        spinBox_object = 'spinBox_object'
        spinBox_styleSheet = self.sample_widget.styleSheet_def(obj_name=spinBox_object,
                                                                color=self.color_class.white_color.get_value(),
                                                                font_size=20)
        spinBox = QSpinBox()
        spinBox.setObjectName(spinBox_object)
        spinBox.setStyleSheet(spinBox_styleSheet)
        spinBox.setMinimum(1)
        spinBox.setMaximum(10000)
        spinBox.setValue(1)
        gridLayout.addWidget(spinBox, 3, 0, 1, 1)

        label = self.sample_widget.label(set_text='Dollar', set_alighment=self.sample_widget.center_alignment)
        label.setFont(font)
        gridLayout.addWidget(label, 3, 1, 1, 1)


        letGetStarted_object = 'next'
        color = self.color_class.setColorVal(r=141, g=141, b=141)
        letGetStarted_styleSheet = self.sample_widget.styleSheet_def(obj_name=letGetStarted_object,
                                                                     background_color=color.get_value(),
                                                                     color=self.color_class.white_color.get_value(),
                                                                     font_size=40,
                                                                     border_radius=10,
                                                                     )
        letsGetStartedPushButton = self.sample_widget.pushButton(set_object_name=letGetStarted_object,
                                                                 set_styleSheet=letGetStarted_styleSheet,
                                                                 set_text='Next',
                                                                 min_size=[350, 54],
                                                                 connect=self.setValue)
        font = QFont()
        font.setBold(True)
        font.setPointSize(15)
        letsGetStartedPushButton.setFont(font)
        gridLayout.addWidget(letsGetStartedPushButton, 5, 0, 1, 2)

        '''

        gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 6, 0, 1, 1)

        return widget

    def allergyWidget(self):
        '''

        :return:
        '''
        widget_object = 'widget'
        color = self.color_class.setColorVal(r=0, g=0, b=0)
        widget_styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object,
                                                                background_color=self.color_class.black_color.get_value(),
                                                                border_radius=1,)

        val = 60
        widget = self.sample_widget.widget_def(set_object_name=widget_object,
                                                set_styleSheet=widget_styleSheet, min_size=[0, val], max_size=[self.sample_widget.max_size, val])
        gridLayout = self.sample_widget.grid_layout(parent_self=widget)
        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents_object = 'scrollAreaWidgetContents'
        scrollAreaWidgetContents_styleSheet = self.sample_widget.styleSheet_def(obj_name=scrollAreaWidgetContents_object,
                                                                                background_color=color.get_value(),
                                                                                )
        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=scrollAreaWidgetContents_object,
                                                                    set_styleSheet=scrollAreaWidgetContents_styleSheet)
        scrollArea.setWidget(scrollAreaWidgetContents)
        gridLayout.addWidget(scrollArea, 0, 0, 1, 1)


        gridLayout_ = self.sample_widget.grid_layout(parent_self=scrollAreaWidgetContents, set_spacing=10)


        get_allergies = self.help_class.getcookingSkill()
        a = 0
        color = self.color_class.setColorVal(r=141, g=141, b=141)
        for each in get_allergies:
            pushButtonObject = 'pushButtonObject'
            pushButton_styleSheet = self.sample_widget.styleSheet_def(obj_name=pushButtonObject,
                                                                      color=self.color_class.white_color.get_value(),
                                                                      border_radius=50,)

            val = pushButtonObject
            space = '    '
            val = "\n#%s:pressed { background-color: rgb(%s);}" % (pushButtonObject, self.color_class.red_color.get_value())
            pushButton_styleSheet = ''.join([pushButton_styleSheet, space, val])

            pushButton = self.sample_widget.checkbox(set_text=each,set_object_name=pushButtonObject,
                                                     set_styleSheet=pushButton_styleSheet,)
            pushButton.setCheckable(True)
            font = QFont()
            font.setBold(True)
            font.setPointSize(15)
            pushButton.setFont(font)

            gridLayout_.addWidget(pushButton, 0, a, 1, 1)
            a += 1



        return widget


    def setValue(self):
        '''

        :return:
        '''
        val = self.spinBox.value()
        self.parent.userData['groceryBudget'] = self.spinBox.value()
        self.parent.set_stakeWidget_def(8)
        self.parent.userData['calender'] = {}
        self.parent.userData['savedMeal'] = {}
        self.parent.userData['savedRecepie'] = {}
        self.parent.userData['forYouMeal'] = {}
        self.parent.userData['shoppingList'] = {}

        try:
            # Code that may raise an exception
            self.help_class.get_set_TempFileName(self.parent.userData)
        except Exception as e:
            # Handle the exception and print the traceback
            traceback.print_exc()





















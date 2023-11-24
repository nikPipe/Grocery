
from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
from ui import commonButton



class getnoOfPeopleWidget(QWidget):
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



        noOfPersonLabel = commonButton.label_def(objName='noOfPersonLabel',
                                                    color=self.color_class.white_color.get_value(),
                                                    val=20,
                                                    name='No Of People Except you want to make meal plan?')
        noOfPersonLabel.setFont(font)
        gridLayout.addWidget(noOfPersonLabel, 1, 0, 1, 1)

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
        self.spinBox.setMinimumSize(QSize(350, 54))
        self.spinBox.setAlignment(Qt.AlignCenter)
        gridLayout.addWidget(self.spinBox, 2, 0, 1, 1)

        nextButton = commonButton.button_def(objName='next',
                                            color=self.color_class.white_color.get_value(),
                                            backgroundColor=self.color_class.setColorVal(r=141, g=141, b=141).get_value(),
                                            val=15, name='Next'
                                            , connect=self.setValue)
        nextButton.setMinimumSize(QSize(350, 54))
        gridLayout.addWidget(nextButton, 3, 0, 1, 1)
        '''

        appName_object = 'appName'
        appName_styleSheet = self.sample_widget.styleSheet_def(obj_name=appName_object,
                                                               color=self.color_class.white_color.get_value(),
                                                               font_size=20)

        appName = self.sample_widget.label(set_object_name=appName_object,
                                                    set_styleSheet=appName_styleSheet,
                                                    set_text='No Of People Except you want to make meal plan?', set_alighment=self.sample_widget.center_alignment)
        appName.setFont(font)
        gridLayout.addWidget(appName, 2, 0, 1, 1)


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




        appName_object = 'appName'
        appName_styleSheet = self.sample_widget.styleSheet_def(obj_name=appName_object,
                                                               color=self.color_class.white_color.get_value(),
                                                               )

        appName = self.sample_widget.label(set_object_name=appName_object,
                                           set_styleSheet=appName_styleSheet,
                                           set_text='Get Started with one Meal Planning simple and personalize for you', set_alighment=self.sample_widget.center_alignment)
        font.setPointSize(15)
        appName.setFont(font)
        gridLayout.addWidget(appName, 4, 0, 1, 1)



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
        gridLayout.addWidget(letsGetStartedPushButton, 5, 0, 1, 1)

        '''

        gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 6, 0, 1, 1)


        return widget




    def setValue(self):
        '''

        :return:
        '''
        self.parent.userData['noOfPeople'] = self.spinBox.value()
        self.parent.set_stakeWidget_def(7)




















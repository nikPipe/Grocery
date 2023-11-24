
from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help


from ui import commonButton

class welcomeWidget(QWidget):
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
        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget)

        gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0, 1, 1)


        #WELCOME TO LABEL
        welcomeTo_label = commonButton.label_def(objName='welcomeLabel', color=self.color_class.white_color.get_value(), val=20, name='Welcome')
        gridLayout.addWidget(welcomeTo_label, 1, 0, 1, 1)

        #APP NAME
        appName_label = commonButton.label_def(objName='appName', color=self.color_class.white_color.get_value(), val=20, name='App Name')
        gridLayout.addWidget(appName_label, 2, 0, 1, 1)

        #LET'S GET STARTED
        letsGetStartedPushButton = commonButton.button_def(objName='letsGetStarted',
                                                           color=self.color_class.white_color.get_value(),
                                                           backgroundColor=self.color_class.setColorVal(r=141, g=141, b=141).get_value(),
                                                           val=15, name='Let\'s Get Started'
                                                           , connect=self.setValue)
        letsGetStartedPushButton.setMinimumSize(QSize(350, 54))
        gridLayout.addWidget(letsGetStartedPushButton, 3, 0, 1, 1)

        #GET STARTED WITH ONE MEAL PLANNING SIMPLE AND PERSONALIZE FOR YOU
        instruction_label = commonButton.label_def(objName='instructionLabel',
                                                   color=self.color_class.white_color.get_value(),
                                                   val=15, name='Get Started with one Meal Planning simple and personalize for you')
        gridLayout.addWidget(instruction_label, 4, 0, 1, 1)


        gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 5, 0, 1, 1)


        return widget

    def setValue(self):
        '''

        :return:
        '''
        self.parent.set_stakeWidget_def(1)




















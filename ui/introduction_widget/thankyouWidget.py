from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
from ui import commonButton


class thankyouWidget(QWidget):
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
        gridLayout = self.sample_widget.grid_layout(parent_self=widget,  set_spacing=10)

        gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0, 1, 1)

        userButton = commonButton.button_def(objName='userButton',
                                             color=self.color_class.white_color.get_value(),
                                             backgroundColor=self.color_class.setColorVal(r=141, g=141,
                                                                                          b=141).get_value(),
                                             val=15, name='')
        userButton.setIcon(QIcon('ui/icon/profile.jpg'))
        userButton.setIconSize(QSize(200, 200))
        userButton.setMinimumSize(QSize(200, 200))
        userButton.setMaximumSize(QSize(200, 200))
        gridLayout.addWidget(userButton, 1, 0, 1, 1)


        #THANK YOU
        thank_you_label = commonButton.label_def(objName='thank_you_label', color=self.color_class.white_color.get_value(), val=20, name='Thank You')
        gridLayout.addWidget(thank_you_label, 2, 0, 1, 1)

        #For setting up your profile
        instruction_label = commonButton.label_def(objName='instruction_label',
                                                    color=self.color_class.white_color.get_value(),
                                                    val=15, name='For setting up your profile')
        gridLayout.addWidget(instruction_label, 3, 0, 1, 1)

        #you are all teh set to start
        instruction_label = commonButton.label_def(objName='instruction_label',
                                                    color=self.color_class.white_color.get_value(),
                                                    val=15, name='You are all the set to start')
        gridLayout.addWidget(instruction_label, 4, 0, 1, 1)

        next_button = commonButton.button_def(objName='next_button',
                                                color=self.color_class.white_color.get_value(),
                                                backgroundColor=self.color_class.setColorVal(r=141, g=141,
                                                                                            b=141).get_value(),
                                                val=15, name='Finish', connect=self.setValue)
        next_button.setMinimumSize(QSize(350, 54))
        gridLayout.addWidget(next_button, 5, 0, 1, 1)


        gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 7, 0, 1, 1)



        return widget

    def setValue(self):
        '''

        :return:
        '''
        self.parent.close()




















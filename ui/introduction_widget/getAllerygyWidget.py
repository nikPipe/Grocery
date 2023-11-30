
from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
from ui import commonButton




class AllerygyWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent

        verticalLayout = QVBoxLayout(self)
        self.allergyList = []

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



        allerygyLabel = commonButton.label_def(objName='allergyLabel',
                                               color=self.color_class.white_color.get_value(),
                                               val=20,
                                               name='Do you have Any Allergy?')
        gridLayout.addWidget(allerygyLabel, 1, 0, 1, 1)

        gridLayout.addWidget(self.allergyWidget(), 2, 0, 1, 1)

        letsGetStartedPushButton = commonButton.button_def(objName='letsGetStarted',
                                                           color=self.color_class.white_color.get_value(),
                                                           backgroundColor=self.color_class.setColorVal(r=141, g=141, b=141).get_value(),
                                                           val=15, name='Next'
                                                           , connect=self.setValue)
        letsGetStartedPushButton.setMinimumSize(QSize(350, 54))
        gridLayout.addWidget(letsGetStartedPushButton, 3, 0, 1, 1)



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


        get_allergies = self.help_class.get_allergies()
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
            #string_val = '%s: %spx %s' % (self.border_left, pix, type)  # f'{self.border_left}: {pix}px {type} '
            pushButton_styleSheet = ''.join([pushButton_styleSheet, space, val])


            pushButton = self.sample_widget.checkbox(set_text=each,set_object_name=pushButtonObject,
                                                     set_styleSheet=pushButton_styleSheet,)
            pushButton.setCheckable(True)
            font = QFont()
            font.setBold(True)
            font.setPointSize(15)
            pushButton.setFont(font)

            gridLayout_.addWidget(pushButton, 0, a, 1, 1)
            self.allergyList.append(pushButton)
            a += 1

        return widget


    def setValue(self):
        '''

        :return:
        '''
        allergy_list = []
        for each in self.allergyList:
            if each.isChecked():
                allergy_list.append(each.text())

        self.parent.userData['allergy'] = allergy_list
        self.parent.set_stakeWidget_def(3)




















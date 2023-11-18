from ui.import_module import *
from ui.sampleWidget import sample_widget_template





class midWidget_recepieWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)


    def initUI(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.listCountryWidget())
        verticalLayout.addWidget(self.numberOfMemberWidget())
        verticalLayout.addWidget(self.recepieWidget())



        return widget

    def listCountryWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def(min_size=(0, 30), max_size=(16777215, 30))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        listItem = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        comboBox = self.sample_widget.comboBox(parent_self=widget, addItems=listItem)
        verticalLayout.addWidget(comboBox)

        return widget

    def numberOfMemberWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def(min_size=(0, 30), max_size=(16777215, 30))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        label = self.sample_widget.label(set_text='Number of Member')
        horizontalLayout.addWidget(label)

        lineEdit = self.sample_widget.line_edit()
        horizontalLayout.addWidget(lineEdit)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(10)
        slider.setValue(1)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(1)
        horizontalLayout.addWidget(slider)


        return widget

    def recepieWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        splitter = self.sample_widget.splitter_def(parent_self=widget)
        splitter.setOrientation(Qt.Horizontal)
        horizontalLayout.addWidget(splitter)

        splitter.addWidget(self.recepieListWidget())
        splitter.addWidget(self.recpieDetailInfo())




        return widget

    def recepieListWidget(self):
        '''

        :return:
        '''
        val = 100
        widget = self.sample_widget.widget_def(min_size=(val, 0), max_size=(val, self.sample_widget.max_size))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setHeaderLabels(['Name', 'Origin'])
        verticalLayout.addWidget(treeWidget)



        return widget

    def recpieDetailInfo(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.recpieDetailMealMenuWidget())
        verticalLayout.addWidget(self.recpieDetailMealMenuDetailWidget())

        return widget

    def recpieDetailMealMenuWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        raidoButton = QRadioButton(widget)
        raidoButton.setText('RadioButton')
        horizontalLayout.addWidget(raidoButton)

        raidoButton_2 = QRadioButton(widget)
        raidoButton_2.setText('RadioButton')
        horizontalLayout.addWidget(raidoButton_2)

        return widget

    def recpieDetailMealMenuDetailWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        tabOne = self.sample_widget.tab_widget(parent_self=widget)
        horizontalLayout.addWidget(tabOne)

        tabOnePageOne = self.sample_widget.widget_def()
        tabOne.addTab(tabOnePageOne, 'Tab 1')

        tabOnePageTwo = self.sample_widget.widget_def()
        tabOne.addTab(tabOnePageTwo, 'Tab 2')

        tabTwo = self.sample_widget.tab_widget(parent_self=widget)
        horizontalLayout.addWidget(tabTwo)

        tabTwoPageOne = self.sample_widget.widget_def()
        tabTwo.addTab(tabTwoPageOne, 'Tab 1')

        tabTwoPageTwo = self.sample_widget.widget_def()
        tabTwo.addTab(tabTwoPageTwo, 'Tab 2')


        return widget









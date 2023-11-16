from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from data import help
import json
from collections import OrderedDict



class dishWidget(QWidget):
    def __init__(self):
        super(dishWidget, self).__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        self.dishDic = OrderedDict()


        self.help_class = help.Help()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #country widget
        verticalLayout.addWidget(self.countryWidget())

        #recpie widget
        verticalLayout.addWidget(self.dishWidget_())

        #list of the recpie widget
        verticalLayout.addWidget(self.dishTreeWidget_())

        #number of member widget
        verticalLayout.addWidget(self.number_of_memberWidget())

        #menu widget
        self.menuWidget_ = self.menuWidget()
        verticalLayout.addWidget(self.menuWidget_)

        #menu detail widget
        self.dishMainMenuWidget_ = self.dishMainMenuWidget()
        verticalLayout.addWidget(self.dishMainMenuWidget_)

        createMealButton = self.sample_widget.pushButton(set_text='Create Meal')
        verticalLayout.addWidget(createMealButton)



        return widget

    def countryWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        totalCountry = self.help_class.totalCountry()
        totalCountry.append('All')

        self.countryComboBox = self.sample_widget.comboBox(parent_self=widget, addItems=totalCountry)
        self.countryComboBox.setCurrentText('India')

        verticalLayout.addWidget(self.countryComboBox)


        return widget

    def dishWidget_(self):
        '''

        :return:
        '''
        val = 50
        widget = self.sample_widget.widget_def(min_size=[0, val], max_size=[self.sample_widget.max_size, val])
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        scrollArea.setWidgetResizable(True)

        containerWidget = self.sample_widget.widget_def()
        containerLayout = self.sample_widget.horizontal_layout(parent_self=containerWidget)
        scrollArea.setWidget(containerWidget)
        verticalLayout.addWidget(scrollArea)

        self.dishList = self.help_class.getDishList(self.countryComboBox.currentText())

        for each in self.dishList:
            checkbox = self.sample_widget.checkbox()
            checkbox.stateChanged.connect(lambda: self.dishListCheckBox(checkbox))
            checkbox.setText(each)
            containerLayout.addWidget(checkbox)
        return widget


    def dishTreeWidget_(self):
        '''

        :return:
        '''
        widegt = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widegt)

        self.dishTreeWidget = self.sample_widget.treeWidget(parent_self=widegt, setHeaderHidden=True)
        self.dishTreeWidget.selectionModel().selectionChanged.connect(self.dishTreeWidgetSelectionChanged)
        self.dishTreeWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        verticalLayout.addWidget(self.dishTreeWidget)

        return widegt

    def number_of_memberWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        label = self.sample_widget.label(set_text='Number of member')
        horizontalLayout.addWidget(label)

        lineedit = self.sample_widget.line_edit()
        horizontalLayout.addWidget(lineedit)

        horizontalSpacer = QSlider()
        horizontalSpacer.setOrientation(Qt.Horizontal)
        horizontalSpacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout.addWidget(horizontalSpacer)


        return widget


    def menuWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        self.test_horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        return widget


    def dishMainMenuWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)


        self.menuTabWidget_ = self.menuTabWidget_(widget)
        horizontalLayout.addWidget(self.menuTabWidget_)


        otherMenuTabWidget = self.menudetailTabWidget(widget)
        horizontalLayout.addWidget(otherMenuTabWidget)

        return widget


    def menudetailTabWidget(self, widget):
        '''

        :return:
        '''
        tabWidget = self.sample_widget.tab_widget(parent_self=widget)

        tabWidget.addTab(self.dishDetail(), 'Detail')

        self.mealSummery_ = self.mealSummery()
        tabWidget.addTab(self.mealSummery_, 'Summery')

        tabWidget.setCurrentIndex(1)

        return tabWidget


    def dishDetail(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)


        return widget

    def mealSummery(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        self.meal_summery_gridLayout = self.sample_widget.grid_layout(parent_self=widget)

        return widget


    def menuTabWidget_(self, widget):
        '''

        :return:
        '''
        tabWidget = self.sample_widget.tab_widget(parent_self=widget)
        return tabWidget

    def dishListCheckBox(self, checkbox):
        '''

        :param checkbox:
        :return:
        '''
        if checkbox.isChecked():
            country = self.countryComboBox.currentText()
            dish = checkbox.text()

            dishList = self.help_class.getListOfDish(country, dish)
            self.dishTreeWidget.clear()
            for each in dishList:
                item = QTreeWidgetItem(self.dishTreeWidget)
                item.setText(0, each['name'])
                item.setData(0, Qt.UserRole, json.dumps(each))

        else:
            self.dishTreeWidget.clear()

    def dishTreeWidgetSelectionChanged(self):
        '''

        :return:
        '''

        selectedItems = self.dishTreeWidget.selectedItems()
        tabWidget = self.menuTabWidget_
        tabWidget.clear()
        if selectedItems:
            item = selectedItems[0]
            #GET MENU DETAIL
            menuDetail = json.loads(item.data(0, Qt.UserRole))
            keyList = list(menuDetail['menu'].keys())
            self.remove_all_widgets_from_container(self.menuWidget_)

            self.dishDic = OrderedDict()

            self.dishDic['name'] = menuDetail['name']


            for each in keyList:
                checkbox = self.sample_widget.checkbox(set_text=each, set_checked=True)
                self.test_horizontalLayout.addWidget(checkbox)

                #ADD THE TAB MENU
                menuWidget = self.menuWidget__(menuDetail['menu'][each], menuname=each)
                tabWidget.addTab(menuWidget, each)

                for key, value in menuDetail['menu'].items():
                    self.dishDic[key] = OrderedDict()
                    self.dishDic[key]['name'] = menuDetail['menu'][key]['default']['name']
                    self.dishDic[key]['id'] = menuDetail['menu'][key]['default']['id']

            self.updateSummery()

    def menuWidget__(self, dicData, menuname):
        '''

        :param dicData:
        :return:
        '''


        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        treeWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        treeWidget.selectionModel().selectionChanged.connect(lambda : self.update_(treeWidget))
        verticalLayout.addWidget(treeWidget)

        default_item = QTreeWidgetItem(treeWidget)
        default_item.setText(0, 'Default')

        defaultItem_name = QTreeWidgetItem(default_item)
        defaultItem_name.setText(0, dicData['default']['name'])
        defaultItem_name.setSelected(True)
        defaultItem_name.setData(0, Qt.UserRole, json.dumps(dicData['default']))

        #variation
        variation_item = QTreeWidgetItem(treeWidget)
        variation_item.setText(0, 'variations')

        for key, value in dicData['variations'].items():
            variationItem_name = QTreeWidgetItem(variation_item)
            variationItem_name.setText(0, key)
            variationItem_name.setData(0, Qt.UserRole, json.dumps(dicData['variations'][key]))
            variationItem_name.setData(0, Qt.UserRole + 1, menuname)



        treeWidget.expandAll()
        return widget

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def remove_all_widgets_from_container(self, container):
        if container.layout() is not None:
            self.clear_layout(container.layout())

    def update_(self, treeWidget):
        for each in treeWidget.selectedItems():
            name = each.text(0)
            item = each.data(0, Qt.UserRole)
            menu = each.data(0, Qt.UserRole + 1)

            self.dishDic[menu] = OrderedDict()
            self.dishDic[menu]['name'] = str(name)
            self.dishDic[menu]['id'] = str(item)




        self.updateSummery()
    def updateSummery(self):
        '''

        :return:
        '''
        self.remove_all_widgets_from_container(self.mealSummery_)
        a = 0
        for each in self.dishDic:
            label = self.sample_widget.label(set_text=each)
            self.meal_summery_gridLayout.addWidget(label, a, 0)
            if type(self.dishDic[each]) == str:

                label = self.sample_widget.label(set_text=self.dishDic[each])
                self.meal_summery_gridLayout.addWidget(label, a, 1)

            elif type(self.dishDic[each]) == OrderedDict:
                label = self.sample_widget.label(set_text=self.dishDic[each]['name'])
                self.meal_summery_gridLayout.addWidget(label, a, 1)
            a += 1

        self.meal_summery_gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), a, 0, 1,
                                             2)
        print(self.dishDic)
        print(json.dumps(self.dishDic, indent=4))









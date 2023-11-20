from functools import partial

from ui_OldOne.import_module import *
from ui_OldOne.sampleWidget import sample_widget_template

from data import help
from data import get_meal_dishe

class midWidget_recepieWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.help = help.Help()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

        self.update_()

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

        listItem = self.help.totalCountry()
        comboBox = self.sample_widget.comboBox(parent_self=widget, addItems=listItem, setEditable=True)
        comboBox.setCurrentText('India')
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

        size_val = 130
        self.number_of_people_lineEdit = self.sample_widget.line_edit()
        self.number_of_people_lineEdit.setValidator(QIntValidator())
        self.number_of_people_lineEdit.setMinimumSize(QSize(size_val, 0))
        self.number_of_people_lineEdit.setMaximumSize(QSize(size_val, 16777215))
        self.number_of_people_lineEdit.setText('1')
        self.number_of_people_lineEdit.setDisabled(True)
        horizontalLayout.addWidget(self.number_of_people_lineEdit)

        self.number_of_people_slider = QSlider(Qt.Horizontal)
        self.number_of_people_slider.setMinimum(1)
        self.number_of_people_slider.setMaximum(10)
        self.number_of_people_slider.setValue(1)
        self.number_of_people_slider.setTickPosition(QSlider.TicksBelow)
        self.number_of_people_slider.setTickInterval(1)
        self.number_of_people_slider.valueChanged.connect(self.number_of_people_lineEdit_def)
        horizontalLayout.addWidget(self.number_of_people_slider)

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
        val = 300
        widget = self.sample_widget.widget_def(min_size=(val, 0), max_size=(val, self.sample_widget.max_size))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)


        self.recepie_treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        self.recepie_treeWidget.setHeaderLabels(['Name'])
        self.recepie_treeWidget.selectionModel().selectionChanged.connect(self.recepie_treeWidget_def)


        verticalLayout.addWidget(self.recepie_treeWidget)
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
        self.recepie_menu_horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        checbox = self.sample_widget.checkbox()
        self.recepie_menu_horizontalLayout.addWidget(checbox)

        return widget

    def recpieDetailMealMenuDetailWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        self.menuMainTab = self.sample_widget.tab_widget(parent_self=widget)
        horizontalLayout.addWidget(self.menuMainTab)

        self.detail_tab = self.sample_widget.tab_widget(parent_self=widget)
        horizontalLayout.addWidget(self.detail_tab)




        return widget


    def number_of_people_lineEdit_def(self):
        '''

        :param value:
        :return:
        '''
        value = self.number_of_people_slider.value()
        self.number_of_people_lineEdit.setText(str(value))

    def update_(self):
        #UPDATE THE TREEWIDGET
        self.update_TreeWidget()

    def update_TreeWidget(self):
        '''

        :return:
        '''
        self.recepie_treeWidget.clear()
        country = get_meal_dishe.getRecepieCountryList()
        mealtime = get_meal_dishe.getRecepieMealtimes()

        for eachCountry in country:
            item = QTreeWidgetItem(self.recepie_treeWidget)
            item.setText(0, eachCountry)

            for eachMealtime in mealtime:
                item_2 = QTreeWidgetItem(item)
                item_2.setText(0, eachMealtime)
                item_2.setData(0, Qt.UserRole, {'country': eachCountry, 'mealtime': eachMealtime})
                item.addChild(item_2)

                dic_data = get_meal_dishe.getListJsonFromCatagoryRecepie(eachMealtime, eachCountry)
                for each in dic_data[eachCountry][eachMealtime]:
                    item_3 = QTreeWidgetItem(item_2)
                    item_3.setText(0, each['name'])
                    item_3.setData(0, Qt.UserRole, each)
                    item_2.addChild(item_3)
        self.recepie_treeWidget.expandAll()

    def recpieDetailMealMenuWidget_update(self, data):
        self.help.clearLayout(self.recepie_menu_horizontalLayout)
        self.check_box_list = []
        for each in data['menu']:
            checbox = self.sample_widget.checkbox(set_text=each, set_checked=True)
            self.check_box_list.append(checbox)
            checbox.stateChanged.connect(partial(self.menuTabCheckboxUpdate, checbox, data))
            self.recepie_menu_horizontalLayout.addWidget(checbox)
        self.menuTabUpdate(data)

    def menuTabUpdate(self, data):
        '''

        :param data:
        :return:
        '''
        self.menuMainTab.clear()
        for each in data['menu']:
            self.menuMainTab.addTab(self.menutabUpdateWidget(data['menu'][each]), each)
    def menutabUpdateWidget(self, data):
        '''

        :param data:
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)
        treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        verticalLayout.addWidget(treeWidget)
        getAllMeal = get_meal_dishe.getAllMeal()
        for each in data:
            if each == 'default':
                meal = {}
                for eachmeal in getAllMeal:
                    if eachmeal['id'] == data[each]['id']:
                        meal = eachmeal
                default_item = QTreeWidgetItem(treeWidget)
                default_item.setText(0, each.upper())
                default_item.setFlags(default_item.flags() & ~Qt.ItemIsSelectable)
                treeWidget.addTopLevelItem(default_item)
                nameItem = QTreeWidgetItem(default_item)
                nameItem.setText(0, data[each]['name'])
                if meal:
                    nameItem.setIcon(0, QIcon(meal['images']['main']))
                default_item.addChild(nameItem)
                nameItem.setSelected(True)
            else:

                varient_item = QTreeWidgetItem(treeWidget)
                varient_item.setText(0, each.upper())
                varient_item.setFlags(varient_item.flags() & ~Qt.ItemIsSelectable)

                treeWidget.addTopLevelItem(varient_item)

                for eachVarient in data[each]:
                    meal = {}
                    for eachMeal in getAllMeal:
                        if data[each][eachVarient] == data[each][eachVarient]:
                            meal = eachMeal

                    eachVarient_item = QTreeWidgetItem(varient_item)
                    eachVarient_item.setText(0, eachVarient)

                    if meal:
                        eachVarient_item.setIcon(0, QIcon(meal['images']['main']))

                    varient_item.addChild(eachVarient_item)
        treeWidget.expandAll()


        return widget

    def menuTabCheckboxUpdate(self, checkbox, data):

        if checkbox.isChecked():

            self.menuMainTab.addTab(self.menutabUpdateWidget(data['menu'][checkbox.text()]), checkbox.text())
        else:

            for i in range(self.menuMainTab.count()):
                if self.menuMainTab.tabText(i) == checkbox.text():
                    self.menuMainTab.removeTab(i)
                    break

    def recepie_treeWidget_def(self):
        '''

        :return:
        '''
        item = self.recepie_treeWidget.currentItem()
        data = item.data(0, Qt.UserRole)
        self.recpieDetailMealMenuWidget_update(data)



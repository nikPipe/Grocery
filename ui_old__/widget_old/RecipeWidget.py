import json
from functools import partial

from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template


from ui_old__.widget_old import leftWidget
from data import get_meal_dishe
from data import help


class RecipeWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.leftWidget_ = leftWidget.lefWidget()
        self.meal_dishe = get_meal_dishe
        self.help = help.Help()

        self.getMealDic = self.meal_dishe.getDic()
        self.getAllMeal = self.meal_dishe.getAllMeal()

        verticalLayout = QVBoxLayout(self)
        widget = self.initUI()
        width = 800

        verticalLayout.addWidget(widget)
        self.update_()

    def initUI(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #COUNTRY COMOBBOX
        comboBox = self.sample_widget.comboBox(parent_self=widget, addItems=self.help.totalCountry())
        verticalLayout.addWidget(comboBox)

        verticalLayout.addWidget(self.numberOfPerson())

        verticalLayout.addWidget(self.recepieWidget())

        verticalLayout.addWidget(self.createmeal_def())

        return widget


    def numberOfPerson(self):
        '''

        :return:
        '''
        height = 30
        widget = self.sample_widget.widget_def(min_size=[0, height], max_size=[16777215, height])
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        #NUMBER ON MEMBER
        label = self.sample_widget.label(set_text='Number of Person', set_alighment=self.sample_widget.center_alignment)
        horizontalLayout.addWidget(label)

        #NUMBER ON MEMBER
        spinBox = QSpinBox(widget)
        spinBox.setMinimum(1)
        spinBox.setMaximum(100)
        horizontalLayout.addWidget(spinBox)

        return widget

    def recepieWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        split = self.sample_widget.splitter_def(parent_self=widget)
        split.setOrientation(Qt.Horizontal)
        verticalLayout.addWidget(split)

        split.addWidget(self.recepieTreeWidget())
        split.addWidget(self.recepieDetailWidget())

        split.setSizes([50, 200])

        return widget


    def createmeal_def(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def(min_size=[0, 50], max_size=[16777215, 50])
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        pyshButton = self.sample_widget.pushButton(set_text='Create Meal', connect=self.createMeal_def)
        verticalLayout.addWidget(pyshButton)

        return widget


    def createMeal_def(self):
        '''

        :return:
        '''
        print(json.dumps(self.recepieData, indent=4, sort_keys=True))

        mealName = {}
        for each in self.recepieData:
            mealName[each] = self.recepieData[each]['name']

        #print(json.dumps(mealName, indent=4, sort_keys=True))


        message = ''
        for each in mealName:
            message = message + each + ' : ' + mealName[each] + '\n'

        msg = self.sample_widget.displayMessage(setWindowTitle='Are you Sure', text=message)
        result = msg.exec_()

        if result == QMessageBox.Ok:
            print("User clicked OK")
        elif result == QMessageBox.Cancel:
            print("User clicked Cancel")







    def recepieTreeWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        self.recepie_treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        self.recepie_treeWidget.setHeaderLabels(["Title", "Summary"])
        self.recepie_treeWidget.setColumnCount(2)
        self.recepie_treeWidget.setColumnWidth(0, 300)
        self.recepie_treeWidget.selectionModel().selectionChanged.connect(self.recepie_treeWidget_def)
        verticalLayout.addWidget(self.recepie_treeWidget)

        return widget

    def recepieDetailWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        split = self.sample_widget.splitter_def(parent_self=widget)
        split.setOrientation(Qt.Horizontal)
        verticalLayout.addWidget(split)

        split.addWidget(self.recepieDetailMenuWidget())
        split.addWidget(self.recepieDetailMenuDetailWidget())
        split.setSizes([50, 200])

        return widget

    def recepieDetailMenuWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.menuCheckbox_def())

        self.recepie_menu_tabWidget = self.sample_widget.tab_widget(parent_self=widget)
        verticalLayout.addWidget(self.recepie_menu_tabWidget)


        return widget

    def recepieDetailMenuDetailWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        tabWidget = self.sample_widget.tab_widget(parent_self=widget)
        verticalLayout.addWidget(tabWidget)

        tabWidget.addTab(self.recepie_eachObjctDetailWidget(), 'OBject Detail')
        tabWidget.addTab(self.recepie_detail_widget(), 'Detail')

        tabWidget.setCurrentIndex(1)


        return widget


    def recepie_eachObjctDetailWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        return widget



    def recepie_detail_widget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        self.recepie_detail_widget_verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        self.recepie_detail_widget_treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        self.recepie_detail_widget_treeWidget.setHeaderLabels(["Image", "Name", 'mealType'])
        self.recepie_detail_widget_treeWidget.setColumnCount(3)
        self.recepie_detail_widget_treeWidget.setIconSize(QSize(300, 300))
        self.recepie_detail_widget_treeWidget.setColumnWidth(0, 300)
        self.recepie_detail_widget_verticalLayout.addWidget(self.recepie_detail_widget_treeWidget)

        return widget


    def menuCheckbox_def(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        self.menuCheckbox_horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        return widget

    def update_(self):
        '''

        :return:
        '''
        self.recepieData = {}


        #UPDATE THE RECEPIE TREE WIDGET
        self.updateRecepieTreeWidget()

    def updateRecepieTreeWidget(self):
        '''

        :return:
        '''
        self.recepie_treeWidget.clear()
        country = get_meal_dishe.getRecepieCountryList()
        mealtime = get_meal_dishe.getRecepieMealtimes()

        for eachCountry in country:
            countryItem = QTreeWidgetItem(self.recepie_treeWidget)
            countryItem.setText(0, eachCountry)
            font1 = QFont()
            font1.setPointSize(10)

            for eachMealtime in mealtime:
                mealtimeItem = QTreeWidgetItem(countryItem)
                mealtimeItem.setText(0, eachMealtime)
                font1 = QFont()
                font1.setPointSize(10)
                mealtimeItem.setFont(0, font1)

                data = get_meal_dishe.getListJsonFromCatagoryRecepie(eachMealtime, eachCountry)
                for each in data[eachCountry][eachMealtime]:
                    item = QTreeWidgetItem(mealtimeItem)
                    item.setText(0, each['name'])
                    item.setData(0, Qt.UserRole, each)
                    font1 = QFont()
                    font1.setPointSize(10)
                    item.setFont(0, font1)
                    mealtimeItem.addChild(item)

        self.recepie_treeWidget.expandAll()


    def recepie_treeWidget_def(self):
        item = self.recepie_treeWidget.currentItem()
        data = item.data(0, Qt.UserRole)
        if data is not None:
            self.recpieDetailMealMenuWidget_update(data)
        #SET THE DEFAULT DATA
        self.recepieData = {}
        for each in data['menu']:
            self.recepieData[each] = data['menu'][each]['default']




        self.update_recepieDetailWidget(self.recepieData)



    def recpieDetailMealMenuWidget_update(self, data):
        '''

        :param data:
        :return:
        '''
        #SET THE CHECKBOX
        self.help.clearLayout(self.menuCheckbox_horizontalLayout)
        for each_menu in data['menu']:
            checkBox = QCheckBox(each_menu)
            checkBox.setChecked(True)
            checkBox.stateChanged.connect(partial(self.menuTabCheckboxUpdate, checkBox, data))
            self.menuCheckbox_horizontalLayout.addWidget(checkBox)

            #SET THE TAB WIDGET

        self.menuTabUpdate(data)


    def menuTabUpdate(self, data):
        '''

        :param data:
        :return:
        '''
        self.recepie_menu_tabWidget.clear()
        for each in data['menu']:
            self.recepie_menu_tabWidget.addTab(self.detail_meny_tab_widget_def(data['menu'][each], each), each)


    def detail_meny_tab_widget_def(self, data, name):
        '''

        :param data:
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setHeaderLabels(["Image", 'Name'])
        treeWidget.setColumnCount(2)
        treeWidget.setIconSize(QSize(300, 300))
        treeWidget.selectionModel().selectionChanged.connect(partial(self.update_detail_menu_tab_widget_def, treeWidget, data, name))

        verticalLayout.addWidget(treeWidget)

        getAllMeal = get_meal_dishe.getAllMeal()
        val = 100
        for each in data:
            if each == 'default':
                meal = {}
                for eachmeal in getAllMeal:
                    if eachmeal['id'] == data[each]['id']:
                        meal = eachmeal

                default_item = QTreeWidgetItem(treeWidget)
                default_item.setText(0, each.upper())
                font1 = QFont()
                font1.setPointSize(10)  # Adjust the point size to increase the text size
                default_item.setFont(0, font1)

                nameItem = QTreeWidgetItem(default_item)
                nameItem.setText(1, data[each]['name'].upper())

                if meal:
                    path = meal['images']['main']
                    icon2 = QIcon(path)  # Replace with the path to your image
                    pixmap2 = icon2.pixmap(val, val)  # Create a larger pixmap (32x32) from the icon
                    nameItem.setIcon(0, QIcon(pixmap2))

                nameItem.setSelected(True)
            else:

                varient_item = QTreeWidgetItem(treeWidget)
                varient_item.setText(0, each.upper())
                varient_item.setFlags(varient_item.flags() & ~Qt.ItemIsSelectable)

                treeWidget.addTopLevelItem(varient_item)

                for eachVarient in data[each]:
                    meal = {}
                    for eachMeal in getAllMeal:
                        if data[each][eachVarient] == eachMeal['id']:
                            meal = eachMeal
                            break

                    eachVarient_item = QTreeWidgetItem(varient_item)
                    eachVarient_item.setText(1, eachVarient.upper())
                    if meal:
                        path = meal['images']['main']
                        icon2 = QIcon(path)  # Replace with the path to your image
                        pixmap2 = icon2.pixmap(val, val)  # Create a larger pixmap (32x32) from the icon
                        eachVarient_item.setIcon(0, QIcon(pixmap2))
                        # eachVarient_item.setIcon(0, QIcon(meal['images']['main']))
                    varient_item.addChild(eachVarient_item)
        treeWidget.setColumnWidth(0, 300)
        treeWidget.expandAll()
        return widget

    def update_detail_menu_tab_widget_def(self, treeWidget, data, name):
        text = treeWidget.selectedItems()[0].text(1)

        for each in data:
            if each == 'default':
                if text.lower() == data[each]['name'].lower():
                    self.recepieData[name] = data[each]
            else:
                for eachVarient in data[each]:
                    if text.lower() == eachVarient.lower():
                        id = data[each][eachVarient]
                        name_ = eachVarient
                        a = {}
                        a['id'] = id
                        a['name'] = name_
                        self.recepieData[name] = a

        self.update_recepieDetailWidget(self.recepieData)
    def menuTabCheckboxUpdate(self, checkbox, data):

        if checkbox.isChecked():

            self.recepie_menu_tabWidget.addTab(self.detail_meny_tab_widget_def(data['menu'][checkbox.text()]), checkbox.text())
            self.recepieData[checkbox.text()] = data['menu'][checkbox.text()]['default']

        else:
            for i in range(self.recepie_menu_tabWidget.count()):
                if self.recepie_menu_tabWidget.tabText(i) == checkbox.text():
                    self.recepie_menu_tabWidget.removeTab(i)
                    break

            del self.recepieData[checkbox.text()]

    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def update_recepieDetailWidget(self, data):
        '''

        :param data:
        :return:
        '''

        self.recepie_detail_widget_treeWidget.clear()
        val = 200
        for each in data:
            item = QTreeWidgetItem(self.recepie_detail_widget_treeWidget)
            item.setText(1, data[each]['name'].upper())
            item.setText(2, each.upper())
            item.setData(0, Qt.UserRole, data[each])
            font1 = QFont()
            font1.setPointSize(10)
            item.setFont(0, font1)
            for each_dic in self.getAllMeal:
                if each_dic['id'] == data[each]['id']:
                    path = each_dic['images']['main']
                    icon2 = QIcon(path)
                    pixmap2 = icon2.pixmap(val, val)  # Create a larger pixmap (32x32) from the icon
                    item.setIcon(0, QIcon(pixmap2))

                    self.recepieData[each]['data'] = each_dic
            self.recepie_detail_widget_treeWidget.addTopLevelItem(item)

    def initUI_(self):
        '''


        :return:
        '''

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setHeaderLabels(["Title", "Summary"])
        treeWidget.setColumnCount(2)
        treeWidget.setSortingEnabled(True)
        verticalLayout.addWidget(treeWidget)
        treeWidget.setIconSize(QSize(300, 300))


        path = "C:/Users/Admin/Desktop/Nikheel/GroceryMain/Grocery/meal/india/Baingan_Bharta_Recipe.png"
        path = "C:/Users/Admin/Desktop/Nikheel/GroceryMain/Grocery/meal/india/Aloo_Mangodi_Recipe.jpg"

        item2 = QTreeWidgetItem(treeWidget)
        item2.setText(0, "Item 2")
        font1 = QFont()
        font1.setPointSize(16)  # Adjust the point size to increase the text size
        item2.setFont(0, font1)

        icon2 = QIcon(path)  # Replace with the path to your image
        pixmap2 = icon2.pixmap(1000, 1000)  # Create a larger pixmap (32x32) from the icon
        item2.setIcon(0, QIcon(pixmap2))

        return widget






















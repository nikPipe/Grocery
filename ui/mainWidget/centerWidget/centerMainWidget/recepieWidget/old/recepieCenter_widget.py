import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os, traceback
file =  os.path.dirname(os.path.realpath(ui.__file__))
from data import get_meal_dishe

from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget.old import recepieDetail_widget


class recepieCenter_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.recepieDict = {}
        self.recepieDetail_widget = recepieDetail_widget.recepieDetail_widget(self.parent)

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)
        self.sampleObjectNmae = 'labelStyleSheet'
        self.labelStyleSheet = self.sample_widget.styleSheet_def(obj_name=self.sampleObjectNmae,
                                                                 color=self.color_class.white_color.get_value())

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        '''
        :return:
        '''
        height = 1000
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        spitter = self.sample_widget.splitter_def(parent_self=widget)
        spitter.setOrientation(Qt.Horizontal)
        verticalLayout.addWidget(spitter)

        spitter.addWidget(self.recepieTreeWidget())
        spitter.addWidget(self.recepieDetail_widget)

        verticalLayout.addWidget(self.addToCalaender())

        return widget

    def addToCalaender(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        pushButton = self.sample_widget.pushButton(parent_self=widget, set_text='Add to Calender', connect=self.addTocalender_def)
        verticalLayout.addWidget(pushButton)

        return widget

    def addTocalender_def(self):
        '''

        :return:
        '''
        selected = self.recepieTreeWidget_treeWidget.selectedItems()
        dic_val = {}
        if selected:
            item = selected[0]
            data = item.data(0, Qt.UserRole)

            if data:
                horizontalLayout = self.recepieDetail_widget.recepie_mainWidget_horizontalLayout
                tabWidget = self.recepieDetail_widget.recepieDetailTabWidget

                for i in reversed(range(horizontalLayout.count())):
                    widget = horizontalLayout.itemAt(i).widget()
                    children = widget.findChildren(QCheckBox)
                    for each in children:
                        for eachTab in range(tabWidget.count()):
                            dic_val[each.text()] = {}
                            if tabWidget.tabText(eachTab) == each.text():
                                widget = tabWidget.widget(eachTab)
                                treeWidget = widget.findChild(QTreeWidget)
                                selected = treeWidget.selectedItems()
                                if selected:
                                    item = selected[0]
                                    data = item.data(1, Qt.UserRole)
                                    if data:
                                        dic_val[each.text()] = data
                                        break

        print(json.dumps(dic_val, indent=4))

    def recepieTreeWidget(self):
        '''
        Recepie Tree Widget
        :return:
        '''

        widget = self.sample_widget.widget_def()
        widget.setFixedWidth(300)

        country = get_meal_dishe.getRecepieCountryList()
        mealtime = get_meal_dishe.getRecepieMealtimes()


        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        treeWidget_objName = 'treeWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=treeWidget_objName, color=self.color_class.white_color.get_value(),
                                                        background=self.color_class.black_color.get_value(),
                                                        border_radius=5)
        self.recepieTreeWidget_treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        self.recepieTreeWidget_treeWidget.setObjectName(treeWidget_objName)
        self.recepieTreeWidget_treeWidget.setStyleSheet(styleSheet_)
        self.recepieTreeWidget_treeWidget.selectionModel().selectionChanged.connect(partial(self.recepieTreeWidget_treeWidget_def, self.recepieTreeWidget_treeWidget))
        verticalLayout.addWidget(self.recepieTreeWidget_treeWidget)

        for eachCountry in country:
            countryItem = QTreeWidgetItem(self.recepieTreeWidget_treeWidget)
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

        self.recepieTreeWidget_treeWidget.expandAll()

        return widget

    def recepieTreeWidget_treeWidget_def(self, treeWidget):
        '''
        Recepie Tree Widget
        :return:
        '''
        selected = treeWidget.selectedItems()

        if selected:
            try:
                item = selected[0]
                data = item.data(0, Qt.UserRole)
                if data:
                    horizontalLayout = self.recepieDetail_widget.recepie_mainWidget_horizontalLayout
                    tabWidget = self.recepieDetail_widget.recepieDetailTabWidget
                    self.help_class.clearLayout(horizontalLayout)
                    tabWidget.clear()

                    #GET THE MENU
                    for eachMenu in data['menu']:
                        recepie_mainWidget_widget = self.recepieDetail_widget.recepie_mainWidget_widget(
                            data['menu'][eachMenu], eachMenu)
                        horizontalLayout.addWidget(recepie_mainWidget_widget)

                        widget_dic = {}

                        tabWidget_widget = self.recepieDetail_widget.tabMainWidget(data=data['menu'][eachMenu])
                        tabWidget.addTab(tabWidget_widget, eachMenu)

                        checkbox = recepie_mainWidget_widget.findChild(QCheckBox)
                        button = recepie_mainWidget_widget.findChild(QPushButton)


                        tabTreeWidget = tabWidget_widget.findChild(QTreeWidget)
                        tabTreeWidget.selectionModel().selectionChanged.connect(partial(self.treeWidget_def, tabWidget, recepie_mainWidget_widget))

                        widget_dic[eachMenu] = {'checkbox': checkbox, 'button': button, 'tabWidget': tabWidget_widget}
                        checkbox.stateChanged.connect(partial(self.recepieCheckboxUpdate, widget_dic, eachMenu, tabWidget))
            except Exception as e:
                traceback.print_exc()



        '''
            try:

                item = selected[0]
                data = item.data(0, Qt.UserRole)
                if data:
                    horizontalLayout = self.recepieDetail_widget.recepie_mainWidget_horizontalLayout
                    tabWidget = self.recepieDetail_widget.recepieDetailTabWidget
                    #recepie_mainWidget_widget = self.recepieDetail_widget.recepie_mainWidget_widget(data)
                    self.help_class.clearLayout(horizontalLayout)
                    tabWidget.clear()

                    widget_dic = {}


                    for each_menu in data['menu']:
                        recepie_mainWidget_widget = self.recepieDetail_widget.recepie_mainWidget_widget(data['menu'][each_menu], each_menu)
                        horizontalLayout.addWidget(recepie_mainWidget_widget)

                        tabWidget_widget = self.recepieDetail_widget.tabMainWidget(data=data['menu'][each_menu])
                        tabWidget.addTab(tabWidget_widget, each_menu)

                        checkbox = recepie_mainWidget_widget.findChild(QCheckBox)
                        button = recepie_mainWidget_widget.findChild(QPushButton)
                        treeWidget_ = tabWidget_widget.findChild(QTreeWidget)
                        treeWidget_.selectionModel().selectionChanged.connect(partial(self.treeWidget_def, treeWidget_, button))
                        #print(treeWidget_)

                        widget_dic[each_menu] = {'checkbox': checkbox, 'button': button, 'tabWidget': tabWidget_widget}
                        checkbox.stateChanged.connect(partial(self.recepieCheckboxUpdate, widget_dic, each_menu, tabWidget))
            except Exception as e:
                traceback.print_exc()
            '''
        '''
        print('treeWidget_def')
        allMeal = get_meal_dishe.getAllMeal()


        selected = treeWidget.selectedItems()
        if selected:
            item = selected[0]
            data = item.data(0, Qt.UserRole)
            if data:
                recepieDetailMenu_treeWidget = self.recepieDetail_widget.recepieDetailMenu_widget.recepieDetailMenu_treeWidget
                recepieDetailMenu_treeWidget.clear()
                recepieDetailMenu_treeWidget.setColumnCount(3)
                recepieDetailMenu_treeWidget.setIconSize(QSize(300, 300))
                for eachMenu in data['menu']:
                    treeWidgetItem = QTreeWidgetItem(recepieDetailMenu_treeWidget)
                    treeWidgetItem.setText(0, eachMenu)
                    treeWidgetItem.setCheckState(0, Qt.Checked)
                    recepieDetailMenu_treeWidget.addTopLevelItem(treeWidgetItem)
                    for eachChild in data['menu'][eachMenu]:
                        if eachChild == 'default':
                            defaultItem = QTreeWidgetItem(treeWidgetItem)
                            defaultItem.setText(1, 'Default')
                            treeWidgetItem.addChild(defaultItem)

                            treeWidgetItemChild = QTreeWidgetItem(treeWidgetItem)
                            treeWidgetItemChild.setText(2, data['menu'][eachMenu]['default']['name'])
                            id = data['menu'][eachMenu]['default']['id']
                            for each in allMeal:
                                if each['id'] == id:
                                    treeWidgetItemChild.setData(0, Qt.UserRole, each)
                                    icon = QIcon()
                                    icon.addPixmap(QPixmap(each['images']['main']), QIcon.Normal, QIcon.Off)

                                    treeWidgetItemChild.setIcon(2, icon)




                                    break

                            defaultItem.addChild(treeWidgetItemChild)

                        else:
                            defaultItem = QTreeWidgetItem(treeWidgetItem)
                            defaultItem.setText(1, 'Variation')
                            treeWidgetItem.addChild(defaultItem)

                            for each_variation in data['menu'][eachMenu][eachChild]:
                                item = QTreeWidgetItem(defaultItem)
                                item.setText(2, each_variation)
                                id = data['menu'][eachMenu][eachChild][each_variation]
                                for each in allMeal:
                                    if each['id'] == id:
                                        item.setData(0, Qt.UserRole, each)
                                        break

                                defaultItem.addChild(item)
                recepieDetailMenu_treeWidget.expandAll()
            #self.recepieDetail_widget.updateUI(data)
            '''


    def recepieCheckboxUpdate(self, dic_val, each_menu, tabWidget):

        '''

        :return:
        '''

        checkbox = dic_val[each_menu]['checkbox']
        tabWidget_ = dic_val[each_menu]['tabWidget']
        button = dic_val[each_menu]['button']
        if checkbox.isChecked():
            tabWidget.addTab(tabWidget_, each_menu)
        else:
            tabWidget.removeTab(tabWidget.indexOf(tabWidget_))


    def treeWidget_def(self, tabWidget, widget):
        '''

        :param treeWidget:
        :return:
        '''
        try:

            horizontalLayout = self.recepieDetail_widget.recepie_mainWidget_horizontalLayout
            #CLEAR LAYOut
            self.help_class.clearLayout(horizontalLayout)



            tabTreeWidget = tabWidget.findChildren(QTreeWidget)
            print(tabTreeWidget)

            for index in range(tabWidget.count()):
                tabName = tabWidget.tabText(index)
                checkbox = self.sample_widget.checkbox(set_text=tabName)

                print(tabName)
                tab_widget = tabWidget.widget(index)
                if tab_widget is not None:
                    treeWidget = tab_widget.findChildren(QTreeWidget)
                    if treeWidget:
                        treeWidget = treeWidget[0]
                        data = treeWidget.selectedItems()
                        if data:
                            item = data[0]
                            data = item.data(1, Qt.UserRole)
                            if data:
                                print(data)
                                recepie_mainWidget_widget = self.recepieDetail_widget.recepie_mainWidget_widget(data, tabName)
                                horizontalLayout.addWidget(recepie_mainWidget_widget)





                '''
                
                
                tab_widget = tabWidget.widget(index)
                if tab_widget is not None:
                    # Check if the tab content contains a QTreeWidget
                    for child_widget in tab_widget.findChildren(QTreeWidget):
                        # Access and manipulate the QTreeWidget here
                        print(f"Found and accessed QTreeWidget in Tab {index + 1}")
                '''
            '''


            if selectedItems:
                item = selectedItems[0]
                data = item.data(1, Qt.UserRole)

                if data:
                    icon = data['images']['main']
                    #button.clicked.connect(partial(self.parent.addTOdetailMeal, data))
                    if icon != '':
                        if button:
                            button.setIcon(QIcon(icon))
                            
            '''

        except Exception as e:
            traceback.print_exc()

















import json
from collections import OrderedDict
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os, traceback

file = os.path.dirname(os.path.realpath(ui.__file__))
from data import get_meal_dishe
from ui.mainWidget.centerWidget.centerMainWidget import popup_calender

from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget.old import recepieDetail_widget


class recepieRightMenuDetail_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        self.tabTreeWidgetList = []
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
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        self.tabWidget = self.sample_widget.tab_widget(parent_self=widget)
        verticalLayout.addWidget(self.tabWidget)

        button_object = 'button_objcet'
        button_styleSheet = self.sample_widget.styleSheet_def(obj_name=button_object,
                                                                color=self.color_class.white_color.get_value(),
                                                                background=self.color_class.black_color.get_value(),
                                                                border_radius=2)
        button = self.sample_widget.pushButton(set_text='Add to Calender', set_object_name=button_object, set_styleSheet=button_styleSheet,
                                               min_size=(0, 30), max_size=(self.sample_widget.max_size, 30),
                                               connect=self.update_recepie_def)
        verticalLayout.addWidget(button)

        return widget


    def update_recepie_def(self):
        '''

        :return:
        '''
        for eachTab in self.tabTreeWidgetList:
            findTreeWidget = self.tabTreeWidgetList[eachTab].findChildren(QTreeWidget)
            if findTreeWidget:
                treeWidget = findTreeWidget[0]
                selectedItem = treeWidget.selectedItems()
                if selectedItem:
                    item__ = selectedItem[0]
                    id = item__.text(1)
                    print(id)

        print('\n')


    def treeWidget_(self, data):
        '''

        :return:
        '''

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        treeWidget_objName = 'treeWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=treeWidget_objName,
                                                        color=self.color_class.white_color.get_value(),
                                                        background=self.color_class.black_color.get_value(),
                                                        border_radius=5)
        treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        treeWidget.setHeaderLabels(['Name'])
        treeWidget.selectionModel().selectionChanged.connect(partial(self.treeWidget_def, treeWidget))


        verticalLayout.addWidget(treeWidget)

        getAllMeal = self.parent.getAllMeal

        dafaultItem = QTreeWidgetItem(treeWidget)
        dafaultItem.setText(0, 'Default')
        id = data['default']['id']
        for eachMeal in getAllMeal:
            if eachMeal['id'].lower() == id.lower():
                dafaultItem.setData(0, Qt.UserRole, eachMeal)
                break
        treeWidget.addTopLevelItem(dafaultItem)

        defaultChild = QTreeWidgetItem(dafaultItem)
        defaultChild.setText(0, data['default']['name'])
        defaultChild.setText(1, data['default']['id'])
        defaultChild.setSelected(True)

        #VARIATION
        variationItem = QTreeWidgetItem(treeWidget)
        variationItem.setText(0, 'Variations')
        treeWidget.addTopLevelItem(variationItem)

        for each in data['variations']:
            item = QTreeWidgetItem(variationItem)
            for eachMeal in getAllMeal:
                if eachMeal['id'].lower() == data['variations'][each].lower():
                    item.setText(1, data['variations'][each])

                    item.setData(0, Qt.UserRole, eachMeal)
                    item.setText(2, str(eachMeal))
                    break
            item.setText(0, each)
        treeWidget.expandAll()
        return widget

    def tabWidget_update(self, data):
        '''

        :return:
        '''
        self.tabWidget.clear()
        self.tabTreeWidgetList = {}
        for each in data['menu']:
            widget = self.treeWidget_(data['menu'][each])
            self.tabWidget.addTab(widget, each)
            self.tabTreeWidgetList[each] = widget


    def treeWidget_def(self, treeWidget):
        '''

        :param treeWidget:
        :return:
        '''

        item = treeWidget.selectedItems()
        if item:
            data = item[0].data(0, Qt.UserRole)
            recepieRightMenu_widget = self.parent.mainCenterWidget.centerMainWidget.recepieMainWidget.recepieCenter_widget.recepieRightMenu_widget
            recepieRightMenu_horizontalLayour = recepieRightMenu_widget.recepieRightMenu_horizontalLayour
            self.help_class.clearLayout(recepieRightMenu_horizontalLayour)
            try:
                for eachTab in self.tabTreeWidgetList:
                    findTreeWidget = self.tabTreeWidgetList[eachTab].findChildren(QTreeWidget)
                    if findTreeWidget:
                        treeWidget = findTreeWidget[0]
                        selectedItem = treeWidget.selectedItems()
                        if selectedItem:
                            item__ = selectedItem[0]
                            id = item__.text(1)

                            for eachMeal in self.parent.getAllMeal:
                                if id.lower() == eachMeal['id'].lower():
                                    widget = recepieRightMenu_widget.update_widget(menuName=eachTab,
                                                                                   data=eachMeal)
                                    recepieRightMenu_horizontalLayour.addWidget(widget)
            except:
                import traceback
                traceback.print_exc()



















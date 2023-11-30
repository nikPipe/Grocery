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

class recepieTree_widget(QWidget):
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
        widget = self.sample_widget.widget_def()
        widget.setFixedWidth(300)

        country = get_meal_dishe.getRecepieCountryList()
        mealtime = get_meal_dishe.getRecepieMealtimes()

        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        treeWidget_objName = 'treeWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=treeWidget_objName,
                                                        color=self.color_class.white_color.get_value(),
                                                        background=self.color_class.black_color.get_value(),
                                                        border_radius=5)
        self.recepieTreeWidget_treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        self.recepieTreeWidget_treeWidget.setObjectName(treeWidget_objName)
        self.recepieTreeWidget_treeWidget.setStyleSheet(styleSheet_)
        self.recepieTreeWidget_treeWidget.selectionModel().selectionChanged.connect(
            partial(self.recepieTreeWidget_treeWidget_def, self.recepieTreeWidget_treeWidget))
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

        :param treeWidget:
        :return:
        '''
        selectedItem = treeWidget.selectedItems()
        if selectedItem:
            item__ = selectedItem[0]
            data = item__.data(0, Qt.UserRole)
            if data:

                recepieRightMenu_widget = self.parent.mainCenterWidget.centerMainWidget.recepieMainWidget.recepieCenter_widget.recepieRightMenu_widget
                recepieRightMenu_horizontalLayour = recepieRightMenu_widget.recepieRightMenu_horizontalLayour

                recepieRightMenu_DetailWidget = self.parent.mainCenterWidget.centerMainWidget.recepieMainWidget.recepieCenter_widget.recepieRightMenuDetail_widget

                self.help_class.clearLayout(recepieRightMenu_horizontalLayour)
                for eachMenu in data['menu']:
                    id = data['menu'][eachMenu]['default']['id']
                    try:
                        for eachMeal in self.parent.getAllMeal:
                            if id.lower() == eachMeal['id'].lower():
                                meal_data = eachMeal
                                widget = recepieRightMenu_widget.update_widget(menuName=eachMenu, data=meal_data)
                                recepieRightMenu_horizontalLayour.addWidget(widget)
                    except:
                        import traceback
                        traceback.print_exc()

                    recepieRightMenu_DetailWidget.tabWidget_update(data=data)

                #recepieRightMenu_widget.update_widget(menuName=eachMenu, data=data)
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from data import get_meal_dishe

from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget import recepieDetailMenu_widget
from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget import recepieDetailMenuDetail_widget

from ui import commonButtonWidget
class recepieDetail_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.allMeal = get_meal_dishe.getAllMeal()

        self.recepieDetailMenu_widget = recepieDetailMenu_widget.recepieDetailMenu_widget(self.parent)
        self.recepieDetailMenuDetail_widget = recepieDetailMenuDetail_widget.recepieDetailMenuDetail_widget(self.parent)

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
        widget = self.sample_widget.widget_def(min_size=(0, height), max_size=(16777215, height))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        spitter = self.sample_widget.splitter_def(parent_self=widget)
        spitter.setOrientation(Qt.Vertical)
        horizontalLayout.addWidget(spitter)

        spitter.addWidget(self.recepie_mainWidget())
        spitter.addWidget(self.recepieDetailWidget())

        return widget

    def recepie_mainWidget(self):
        '''
        Recepie Tree Widget
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        scrollArea.setWidgetResizable(True)
        verticalLayout.addWidget(scrollArea)

        self.recepie_mainWidget_horizontalLayout = self.sample_widget.horizontal_layout(parent_self=scrollArea,
                                                                                        set_spacing=10)
        return widget


    def recepie_mainWidget_widget(self, data, eachMenu):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        checkbox = self.sample_widget.checkbox(set_text=eachMenu, set_checked=True)
        verticalLayout.addWidget(checkbox)


        dic_data = {}
        for each in self.allMeal:
            if data['default']['id'] == each['id']:
                dic_data = each


        try:
            if dic_data:
                widget_ = commonButtonWidget.commonWidget(dic_data)
                widget_.findChild(QPushButton).clicked.connect(partial(self.pushClick, dic_data))
                verticalLayout.addWidget(widget_)
        except:
            import traceback
            traceback.print_exc()

        '''
        
        val = 200
        image = ''
        for each in self.allMeal:
            if data['default']['id'] == each['id']:
                image = each['images']['main']

        object_name = eachMenu + '_object'
        width = 250
        height = 150
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object_name,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        pushButton = self.sample_widget.pushButton(set_text='', min_size=(width, height),
                                                   max_size=(width, height), set_object_name=object_name,
                                                   set_styleSheet=styleSheet, set_icon=image, set_icon_size=(width, height))
        verticalLayout.addWidget(pushButton)
        '''
        return widget

    def recepieDetailWidget(self):
        '''

        :return:
        '''
        height = 800
        widget = self.sample_widget.widget_def(min_size=(0, height), max_size=(16777215, height))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        self.recepieDetailTabWidget = self.sample_widget.tab_widget(parent_self=widget)
        verticalLayout.addWidget(self.recepieDetailTabWidget)

        return widget


    def tabMainWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        treeWidget.setColumnCount(2)
        verticalLayout.addWidget(treeWidget)

        #DEFAULT ITEM
        defaultItem = QTreeWidgetItem(treeWidget)
        defaultItem.setText(0, 'Default')

        treeWidgetData = {}
        for each in self.allMeal:
            if data['default']['id'] == each['id']:
                treeWidgetData = each
        item = QTreeWidgetItem(defaultItem)

        item.setText(1, data['default']['name'])
        item.setData(1, Qt.UserRole, treeWidgetData)
        item.setSelected(True)

        #VARIATION ITEM
        variationItem = QTreeWidgetItem(treeWidget)
        variationItem.setText(0, 'Variation')
        for each in data['variations']:
            item = QTreeWidgetItem(variationItem)
            treeWidgetData = {}
            for eachMeal in self.allMeal:
                if data['variations'][each].lower() == eachMeal['id'].lower():
                    treeWidgetData = eachMeal
                    break
            item.setText(1, each)
            item.setData(1, Qt.UserRole, treeWidgetData)
        treeWidget.expandAll()
        return widget


    def pushClick(self, data):
        print('pushClick')
        self.parent.mainCenterWidget.centerMainWidget.stackedWidget.setCurrentIndex(1)
        self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.stakeWidget.setCurrentIndex(1)

        self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.mealMain_widget.mealbutton_def(data)



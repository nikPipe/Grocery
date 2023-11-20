from ui_old.import_module import *
from ui_old.sampleWidget import sample_widget_template
import json
from data import get_meal_dishe
from meal import mealCleanup


class mealWidget(QWidget):
    def __init__(self):
        super(mealWidget, self).__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.meal_dishe = get_meal_dishe
        self.meal_cleanup = mealCleanup


        verticalLayout = QVBoxLayout(self)
        widget = self.initUI()
        verticalLayout.addWidget(widget)
        self.update_()

    def initUI(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #FILTER MEAL
        filter_meal_lineEdit = self.sample_widget.line_edit(set_PlaceholderText='Filter your meal')
        verticalLayout.addWidget(filter_meal_lineEdit)

        self.meal_treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        self.meal_treeWidget.setHeaderLabels(['Name', 'Origin'])
        verticalLayout.addWidget(self.meal_treeWidget)

        return widget

    def update_(self):
        '''

        :return:
        '''
        allMeal = self.meal_dishe.getAllMeal()
        for each in allMeal:
            print(each)
            mealClass = self.meal_cleanup.mealClass(each)


            item = QTreeWidgetItem(self.meal_treeWidget)
            item.setText(0, mealClass.name)
            item.setText(1, each['origin'])

            item.setData(0, Qt.UserRole, each)
            self.meal_treeWidget.addTopLevelItem(item)






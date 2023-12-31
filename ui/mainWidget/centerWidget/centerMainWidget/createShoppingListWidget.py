import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from data import mealClass


class createShoppingList(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.data = data


        self.setWindowTitle('Shopping List')
        self.setModal(True)  # Set the dialog as modal
        self.setMinimumSize(500, 500)

        layout = QVBoxLayout(self)
        layout.addWidget(self.initUI())


    def initUI(self):
        '''

        :return:
        '''
        widget  = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        label = self.sample_widget.label(set_text='Do you want to create shopping list for this selected Meal?')
        verticalLayout.addWidget(label)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setHeaderLabels(['Name', 'No Of People'])
        treeWidget.setColumnWidth(0, 200)
        verticalLayout.addWidget(treeWidget)

        readJson = self.help_class.getTempJsonFile()
        noOfPeople = readJson['noOfPeople']


        for each in self.data:
            item = QTreeWidgetItem(treeWidget)
            item.setText(0, each)
            item.setText(1, str(noOfPeople))
            item.setCheckState(0, Qt.Checked)
            item.setFlags(item.flags() | Qt.ItemIsEditable)

            treeWidget.addTopLevelItem(item)

        pushBUtton = self.sample_widget.pushButton(set_text='Create Shopping List Selected Item', connect=partial(self.createShoppingList, treeWidget))
        verticalLayout.addWidget(pushBUtton)

        return widget

    def createShoppingList(self, treeWidget):
        '''

        :return:
        '''
        try:
            getAllMeal = self.parent.parent.mainWidget.getAllMeal
            itemDic = {}
            ingredientList = {}

            # Iterate through the items and check if they are checked
            for row in range(treeWidget.topLevelItemCount()):
                item = treeWidget.topLevelItem(row)
                if item.checkState(0) == Qt.Checked:
                    for eachMeal in getAllMeal:
                        eachMeal = getAllMeal[eachMeal]
                        if eachMeal['id'].lower() == item.text(0).lower():
                            meal_class = mealClass.mealClass(json=eachMeal)

                            for eachItem in eachMeal['ingredients']:
                                item = eachItem['item']
                                if item not in ingredientList:
                                    ingredientList[item] = eachItem
                                    ingredientList[item]['recepie'] = [meal_class.name]
                                else:
                                    try:
                                        if not ingredientList[item]['weight']['value'] == 'Variable':
                                            ingredientList[item]['weight']['value'] =  str(float(ingredientList[item]['weight']['value']) + float(ingredientList[item]['weight']['value']))
                                            ingredientList[item]['recepie'].append(meal_class.name)
                                    except:
                                        import traceback
                                        traceback.print_exc()
                            break

            print('thi sis itemDic: ', ingredientList)
            for each in ingredientList:
                print(each)
                #print(ingredientList[each]['recepie'])

            self.close()
        except Exception as e:
            import traceback
            traceback.print_exc()













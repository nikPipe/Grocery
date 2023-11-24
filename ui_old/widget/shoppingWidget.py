from ui_old.import_module import *
from ui_old.sampleWidget import sample_widget_template
import json



class shoppingWidget(QWidget):
    def __init__(self):
        super(shoppingWidget, self).__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        verticalLayout = QVBoxLayout(self)


        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #SHOPPING LIST LABEL
        shopping_list_label = self.sample_widget.label(set_text='Shopping List', set_alighment=self.sample_widget.center_alignment)
        verticalLayout.addWidget(shopping_list_label)

        #SHOPPING filter widget_old
        verticalLayout.addWidget(self.shoppingFilter_def())

        #SHOPPING TREEWIDGET
        verticalLayout.addWidget(self.shoppingListTreeWidget())

        return widget


    def shoppingFilter_def(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        #ADD TOE SHOPPING LIST BUTTON
        add_to_shopping_list_button = self.sample_widget.pushButton(set_text='Add to shopping list')
        horizontalLayout.addWidget(add_to_shopping_list_button)

        horizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        #CATAEGORY BUTTON
        category_button = self.sample_widget.pushButton(set_text='Category')
        horizontalLayout.addWidget(category_button)

        #DISH BUTTON
        dish_button = self.sample_widget.pushButton(set_text='Dish')
        horizontalLayout.addWidget(dish_button)


        return widget



    def shoppingListTreeWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #TREEWIDGET
        self.shopping_treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        verticalLayout.addWidget(self.shopping_treeWidget)

        return widget



















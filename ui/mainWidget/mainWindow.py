

import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
from ui.mainWidget.topWidget import topWidgetMain
from ui.mainWidget.centerWidget import mainCenterWidget
from ui.mainWidget.centerWidget.centerMainWidget import popup_detailMeal
from ui.mainWidget.centerWidget.centerMainWidget import popup_calender

from data import get_meal_dishe

class mainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.color_variable = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.getAllMeal = get_meal_dishe.getAllMeal()
        self.mainCenterWidget = mainCenterWidget.centerMainWidget(self)
        self.topWidgetMain = topWidgetMain.topMainWidget(self)



        self.get_meal_dishe = get_meal_dishe
        self.popup_detailMeal = popup_detailMeal
        self.popup_calender = popup_calender

        self.initUI()

    def initUI(self):
        # Set window size.
        self.resize(1500, 800)

        # Set window title
        self.setWindowTitle('Meal Planner Window')

        widget = self.uiWidget()
        self.setCentralWidget(widget)

        # Show window
        self.show()


    def uiWidget(self):
        '''
        :return: QWidget
        '''
        # Create widget
        select_all_object = 'mainWidget'
        color = self.color_variable.setColorVal(r=36, g=36, b=36)
        select_all_styleSheet = self.sample_widget.styleSheet_def(obj_name=select_all_object,
                                                                  background_color=color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=select_all_object, set_styleSheet=select_all_styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #TOP WIDGET
        verticalLayout.addWidget(self.topWidgetMain)

        #CENTER WIDGET
        verticalLayout.addWidget(self.mainCenterWidget)

        return widget

    def addToCalender(self, data):
        try:

            popup = self.popup_calender.AddToCalender(self, data)
            result = popup.exec_()
            if result == QDialog.Accepted:
                print('Accepted')
            else:
                print('Rejected')
        except Exception as e:
            import traceback
            traceback.print_exc()

    def addTOdetailMeal(self, data):
        '''

        :param data:
        :return:
        '''
        popup = popup_detailMeal.mealDeatail(self, data)
        result = popup.exec_()  # This makes the dialog modal
        if result == QDialog.Accepted:
            print('Accepted')
        else:
            print('Rejected')

    def daddToDeatailMeal(self, button):
        '''

        :param data:
        :return:
        '''
        data = button.userData(0)
        print(data)

    def getCenterWidget(self):
        return self.mainCenterWidget
from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))

from ui.mainWidget.centerWidget.centerMainWidget.homeWidget import homeWidgetMain
from ui.mainWidget.centerWidget.centerMainWidget.mealWidget import mealMainWidget
from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget import recepieMainWidget
from ui.mainWidget.centerWidget.centerMainWidget.groceryWidget import groceryMainWidget
from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderMainWidget
from ui.mainWidget.centerWidget.centerMainWidget.savedRecepieWidget import savedRecepieMainWidget
from ui.mainWidget.centerWidget.centerMainWidget.savedMealWidget import savedMealMainWidget
from ui.mainWidget.centerWidget.centerMainWidget.savedGroceryWidget import savedGroceryMain_widget
from ui.mainWidget.centerWidget.centerMainWidget.pantryWidget import pantryMainWidget
from ui.mainWidget.centerWidget.centerMainWidget.alertWidget import alertMainWidget
from ui.mainWidget.centerWidget.centerMainWidget.userWidget import userMainWidget



class centerMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent

        self.homeWidgetMain = homeWidgetMain.homwMainWidget(self.parent)
        self.mealMainWidget = mealMainWidget.mealMainWidget(self.parent)
        self.recepieMainWidget = recepieMainWidget.recepieMainWidget(self.parent)
        self.groceryMainWidget = groceryMainWidget.groceryMainWidget(self.parent)
        self.calenderMainWidget = calenderMainWidget.calenderMainWidget(self.parent)
        self.savedRecepieMainWidget = savedRecepieMainWidget.savedRecepieMainWidget(self.parent)
        self.savedMealMainWidget = savedMealMainWidget.savedMainWidget(self.parent)
        self.savedGroceryMainWidget = savedGroceryMain_widget.savedGroceryMainWidget(self.parent)
        self.pantryMainWidget = pantryMainWidget.pantryMainWidget(self.parent)
        self.alertMainWidget = alertMainWidget.alertMainWidget(self.parent)
        self.userMainWidget = userMainWidget.userMainWidget(self.parent)


        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)


    def initUI(self):
        '''


        :return:
        '''
        widget_object = 'centerMainWidget'
        color = self.color_class.setColorVal(r=36, g=36, b=36)
        backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        self.stackedWidget = QStackedWidget(widget)
        verticalLayout.addWidget(self.stackedWidget)

        #HOME WIDGET
        self.stackedWidget.addWidget(self.homeWidgetMain)

        #MEAL WIDGET
        self.stackedWidget.addWidget(self.mealMainWidget)

        #RECEPIE WIDGET
        self.stackedWidget.addWidget(self.recepieMainWidget)

        #GROCERY WIDGET
        self.stackedWidget.addWidget(self.groceryMainWidget)

        #CALENDER WIDGET
        self.stackedWidget.addWidget(self.calenderMainWidget)

        #SAVED MEAL WIDGET
        self.stackedWidget.addWidget(self.savedMealMainWidget)

        #SAVED RECEPIE WIDGET
        self.stackedWidget.addWidget(self.savedRecepieMainWidget)

        #SAVED GROCERY WIDGET
        self.stackedWidget.addWidget(self.savedGroceryMainWidget)

        #PANTRY WIDGET
        self.stackedWidget.addWidget(self.pantryMainWidget)

        #ALERT WIDGET
        self.stackedWidget.addWidget(self.alertMainWidget)

        #USER WIDGET
        self.stackedWidget.addWidget(self.userMainWidget)



        return widget



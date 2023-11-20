from ui_old.import_module import *
from ui_old.sampleWidget import sample_widget_template

from ui_old.widget import homeWidget
from ui_old.widget import mealWidget
from ui_old.widget import dishWidget
from ui_old.widget import shoppingWidget
from ui_old.widget import profileWidget


class mainWidget(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.home_widget = homeWidget.homeWidget()
        self.meal_widget = mealWidget.mealWidget()
        self.recepie_widget = dishWidget.dishWidget()
        self.shopping_widget = shoppingWidget.shoppingWidget()
        self.profile_widget = profileWidget.profileWidget()


        self.initUI()  # Call the UI setup method

        self.show()

    def initUI(self):
        # Set window size.
        self.resize(800, 800)

        # Set window title
        self.setWindowTitle('Meal Planner')

        widget = self.uiWidget()
        self.setCentralWidget(widget)

        # Show window
        self.show()

    def uiWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #CREATE TAB WIDGET
        tabWidget = self.sample_widget.tab_widget(parent_self=widget)
        tabWidget.setTabPosition(QTabWidget.South)
        verticalLayout.addWidget(tabWidget)

        #HOME TAB
        tabWidget.addTab(self.home_widget, "Home")
        tabWidget.addTab(self.meal_widget, "Meal")
        tabWidget.addTab(self.recepie_widget, "Dish")
        tabWidget.addTab(self.shopping_widget, "Shopping")
        tabWidget.addTab(self.profile_widget, "Profile")
        tabWidget.setCurrentIndex(3)
        return widget















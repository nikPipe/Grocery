from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template


from ui.widget import midWidget_MealWidget
from ui.widget import midWidget_recepieWidget
from ui.widget import midWidget_shoppingWidget


class midWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.midWidget_MealWidget = midWidget_MealWidget.midWidget_MealWidget()
        self.midWidget_recepieWidget = midWidget_recepieWidget.midWidget_recepieWidget()
        self.midWidget_shoppingWidget = midWidget_shoppingWidget.midWidget_shoppingWidget()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        stakeWidget = self.centerWidget()
        leftWidget = self.leftWidget()

        horizontalLayout.addWidget(leftWidget)
        horizontalLayout.addWidget(stakeWidget)

        return widget

    def leftWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #HOME BUTTON
        homeButton = self.sample_widget.pushButton(set_text='Home',
                                                   connect=partial(self.stakewidget.setCurrentIndex, 0))
        verticalLayout.addWidget(homeButton)

        #MEAL BUTTON
        mealButton = self.sample_widget.pushButton(set_text='Meal'
                                                   , connect=partial(self.stakewidget.setCurrentIndex, 1))
        verticalLayout.addWidget(mealButton)

        #RECIPE BUTTON
        recipeButton = self.sample_widget.pushButton(set_text='Recipe'
                                                     , connect=partial(self.stakewidget.setCurrentIndex, 2))
        verticalLayout.addWidget(recipeButton)

        #CALENDAR BUTTON
        calendarButton = self.sample_widget.pushButton(set_text='Calendar'
                                                       , connect=partial(self.stakewidget.setCurrentIndex, 3))
        verticalLayout.addWidget(calendarButton)

        #SHOPPING BUTTON
        shoppingButton = self.sample_widget.pushButton(set_text='Shopping'
                                                       , connect=partial(self.stakewidget.setCurrentIndex, 4))
        verticalLayout.addWidget(shoppingButton)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #? BUTTON
        questionButton = self.sample_widget.pushButton(set_text='?')
        verticalLayout.addWidget(questionButton)

        #YOUR LIST BUTTON
        yourListButton = self.sample_widget.pushButton(set_text='Your List')
        verticalLayout.addWidget(yourListButton)

        #SETTING BUTTON
        settingButton = self.sample_widget.pushButton(set_text='Setting')
        verticalLayout.addWidget(settingButton)

        #PRIFILE BUTTON
        profileButton = self.sample_widget.pushButton(set_text='Profile')
        verticalLayout.addWidget(profileButton)

        return widget

    def centerWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        self.stakewidget = QStackedWidget()
        verticalLayout.addWidget(self.stakewidget)

        self.stakewidget.addWidget(self.homeWidget())
        self.stakewidget.addWidget(self.mealWidget())
        self.stakewidget.addWidget(self.recepieWidget())
        self.stakewidget.addWidget(self.calendarWidget())
        self.stakewidget.addWidget(self.shoppingWidget())


        return widget

    def homeWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #FILTER MEAL
        search_the_product_lineEdit = self.sample_widget.line_edit(set_PlaceholderText='Search the product')
        search_the_product_lineEdit.setAlignment(Qt.AlignCenter)
        verticalLayout.addWidget(search_the_product_lineEdit)

        return widget


    def mealWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)


        verticalLayout.addWidget(self.midWidget_MealWidget)

        return widget

    def recepieWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.midWidget_recepieWidget)

        return widget

    def calendarWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='Calendar')
        verticalLayout.addWidget(button)

        return widget

    def shoppingWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.midWidget_shoppingWidget)

        return widget







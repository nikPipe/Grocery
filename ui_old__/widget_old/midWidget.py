from functools import partial

from ui_OldOne.import_module import *
from ui_OldOne.sampleWidget import sample_widget_template


from ui_old__.widget_old import leftWidget
from ui_old__.widget_old import centrealWidget


class midWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.centerWidget_ = centrealWidget.centralWidget()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)
        verticalLayout.setAlignment(Qt.AlignTop)


    def initUI(self):
        height_val = 800
        width_val = 50

        widget = self.sample_widget.widget_def(min_size=(width_val, height_val), max_size=(self.sample_widget.max_size, height_val))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        spitter = self.sample_widget.splitter_def(parent_self=widget, set_orientation=self.sample_widget.horizonatal)
        horizontalLayout.addWidget(spitter)

        leftWidget = self.leftWidget()
        spitter.addWidget(leftWidget)

        stakeWidget = self.centerWidget()
        spitter.addWidget(self.centerWidget_)

        spitter.setSizes([100, 600])

        return widget


    def centerWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        self.stakewidget = QStackedWidget()
        verticalLayout.addWidget(self.stakewidget)

        widgetOne = self.sample_widget.widget_def()
        verticalLayoutOne = self.sample_widget.vertical_layout(parent_self=widgetOne)

        button = self.sample_widget.pushButton(set_text='Button')
        verticalLayoutOne.addWidget(button)

        self.stakewidget.addWidget(widgetOne)
        return widget

    def leftWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        # HOME BUTTON
        homeButton = self.sample_widget.pushButton(set_text='Home', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 0))
        verticalLayout.addWidget(homeButton)

        # MEAL BUTTON
        mealButton = self.sample_widget.pushButton(set_text='Meal', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 1))
        verticalLayout.addWidget(mealButton)

        # RECIPE BUTTON
        recipeButton = self.sample_widget.pushButton(set_text='Recipe', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 2))
        verticalLayout.addWidget(recipeButton)

        groceryListButton = self.sample_widget.pushButton(set_text='Grocery List', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 3))
        verticalLayout.addWidget(groceryListButton)

        calendarButton = self.sample_widget.pushButton(set_text='Calendar')
        verticalLayout.addWidget(calendarButton)

        pinnedRecetButton = self.sample_widget.pushButton(set_text='Pinned Recipe and put the Expire Date')
        verticalLayout.addWidget(pinnedRecetButton)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        savedMealButton = self.sample_widget.pushButton(set_text='saved Meal', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 4))
        verticalLayout.addWidget(savedMealButton)

        # saveRecepie
        saveRecepieButton = self.sample_widget.pushButton(set_text='save Recepie', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 5))
        verticalLayout.addWidget(saveRecepieButton)

        # saveGroceryList
        saveGroceryListButton = self.sample_widget.pushButton(set_text='save Grocery List', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 6))
        verticalLayout.addWidget(saveGroceryListButton)

        # pantary
        pantaryButton = self.sample_widget.pushButton(set_text='pantary', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 7))
        verticalLayout.addWidget(pantaryButton)

        # SETTING BUTTON
        settingButton = self.sample_widget.pushButton(set_text='Setting', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 8))
        verticalLayout.addWidget(settingButton)

        # PROFILE BUTTON
        profileButton = self.sample_widget.pushButton(set_text='Profile', connect=partial(self.centerWidget_.stakewidget.setCurrentIndex, 9))
        verticalLayout.addWidget(profileButton)

        return widget



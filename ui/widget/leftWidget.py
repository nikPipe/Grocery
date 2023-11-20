from ui_OldOne.import_module import *
from ui_OldOne.sampleWidget import sample_widget_template

from ui.widget import centrealWidget

class lefWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        #self.centerWidget_ = centrealWidget.centralWidget()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        min_size = 120

        #widget.setMinimumSize(QSize(min_size, 0))
        #widget.setMaximumSize(QSize(min_size, self.sample_widget.max_size))
        verticalLayout.addWidget(widget)

    def initUI(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        #HOME BUTTON
        homeButton = self.sample_widget.pushButton(set_text='Home')
        verticalLayout.addWidget(homeButton)

        #MEAL BUTTON
        mealButton = self.sample_widget.pushButton(set_text='Meal')
        verticalLayout.addWidget(mealButton)

        #RECIPE BUTTON
        recipeButton = self.sample_widget.pushButton(set_text='Recipe')
        verticalLayout.addWidget(recipeButton)

        groceryListButton = self.sample_widget.pushButton(set_text='Grocery List')
        verticalLayout.addWidget(groceryListButton)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        savedMealButton = self.sample_widget.pushButton(set_text='saved Meal')
        verticalLayout.addWidget(savedMealButton)

        #saveRecepie
        saveRecepieButton = self.sample_widget.pushButton(set_text='save Recepie')
        verticalLayout.addWidget(saveRecepieButton)

        #saveGroceryList
        saveGroceryListButton = self.sample_widget.pushButton(set_text='save Grocery List')
        verticalLayout.addWidget(saveGroceryListButton)

        #pantary
        pantaryButton = self.sample_widget.pushButton(set_text='pantary')
        verticalLayout.addWidget(pantaryButton)

        #SETTING BUTTON
        settingButton = self.sample_widget.pushButton(set_text='Setting')
        verticalLayout.addWidget(settingButton)

        #PROFILE BUTTON
        profileButton = self.sample_widget.pushButton(set_text='Profile')
        verticalLayout.addWidget(profileButton)

        return widget
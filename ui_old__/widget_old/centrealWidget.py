from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template


from ui_old__.widget_old import homeWidget
from ui_old__.widget_old import mealWidget
from ui_old__.widget_old import saveedRecipeWidget
from ui_old__.widget_old import saveedGroceryWidget
from ui_old__.widget_old import saveedMealWidget
from ui_old__.widget_old import RecipeWidget
from ui_old__.widget_old import GroceryWidget
from ui_old__.widget_old import pantaryWidget
from ui_old__.widget_old import settingWidget
from ui_old__.widget_old import profileWidget





class centralWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.homeWidget_ = homeWidget.HomeWidget()
        self.mealWidget_ = mealWidget.MealWidget()
        self.saveedMealWidget_ = saveedMealWidget.saveedMealWidget()
        self.saveedRecipeWidget_ = saveedRecipeWidget.saveedRecipeWidget()
        self.saveedGroceryWidget_ = saveedGroceryWidget.saveedGroceryWidget()
        self.recipeWidget_ = RecipeWidget.RecipeWidget()
        self.groceryWidget_ = GroceryWidget.GroceryWidget()
        self.pantaryWidget_ = pantaryWidget.pantaryWidget()
        self.settingWidget_ = settingWidget.settingWidget()
        self.profileWidget_ = profileWidget.profileWidget()




        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        width = 800

        verticalLayout.addWidget(widget)

    def initUI(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        self.stakewidget = QStackedWidget()
        verticalLayout.addWidget(self.stakewidget)

        #self.homeWidget_ = self.homeWidget()
        self.stakewidget.addWidget(self.homeWidget_)

        #self.mealWidget_ = self.MealWidget()
        self.stakewidget.addWidget(self.mealWidget_)

        #self.recipeWidget_ = self.RecipeWidget()
        self.stakewidget.addWidget(self.recipeWidget_)

        #self.groceryWidget_ = self.GroceryWidget()
        self.stakewidget.addWidget(self.groceryWidget_)

        #self.saveedMealWidget_ = self.saveedMealWidget()
        self.stakewidget.addWidget(self.saveedMealWidget_)

        #self.saveedRecipeWidget_ = self.saveedRecipeWidget()
        self.stakewidget.addWidget(self.saveedRecipeWidget_)

        #self.saveedGroceryWidget_ = self.saveedGroceryWidget()
        self.stakewidget.addWidget(self.saveedGroceryWidget_)

        #self.pantaryWidget_ = self.pantaryWidget()
        self.stakewidget.addWidget(self.pantaryWidget_)

        #self.settingWidget_ = self.settingWidget()
        self.stakewidget.addWidget(self.settingWidget_)

        #self.profileWidget_ = self.profileWidget()
        self.stakewidget.addWidget(self.profileWidget_)

        return widget


    def homeWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        lineEdit = self.sample_widget.line_edit(set_PlaceholderText='Search The Grocery name')
        lineEdit.setAlignment(Qt.AlignCenter)
        verticalLayout.addWidget(lineEdit)



        return widget

    def MealWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='Meal')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Meal')
        verticalLayout.addWidget(button)

        return widget

    def RecipeWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='Recipe')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Recipe')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Recipe')
        verticalLayout.addWidget(button)

        return widget

    def GroceryWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='Grocery')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Grocery')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Grocery')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Grocery')
        verticalLayout.addWidget(button)

        return widget

    def saveedMealWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='saveed Meal')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='saveed Meal')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='saveed Meal')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='saveed Meal')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='saveed Meal')
        verticalLayout.addWidget(button)


        return widget

    def saveedRecipeWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='saveed Recipe')
        verticalLayout.addWidget(button)

        return widget

    def saveedGroceryWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='saveed Grocery')
        verticalLayout.addWidget(button)

        return widget


    def pantaryWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='pantary')
        verticalLayout.addWidget(button)

        return widget

    def settingWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='setting')
        verticalLayout.addWidget(button)

        return widget

    def profileWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='profile')
        verticalLayout.addWidget(button)

        return widget



















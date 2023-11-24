from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


class leftMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)


    def button_def(self, name='', background_color='', color='', border_radius=0, min_size=(0, 0), max_size=(0, 0), icon='',
                   icon_size=(0, 0)):
        '''

        :param set_text:
        :param set_icon:
        :param set_object_name:
        :param set_styleSheet:
        :param min_size:
        :param max_size:
        :return:
        '''

        if ' ' in name:
            new_name = name.replace(' ', '_')
        else:
            new_name = name

        set_object_name = new_name + 'ButtonObject'
        styleSheet_def = self.sample_widget.styleSheet_def(obj_name=set_object_name,
                                                       background_color=background_color,
                                                       color=color,
                                                       border_radius=border_radius)

        button = self.sample_widget.pushButton(set_text=name, set_icon=icon, set_object_name=set_object_name,
                                               set_styleSheet=styleSheet_def, min_size=min_size, max_size=max_size,
                                               set_icon_size=icon_size)

        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        button.setFont(font)

        return button

    def initUI(self):
        '''


        :return:
        '''
        color = self.color_class.setColorVal(r=36, g=36, b=36)
        backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=5)


        #Home Button
        icon = file + '/icon/home_open.png'
        button = self.button_def(name='Home', background_color=backgroundColor.get_value(),
                                 color=color.get_value(), border_radius=20, min_size=(150, 40),
                                 max_size=(150, 40), icon=icon, icon_size=(25, 25))
        button.clicked.connect(partial(self.centerWidgetSwitch, 0))
        verticalLayout.addWidget(button)


        #MEAL BUTTON
        icon = file + '/icon/meal.png'
        mealButton = self.button_def(name='Meal', background_color=backgroundColor.get_value(),
                                    color=color.get_value(), border_radius=20, min_size=(150, 40),
                                    max_size=(150, 40), icon=icon, icon_size=(30, 30))
        mealButton.clicked.connect(partial(self.centerWidgetSwitch, 1))
        verticalLayout.addWidget(mealButton)


        #RECEPIE BUTTON
        recepieButton = self.button_def(name='Recepie', background_color=backgroundColor.get_value(),
                                        color=color.get_value(), border_radius=20, min_size=(150, 40),
                                        max_size=(150, 40))
        recepieButton.clicked.connect(partial(self.centerWidgetSwitch, 2))
        verticalLayout.addWidget(recepieButton)

        #GROCERY BUTTON
        groceryButton = self.button_def(name='Grocery', background_color=backgroundColor.get_value(),
                                        color=color.get_value(), border_radius=20, min_size=(150, 40),
                                        max_size=(150, 40))
        groceryButton.clicked.connect(partial(self.centerWidgetSwitch, 3))
        verticalLayout.addWidget(groceryButton)

        #CALENDAR BUTTON
        calendarButton = self.button_def(name='Calendar', background_color=backgroundColor.get_value(),
                                        color=color.get_value(), border_radius=20, min_size=(150, 40),
                                        max_size=(150, 40))
        calendarButton.clicked.connect(partial(self.centerWidgetSwitch, 4))
        verticalLayout.addWidget(calendarButton)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # SAVE MEAL BUTTON
        saveMealButton = self.button_def(name='Save Meal', background_color=backgroundColor.get_value(),
                                         color=color.get_value(), border_radius=20, min_size=(150, 40),
                                         max_size=(150, 40))
        saveMealButton.clicked.connect(partial(self.centerWidgetSwitch, 5))
        verticalLayout.addWidget(saveMealButton)

        #SAVE RECEPIE BUTTON
        saveRecepieButton = self.button_def(name='Save Recepie', background_color=backgroundColor.get_value(),
                                        color=color.get_value(), border_radius=20, min_size=(150, 40),
                                        max_size=(150, 40))
        saveRecepieButton.clicked.connect(partial(self.centerWidgetSwitch, 6))
        verticalLayout.addWidget(saveRecepieButton)

        #SAVE GROCERY BUTTON
        saveGroceryButton = self.button_def(name='Save Grocery', background_color=backgroundColor.get_value(),
                                        color=color.get_value(), border_radius=20, min_size=(150, 40),
                                        max_size=(150, 40))
        saveGroceryButton.clicked.connect(partial(self.centerWidgetSwitch, 7))
        verticalLayout.addWidget(saveGroceryButton)

        #SAVE PANTY BUTTON
        savePantyButton = self.button_def(name='Save Panty', background_color=backgroundColor.get_value(),
                                        color=color.get_value(), border_radius=20, min_size=(150, 40),
                                        max_size=(150, 40))
        savePantyButton.clicked.connect(partial(self.centerWidgetSwitch, 8))
        verticalLayout.addWidget(savePantyButton)

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #ABOUT BUTTON
        aboutButton = self.button_def(name='About', background_color=backgroundColor.get_value(),
                                        color=color.get_value(), border_radius=20, min_size=(150, 40),
                                        max_size=(150, 40))

        verticalLayout.addWidget(aboutButton)

        #HELP BUTTON
        helpButton = self.button_def(name='Help', background_color=backgroundColor.get_value(),
                                        color=color.get_value(), border_radius=20, min_size=(150, 40),
                                        max_size=(150, 40))
        
        verticalLayout.addWidget(helpButton)


        return widget


    def centerWidgetSwitch(self, value):
        '''

        :param widget:
        :return:
        '''
        self.parent.mainCenterWidget.centerMainWidget.stackedWidget.setCurrentIndex(value)

        if value == 0:
            self.parent.mainCenterWidget.centerMainWidget.homeWidgetMain.stakeWidget.setCurrentIndex(0)

        elif value == 1:
            self.parent.mainCenterWidget.centerMainWidget.mealMainWidget.stakeWidget.setCurrentIndex(0)
            print('this is meal')
        elif value == 2:
            print('this is recepie')
        elif value == 3:
            print('this is grocery')
        elif value == 4:
            print('this is calendar')
        elif value == 5:
            print('this is save meal')
        elif value == 6:
            print('this is save recepie')
        elif value == 7:
            print('this is save grocery')
        elif value == 8:
            print('this is save panty')
        else:
            print('this is about')


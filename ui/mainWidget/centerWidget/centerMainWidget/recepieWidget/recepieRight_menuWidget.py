import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os, traceback
file =  os.path.dirname(os.path.realpath(ui.__file__))
from data import get_meal_dishe

from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget.old import recepieDetail_widget
from ui.mainWidget.centerWidget.centerMainWidget import popup_detailMeal

class recepieRightMenu_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.recepieDict = {}
        self.recepieDetail_widget = recepieDetail_widget.recepieDetail_widget(self.parent)

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)
        self.sampleObjectNmae = 'labelStyleSheet'
        self.labelStyleSheet = self.sample_widget.styleSheet_def(obj_name=self.sampleObjectNmae,
                                                                 color=self.color_class.white_color.get_value())

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

        self.update_()


    def initUI(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        verticalLayout.addWidget(self.menuWidget())

        #SAVE BUTTON
        saveButton_object = 'saveButton'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=saveButton_object,
                                                        color=self.color_class.white_color.get_value(),
                                                        border_radius=5)
        saveButton = self.sample_widget.pushButton(set_text='Save', set_object_name=saveButton_object, set_styleSheet=styleSheet_,
                                                   connect=self.saveButton_def)
        self.recepieRightMenu_horizontalLayour.addWidget(saveButton)

        return widget

    def menuWidget(self):
        widget = self.sample_widget.widget_def()

        self.recepieRightMenu_horizontalLayour = self.sample_widget.horizontal_layout(parent_self=widget,
                                                                                      set_contents_margins=(0, 0, 0, 0))
        return widget

    def saveButton_def(self):
        print('saving the object')

    def update_widget(self, menuName='', data=None):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))


        checkbox_object = 'checkbox'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=checkbox_object,
                                                        color=self.color_class.white_color.get_value(),
                                                        border_radius=5)
        checkbox = self.sample_widget.checkbox(set_text=menuName, set_object_name=checkbox_object, set_styleSheet=styleSheet_,
                                               set_checked=True)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        checkbox.setFont(font)
        verticalLayout.addWidget(checkbox)


        if data:
            iconPath = data['images']['main']
        else:
            iconPath = ''
        pushButton_object = 'pushButton'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=pushButton_object,
                                                        color=self.color_class.white_color.get_value(),
                                                        border_radius=5)
        pushButton = self.sample_widget.pushButton(set_text='', min_size=(100, 100), max_size=(100, 100),
                                                   set_object_name=pushButton_object, set_styleSheet=styleSheet_,
                                                   set_icon=iconPath, set_icon_size=(100, 100),
                                                   connect=partial(self.pushButton_def, data))
        verticalLayout.addWidget(pushButton)

        label_object = 'label'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=label_object,
                                                        color=self.color_class.white_color.get_value(),
                                                        border_radius=5)

        if data:
            name = data['name']
        else:
            name = ''

        label = self.sample_widget.label(set_text=name, set_object_name=label_object, set_styleSheet=styleSheet_)
        verticalLayout.addWidget(label)


        return widget


    def pushButton_def(self, data):
        '''

        :return:
        '''
        detailMeal = popup_detailMeal.mealDeatail(self.parent, data)
        detailMeal.exec_()


    def update_(self):
        '''

        :return:
        '''
        for each in range(0, 5):
            widget = self.update_widget()
            self.recepieRightMenu_horizontalLayour.addWidget(widget)
            pass





















from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


from ui.mainWidget.centerWidget.centerMainWidget.mealWidget import mealMain_widget
from ui.mainWidget.centerWidget.centerMainWidget.mealWidget import mealDetail_widget

class mealSearch_Widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        self.mealMain_widget = mealMain_widget.mealMain_Widget(self.parent)

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)
    def initUI(self):
        '''


        :return:
        '''
        widget = self.sample_widget.widget_def()
        mealSearch_widget_verticalLayout_ = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        mealSearch_widget_verticalLayout_.addWidget(scrollArea)
        object = 'scrollArea'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.color.get_value(),
                                                       border_radius=20)
        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=object, set_styleSheet=styleSheet)
        scrollArea.setWidget(scrollAreaWidgetContents)

        self.mealSearch_widget_verticalLayout = self.sample_widget.vertical_layout(parent_self=scrollAreaWidgetContents, set_spacing=10)

        pushButton = self.sample_widget.pushButton(set_text='Search', set_object_name='searchButton')
        self.mealSearch_widget_verticalLayout.addWidget(pushButton)

        return widget


    def filterWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def(min_size=(0, 50), max_size=(16777215, 50))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_spacing=15)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        horizontalLayout.addWidget(scrollArea)
        scrollAreaWidgetContents = self.sample_widget.widget_def()
        scrollArea.setWidget(scrollAreaWidgetContents)

        horizontalLayout_ = self.sample_widget.horizontal_layout(parent_self=scrollAreaWidgetContents, set_spacing=10)

        for i in range(10):
            button = self.sample_widget.pushButton(set_text='Search', set_object_name='searchButton')
            horizontalLayout_.addWidget(button)


        return widget


    def widgetList(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_spacing=15)

        horizontalLayout.addWidget(self.mealButtonWidget(data=data))

        horizontalLayout.addWidget(self.name_history_descriptionWidget(data=data))

        horizontalLayout.addWidget(self.minute_calaryWidget(data=data))

        horizontalLayout.addWidget(self.addToCalender_showDetailWidget(data=data))

        return widget


    def mealButtonWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        size = 200
        name = data['name']
        if data:
            image = data['images']['main']
        else:
            image = ''
        pushButtonObject = data['id'] + '_pushButton'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=pushButtonObject,
                                                        background_color=self.backgroundColor.get_value(),
                                                        border_radius=20)

        pusButton = self.sample_widget.pushButton(set_text='', set_object_name=pushButtonObject,
                                                  min_size=(size, size), max_size=(size, size),
                                                  set_styleSheet=styleSheet_, set_icon=image,
                                                  set_icon_size=(size, size),connect=partial(self.mealSearchWidget_def, data))

        verticalLayout.addWidget(pusButton)

        return widget

    def mealSearchWidget_def(self, data):
        '''

        :return:
        '''
        popup = self.parent.popup_detailMeal.mealDeatail(parent=self.parent, data=data)
        result = popup.exec_()  # This makes the dialog modal


    def name_history_descriptionWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()

        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        verticalLayout.addWidget(self.nameWidget(data=data))

        verticalLayout.addWidget(self.history_descriptionWidget(data=data))

        return widget


    def nameWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        label_object = data['id'] + '_label'
        name = data['name']
        if data:
            image = data['images']['main']
        else:
            image = ''
        styleSheet = self.sample_widget.styleSheet_def(obj_name=label_object,
                                                         color=self.color_class.white_color.get_value(),
                                                         border_radius=20)
        label = self.sample_widget.label(set_text=name, set_object_name=label_object, set_styleSheet=styleSheet,
                                         set_alighment=self.sample_widget.center_alignment)
        font = self.font
        font.setPointSize(15)
        label.setFont(font)

        verticalLayout.addWidget(label)

        return widget


    def history_descriptionWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=5)

        #historyButton = self.sample_widget.pushButton(set_text='History', set_object_name='historyButton')
        #horizontalLayout.addWidget(historyButton)

        width = 500

        objectNmae = data['id'] + '_history_label'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=objectNmae,
                                                            color=self.backgroundColor.get_value())

        history_label = self.sample_widget.label(set_text='History', set_object_name=objectNmae,
                                                     set_alighment=self.sample_widget.center_alignment,
                                                     set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        history_label.setFont(font)
        verticalLayout.addWidget(history_label)


        historyText = self.sample_widget.plainTextEdit()
        objectNmae = data['id'] + '_historyText'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=objectNmae,
                                                            background_color=self.backgroundColor.get_value(),
                                                            border_radius=20)
        historyText.setStyleSheet(styleSheet)
        historyText.setObjectName(objectNmae)
        historyText.setMinimumSize(QSize(width, 0))
        historyText.setMaximumSize(QSize(width, 16777215))
        historyText.setPlainText(data['history'])
        historyText.setReadOnly(True)
        font = self.font
        font.setPointSize(10)
        historyText.setFont(font)
        verticalLayout.addWidget(historyText)



        objectNmae = data['id'] + '_description_label'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=objectNmae,
                                                            color=self.backgroundColor.get_value())
        description_label = self.sample_widget.label(set_text='Description', set_object_name=objectNmae,
                                                     set_alighment=self.sample_widget.center_alignment, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        description_label.setFont(font)
        verticalLayout.addWidget(description_label)


        descriptionText = self.sample_widget.plainTextEdit()
        objectNmae = data['id'] + '_descriptionText'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=objectNmae,
                                                            background_color=self.backgroundColor.get_value(),
                                                            border_radius=20)
        descriptionText.setStyleSheet(styleSheet)
        descriptionText.setObjectName(objectNmae)
        descriptionText.setMinimumSize(QSize(width, 0))
        descriptionText.setMaximumSize(QSize(width, 16777215))
        descriptionText.setPlainText(data['description'])
        descriptionText.setReadOnly(True)
        font = self.font
        font.setPointSize(10)
        descriptionText.setFont(font)
        verticalLayout.addWidget(descriptionText)


        return widget

    def minute_calaryWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)


        totoalMinute = str(data['time']['totalTime']['value']) + ' ' + str(data['time']['totalTime']['unit'])
        label_obj = data['id'] + '_minuteLabel'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=label_obj,
                                                            color=self.color_class.white_color.get_value(),
                                                            border_radius=20)
        label = self.sample_widget.label(set_text=totoalMinute, set_object_name=label_obj,
                                          set_styleSheet=styleSheet, set_alighment=self.sample_widget.center_alignment)
        font = self.font
        font.setPointSize(15)
        label.setFont(font)
        verticalLayout.addWidget(label)


        label_obj = data['id'] + '_calaryLabel'
        cal = str(data['nutrition']['calories'])
        styleSheet = self.sample_widget.styleSheet_def(obj_name=label_obj,
                                                            color=self.color_class.white_color.get_value(),
                                                            border_radius=20)
        label = self.sample_widget.label(set_text=cal, set_object_name=label_obj,
                                          set_styleSheet=styleSheet, set_alighment=self.sample_widget.center_alignment)
        font = self.font
        font.setPointSize(15)
        label.setFont(font)
        verticalLayout.addWidget(label)

        return widget

    def addToCalender_showDetailWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        add_toCalener_object = data['id'] + '_addToCalenderButton'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=add_toCalener_object,
                                                            background_color=self.backgroundColor.get_value(),
                                                            border_radius=15)
        button = self.sample_widget.pushButton(set_text='Add to Calender', set_object_name=add_toCalener_object,
                                                  set_styleSheet=styleSheet,
                                               min_size=(100, 40), max_size=(100, 40),
                                               connect=partial(self.addToCalender_def, data))
        verticalLayout.addWidget(button)


        showDetail_object = data['id'] + '_showDetailButton'
        if 'Non-Vegetarian' in data['dietTypes'] or 'Non-Vegetarian' in data['dietTypes'] or 'Pescatarian' in data[
            'dietTypes'] or 'Pescatarian' in data['dietTypes']:
            color = self.color_class.red_color.get_value()
        else:
            color = self.color_class.green_color.get_value()


        styleSheet = self.sample_widget.styleSheet_def(obj_name=showDetail_object,
                                                            background_color=color,
                                                            border_radius=15)

        button = self.sample_widget.pushButton(set_text='', set_object_name=showDetail_object,
                                                  set_styleSheet=styleSheet,
                                               min_size=(100, 40), max_size=(100, 40))
        verticalLayout.addWidget(button)



        return widget


    def addToCalender_def(self, data):
        '''

        :param data:
        :return:
        '''
        calender_ = self.parent.popup_calender.AddToCalender(parent=self.parent, data=data)
        result = calender_.exec_()


    def update_Widget(self, data):
        '''

        :return:
        '''
        widget = self.widgetList(data=data)
        return widget
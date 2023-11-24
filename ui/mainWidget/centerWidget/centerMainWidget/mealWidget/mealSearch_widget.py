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
        self.mealDetailWidet = mealDetail_widget.mealMain_Widget(self.parent)

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
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)



        verticalLayout.addWidget(self.filterWidget())

        verticalLayout.addWidget(self.widgetList())
        #verticalLayout.addWidget(self.widgetList())



        verticalLayout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))


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


    def widgetList(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_spacing=15)

        horizontalLayout.addWidget(self.mealButtonWidget())

        horizontalLayout.addWidget(self.name_history_descriptionWidget())

        horizontalLayout.addWidget(self.minute_calaryWidget())

        horizontalLayout.addWidget(self.addToCalender_showDetailWidget())

        return widget


    def mealButtonWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)


        size = 200
        pusButton = self.sample_widget.pushButton(set_text='Meal', set_object_name='mealButton',
                                                  min_size=(size, size), max_size=(size, size))
        verticalLayout.addWidget(pusButton)

        return widget


    def name_history_descriptionWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()

        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        verticalLayout.addWidget(self.nameWidget())

        verticalLayout.addWidget(self.history_descriptionWidget())

        return widget


    def nameWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        label_object = 'label_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=label_object,
                                                         color=self.backgroundColor.get_value(),
                                                         border_radius=20)
        label = self.sample_widget.label(set_text='Name', set_object_name=label_object, set_styleSheet=styleSheet,
                                         set_alighment=self.sample_widget.center_alignment)
        font = self.font
        font.setPointSize(15)
        label.setFont(font)

        verticalLayout.addWidget(label)

        return widget


    def history_descriptionWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_spacing=15)

        historyButton = self.sample_widget.pushButton(set_text='History', set_object_name='historyButton')
        horizontalLayout.addWidget(historyButton)

        descriptionButton = self.sample_widget.pushButton(set_text='Description', set_object_name='descriptionButton')
        horizontalLayout.addWidget(descriptionButton)


        return widget

    def minute_calaryWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        button = self.sample_widget.pushButton(set_text='Minute', set_object_name='minuteButton')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Calary', set_object_name='calaryButton')
        verticalLayout.addWidget(button)

        return widget

    def addToCalender_showDetailWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        button = self.sample_widget.pushButton(set_text='Add to Calender', set_object_name='addToCalenderButton')
        verticalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Show Detail', set_object_name='showDetailButton')
        verticalLayout.addWidget(button)



        return widget
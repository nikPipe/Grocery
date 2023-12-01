import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))

from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderTop_widget
from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderCenter_widget



class calenderMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        self.currentDay = QDate.currentDate().toString('dd.MM.yyyy')

        self.calenderTop_widget = calenderTop_widget.calenderTop_widget(self)
        self.calenderCenter_widget = calenderCenter_widget.calenderCenter_widget(self)


        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.dateList = self.getDateList()
        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)
    def initUI(self):
        '''
        :return:
        '''
        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        verticalLayout.addWidget(self.calenderTop_widget)
        verticalLayout.addWidget(self.calenderCenter_widget)

        return widget


    def getDateList(self):
        start_year = 2010
        num_years = 50

        # Initialize an empty list to store the dates
        date_list = []

        # Loop through each year
        for year in range(start_year, start_year + num_years):
            # Calculate the first day of the year (January 1)
            first_day = QDate(year, 1, 1)

            # Calculate the last day of the year (December 31)
            last_day = QDate(year, 12, 31)

            # Loop through the dates for the current year and append to date_list
            current_date = first_day
            while current_date <= last_day:
                date_list.append(current_date)
                current_date = current_date.addDays(1)

        return date_list


    def calenderTop_widget_def(self, data):
        '''

        :return:
        '''
        popup = AddToCalender(self.parent, data)
        result = popup.exec_()  # This makes the dialog modal


    def getCurrentDay(self):
        return self.currentDay

    def update_(self):
        '''

        :return:
        '''
        self.calenderCenter_widget.update_()

class AddToCalender(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.data = data

        self.setWindowTitle("Add to Calender")
        self.setModal(True)  # Set the dialog as modal

        layout = QVBoxLayout(self)

        layout.addWidget(self.initUI())

    def initUI(self):
        '''

        :return:
        '''
        widget  = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)


        calender_Widget = QCalendarWidget(widget)
        calender_Widget.setGridVisible(True)
        verticalLayout.addWidget(calender_Widget)

        timeWidget = QTimeEdit(widget)
        timeWidget.setDisplayFormat("hh:mm AP")
        verticalLayout.addWidget(timeWidget)

        mealName = QLineEdit(widget)
        mealName.setText(self.data['name'])
        mealName.setReadOnly(True)
        verticalLayout.addWidget(mealName)

        button = self.sample_widget.pushButton(set_text='Add to Calender', connect=partial(self.addToCalender, calender_Widget, timeWidget, self.data))
        verticalLayout.addWidget(button)


        return widget

    def addToCalender(self, calender_Widget, timeWidget, data):
        '''

        :return:
        '''
        tempFile = self.help_class.getTempFile(self.help_class.tempFileName)
        jsonFile = self.help_class.readjsonFile(tempFile)
        if 'calender' not in jsonFile:
            jsonFile['calender'] = {}
        if calender_Widget.selectedDate().toString('yyyyMMdd') not in jsonFile['calender']:
            jsonFile['calender'][calender_Widget.selectedDate().toString('yyyyMMdd')] = {}
        if timeWidget.time().toString('hhmmss') not in jsonFile['calender'][calender_Widget.selectedDate().toString('yyyyMMdd')]:
            jsonFile['calender'][calender_Widget.selectedDate().toString('yyyyMMdd')][timeWidget.time().toString('hhmmss')] = []
        jsonFile['calender'][calender_Widget.selectedDate().toString('yyyyMMdd')][timeWidget.time().toString('hhmmss')].append(data['id'])
        self.help_class.get_set_TempFileName(jsonFile)

        self.close()



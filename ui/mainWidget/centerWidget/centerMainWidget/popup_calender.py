import json
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


class AddToCalender(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.data = data

        name = 'Add to Calender: ' + str(self.data['name'])
        self.setWindowTitle(name)
        self.setModal(True)  # Set the dialog as modal

        layout = QVBoxLayout(self)


        layout.addWidget(self.initUI())

    def initUI(self):
        '''

        :return:
        '''
        width = 800
        height = 600
        widget  = self.sample_widget.widget_def(min_size=(width, height), max_size=(width, height))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)


        calender_Widget = QCalendarWidget(widget)
        calender_Widget.setGridVisible(True)
        verticalLayout.addWidget(calender_Widget)


        timeWidget = QTimeEdit(widget)
        timeWidget.setDisplayFormat("hh:mm AP")
        timeWidget.setTime(QTime(8, 0, 0))
        verticalLayout.addWidget(timeWidget)
        font = QFont()
        font.setPointSize(12)
        timeWidget.setFont(font)

        try:
            verticalLayout.addWidget(self.breakfast_lunch_snack_dinner_def(timeWidget))
        except Exception as e:
            import traceback
            traceback.print_exc()


        mealName = self.sample_widget.line_edit(set_object_name='mealName')
        mealName.setText(self.data['name'])
        mealName.setAlignment(Qt.AlignCenter)
        mealName.setFont(font)

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

        date = calender_Widget.selectedDate().fromString(calender_Widget.selectedDate().toString('yyyyMMdd'), 'yyyyMMdd')
        date = date.toString('yyyy-MM-dd')
        time = timeWidget.time().fromString(timeWidget.time().toString('hhmmss'), 'hhmmss')
        time = time.toString('hh:mm:ss')
        string_val = 'Adding %s to %s and time %s' % (data['name'], str(date), str(time))
        display = self.sample_widget.displayMessage(string_val, 'Meal Added to Calender', 'success')
        val = display.exec_()
        if val == QMessageBox.Ok:
            self.help_class.get_set_TempFileName(jsonFile)
            self.close()


    def breakfast_lunch_snack_dinner_def(self, timeWidget):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        breakfast = self.sample_widget.pushButton(set_text='Breakfast', set_object_name='breakfast',
                                                  connect=partial(self.breakfast_lunch_snack_dinner_button_def, 'breakfast', timeWidget))
        horizontalLayout.addWidget(breakfast)

        lunch = self.sample_widget.pushButton(set_text='Lunch', set_object_name='lunch',
                                              connect=partial(self.breakfast_lunch_snack_dinner_button_def, 'lunch', timeWidget))
        horizontalLayout.addWidget(lunch)

        snack = self.sample_widget.pushButton(set_text='Snack', set_object_name='snack',
                                              connect=partial(self.breakfast_lunch_snack_dinner_button_def, 'snack', timeWidget))
        horizontalLayout.addWidget(snack)

        dinner = self.sample_widget.pushButton(set_text='Dinner', set_object_name='dinner',
                                               connect=partial(self.breakfast_lunch_snack_dinner_button_def, 'dinner', timeWidget))
        horizontalLayout.addWidget(dinner)

        return widget

    def breakfast_lunch_snack_dinner_button_def(self, button, timeWidget):
        '''

        :param button:
        :return:
        '''
        if button == 'breakfast':
            timeWidget.setTime(QTime(8, 0, 0))

        elif button == 'lunch':
            timeWidget.setTime(QTime(13, 0, 0))

        elif button == 'snack':
            timeWidget.setTime(QTime(17, 0, 0))

        elif button == 'dinner':
            timeWidget.setTime(QTime(20, 0, 0))

        else:
            pass

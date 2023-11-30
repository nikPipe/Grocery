from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from datetime import datetime, timedelta

class calenderTop_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)
        self.sampleObjectNmae = 'labelStyleSheet'
        self.labelStyleSheet = self.sample_widget.styleSheet_def(obj_name=self.sampleObjectNmae,
                                                                 color=self.color_class.white_color.get_value())
        self.currentDay = self.parent.currentDay

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
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=0)

        #CALENDER LABEL
        calenderLabel_object = 'calenderLabel_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=calenderLabel_object, color=self.color_class.white_color.get_value(),
                                                       border_radius=0)
        calenderLabel = self.sample_widget.label(set_text='Calender', set_alighment=self.sample_widget.center_alignment, set_object_name=calenderLabel_object,
                                                 set_styleSheet=styleSheet_)
        font = self.font
        font.setPointSize(15)
        calenderLabel.setFont(font)
        horizontalLayout.addWidget(calenderLabel)

        #CURRENT DATA BUTTON
        currentDayButton_object = 'currentDayButton_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=currentDayButton_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        currentDayButton = self.sample_widget.pushButton(set_text='Today', set_object_name=currentDayButton_object, set_styleSheet=styleSheet_,
                                                         connect=self.currentDayButton_)
        currentDayButton.setFont(font)
        horizontalLayout.addWidget(currentDayButton)

        #PREVIOU DAY BUTTON
        previousDayButton_object = 'previousDayButton_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=previousDayButton_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        previousDayButton = self.sample_widget.pushButton(set_text='<', set_object_name=previousDayButton_object, set_styleSheet=styleSheet_,
                                                          connect=self.previousDayButton_)
        previousDayButton.setFont(font)
        horizontalLayout.addWidget(previousDayButton)

        #NEXT DAY BUTTON
        nextDayButton_object = 'nextDayButton_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=nextDayButton_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        nextDayButton = self.sample_widget.pushButton(set_text='>', set_object_name=nextDayButton_object, set_styleSheet=styleSheet_,
                                                      connect=self.nextDayButton_)
        nextDayButton.setFont(font)
        horizontalLayout.addWidget(nextDayButton)

        #CALENDER LABEL BUTTON
        date_ = self.help_class.converDateToString(self.currentDay) + ' ' + self.help_class.getDay(self.currentDay)

        calenderLabelButton_object = 'calenderLabelButton_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=calenderLabelButton_object, color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        self.calenderLabel = self.sample_widget.label(set_text=date_, set_alighment=self.sample_widget.center_alignment, set_object_name=calenderLabelButton_object,
                                                       set_styleSheet=styleSheet_, min_size=(0, 40))
        font = self.font
        font.setPointSize(15)
        self.calenderLabel.setFont(font)
        horizontalLayout.addWidget(self.calenderLabel)

        horizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Maximum))

        #CALENDER SWITCH COMBOBOX
        calenderSwitchComboBox_object = 'calenderSwitchComboBox_object'
        comboBoxItem = ['Day', 'Week', 'Month']
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=calenderSwitchComboBox_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        calenderSwitchComboBox = self.sample_widget.comboBox(set_object_name=calenderSwitchComboBox_object, set_styleSheet=styleSheet_,
                                                             addItems=comboBoxItem,
                                                             currentIndexChanged=self.clenaderSwitchComboBox_def)
        calenderSwitchComboBox.setFont(font)
        horizontalLayout.addWidget(calenderSwitchComboBox)


        return widget

    def previousDayButton_(self):
        stakeWidget = self.parent.calenderCenter_widget.calenderCenter_stakeWidget
        if stakeWidget.currentIndex() == 0:
            date_object = datetime.strptime(self.currentDay, "%d.%m.%Y")
            previous_day = date_object - timedelta(days=1)
            currentDay = previous_day.strftime("%d.%m.%Y")
            self.currentDateUpdate(date=currentDay)
            date_ = self.help_class.converDateToString(self.currentDay) + ' ' + self.help_class.getDay(self.currentDay)
            self.calenderLabel.setText(date_)

            self.parent.calenderCenter_widget.calenderCenterDay_widget.previousDayButton_(self.currentDay)

        elif stakeWidget.currentIndex() == 1:
            self.parent.calenderCenter_widget.calenderCenterWeek_widget.previousWeekButton_()
            weekstart, weekend = self.parent.calenderCenter_widget.calenderCenterWeek_widget.week_start, self.parent.calenderCenter_widget.calenderCenterWeek_widget.week_end
            date_ = self.help_class.converDateToString(weekstart) + ' --- ' + self.help_class.converDateToString(weekend)
            self.calenderLabel.setText(date_)


        elif stakeWidget.currentIndex() == 2:
            self.parent.calenderCenter_widget.calenderCenterMonth_widget.previousMonthButton_()
            month = self.parent.calenderCenter_widget.calenderCenterMonth_widget.currentMonth
            year = self.parent.calenderCenter_widget.calenderCenterMonth_widget.currentYear
            monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                         'October', 'November', 'December']
            month_ = monthList[month - 1]
            date_ = str(month_) + ' ' + str(year)
            self.calenderLabel.setText(date_)

    def nextDayButton_(self):
        stakeWidget = self.parent.calenderCenter_widget.calenderCenter_stakeWidget
        if stakeWidget.currentIndex() == 0:
            date_object = datetime.strptime(self.currentDay, "%d.%m.%Y")
            previous_day = date_object + timedelta(days=1)
            currentDay = previous_day.strftime("%d.%m.%Y")
            self.currentDateUpdate(date=currentDay)
            date_ = self.help_class.converDateToString(self.currentDay) + ' ' + self.help_class.getDay(self.currentDay)
            self.calenderLabel.setText(date_)
            self.parent.calenderCenter_widget.calenderCenterDay_widget.nextDayButton_(self.currentDay)

        elif stakeWidget.currentIndex() == 1:
            self.parent.calenderCenter_widget.calenderCenterWeek_widget.nextWeekButton_()
            weekstart, weekend = self.parent.calenderCenter_widget.calenderCenterWeek_widget.week_start, self.parent.calenderCenter_widget.calenderCenterWeek_widget.week_end
            date_ = self.help_class.converDateToString(weekstart) + ' --- ' + self.help_class.converDateToString(weekend)
            self.calenderLabel.setText(date_)

        elif stakeWidget.currentIndex() == 2:
            self.parent.calenderCenter_widget.calenderCenterMonth_widget.nextMonthButton_()
            month = self.parent.calenderCenter_widget.calenderCenterMonth_widget.currentMonth
            year = self.parent.calenderCenter_widget.calenderCenterMonth_widget.currentYear
            monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                         'October', 'November', 'December']
            month_ = monthList[month - 1]
            date_ = str(month_) + ' ' + str(year)
            self.calenderLabel.setText(date_)

    def currentDateUpdate(self, date):
        '''

        :param date:
        :return:
        '''
        self.currentDay = date
        self.parent.currentDay = date


    def currentDayButton_(self):
        current_day = QDate.currentDate().toString('dd.MM.yyyy')
        self.currentDateUpdate(date=current_day)
        stakeWidget = self.parent.calenderCenter_widget.calenderCenter_stakeWidget
        if stakeWidget.currentIndex() == 0:
            date_ = self.help_class.converDateToString(self.currentDay) + ' ' + self.help_class.getDay(self.currentDay)
            self.calenderLabel.setText(date_)
            self.parent.calenderCenter_widget.calenderCenterDay_widget.currentDayButton_(self.currentDay)

        elif stakeWidget.currentIndex() == 1:
            self.parent.calenderCenter_widget.calenderCenterWeek_widget.update_(self.currentDay)

        elif stakeWidget.currentIndex() == 2:
            self.parent.calenderCenter_widget.calenderCenterMonth_widget.update_(self.currentDay)
            month = self.help_class.getMonth(self.currentDay)
            year = self.help_class.getYear(self.currentDay)
            monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                         'October', 'November', 'December']
            month_ = monthList[month - 1]
            date_ = str(month_) + ' ' + str(year)
            self.calenderLabel.setText(date_)


    def clenaderSwitchComboBox_def(self, index):
        '''

        :return:
        '''
        stakeWidget = self.parent.calenderCenter_widget.calenderCenter_stakeWidget
        stakeWidget.setCurrentIndex(index)
        if index == 0:
            date_ = self.help_class.converDateToString(self.currentDay) + ' ' + self.help_class.getDay(self.currentDay)
            self.calenderLabel.setText(date_)
            self.parent.calenderCenter_widget.calenderCenterDay_widget.update_(self.currentDay)
        elif index == 1:
            self.parent.calenderCenter_widget.calenderCenterWeek_widget.update_(self.currentDay)
            week_start, week_end = self.help_class.getWeek(self.currentDay)

            week_start_ = self.help_class.converDateToString(week_start) + '\n' + self.help_class.getDay(week_end)
            week_end_ = self.help_class.converDateToString(week_end) + '\n' + self.help_class.getDay(week_end)
            date_ = week_start_ + ' - ' + week_end_
            self.calenderLabel.setText(date_)

        elif index == 2:
            self.parent.calenderCenter_widget.calenderCenterMonth_widget.update_(self.currentDay)
            month = self.help_class.getMonth(self.currentDay)
            year = self.help_class.getYear(self.currentDay)
            month_names = [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ]
            month_ = ''
            if 1 <= month <= 12:
                # Subtract 1 from the numeric month to match the list indexing (January is at index 0)
                month_ = month_names[month - 1]
            date_ = str(month_) + ' ' + str(year)
            self.calenderLabel.setText(date_)

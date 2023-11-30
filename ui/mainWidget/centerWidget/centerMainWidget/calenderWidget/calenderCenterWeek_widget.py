from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from datetime import datetime, timedelta
from ui.mainWidget.centerWidget.centerMainWidget.createShoppingListWidget import createShoppingList


class calenderCenterWeek_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        self.currentDay = self.parent.currentDay
        self.week_start, self.week_end = self.help_class.getWeek(self.currentDay)

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)
        self.sampleObjectNmae = 'labelStyleSheet'
        self.labelStyleSheet = self.sample_widget.styleSheet_def(obj_name=self.sampleObjectNmae,
                                                                 color=self.color_class.white_color.get_value())
        self.treeWidgetList = []

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)
    def initUI(self):
        '''

        :return:
        '''

        mainWidegt = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=mainWidegt, set_contents_margins=(0, 0, 0, 0), set_spacing=5)


        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout.addWidget(widget)
        self.week_horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=5)


        createShoppintButton_object = 'createShoppintButton_object'
        createShoppintButton_styleSheet = self.sample_widget.styleSheet_def(obj_name=createShoppintButton_object,
                                                                            color=self.color_class.black_color.get_value(),
                                                                            border_radius=0)
        createShoppintButton = self.sample_widget.pushButton(set_text='Create Shopping List', set_object_name=createShoppintButton_object,
                                                                set_styleSheet=createShoppintButton_styleSheet,
                                                             connect=self.createShoppingList_)
        font = self.font
        font.setPointSize(15)
        createShoppintButton.setFont(font)

        verticalLayout.addWidget(createShoppintButton)



        return mainWidegt


    def weekWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=5)

        label_object = 'label_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=label_object, color=self.color_class.white_color.get_value(),
                                                        border_radius=0)

        label = self.sample_widget.label(set_text='Data', set_alighment=self.sample_widget.center_alignment, set_object_name=label_object,
                                         set_styleSheet=styleSheet_)
        font = self.font
        font.setPointSize(15)
        label.setFont(font)
        verticalLayout.addWidget(label)

        treeWidget = self.sample_widget.treeWidget(setHeaderHidden=True)
        verticalLayout.addWidget(treeWidget)



        return widget

    def weekUpdate(self, date):
        '''

        :param date:
        :return:
        '''
        self.treeWidgetList = []
        week_start, week_end = self.help_class.getWeek(date)
        week_start_day = self.help_class.getDay(week_start)
        week_end_day = self.help_class.getDay(week_end)

        current_date = datetime.strptime(week_start, "%d.%m.%Y")

        # Parse the end date string into a datetime object
        end_date = datetime.strptime(week_end, "%d.%m.%Y")

        # Define a list to store the formatted dates
        date_list = []
        day_list = []

        # Iterate through the dates and add them to the list
        while current_date <= end_date:
            # Format the current date as "dd.mm.yyyy" and append it to the list
            formatted_date = current_date.strftime("%d.%m.%Y")
            date_list.append(formatted_date)

            # Format the current date's weekday name (i.e. Monday, Tuesday, etc.) and append it to the list
            weekday_name = current_date.strftime("%A")
            day_list.append(weekday_name)

            # Increment the current date by one day
            current_date += timedelta(days=1)

        for date, day in zip(date_list, day_list):
            date_ = self.help_class.converDateToString(date) + '\n' + self.help_class.getDay(date)


            widget_ = self.sample_widget.widget_def()
            verticalLayout = self.sample_widget.vertical_layout(parent_self=widget_, set_contents_margins=(0, 0, 0, 0), set_spacing=5)

            label_object = 'label_object'
            if day.lower() == 'saturday' or day.lower() == 'sunday':
                styleSheet_ = self.sample_widget.styleSheet_def(obj_name=label_object, color=self.color_class.red_color.get_value(),
                                                                border_radius=0)
            else:
                styleSheet_ = self.sample_widget.styleSheet_def(obj_name=label_object, color=self.color_class.white_color.get_value(),
                                                                border_radius=0)

            label = self.sample_widget.label(set_text=date_, set_alighment=self.sample_widget.center_alignment, set_object_name=label_object,
                                                set_styleSheet=styleSheet_)
            font = self.font
            font.setPointSize(15)
            label.setFont(font)

            verticalLayout.addWidget(label)

            treeWidget = self.sample_widget.treeWidget(setHeaderHidden=True)
            treeWidget.setHeaderLabels(['Time', 'Meal'])
            self.treeWidgetList.append(treeWidget)

            verticalLayout.addWidget(treeWidget)

            jsonFile = self.help_class.get_TempFileData()
            font = QFont()
            font.setPointSize(10)


            for eachCalender in jsonFile['calender']:
                date_str = eachCalender
                if date == f"{date_str[6:8]}.{date_str[4:6]}.{date_str[:4]}":
                    for eachTime in jsonFile['calender'][date_str]:
                        time_str = str(eachTime)
                        time_object = datetime.strptime(time_str, "%H%M%S")
                        formatted_time = time_object.strftime("%I.%M %p")
                        text = ''
                        for each in jsonFile['calender'][date_str][eachTime]:
                            text = text + each + '\n'
                        item = QTreeWidgetItem(treeWidget)
                        item.setText(0, formatted_time)
                        item.setText(1, text)
                        item.setFont(0, font)
                        item.setFont(1, font)


            self.week_horizontalLayout.addWidget(widget_)

    def date_update(self, date):
        '''

        :param date:
        :return:
        '''
        self.currentDay = date
        self.week_start, self.week_end = self.help_class.getWeek(self.currentDay)


    def update_(self, date):
        '''

        :return:
        '''
        self.date_update(date=date)
        self.help_class.clearLayout(self.week_horizontalLayout)
        self.week_horizontalLayout.addWidget(self.weekUpdate(date=self.currentDay))

    def previousWeekButton_(self):
        '''

        :param date:
        :return:
        '''
        date_object = datetime.strptime(self.week_start, "%d.%m.%Y")
        previous_day = date_object - timedelta(days=1)
        self.update_(date=previous_day.strftime("%d.%m.%Y"))

    def nextWeekButton_(self):
        '''

        :param date:
        :return:
        '''
        date_object = datetime.strptime(self.week_end, "%d.%m.%Y")
        next_dau = date_object + timedelta(days=1)
        self.update_(date=next_dau.strftime("%d.%m.%Y"))



    def createShoppingList_(self):
        '''

        :return:
        '''
        itemList = []
        for eachTreeWidgetList in self.treeWidgetList:
            selectAllItem = eachTreeWidgetList.selectAll()
            selectedItem = eachTreeWidgetList.selectedItems()
            eachTreeWidgetList.clearSelection()
            for eachSelection in selectedItem:
                if eachSelection.text(1) != '':
                    split = eachSelection.text(1).split('\n')
                    for each in split:
                        if each != '':
                            itemList.append(each)
        shoppingListWindow = createShoppingList(parent=self.parent, data=itemList)
        shoppingListWindow.exec_()

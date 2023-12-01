from datetime import datetime
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget.createShoppingListWidget import createShoppingList


class calenderCenterMonth_widget(QWidget):
    def __init__(self, parent, shoppingListHide=False):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        self.currentDay = self.parent.currentDay
        self.currentMonth = self.help_class.getMonth(self.currentDay)
        self.currentYear = self.help_class.getYear(self.currentDay)
        self.shoppingListHide = shoppingListHide


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

        self.Mainwidget = self.initUI()
        verticalLayout.addWidget(self.Mainwidget)
    def initUI(self):
        '''

        :return:
        '''
        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        gridLayout = self.sample_widget.grid_layout(parent_self=widget, set_contents_margins=(5, 5, 5, 5), set_spacing=15)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = self.sample_widget.widget_def()
        scrollArea.setWidget(scrollAreaWidgetContents)
        gridLayout.addWidget(scrollArea, 0, 0, 1, 2)

        verticalLayout = self.sample_widget.vertical_layout(parent_self=scrollAreaWidgetContents, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        verticalLayout.addWidget(self.monthWidget())

        createShoppintButton_object = 'createShoppintButton_object'
        createShoppintButton_styleSheet = self.sample_widget.styleSheet_def(obj_name=createShoppintButton_object,
                                                                            color=self.color_class.black_color.get_value(),
                                                                            border_radius=0)

        if self.shoppingListHide == False :
            createShoppintButton = self.sample_widget.pushButton(set_text='Create Shopping List', set_object_name=createShoppintButton_object,
                                                                    set_styleSheet=createShoppintButton_styleSheet,
                                                                 connect=self.createShoppingList_)
            verticalLayout.addWidget(createShoppintButton)


        return widget

    def monthWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        self.verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        monthWidget = self.populate_dates()
        self.verticalLayout.addWidget(monthWidget)

        return widget


    def createShoppingList_(self):
        '''

        :return:
        '''
        try:

            treeWidget = self.monthWidget.findChildren(QTreeWidget)
            recepieList = []
            for eachTreeWidget in treeWidget:
                eachTreeWidget.selectAll()
                items = eachTreeWidget.selectedItems()
                eachTreeWidget.clearSelection()
                for eachSelection in items:
                    text = eachSelection.text(0)
                    if text != '':
                        textSplit = text.split('\n')
                        for each in textSplit:
                            if each != '':
                                recepieList.append(each)

            shoppingListWindow = createShoppingList(parent=self.parent, data=recepieList)
            shoppingListWindow.exec_()




        except Exception as e:
            import traceback
            traceback.print_exc()

    def populate_dates(self):
        self.treeWidgetList = []
        # Define the start date and the number of days to display
        start_date = self.currentDay
        start_date = datetime.strptime(start_date, '%d.%m.%Y').date()
        start_date = QDate(start_date.year, start_date.month, 1)

        #start_date = QDate(2023, 11, 1)
        num_days = 35  # Display 35 days (5 weeks)

        # Set the column headers with weekday names
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        #self.table_widget.setHorizontalHeaderLabels(weekdays)

        # Iterate through the days and add them to the table
        widget_object = 'widget_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet_)
        self.gridLayout = self.sample_widget.grid_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        current_date = start_date
        for row in range(5):
            for col in range(7):
                widget_object = 'widget_object'
                styleSheet_ = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.backgroundColor.get_value(),
                                                                border_radius=0)

                widget_ = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet_)
                self.treeWidgetList.append(widget_)
                if current_date.month() == start_date.month():

                    verticalLayout = self.sample_widget.vertical_layout(parent_self=widget_, set_contents_margins=(0, 0, 0, 0), set_spacing=0)


                    #DATE LABEL
                    date_label_object = 'date_label_object'
                    styleSheet_ = self.sample_widget.styleSheet_def(obj_name=date_label_object, color=self.color_class.black_color.get_value(),
                                                                    border_radius=0)
                    date_label = self.sample_widget.label(set_text=str(current_date.day()), set_alighment=self.sample_widget.center_alignment, set_object_name=date_label_object,
                                                            set_styleSheet=styleSheet_)
                    font = self.font
                    font.setPointSize(15)
                    date_label.setFont(font)
                    verticalLayout.addWidget(date_label)

                    treeWidget = self.sample_widget.treeWidget(setHeaderHidden=True)
                    treeWidget.setHeaderLabels(['Meal'])


                    #treeWidget.setHeaderLabels(['Time', 'Meal'])
                    verticalLayout.addWidget(treeWidget)

                    jsonFile = self.help_class.get_TempFileData()
                    font = QFont()
                    font.setPointSize(10)
                    date = str(current_date.day())
                    formatted_date = current_date.toString("yyyyMMdd")
                    for eachCalender in jsonFile['calender']:
                        if str(eachCalender) == formatted_date:
                            for eachday in jsonFile['calender'][eachCalender]:
                                for eachTime in jsonFile['calender'][eachCalender][eachday]:
                                    item = QTreeWidgetItem(treeWidget)
                                    item.setText(0, eachTime)
                                    item.setFont(0, font)


                self.gridLayout.addWidget(widget_, row, col, 1, 1)
                # Move to the next day
                current_date = current_date.addDays(1)


        return widget





    def update_(self, date):
        '''

        :return:
        '''
        self.currentDay = date
        self.help_class.clearLayout(self.verticalLayout)
        self.monthWidget = self.populate_dates()
        self.verticalLayout.addWidget(self.monthWidget)

    def nextWeekButton_(self, date):
        '''

        :return:
        '''
        month = self.help_class.getMonth(self.currentDay)
        if month == 12:
            year = self.help_class.getYear(self.currentDay)
            year = year + 1
            month = 1
        else:
            year = self.help_class.getYear(self.currentDay)
            month = month + 1
        self.currentDay = str(month) + '.' + str(year)

    def setMonth(self, month, year):
        '''

        :return:
        '''
        self.currentMonth = month
        self.currentYear = year
        self.currentDay = '1.' + str(self.currentMonth) + '.' + str(self.currentYear)

    def previousMonthButton_(self):
        '''

        :return:
        '''
        if self.currentMonth == 1:
            self.currentYear = self.currentYear - 1
            self.currentMonth = 12
        else:
            self.currentMonth = self.currentMonth - 1

        self.setMonth(month=self.currentMonth, year=self.currentYear)
        self.update_(date=self.currentDay)

    def nextMonthButton_(self):
        '''

        :return:
        '''
        if self.currentMonth == 12:
            self.currentYear = self.currentYear + 1
            self.currentMonth = 1
        else:
            self.currentMonth = self.currentMonth + 1

        self.setMonth(month=self.currentMonth, year=self.currentYear)
        self.update_(date=self.currentDay)












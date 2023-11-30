from datetime import datetime, timedelta
from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget.createShoppingListWidget import createShoppingList

from datetime import datetime
class calenderCenterDay_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        self.currentDay = self.parent.currentDay

        self.calenderMainWidget = self.parent.parent

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

        self.treeWidgetUpdate(date=self.currentDay)

    def initUI(self):
        '''

        :return:
        '''
        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        stakeWidget = QStackedWidget()
        verticalLayout.addWidget(stakeWidget)

        stakeWidget.addWidget(self.dateWidget(data=self.currentDay))

        return widget

    def dateWidget(self, data):
        '''

        :param data:
        :return:
        '''

        date_ = self.help_class.converDateToString(date=data)

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=0)

        #DATE LABEL
        self.date_label_object = 'date_label_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=self.date_label_object, color=self.color_class.white_color.get_value(),
                                                        border_radius=0)
        self.date_label = self.sample_widget.label(set_text=date_, set_alighment=self.sample_widget.center_alignment, set_object_name=self.date_label_object,
                                                    set_styleSheet=styleSheet_)
        font = self.font
        font.setPointSize(15)
        self.date_label.setFont(font)
        verticalLayout.addWidget(self.date_label)


        self.calenderCenterDay_treeWidget = self.sample_widget.treeWidget()
        self.calenderCenterDay_treeWidget.setHeaderLabels(['Time', 'Meal'])
        verticalLayout.addWidget(self.calenderCenterDay_treeWidget)

        #ADD TO SHOPPING LIST BUTTON
        shoppingList_object = 'shoppingList_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=shoppingList_object, color=self.color_class.black_color.get_value(),
                                                        border_radius=0)
        font = self.font
        font.setPointSize(10)

        self.shoppingList_button = self.sample_widget.pushButton(set_text='Add to Shopping List', set_object_name=shoppingList_object,
                                                                    set_styleSheet=styleSheet_,
                                                                 connect=self.shoppingListWidget_button)
        self.shoppingList_button.setFont(font)
        verticalLayout.addWidget(self.shoppingList_button)

        return widget

    def shoppingListWidget_button(self):
        '''

        :return:
        '''
        self.calenderCenterDay_treeWidget.selectAll()
        selectedItem = self.calenderCenterDay_treeWidget.selectedItems()
        self.calenderCenterDay_treeWidget.clearSelection()
        recepieList = []
        if selectedItem:
            for each in selectedItem:
                text = each.text(1)
                text = text.replace('\n', ',')
                text = text.split(',')
                for each in text:
                    if each != '':
                        recepieList.append(each)

        try:
            shoppingListWindow = createShoppingList(parent=self.parent, data=recepieList)
            shoppingListWindow.exec_()
        except Exception as e:
            import traceback
            traceback.print_exc()

    def treeWidgetUpdate(self, date=None):
        '''

        :return:
        '''
        self.calenderCenterDay_treeWidget.clear()

        time = ['01.00 PM', '02.00 PM', '03.00 PM', '04.00 PM', '05.00 PM', '06.00 PM', '07.00 PM', '08.00 PM', '09.00 PM', '10.00 PM', '11.00 PM', '12.00 PM'
                , '01.00 AM', '02.00 AM', '03.00 AM', '04.00 AM', '05.00 AM', '06.00 AM', '07.00 AM', '08.00 AM', '09.00 AM', '10.00 AM', '11.00 AM', '12.00 AM']
        time.reverse()

        jsonFile = self.help_class.get_TempFileData()
        font = self.calenderCenterDay_treeWidget.font()
        font.setPointSize(10)

        for each in time:
            item = QTreeWidgetItem(self.calenderCenterDay_treeWidget)
            item.setText(0, each)
            item.setFont(0, font)

            for eachCalender in jsonFile['calender']:
                date_str = eachCalender
                if self.currentDay == f"{date_str[6:8]}.{date_str[4:6]}.{date_str[:4]}":
                    for eachTime in jsonFile['calender'][date_str]:
                        time_str = str(eachTime)
                        time_object = datetime.strptime(time_str, "%H%M%S")
                        formatted_time = time_object.strftime("%I.%M %p")
                        if each == formatted_time:
                            text = ''
                            for each in jsonFile['calender'][date_str][eachTime]:
                                text = text + each + '\n'
                            item.setText(1, text)
                            item.setFont(1, font)

    def nextDayButton_(self, currentDay):
        '''

        :return:
        '''
        self.currentDay = currentDay

        self.date_label.setText(self.help_class.converDateToString(date=self.currentDay))
        self.treeWidgetUpdate(date=self.currentDay)



    def previousDayButton_(self, currentDay):
        '''

        :return:
        '''
        self.currentDay = currentDay

        self.date_label.setText(self.help_class.converDateToString(date=self.currentDay))
        self.treeWidgetUpdate(date=self.currentDay)

        print('this is date update')

    def currentDayButton_(self, currentDay):
        '''

        :return:
        '''
        self.currentDay = currentDay

        self.date_label.setText(self.help_class.converDateToString(date=self.currentDay))
        self.treeWidgetUpdate(date=self.currentDay)

        print('this is date update')


    def update_(self, date):
        '''

        :return:
        '''
        self.currentDayButton_(currentDay=self.currentDay)

class CustomItemDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        # Adjust the item height to add spacing
        size = super().sizeHint(option, index)
        size.setHeight(size.height() + 30)  # Increase the height by 10 (adjust as needed)
        return size
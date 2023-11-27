from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


class calenderCenterDay_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        print(self.parent)
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

        self.treeWidgetUpdate()
    def initUI(self):
        '''

        :return:
        '''
        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)


        '''
        stakeWidget = QStackedWidget()
        verticalLayout.addWidget(stakeWidget)

        for each in dateList:
            widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
            verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)
            stakeWidget.addWidget(widget)

            label = self.sample_widget.label(set_object_name=self.sampleObjectNmae)
            verticalLayout.addWidget(label)
        '''


        self.calenderCenterDay_treeWidget = self.sample_widget.treeWidget()
        self.calenderCenterDay_treeWidget.setHeaderLabels(['Time', 'Meal'])
        self.calenderCenterDay_treeWidget.setStyleSheet(styleSheet)
        item_delegate = CustomItemDelegate(self.calenderCenterDay_treeWidget)
        self.calenderCenterDay_treeWidget.setItemDelegate(item_delegate)
        verticalLayout.addWidget(self.calenderCenterDay_treeWidget)


        return widget


    def treeWidgetUpdate(self):
        '''

        :return:
        '''
        self.calenderCenterDay_treeWidget.clear()
        time = ['01.00 PM', '02.00 PM', '03.00 PM', '04.00 PM', '05.00 PM', '06.00 PM', '07.00 PM', '08.00 PM', '09.00 PM', '10.00 PM', '11.00 PM', '12.00 PM'
                , '01.00 AM', '02.00 AM', '03.00 AM', '04.00 AM', '05.00 AM', '06.00 AM', '07.00 AM', '08.00 AM', '09.00 AM', '10.00 AM', '11.00 AM', '12.00 AM']

        font = self.calenderCenterDay_treeWidget.font()
        font.setPointSize(10)

        for each in time:
            item = QTreeWidgetItem(self.calenderCenterDay_treeWidget)
            item.setText(0, each)
            item.setFont(0, font)


        '''
        for each in range(12):
            item = QTreeWidgetItem(self.calenderCenterDay_treeWidget)
            item.setText(0, 'Item {}'.format(each))
            self.calenderCenterDay_treeWidget.addTopLevelItem(item)
        '''

class CustomItemDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        # Adjust the item height to add spacing
        size = super().sizeHint(option, index)
        size.setHeight(size.height() + 30)  # Increase the height by 10 (adjust as needed)
        return size
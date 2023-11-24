from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderCenterDay_widget
from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderCenterWeek_widget
from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderCenterMonth_widget

class calenderCenter_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.calenderCenterDay_widget = calenderCenterDay_widget.calenderCenterDay_widget(self.parent)
        self.calenderCenterWeek_widget = calenderCenterWeek_widget.calenderCenterWeek_widget(self.parent)
        self.calenderCenterMonth_widget = calenderCenterMonth_widget.calenderCenterMonth_widget(self.parent)

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
    def initUI(self):
        '''


        :return:
        '''
        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        stakeWidget_object = 'stakeWidget_object'
        stakeWidget = QStackedWidget()
        stakeWidget.setStyleSheet(styleSheet)
        stakeWidget.setObjectName(stakeWidget_object)
        verticalLayout.addWidget(stakeWidget)


        stakeWidget.addWidget(self.calenderCenterDay_widget)
        stakeWidget.addWidget(self.calenderCenterWeek_widget)
        stakeWidget.addWidget(self.calenderCenterMonth_widget)

        stakeWidget.setCurrentIndex(2)

        return widget



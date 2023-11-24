from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


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
        currentDayButton = self.sample_widget.pushButton(set_text='Today', set_object_name=currentDayButton_object, set_styleSheet=styleSheet_)
        currentDayButton.setFont(font)
        horizontalLayout.addWidget(currentDayButton)

        #PREVIOU DAY BUTTON
        previousDayButton_object = 'previousDayButton_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=previousDayButton_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        previousDayButton = self.sample_widget.pushButton(set_text='<', set_object_name=previousDayButton_object, set_styleSheet=styleSheet_)
        previousDayButton.setFont(font)
        horizontalLayout.addWidget(previousDayButton)

        #NEXT DAY BUTTON
        nextDayButton_object = 'nextDayButton_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=nextDayButton_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        nextDayButton = self.sample_widget.pushButton(set_text='>', set_object_name=nextDayButton_object, set_styleSheet=styleSheet_)
        nextDayButton.setFont(font)
        horizontalLayout.addWidget(nextDayButton)

        #CALENDER LABEL BUTTON
        calenderLabelButton_object = 'calenderLabelButton_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=calenderLabelButton_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        calenderLabel = self.sample_widget.label(set_text='Today', set_alighment=self.sample_widget.center_alignment, set_object_name=calenderLabelButton_object,
                                                       set_styleSheet=styleSheet_, min_size=(0, 40))
        calenderLabel.setFont(font)
        horizontalLayout.addWidget(calenderLabel)

        horizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Maximum))

        #CALENDER SWITCH COMBOBOX
        calenderSwitchComboBox_object = 'calenderSwitchComboBox_object'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=calenderSwitchComboBox_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=0)
        calenderSwitchComboBox = self.sample_widget.comboBox(set_object_name=calenderSwitchComboBox_object, set_styleSheet=styleSheet_)
        calenderSwitchComboBox.setFont(font)
        horizontalLayout.addWidget(calenderSwitchComboBox)





        return widget



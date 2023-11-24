from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))




class recepieTop_widget(QWidget):
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

        widget = self.sample_widget.widget_def(min_size=(0, 50), max_size=(16777215, 50))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        countryList = self.help_class.totalCountry()
        country_combo_objName = 'country_combo'
        combo_styleSheet = self.sample_widget.styleSheet_def(obj_name=country_combo_objName, color=self.color_class.white_color.get_value(),
                                                             background=self.color_class.black_color.get_value(),
                                                                border_radius=5)

        country_combo = self.sample_widget.comboBox(parent_self=widget, set_object_name=country_combo_objName, addItems=countryList,
                                                    set_styleSheet=combo_styleSheet, setEditable=True)
        country_combo.setMinimumSize(QSize(0, 30))
        country_combo.setMaximumSize(QSize(16777215, 30))
        country_combo.setFont(self.font)
        horizontalLayout.addWidget(country_combo)

        peopleLabel_objName = 'peopleLabel'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=peopleLabel_objName, color=self.color_class.white_color.get_value())

        peopleLabel = self.sample_widget.label(set_object_name=peopleLabel_objName, set_text='People', set_styleSheet=styleSheet_,
                                               set_alighment=self.sample_widget.center_alignment)
        font = self.font
        font.setPointSize(10)
        peopleLabel.setFont(font)
        horizontalLayout.addWidget(peopleLabel)

        peopleSpine_objName = 'peopleSpine'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=peopleSpine_objName, color=self.color_class.white_color.get_value(),
                                                        background=self.backgroundColor.get_value(),
                                                        border_radius=5)
        peopleSpinBox = QSpinBox(widget)
        peopleSpinBox.setMinimumSize(QSize(0, 30))
        peopleSpinBox.setMaximumSize(QSize(16777215, 30))
        peopleSpinBox.setFont(self.font)
        peopleSpinBox.setObjectName(peopleSpine_objName)
        peopleSpinBox.setStyleSheet(styleSheet_)
        peopleSpinBox.setMinimum(1)
        peopleSpinBox.setMaximum(10000)
        horizontalLayout.addWidget(peopleSpinBox)


        return widget
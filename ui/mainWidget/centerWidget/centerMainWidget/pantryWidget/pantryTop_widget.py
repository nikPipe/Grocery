from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))

from ui.mainWidget.centerWidget.centerMainWidget.recepieWidget import recepieDetail_widget


class pantryTop_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.recepieDetail_widget = recepieDetail_widget.recepieDetail_widget(self.parent)


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
        height = 1000
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))


        buttonOne = self.sample_widget.pushButton(set_text='',
                                                  min_size=(50, 50),
                                                  max_size=(50, 50))
        horizontalLayout.addWidget(buttonOne)

        buttonTwo = self.sample_widget.pushButton(set_text='',
                                                  min_size=(50, 50),
                                                  max_size=(50, 50))
        horizontalLayout.addWidget(buttonTwo)

        buttonThree = self.sample_widget.pushButton(set_text='',
                                                    min_size=(50, 50),
                                                    max_size=(50, 50))
        horizontalLayout.addWidget(buttonThree)

        horizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Maximum))

        label_objectName = 'labelStyleSheet'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=label_objectName,
                                                       color=self.color_class.white_color.get_value())

        label = self.sample_widget.label(set_text='Pantry', set_object_name=label_objectName, set_styleSheet=styleSheet_,
                                         set_alighment=self.sample_widget.center_alignment)
        font = self.font
        font.setPointSize(20)
        font.setBold(True)
        label.setFont(font)
        horizontalLayout.addWidget(label)

        horizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Maximum))

        filterLineEdit = self.sample_widget.line_edit(set_PlaceholderText='Search')
        val = 25
        filterLineEdit.setMinimumSize(QSize(200, val))
        filterLineEdit.setMaximumSize(QSize(200, val))
        horizontalLayout.addWidget(filterLineEdit)


        return widget





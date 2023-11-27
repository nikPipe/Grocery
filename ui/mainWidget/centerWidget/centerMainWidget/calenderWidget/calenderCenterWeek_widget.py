from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


class calenderCenterWeek_widget(QWidget):
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
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=5)


        for each in range(7):
            horizontalLayout.addWidget(self.weekWidget())


        return widget


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
from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))



class alertMainWidget(QWidget):
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

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)



    def initUI(self):
        '''


        :return:
        '''

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0),
                                                            set_spacing=8)

        verticalLayout.addWidget(self.widget())
        verticalLayout.addWidget(self.widget())

        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


        return widget


    def widget(self):
        '''

        :return:
        '''
        widget_object = 'alertMainWidget'
        height= 200
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.backgroundColor.get_value(),
                                                        border_radius=20)
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet_,
                                               min_size=(0, height), max_size=(self.sample_widget.max_size, height))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))


        button = self.sample_widget.pushButton(set_text='Alert')
        verticalLayout.addWidget(button)

        return widget
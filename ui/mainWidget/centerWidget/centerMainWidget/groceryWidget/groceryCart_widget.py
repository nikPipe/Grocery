
from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget.groceryWidget import groceryItem_widget


class groceryCart_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        self.groceryItem_widget = groceryItem_widget.groceryItem_widget(self)

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
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet,
                                               min_size=(300, 0), max_size=(self.sample_widget.max_size, self.sample_widget.max_size))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)


        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        verticalLayout.addWidget(scrollArea)
        object_name = 'scrollAreaWidgetContents'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=object_name, background_color=self.color.get_value())
        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=object_name, set_styleSheet=styleSheet_)
        scrollArea.setWidget(scrollAreaWidgetContents)

        verticalLayout_ = self.sample_widget.vertical_layout(parent_self=scrollAreaWidgetContents, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        verticalLayout_.addWidget(self.groceryItem_widget)

        verticalLayout_.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


        return widget


    def widgetTest(self, name):
        '''

        :return:
        '''
        obj_name = 'groceryCartWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=obj_name,
                                                       background_color=self.color_class.red_color.get_value(),
                                                       border_color=self.color_class.black_color.get_value(),
                                                       border_radius=10)

        widget = self.sample_widget.widget_def(min_size=(0, 200), max_size=(self.sample_widget.max_size, 200),
                                               set_object_name=obj_name, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        pushButton = self.sample_widget.pushButton(set_text=name)
        verticalLayout.addWidget(pushButton)

        return widget





















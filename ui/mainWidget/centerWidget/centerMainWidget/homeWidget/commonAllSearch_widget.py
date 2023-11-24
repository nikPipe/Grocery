


from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


class commonAllSearch_Widget(QWidget):
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
        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        verticalLayout.addWidget(self.searchWidget())
        verticalLayout.addWidget(self.mealViewWidget())

        verticalLayout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        return widget



    def searchWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        lineEdit_object = 'lineEdit_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=lineEdit_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        self.lineEdit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet)
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setMaximumSize(QSize(16777215, 40))
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setPlaceholderText('Search the Meal')
        #lineEdit.textChanged.connect(self.lineEditTextChanged)
        verticalLayout.addWidget(self.lineEdit)


        return widget


    def mealViewWidget(self):
        '''

        :return:
        '''
        height = 180
        widget_object = 'mealViewWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                         border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(min_size=(0, height), max_size=(self.sample_widget.max_size, height),
                                               set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        verticalLayout.addWidget(scrollArea)
        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        scrollArea.setWidget(scrollAreaWidgetContents)

        horizontalLayout_ = self.sample_widget.horizontal_layout(parent_self=scrollAreaWidgetContents, set_spacing=10,)
        width = 250
        height = 150
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        for each in range(0, 4):
            pushButton_object = 'pushButton_object'
            styleSheet = self.sample_widget.styleSheet_def(obj_name=pushButton_object,
                                                           background_color=self.backgroundColor.get_value(),
                                                           border_radius=20)

            pushButton = self.sample_widget.pushButton(set_text='mealtime', min_size=(width, height),
                                                       max_size=(width, height),
                                                       set_styleSheet=styleSheet, set_object_name=pushButton_object)
            pushButton.setFont(font)

            horizontalLayout_.addWidget(pushButton)





        return widget
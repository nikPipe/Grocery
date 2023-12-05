from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))



class savedGroceryLeft_widget(QWidget):
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
        height = 1000
        width = 200
        widget = self.sample_widget.widget_def(min_size=(width, height), max_size=(width, height))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        verticalLayout.addWidget(self.name_button())

        verticalLayout.addWidget(self.savedRecepieTreeWidget())

        return widget


    def name_button(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        label_objectName = 'label'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=label_objectName, color=self.color_class.white_color.get_value())

        label = self.sample_widget.label(set_text='Saved Grocery', set_object_name=label_objectName, set_styleSheet=styleSheet_,
                                         set_alighment=self.sample_widget.center_alignment)
        label.setFont(self.font)
        horizontalLayout.addWidget(label)

        button = self.sample_widget.pushButton(set_text='', min_size=(30, 30), max_size=(30, 30))
        horizontalLayout.addWidget(button)

        return widget


    def savedRecepieTreeWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        treeWidget = self.sample_widget.treeWidget(setHeaderHidden=True)
        verticalLayout.addWidget(treeWidget)

        for each in range(3):
            item = QTreeWidgetItem(treeWidget)
            item.setText(0, 'Item {}'.format(each))
            treeWidget.addTopLevelItem(item)


        return widget


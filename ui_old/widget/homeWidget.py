from ui_old.import_module import *
from ui_old.sampleWidget import sample_widget_template

from data import help



class homeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.help = help.Help()


        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)


    def initUI(self):
        '''
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        space = self.sample_widget.spaceItem()
        verticalLayout.addItem(space)

        lineedit = self.sample_widget.line_edit(set_PlaceholderText='Search the Product')
        verticalLayout.addWidget(lineedit)

        return widget
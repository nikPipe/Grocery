from ui_old.import_module import *
from ui_old.sampleWidget import sample_widget_template
import json



class profileWidget(QWidget):
    def __init__(self):
        super(profileWidget, self).__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)







        return widget
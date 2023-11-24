from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template




class cartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        width = 800

        verticalLayout.addWidget(widget)


    def initUI(self):
        '''

        :return:
        '''

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        cartLabel = self.sample_widget.label(set_text='Cart')
        verticalLayout.addWidget(cartLabel)

        cartTreeWidget = self.sample_widget.treeWidget()
        verticalLayout.addWidget(cartTreeWidget)

        return widget



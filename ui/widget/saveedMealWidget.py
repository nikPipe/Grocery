from ui.import_module import *
from ui.sampleWidget import sample_widget_template


from ui.widget import leftWidget


class saveedMealWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.leftWidget_ = leftWidget.lefWidget()

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

        lineEdit = self.sample_widget.line_edit(set_PlaceholderText='Search The Grocery name')
        lineEdit.setAlignment(Qt.AlignCenter)
        verticalLayout.addWidget(lineEdit)

        return widget






















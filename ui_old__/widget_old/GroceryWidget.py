from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template


from ui_old__.widget_old import leftWidget
from ui_old__.widget_old import cartWidget


class GroceryWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.leftWidget_ = leftWidget.lefWidget()
        self.cartWidget_ = cartWidget.cartWidget()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        width = 800

        verticalLayout.addWidget(widget)


    def initUI(self):
        '''


        :return:
        '''

        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        lineEdit = self.sample_widget.line_edit(set_PlaceholderText='another Grocery name')
        lineEdit.setAlignment(Qt.AlignCenter)
        horizontalLayout.addWidget(lineEdit)

        horizontalLayout.addWidget(self.cartWidget_)


        return widget






















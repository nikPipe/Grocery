from ui_OldOne.import_module import *
from ui_OldOne.sampleWidget import sample_widget_template

class midWidget_shoppingWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.shoppingListLabelWidget())
        verticalLayout.addWidget(self.shoppingListWidget())

        return widget

    def shoppingListLabelWidget(self):
        '''
        :return:
        '''
        widget = self.sample_widget.widget_def(min_size=(0, 30), max_size=(16777215, 30))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        label = self.sample_widget.label(set_text='Shopping List', set_alighment=self.sample_widget.left_alignment)
        horizontalLayout.addWidget(label)

        horizontalLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        button = self.sample_widget.pushButton(set_text='Add')
        horizontalLayout.addWidget(button)

        button = self.sample_widget.pushButton(set_text='Delete')
        horizontalLayout.addWidget(button)

        return widget


    def shoppingListWidget(self):
        '''
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)
        verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        return widget







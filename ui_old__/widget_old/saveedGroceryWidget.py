from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template


from ui_old__.widget_old import leftWidget


class saveedGroceryWidget(QWidget):
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

        split = self.sample_widget.splitter_def(parent_self=widget,
            set_orientation=self.sample_widget.horizonatal)
        verticalLayout.addWidget(split)

        split.addWidget(self.catgoryWidget())
        split.addWidget(self.allGroceryWidget())

        return widget


    def catgoryWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        treeWidget = self.sample_widget.treeWidget()
        verticalLayout.addWidget(treeWidget)

        return widget


    def allGroceryWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        treeWidget = self.sample_widget.treeWidget()
        verticalLayout.addWidget(treeWidget)

        return widget





















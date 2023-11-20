from ui_OldOne.import_module import *
from ui_OldOne.sampleWidget import sample_widget_template


from ui_OldOne.widget import topWidget
from ui_OldOne.widget import midWidget
from ui_OldOne.widget import bottomWidget

class mainWidget(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.topWidget = topWidget.topWidget()
        self.midWidget = midWidget.midWidget()
        self.bottomWidget = bottomWidget.bottomWidget()

        self.initUI()  # Call the UI setup method
        self.show()


    def initUI(self):
        # Set window size.
        self.resize(1200, 800)

        # Set window title
        self.setWindowTitle('Meal Planner')

        widget = self.uiWidget()
        self.setCentralWidget(widget)

    def uiWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.topWidget)
        verticalLayout.addWidget(self.midWidget)
        verticalLayout.addWidget(self.bottomWidget)

        return widget




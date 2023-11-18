from ui.import_module import *
from ui.sampleWidget import sample_widget_template



class topWidget(QWidget):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)
        verticalLayout.setAlignment(Qt.AlignTop)


    def initUI(self):
        widget = self.sample_widget.widget_def(min_size=(0, 30), max_size=(16777215, 30))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        size = 30
        maintopButton = self.sample_widget.pushButton(set_text='', min_size=(size, size), max_size=(size, size))
        horizontalLayout.addWidget(maintopButton)


        windowName = self.sample_widget.label(set_text='Meal Planner', set_alighment=self.sample_widget.center_alignment)
        horizontalLayout.addWidget(windowName)


        horizontalLayout.addWidget(self.window_minimize_maximize())



        return widget

    def window_minimize_maximize(self):
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)


        size = 30
        minimizeButton = self.sample_widget.pushButton(set_text='', min_size=(size, size), max_size=(size, size))
        horizontalLayout.addWidget(minimizeButton)

        maximizeButton = self.sample_widget.pushButton(set_text='', min_size=(size, size), max_size=(size, size))
        horizontalLayout.addWidget(maximizeButton)

        closeButton = self.sample_widget.pushButton(set_text='', min_size=(size, size), max_size=(size, size))
        horizontalLayout.addWidget(closeButton)

        horizontalLayout.setAlignment(Qt.AlignRight)




        return widget







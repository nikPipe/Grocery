from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template



class mainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

        self.initUI()

    def initUI(self):
        # Set window size.
        self.resize(800, 800)

        # Set window title
        self.setWindowTitle('Meal Planner')

        widget = self.uiWidget()
        self.setCentralWidget(widget)

        # Show window

    def uiWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        button = self.sample_widget.pushButton(set_text='another window showing', connect=self.buttonClicked)
        verticalLayout.addWidget(button)

        return widget

    def buttonClicked(self):
        print('buttonClicked')
        self.close()
        print('something is happening')

















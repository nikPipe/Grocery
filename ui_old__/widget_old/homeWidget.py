from ui_old__.import_module import *
from ui_old__.sampleWidget import sample_widget_template


from ui_old__.widget_old import leftWidget


class HomeWidget(QWidget):
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


        text = ''
        text += 'Welcome to the Meal Planner App(also do change the background based on time to easy to make)\n'
        text += '\n'
        text += 'Quick Search bar to save Grocery Meal and pantary\n'
        text += 'next Meal Plan\n'
        text += 'pantary information\n'
        text += 'Reminder list\n'
        text += 'Tips\n'
        text += 'give infomration new thing to try in the resturant\n'
        text += 'give infomration new thing to try in holiday season\n'
        text += 'help us to find your favorite meal\n'






        plainTextEdit = self.sample_widget.plainTextEdit()
        plainTextEdit.setPlainText(text)
        verticalLayout.addWidget(plainTextEdit)

        return widget






















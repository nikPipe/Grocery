



from ui.widget import introductionWidget
from ui.widget import mainWidget
from ui.import_module import *
from data import help

#widget = mainWidget.MainWidget()
import sys

help_class = help.Help()


def introductionWidget_main():
    app = QApplication(sys.argv)
    ex = introductionWidget.mainWidget()
    sys.exit(app.exec_())

def mainWidget_main():
    app = QApplication(sys.argv)
    ex = mainWidget.mainWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    if help_class.getTempFile(name=help_class.tempFileName):
        mainWidget_main()
    else:
        introductionWidget_main()
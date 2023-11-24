from import_module import *
from data import help

#widget_old = mainWidget.MainWidget()
import sys
from ui.introduction_widget import introductionMainWidget
from ui.mainWidget import mainWindow

help_class = help.Help()


def mainWidget_main():
    app = QApplication(sys.argv)
    ex = mainWindow.mainWidget()
    sys.exit(app.exec_())


def introductionWidget_main():
    app = QApplication(sys.argv)
    ex = introductionMainWidget.mainWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if help_class.getTempFile(name=help_class.tempFileName):
        print(help_class.getTempFile(name=help_class.tempFileName))
        mainWidget_main()
    else:
        introductionWidget_main()
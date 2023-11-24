from ui_OldOne.widget import mainWIndow
from ui_old.import_module import *


#widget_old = mainWidget.MainWidget()
import sys



def main():
    app = QApplication(sys.argv)
    ex = mainWIndow.mainWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
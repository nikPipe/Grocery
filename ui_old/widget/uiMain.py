from ui_old.widget import mainWidget
from ui_old.import_module import *


#widget_old = mainWidget.MainWidget()
import sys



def main():
    app = QApplication(sys.argv)
    ex = mainWidget.mainWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
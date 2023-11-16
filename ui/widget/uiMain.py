from ui.widget import mainWidget
from ui.import_module import *


#widget = mainWidget.MainWidget()
import sys



def main():
    app = QApplication(sys.argv)
    ex = mainWidget.mainWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
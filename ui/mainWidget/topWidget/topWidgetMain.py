from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))



class topMainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        verticalLayout = QVBoxLayout(self)
        widget = self.initUI()
        verticalLayout.addWidget(widget)

    def initUI(self):
        '''

        :return:
        '''
        val = 40
        widget = self.sample_widget.widget_def(min_size=(0, val), max_size=(self.sample_widget.max_size, val))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        #MENU BUTTON
        menuButton_object = 'menuButton_object'
        menuIconPath = file + "/icon/menu.jpg"

        menuButton = self.sample_widget.pushButton(set_text='',
                                                   min_size=(50, 50),
                                                    max_size=(50, 50),
                                                   set_icon=menuIconPath,
                                                   set_icon_size=(50, 50),)
        horizontalLayout.addWidget(menuButton)

        #NAME
        nameObject = 'nameObject'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=nameObject, color=self.color_class.white_color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        name = self.sample_widget.label(set_text='Name', set_alighment=self.sample_widget.center_alignment, set_object_name=nameObject,
                                        set_styleSheet=styleSheet)
        font = QFont()
        font.setBold(True)
        font.setPointSize(15)
        name.setFont(font)
        horizontalLayout.addWidget(name)

        #SEARCH
        searchIcon = file + "/icon/search.jpg"
        search = self.sample_widget.pushButton(set_text='', set_icon=searchIcon, set_icon_size=(50, 50),
                                               min_size=(50, 50),
                                               max_size=(50, 50),
                                               connect=self.searchWidget)
        horizontalLayout.addWidget(search)

        #NOTIFICATION
        notificationIcon = file + "/icon/notification.jpg"
        notification = self.sample_widget.pushButton(set_text='', set_icon=notificationIcon, set_icon_size=(50, 50),
                                               min_size=(50, 50),
                                               max_size=(50, 50),
                                                     connect=partial(self.centerWidgetSwitch, value=9))
        horizontalLayout.addWidget(notification)

        #USER
        userIcon = file + "/icon/user.jpg"
        user = self.sample_widget.pushButton(set_text='', set_icon=userIcon, set_icon_size=(50, 50),
                                               min_size=(50, 50),
                                               max_size=(50, 50),
                                             connect=partial(self.centerWidgetSwitch, value=10))
        horizontalLayout.addWidget(user)

        horizontalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        return widget

    def centerWidgetSwitch(self, value):
        '''

        :param widget:
        :return:
        '''
        self.parent.mainCenterWidget.centerMainWidget.stackedWidget.setCurrentIndex(value)


    def searchWidget(self):
        '''

        :return:
        '''
        print('searchWidget')
        self.parent.mainCenterWidget.centerMainWidget.stackedWidget.setCurrentIndex(0)

        self.parent.mainCenterWidget.centerMainWidget.homeWidgetMain.stakeWidget.setCurrentIndex(1)
















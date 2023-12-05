from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget import mealWidget_sample



class savedGrocery_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()

        self.parent = parent
        self.mainWidget = self.parent.parent.parent.parent
        self.getCookingSkillList = []

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)
        self.sampleObjectNmae = 'labelStyleSheet'
        self.labelStyleSheet = self.sample_widget.styleSheet_def(obj_name=self.sampleObjectNmae,
                                                                 color=self.color_class.white_color.get_value())

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)


    def initUI(self):
        '''

        :return:
        '''

        objectName = 'savedGroceryWidget'
        height = 200
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=objectName, background_color=self.color_class.gray_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=objectName, set_styleSheet=styleSheet_,
                                               min_size=(0, height), max_size=(self.sample_widget.max_size, height))
        size = 5
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_contents_margins=(size, size, size, size),
                                                                set_spacing=5)


        #MAIN ITEM WIDGET
        mainItemWidget = self.mainItemWidget()
        horizontalLayout.addWidget(mainItemWidget)

        #NAME PRODUCT PRICE WIDGET
        nameProduct_priceWidget = self.nameProduct_priceWidget()
        horizontalLayout.addWidget(nameProduct_priceWidget)

        #SUPERSTORE RECEPIE WIDGET
        superstore_recepieWidget = self.superstore_recepieWidget()
        horizontalLayout.addWidget(superstore_recepieWidget)


        return widget


    def mainItemWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        size = 150
        object = 'mainItemWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.color.get_value(),
                                                        color=self.color_class.white_color.get_value(),
                                                        border_radius=20)
        pushButton = self.sample_widget.pushButton(set_text='test', min_size=(size, size), max_size=(size, size),
                                                   set_styleSheet=styleSheet_, set_object_name=object)
        gridLayout.addWidget(pushButton, 0, 0, 1, 1)

        return widget

    def nameProduct_priceWidget(self):
        '''

        :return:
        '''

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))

        objectName = 'nameProduct_priceWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=objectName, color=self.color_class.white_color.get_value())
        name_label = self.sample_widget.label(set_text='Name of the Product', set_object_name=objectName, set_styleSheet=styleSheet_,
                                              set_alighment=self.sample_widget.center_alignment)
        font = self.font
        font.setPointSize(15)
        name_label.setFont(font)
        verticalLayout.addWidget(name_label)

        objectName = 'nameProduct_priceWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=objectName, color=self.color_class.white_color.get_value())
        price_label = self.sample_widget.label(set_text='Product Price', set_object_name=objectName, set_styleSheet=styleSheet_,
                                               set_alighment=self.sample_widget.center_alignment)
        price_label.setFont(font)
        verticalLayout.addWidget(price_label)

        return widget


    def superstore_recepieWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0))
        width_height = 80

        object = 'superstore_recepieWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=object, color=self.color.get_value(),
                                                        background=self.backgroundColor.get_value(),
                                                        border_radius=5)
        superstoreButton = self.sample_widget.pushButton(set_text='Superstore', min_size=(width_height, width_height), max_size=(width_height, width_height),
                                                         set_styleSheet=styleSheet_, set_object_name=object)
        verticalLayout.addWidget(superstoreButton)

        object = 'recepieWidget'
        styleSheet_ = self.sample_widget.styleSheet_def(obj_name=object, color=self.color.get_value(),
                                                        background=self.backgroundColor.get_value(),
                                                        border_radius=5)
        recepieButton = self.sample_widget.pushButton(set_text='Recepie', min_size=(width_height, width_height), max_size=(width_height, width_height),
                                                         set_styleSheet=styleSheet_, set_object_name=object)
        verticalLayout.addWidget(recepieButton)

        return widget


















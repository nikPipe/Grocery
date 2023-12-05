
from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


class groceryItem_widget(QWidget):
    def __init__(self, parent, addItemButton=None):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []
        self.addItemButton = addItemButton

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.grayColor = self.color_class.setColorVal(r=149, g=149, b=149)
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
        object = 'groceryItemWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.backgroundColor.get_value(),
                                                         border_radius=10)
        widget = self.sample_widget.widget_def(set_object_name=object, set_styleSheet=styleSheet)
        size= 5
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(size, size, size, size), set_spacing=10)

        #NAME OF THE PRODUCT
        verticalLayout.addWidget(self.topWidget())

        verticalLayout.addWidget(self.bottomWidget())

        if self.addItemButton:
            verticalLayout.addWidget(self.addItemButton)

        return widget

    def topWidget(self):
        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget, set_spacing=10, set_contents_margins=(0, 0, 0, 0))

        #NAME OF THE PRODUCT
        laebel = self.sample_widget.label(set_text='Name of the product', set_alighment=self.sample_widget.center_alignment)
        font = self.font
        font.setPointSize(12)
        laebel.setFont(font)
        gridLayout.addWidget(laebel, 0, 0, 1, 1)

        #SAVE BUTTON
        widhth_height = 40
        object = 'groceryItemWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.grayColor.get_value(),
                                                            border_radius=20)
        button = self.sample_widget.pushButton(set_text='Save', set_object_name=object, set_styleSheet=styleSheet,
                                                    min_size=(widhth_height, widhth_height), max_size=(widhth_height, widhth_height))

        button.setFont(font)
        gridLayout.addWidget(button, 0, 1, 1, 1)


        #Superstore
        object = 'groceryItemWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.grayColor.get_value(),
                                                            border_radius=20)
        laebel = self.sample_widget.pushButton(set_text='', set_object_name=object, set_styleSheet=styleSheet,
                                                  min_size=(widhth_height, widhth_height), max_size=(widhth_height, widhth_height))
        icon_path = "C:/Users/Admin/Desktop/Nikheel/GroceryMain/Grocery/groceryData/superStore/walmart.jpg"
        icon = QIcon(icon_path)
        laebel.setIcon(icon)
        laebel.setIconSize(QSize(40, 40))
        gridLayout.addWidget(laebel, 0, 2, 1, 1)

        return widget

    def bottomWidget(self):

        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget, set_spacing=10, set_contents_margins=(0, 0, 0, 0))

        # PRODUCT IMAGE
        widhth_height = 100
        object = 'groceryItemWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.color.get_value(),
                                                         border_radius=10)
        button = self.sample_widget.pushButton(set_text='Product Image',
                                               min_size=(widhth_height, widhth_height),
                                               max_size=(widhth_height, widhth_height),
                                               set_object_name=object, set_styleSheet=styleSheet)
        gridLayout.addWidget(button, 1, 0, 1, 1)

        # PRODUCT INFORMATION
        gridLayout.addWidget(self.totalValueInformation_addRemoveWidget(), 1, 1, 1, 1)

        return widget

    def totalValueInformation_addRemoveWidget(self):

        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=10)

        verticalLayout.addWidget(self.totalValueInformation())
        verticalLayout.addWidget(self.addRemoveWidget())

        return widget

    def totalValueInformation(self):
        '''
        This method will return the total value of the grocery item
        :return:
        '''
        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget, set_spacing=10, set_contents_margins=(0, 0, 0, 0))

        #TOTAL VALUE
        laebel = self.sample_widget.label(set_text='Total Value', set_alighment=self.sample_widget.center_alignment)
        font = self.font
        font.setPointSize(12)
        laebel.setFont(font)
        gridLayout.addWidget(laebel, 0, 0, 1, 1)

        #INFORAMTION BUTTON
        widhth_height = 40
        object = 'groceryItemWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.grayColor.get_value(),
                                                            border_radius=20)
        button = self.sample_widget.pushButton(set_text='I', set_object_name=object, set_styleSheet=styleSheet,
                                               min_size=(widhth_height, widhth_height), max_size=(widhth_height, widhth_height))
        gridLayout.addWidget(button, 0, 1, 1, 1)

        return widget

    def addRemoveWidget(self):
        '''

        :return:
        '''
        objcect = 'groceryItemWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=objcect,
                                                            border_radius=10)
        widget = self.sample_widget.widget_def(set_object_name=objcect, set_styleSheet=styleSheet)
        gridLayout = self.sample_widget.grid_layout(parent_self=widget, set_spacing=1, set_contents_margins=(1, 1, 1, 1))

        #ADD BUTTON
        widhth_height = 40
        object = 'groceryItemWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.grayColor.get_value(),
                                                            border_radius=20)
        button = self.sample_widget.pushButton(set_text='-', set_object_name=object,
                                                  set_styleSheet=styleSheet,
                                               min_size=(widhth_height, widhth_height), max_size=(widhth_height, widhth_height))
        font = self.font
        font.setPointSize(12)
        button.setFont(font)
        gridLayout.addWidget(button, 0, 0, 1, 1)

        #LINEEDIT
        object = 'groceryItemWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.color_class.red_color.get_value(),
                                                            border_radius=20)
        lineEdit = self.sample_widget.line_edit(set_object_name=object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(12)
        lineEdit.setFont(font)
        lineEdit.setValidator(QIntValidator())
        lineEdit.setText('1')
        lineEdit.setAlignment(Qt.AlignCenter)

        gridLayout.addWidget(lineEdit, 0, 1, 1, 1)

        #REMOVE BUTTON
        object = 'groceryItemWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object, background_color=self.grayColor.get_value(),
                                                            border_radius=20)
        button = self.sample_widget.pushButton(set_text='+', set_object_name=object,
                                                    set_styleSheet=styleSheet,
                                               min_size=(widhth_height, widhth_height), max_size=(widhth_height, widhth_height))
        font = self.font
        font.setPointSize(12)
        button.setFont(font)
        gridLayout.addWidget(button, 0, 2, 1, 1)

        return widget



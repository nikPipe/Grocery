from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
from ui import commonButton


class thankyouWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        width = 800

        verticalLayout.addWidget(widget)


    def initUI(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget,  set_spacing=10)

        gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 0, 0, 1, 1)

        userButton = commonButton.button_def(objName='userButton',
                                             color=self.color_class.white_color.get_value(),
                                             backgroundColor=self.color_class.setColorVal(r=141, g=141,
                                                                                          b=141).get_value(),
                                             val=15, name='')
        userButton.setIcon(QIcon('ui/icon/profile.jpg'))
        userButton.setIconSize(QSize(200, 200))
        userButton.setMinimumSize(QSize(200, 200))
        userButton.setMaximumSize(QSize(200, 200))
        gridLayout.addWidget(userButton, 1, 0, 1, 1)


        #THANK YOU
        thank_you_label = commonButton.label_def(objName='thank_you_label', color=self.color_class.white_color.get_value(), val=20, name='Thank You')
        gridLayout.addWidget(thank_you_label, 2, 0, 1, 1)

        #For setting up your profile
        instruction_label = commonButton.label_def(objName='instruction_label',
                                                    color=self.color_class.white_color.get_value(),
                                                    val=15, name='For setting up your profile')
        gridLayout.addWidget(instruction_label, 3, 0, 1, 1)

        #you are all teh set to start
        instruction_label = commonButton.label_def(objName='instruction_label',
                                                    color=self.color_class.white_color.get_value(),
                                                    val=15, name='You are all the set to start')
        gridLayout.addWidget(instruction_label, 4, 0, 1, 1)

        next_button = commonButton.button_def(objName='next_button',
                                                color=self.color_class.white_color.get_value(),
                                                backgroundColor=self.color_class.setColorVal(r=141, g=141,
                                                                                            b=141).get_value(),
                                                val=15, name='Finish', connect=self.setValue)
        next_button.setMinimumSize(QSize(350, 54))
        gridLayout.addWidget(next_button, 5, 0, 1, 1)
        '''

        welcomeTo_object = 'welcomeTo'
        welcomeTo_styleSheet = self.sample_widget.styleSheet_def(obj_name=welcomeTo_object,
                                                                 color=self.color_class.white_color.get_value(),
                                                                 font_size=40)
        font = QFont()
        font.setBold(True)
        font.setPointSize(20)
        welcomeTo = self.sample_widget.pushButton(set_object_name=welcomeTo_object,
                                                    set_styleSheet=welcomeTo_styleSheet,
                                                    set_text='',
                                                  min_size=[200, 200])
        icon = QIcon()
        icon.addPixmap(QPixmap("ui/icon/profile.jpg"), QIcon.Normal, QIcon.Off)
        welcomeTo.setFont(font)
        gridLayout.addWidget(welcomeTo, 1, 0, 1, 1)

        #FIRST NAME LABLE
        first_name_object = 'first_name'
        first_name_styleSheet = self.sample_widget.styleSheet_def(obj_name=first_name_object,
                                                                 color=self.color_class.white_color.get_value(),
                                                                 font_size=40,)
        first_name = self.sample_widget.label(set_object_name=first_name_object,
                                                    set_styleSheet=first_name_styleSheet,
                                                    set_text='First Name', set_alighment=self.sample_widget.center_alignment)
        first_name.setFont(font)
        gridLayout.addWidget(first_name, 2, 0, 1, 1)

        
        #FIRST NAME LINEEDIT
        first_name_lineEdit_object = 'first_name_lineEdit'
        first_name_lineEdit_styleSheet = self.sample_widget.styleSheet_def(obj_name=first_name_lineEdit_object,
                                                                 color=self.color_class.black_color.get_value(),
                                                                 font_size=40, border_radius=10)
        first_name_lineEdit = self.sample_widget.line_edit(set_object_name=first_name_lineEdit_object,
                                                           set_styleSheet=first_name_lineEdit_styleSheet,
                                                           set_PlaceholderText='First Name')
        first_name_lineEdit.setFont(font)
        gridLayout.addWidget(first_name_lineEdit, 2, 1, 1, 1)

        #LAST NAME LABLE
        last_name_object = 'last_name'
        last_name_styleSheet = self.sample_widget.styleSheet_def(obj_name=last_name_object,
                                                                 color=self.color_class.white_color.get_value(),
                                                                 font_size=40)
        last_name = self.sample_widget.label(set_object_name=last_name_object,
                                                    set_styleSheet=last_name_styleSheet,
                                                    set_text='Last Name', set_alighment=self.sample_widget.center_alignment)
        last_name.setFont(font)
        gridLayout.addWidget(last_name, 3, 0, 1, 1)

        last_name_lineEdit_object = 'last_name_lineEdit'
        last_name_lineEdit_styleSheet = self.sample_widget.styleSheet_def(obj_name=last_name_lineEdit_object,
                                                                 color=self.color_class.black_color.get_value(),
                                                                 font_size=40, border_radius=10)
        last_name_lineEdit = self.sample_widget.line_edit(set_object_name=last_name_lineEdit_object,
                                                              set_styleSheet=last_name_lineEdit_styleSheet,
                                                              set_PlaceholderText='Last Name')
        last_name_lineEdit.setFont(font)
        gridLayout.addWidget(last_name_lineEdit, 3, 1, 1, 1)

        #EMAIL LABLE
        email_object = 'email'
        email_styleSheet = self.sample_widget.styleSheet_def(obj_name=email_object,
                                                                 color=self.color_class.white_color.get_value(),
                                                                 font_size=40)
        email = self.sample_widget.label(set_object_name=email_object,
                                                    set_styleSheet=email_styleSheet,
                                                    set_text='Email', set_alighment=self.sample_widget.center_alignment)
        email.setFont(font)
        gridLayout.addWidget(email, 4, 0, 1, 1)

        #EMAIL LINEEDIT
        email_lineEdit_object = 'email_lineEdit'
        email_lineEdit_styleSheet = self.sample_widget.styleSheet_def(obj_name=email_lineEdit_object,
                                                                 color=self.color_class.black_color.get_value(),
                                                                 font_size=40, border_radius=10)
        email_lineEdit = self.sample_widget.line_edit(set_object_name=email_lineEdit_object,
                                                                set_styleSheet=email_lineEdit_styleSheet,
                                                                set_PlaceholderText='Email')
        email_lineEdit.setFont(font)

        gridLayout.addWidget(email_lineEdit, 4, 1, 1, 1)

        #cOUNTRY LABLE
        country_object = 'country'
        country_styleSheet = self.sample_widget.styleSheet_def(obj_name=country_object,
                                                                 color=self.color_class.white_color.get_value(),
                                                                 font_size=40)
        country = self.sample_widget.label(set_object_name=country_object,
                                                    set_styleSheet=country_styleSheet,
                                                    set_text='Country', set_alighment=self.sample_widget.center_alignment)
        country.setFont(font)
        gridLayout.addWidget(country, 5, 0, 1, 1)

        #COUNTRY LINEEDIT
        country_lineEdit_object = 'country_lineEdit'
        country_lineEdit_styleSheet = self.sample_widget.styleSheet_def(obj_name=country_lineEdit_object,
                                                                 color=self.color_class.black_color.get_value(),
                                                                 font_size=40, border_radius=10)
        countryList = self.help_class.totalCountry()
        country_lineEdit = self.sample_widget.comboBox(addItems=countryList, setEditable=True)
        country_lineEdit.setFont(font)
        gridLayout.addWidget(country_lineEdit, 5, 1, 1, 1)

        #NEXT BUTTON
        next_object = 'next'
        color = self.color_class.setColorVal(r=141, g=141, b=141)
        next_styleSheet = self.sample_widget.styleSheet_def(obj_name=next_object,
                                                            color=self.color_class.white_color.get_value(),
                                                            background=color.get_value(),
                                                            font_size=40, border_radius=10)
        next = self.sample_widget.pushButton(set_object_name=next_object,
                                                    set_styleSheet=next_styleSheet,
                                                    set_text='Next',
                                             connect=self.setValue)
        next.setFont(font)
        gridLayout.addWidget(next, 6, 0, 1, 2)
        '''


        gridLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), 7, 0, 1, 1)



        return widget

    def setValue(self):
        '''

        :return:
        '''
        self.parent.close()




















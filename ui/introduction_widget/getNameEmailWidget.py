from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help

from ui import commonButton



class getNameEmailWidget(QWidget):
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


        #WELCOME TO LABEL
        userButton = commonButton.button_def(objName='userButton',
                                             color=self.color_class.white_color.get_value(),
                                             backgroundColor=self.color_class.setColorVal(r=141, g=141, b=141).get_value(),
                                             val=15, name='')
        userButton.setIcon(QIcon('ui/icon/profile.jpg'))
        userButton.setIconSize(QSize(200, 200))
        userButton.setMinimumSize(QSize(200, 200))
        userButton.setMaximumSize(QSize(200, 200))
        gridLayout.addWidget(userButton, 1, 0, 1, 1)


        size = 15
        #FIRST NAME LABLE
        first_name_label = commonButton.label_def(objName='first_name_label',
                                                  color=self.color_class.white_color.get_value(),
                                                  val=size, name='First Name')
        gridLayout.addWidget(first_name_label, 2, 0, 1, 1)

        self.first_name_lineEdit = commonButton.lineEdit_def(objName='first_name_lineEdit',
                                                        color=self.color_class.white_color.get_value(),
                                                        backgroundColor=self.color_class.setColorVal(r=141, g=141, b=141).get_value(),
                                                        val=15, name='')
        self.first_name_lineEdit.setPlaceholderText('First Name')

        self.first_name_lineEdit.setMinimumSize(QSize(350, 54))
        gridLayout.addWidget(self.first_name_lineEdit, 2, 1, 1, 1)

        #LAST NAME LABLE
        last_name_label = commonButton.label_def(objName='last_name_label',
                                                  color=self.color_class.white_color.get_value(),
                                                  val=size, name='Last Name')
        gridLayout.addWidget(last_name_label, 3, 0, 1, 1)

        #LAST NAME LINEEDIT
        self.last_name_lineEdit = commonButton.lineEdit_def(objName='last_name_lineEdit',
                                                        color=self.color_class.white_color.get_value(),
                                                        backgroundColor=self.color_class.setColorVal(r=141, g=141, b=141).get_value(),
                                                        val=15, name='')
        self.last_name_lineEdit.setMinimumSize(QSize(350, 54))
        self.last_name_lineEdit.setPlaceholderText('Last Name')
        gridLayout.addWidget(self.last_name_lineEdit, 3, 1, 1, 1)


        #EMAIL LABLE
        email_label = commonButton.label_def(objName='email_label',
                                                  color=self.color_class.white_color.get_value(),
                                                  val=size, name='Email')
        gridLayout.addWidget(email_label, 4, 0, 1, 1)

        #EMAIL LINEEDIT
        self.email_lineEdit = commonButton.lineEdit_def(objName='email_lineEdit',
                                                        color=self.color_class.white_color.get_value(),
                                                        backgroundColor=self.color_class.setColorVal(r=141, g=141, b=141).get_value(),
                                                        val=15, name='')
        self.email_lineEdit.setMinimumSize(QSize(350, 54))
        self.email_lineEdit.setPlaceholderText('Email')
        gridLayout.addWidget(self.email_lineEdit, 4, 1, 1, 1)

        #COUNTRY LABLE
        country_label = commonButton.label_def(objName='country_label',
                                                  color=self.color_class.white_color.get_value(),
                                                  val=size, name='Country')
        gridLayout.addWidget(country_label, 5, 0, 1, 1)

        #COUNTRY LINEEDIT
        countryList = self.help_class.totalCountry()
        self.country_comboBox = self.sample_widget.comboBox(addItems=countryList, setEditable=True)
        self.country_comboBox.setMinimumSize(QSize(350, 54))
        font = QFont()
        font.setBold(True)
        font.setPointSize(size)
        self.country_comboBox.setFont(font)

        gridLayout.addWidget(self.country_comboBox, 5, 1, 1, 1)

        #NEXT BUTTON
        next = commonButton.button_def(objName='next',
                                             color=self.color_class.white_color.get_value(),
                                             backgroundColor=self.color_class.setColorVal(r=141, g=141, b=141).get_value(),
                                             val=15, name='Next',
                                             connect=self.setValue)
        next.setMinimumSize(QSize(350, 54))
        gridLayout.addWidget(next, 6, 0, 1, 2)
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
        if self.first_name_lineEdit.text() == '':
            firstNameError = self.sample_widget.displayMessage('Please enter your first name', 'Error')
            firstNameError.exec_()
            return

        if self.last_name_lineEdit.text() == '':
            lastNameError = self.sample_widget.displayMessage('Please enter your last name', 'Error')
            lastNameError.exec_()
            return

        if self.email_lineEdit.text() == '':
            emailError = self.sample_widget.displayMessage('Please enter your email', 'Error')
            emailError.exec_()
            return

        self.parent.userData['first_name'] = self.first_name_lineEdit.text()
        self.parent.userData['last_name'] = self.last_name_lineEdit.text()
        self.parent.userData['email'] = self.email_lineEdit.text()
        self.parent.userData['country'] = self.country_comboBox.currentText()

        self.parent.set_stakeWidget_def(2)




















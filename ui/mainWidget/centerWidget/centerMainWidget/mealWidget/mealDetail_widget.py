


from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))


class mealMain_Widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.getCookingSkillList = []

        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)

        verticalLayout = QVBoxLayout(self)

        widget = self.initUI()
        verticalLayout.addWidget(widget)
    def initUI(self):
        '''


        :return:
        '''
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(10)

        self.sampleObjectNmae = 'labelStyleSheet'
        self.labelStyleSheet = self.sample_widget.styleSheet_def(obj_name=self.sampleObjectNmae,
                                                                 color=self.color_class.white_color.get_value())



        widget_object = 'centerMainWidget'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object, background_color=self.color.get_value(),
                                                       border_color=self.color_class.black_color.get_value())
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0), set_spacing=15)

        #verticalLayout.addWidget(self.searchWidget())
        verticalLayout.addWidget(self.mealDeatailWidget())

        verticalLayout.addItem(QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))



        return widget


    def mealDeatailWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.topWidget())
        verticalLayout.addWidget(self.bottomWidget())


        return widget

    def topWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        gridLayout = self.sample_widget.grid_layout(parent_self=widget, set_spacing=5)

        gridLayout.addWidget(self.nameWidget(), 0, 0, 1, 1)

        gridLayout.addWidget(self.historyWidget(), 1, 0, 1, 1)

        gridLayout.addWidget(self.ingredientsWidget(), 2, 0, 1, 1)

        gridLayout.addWidget(self.addToCalenderWidegt(), 3, 0, 1, 1)

        gridLayout.addWidget(self.recepieImageButtonWidget(), 0, 1, 4, 2)

        return widget


    def bottomWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        verticalLayout.addWidget(self.descriptionWidget())
        verticalLayout.addWidget(self.nutritionWidget())
        verticalLayout.addWidget(self.mealTabWidget())

        return widget


    def nameWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)


        name_object = 'nameLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, name_object)
        nameLabel =  self.sample_widget.label(set_text='Name', set_alighment=self.sample_widget.center_alignment,
                                              set_object_name=name_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        nameLabel.setFont(font)
        verticalLayout.addWidget(nameLabel)

        return widget

    def historyWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        history_object = 'historyLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, history_object)
        historyLabel = self.sample_widget.label(set_text='History', set_alighment=self.sample_widget.center_alignment,
                                                set_object_name=history_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        historyLabel.setFont(font)
        verticalLayout.addWidget(historyLabel)

        return widget

    def ingredientsWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        #INGREDIETN LABEL
        ingredient_object = 'ingredientLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, ingredient_object)
        ingredientLabel = self.sample_widget.label(set_text='Ingredients', set_alighment=self.sample_widget.center_alignment,
                                                   set_object_name=ingredient_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        ingredientLabel.setFont(font)
        horizontalLayout.addWidget(ingredientLabel)

        #MINIUTE LABEL
        miniute_object = 'miniuteLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, miniute_object)
        miniuteLabel = self.sample_widget.label(set_text='Miniute', set_alighment=self.sample_widget.center_alignment,
                                                set_object_name=miniute_object, set_styleSheet=styleSheet)
        miniuteLabel.setFont(font)
        horizontalLayout.addWidget(miniuteLabel)


        #CALORIES LABEL
        calories_object = 'caloriesLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, calories_object)
        caloriesLabel = self.sample_widget.label(set_text='Calories', set_alighment=self.sample_widget.center_alignment,
                                                 set_object_name=calories_object, set_styleSheet=styleSheet)
        caloriesLabel.setFont(font)
        horizontalLayout.addWidget(caloriesLabel)



        return widget

    def addToCalenderWidegt(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_spacing=15)

        horizontalLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Maximum))

        addToClaender_object = 'addToClaenderLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, addToClaender_object)
        addToCalenderLabel = self.sample_widget.label(set_text='Add to Calender', set_alighment=self.sample_widget.center_alignment,
                                                      set_object_name=addToClaender_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        addToCalenderLabel.setFont(font)
        horizontalLayout.addWidget(addToCalenderLabel)

        addToCalender_object = 'addToCalenderButtonObject'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=addToCalender_object,
                                                         background_color=self.backgroundColor.get_value(),
                                                         border_radius=30)
        size = 100
        addToCalenderButton = self.sample_widget.pushButton(set_text='Add', set_object_name=addToCalender_object,
                                                              set_styleSheet=styleSheet,
                                                              min_size=(size, size), max_size=(size, size))

        horizontalLayout.addWidget(addToCalenderButton)


        return widget


    def mealViewWidget(self):
        widegt = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widegt, set_spacing=15)

        mealButton = self.sample_widget.pushButton(set_text='Meal', set_object_name='mealButton')
        verticalLayout.addWidget(mealButton)

        return widegt

    def recepieImageButtonWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)



        size = 300
        recepoieImage_object = 'recepoieImageLabelObject'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=recepoieImage_object,
                                                         background_color=self.backgroundColor.get_value(),
                                                         border_radius=20)
        recepieImageButton = self.sample_widget.pushButton(set_text='Recepie Image', set_object_name=recepoieImage_object,
                                                           min_size=(size, size), max_size=(size, size),
                                                           set_styleSheet=styleSheet)
        verticalLayout.addWidget(recepieImageButton)

        return widget



    def descriptionWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        description_object = 'descriptionLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, description_object)
        descriptionLabel = self.sample_widget.label(set_text='Description', set_alighment=self.sample_widget.center_alignment,
                                                    set_object_name=description_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        descriptionLabel.setFont(font)
        verticalLayout.addWidget(descriptionLabel)

        heightSize = 100
        description_object = 'descriptionTextEditObject'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=description_object,
                                                            background_color=self.backgroundColor.get_value(),
                                                            border_radius=5)
        descriptionTextEdit = QTextEdit()
        descriptionTextEdit.setReadOnly(True)
        descriptionTextEdit.setMinimumSize(QSize(0, heightSize))
        descriptionTextEdit.setMaximumSize(QSize(16777215, heightSize))
        descriptionTextEdit.setText('Description')
        descriptionTextEdit.setObjectName(description_object)
        descriptionTextEdit.setStyleSheet(styleSheet)


        verticalLayout.addWidget(descriptionTextEdit)


        return widget


    def nutritionWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        nutri_object = 'nutriLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, nutri_object)
        nutritop_label = self.sample_widget.label(set_text='Nutrition', set_alighment=self.sample_widget.center_alignment,
                                                   set_object_name=nutri_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        nutritop_label.setFont(font)
        verticalLayout.addWidget(nutritop_label)

        verticalLayout.addWidget(self.nutritionListWidget())

        return widget

    def nutritionListWidget(self):

        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_spacing=15)
        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        horizontalLayout.addWidget(scrollArea)
        scrollArea.setWidgetResizable(True)
        widget_object = 'scrollAreaWidgetContents'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object,
                                                         background_color=self.color.get_value(),
                                                         border_radius=0)

        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet)

        scrollArea.setWidget(scrollAreaWidgetContents)
        horizontalLayout_ = self.sample_widget.horizontal_layout(parent_self=scrollAreaWidgetContents, set_spacing=15)

        for each in range(0, 4):
            buttonObject = 'nutritionButton'
            styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonObject,
                                                              background_color=self.backgroundColor.get_value(),
                                                              border_radius=50)
            button = self.sample_widget.pushButton(set_text='Nutrition', set_object_name=buttonObject,
                                                       set_styleSheet=styleSheet,
                                                       min_size=(100, 100), max_size=(100, 100))
            horizontalLayout_.addWidget(button)

        return widget

    def mealTabWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        tabWidget = QTabWidget()
        verticalLayout.addWidget(tabWidget)

        return widget

    def searchWidget(self):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        lineEdit_object = 'lineEdit_object'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=lineEdit_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        lineEdit = self.sample_widget.line_edit(set_object_name=lineEdit_object, set_styleSheet=styleSheet)
        lineEdit.setMinimumSize(QSize(0, 40))
        lineEdit.setMaximumSize(QSize(16777215, 40))
        lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        lineEdit.setFont(font)
        lineEdit.setPlaceholderText('Search the Meal')
        #lineEdit.textChanged.connect(self.lineEditTextChanged)
        verticalLayout.addWidget(lineEdit)


        return widget



   
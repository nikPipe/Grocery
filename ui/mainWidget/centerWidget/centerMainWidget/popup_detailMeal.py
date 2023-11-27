from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help
import ui, os
file =  os.path.dirname(os.path.realpath(ui.__file__))
from ui.mainWidget.centerWidget.centerMainWidget.calenderWidget import calenderMainWidget

class mealDeatail(QDialog):
    def __init__(self, parent=None, data=None):
        super().__init__(parent)
        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.styleSheet_class = styleSheet.STYLESHEET()
        self.color_class = sample_color_variable.COLOR_VARIABLE()
        self.help_class = help.Help()
        self.parent = parent
        self.data = data
        self.color = self.color_class.setColorVal(r=36, g=36, b=36)
        self.backgroundColor = self.color_class.setColorVal(r=179, g=179, b=179)

        self.setWindowTitle(data['name'])
        self.setModal(True)  # Set the dialog as modal

        layout = QVBoxLayout(self)
        label = QLabel("This is a modal popup dialog.", self)
        layout.addWidget(self.initUI())

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
        widget = self.sample_widget.widget_def(set_object_name=widget_object, set_styleSheet=styleSheet,
                                               min_size=(1000, 800), max_size=(16777215, 16777215))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0),
                                                            set_spacing=15)

        # verticalLayout.addWidget(self.searchWidget())
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

        gridLayout.addWidget(self.nameWidget(data=self.data), 0, 0, 1, 1)

        gridLayout.addWidget(self.historyWidget(data=self.data), 1, 0, 1, 1)

        gridLayout.addWidget(self.ingredientsWidget(data=self.data), 2, 0, 1, 1)

        gridLayout.addWidget(self.addToCalenderWidegt(data=self.data), 3, 0, 1, 1)

        gridLayout.addWidget(self.recepieImageButtonWidget(data=self.data), 0, 1, 4, 2)

        return widget

    def bottomWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        verticalLayout.addWidget(scrollArea)
        scrollAreaWidgetContents = self.sample_widget.widget_def()
        scrollArea.setWidget(scrollAreaWidgetContents)
        verticalLayout_ = self.sample_widget.vertical_layout(parent_self=scrollAreaWidgetContents, set_spacing=15)

        verticalLayout_.addWidget(self.descriptionWidget(data=self.data))
        verticalLayout_.addWidget(self.nutritionWidget(data=self.data))
        verticalLayout_.addWidget(self.mealTabWidget(data=self.data))

        return widget

    def nameWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        name_object = data['id'] + '_nameLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, name_object)
        name = data['name']

        self.mealNameLabel = self.sample_widget.label(set_text=name,
                                                      set_alighment=self.sample_widget.center_alignment,
                                                      set_object_name=name_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        self.mealNameLabel.setFont(font)
        verticalLayout.addWidget(self.mealNameLabel)

        return widget

    def historyWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        history_object = data['id'] + '_historyLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, history_object)
        historyLabel = self.sample_widget.label(set_text='History', set_alighment=self.sample_widget.center_alignment,
                                                set_object_name=history_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        historyLabel.setFont(font)
        verticalLayout.addWidget(historyLabel)

        textEdit_object = data['id'] + '_historyTextEditObject'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=textEdit_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=5)
        self.historyTextEdit = QTextEdit()
        self.historyTextEdit.setReadOnly(True)
        self.historyTextEdit.setText(data['history'])
        self.historyTextEdit.setObjectName(textEdit_object)
        self.historyTextEdit.setStyleSheet(styleSheet)
        self.historyTextEdit.setFont(font)
        verticalLayout.addWidget(self.historyTextEdit)

        return widget

    def ingredientsWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget)

        # INGREDIETN LABEL
        ingredient_object = data['id'] + '_ingredientLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, ingredient_object)
        label = 'Ingredients :\n' + str(len(data['ingredients']))
        self.ingredientLabel = self.sample_widget.label(set_text=label,
                                                        set_alighment=self.sample_widget.center_alignment,
                                                        set_object_name=ingredient_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        self.ingredientLabel.setFont(font)
        horizontalLayout.addWidget(self.ingredientLabel)

        # MINIUTE LABEL
        miniute_object = data['id'] + '_miniuteLabelObject'
        label = 'Miniute :\n' + str(data['time']['totalTime']['value']) + ' ' + data['time']['totalTime']['unit']

        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, miniute_object)
        self.miniuteLabel = self.sample_widget.label(set_text=label,
                                                     set_alighment=self.sample_widget.center_alignment,
                                                     set_object_name=miniute_object, set_styleSheet=styleSheet)
        self.miniuteLabel.setFont(font)
        horizontalLayout.addWidget(self.miniuteLabel)

        # CALORIES LABEL
        calories_object = 'caloriesLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, calories_object)
        calories = 'Calories :\n' + str(data['nutrition']['calories'])
        self.caloriesLabel = self.sample_widget.label(set_text=calories,
                                                      set_alighment=self.sample_widget.center_alignment,
                                                      set_object_name=calories_object, set_styleSheet=styleSheet)
        self.caloriesLabel.setFont(font)
        horizontalLayout.addWidget(self.caloriesLabel)

        return widget

    def addToCalenderWidegt(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_spacing=15)

        horizontalLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Maximum))

        addToClaender_object = data['id'] + '_addToCalenderLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, addToClaender_object)
        addToCalenderLabel = self.sample_widget.label(set_text='Add to Calender',
                                                      set_alighment=self.sample_widget.center_alignment,
                                                      set_object_name=addToClaender_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        addToCalenderLabel.setFont(font)
        horizontalLayout.addWidget(addToCalenderLabel)

        addToCalender_object = data['id'] + '_addToCalenderButtonObject'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=addToCalender_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=30)
        size = 100
        addToCalenderButton = self.sample_widget.pushButton(set_text='Add', set_object_name=addToCalender_object,
                                                            set_styleSheet=styleSheet,
                                                            min_size=(size, size), max_size=(size, size),
                                                            connect=partial(self.addToCalender, data=data))

        horizontalLayout.addWidget(addToCalenderButton)

        return widget

    def addToCalender(self, data):

        popup = self.parent.popup_calender.AddToCalender(self.parent, data)
        #popup = AddToCalender(self.parent, data)
        result = popup.exec_()  # This makes the dialog modal
        if result == QDialog.Accepted:
            print("Popup was accepted")
        else:
            print("Popup was rejected")
        print('add to calender')

    def mealViewWidget(self):
        widegt = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widegt, set_spacing=15)

        mealButton = self.sample_widget.pushButton(set_text='Meal', set_object_name='mealButton')
        verticalLayout.addWidget(mealButton)

        return widegt

    def recepieImageButtonWidget(self, data):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget)

        size = 300
        recepoieImage_object = data['id'] + '_recepieImageObject'
        image = data['images']['main']
        styleSheet = self.sample_widget.styleSheet_def(obj_name=recepoieImage_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=20)
        self.recepieImageButton = self.sample_widget.pushButton(set_text='',
                                                                set_object_name=recepoieImage_object,
                                                                min_size=(size, size), max_size=(size, size),
                                                                set_styleSheet=styleSheet,
                                                                set_icon=image, set_icon_size=(size, size))
        verticalLayout.addWidget(self.recepieImageButton)

        return widget

    def descriptionWidget(self, data):
        widget_obj = data['id'] + '_descriptionWidgetObject'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_obj,
                                                         background_color=self.color.get_value(),
                                                            border_radius=0)

        widget = self.sample_widget.widget_def(set_object_name=widget_obj, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        description_object = data['id'] + '_descriptionLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, description_object)
        descriptionLabel = self.sample_widget.label(set_text='Description',
                                                    set_alighment=self.sample_widget.center_alignment,
                                                    set_object_name=description_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        descriptionLabel.setFont(font)
        verticalLayout.addWidget(descriptionLabel)

        heightSize = 100
        description_object = data['id'] + '_descriptionTextEditObject'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=description_object,
                                                       background_color=self.backgroundColor.get_value(),
                                                       border_radius=5)
        self.descriptionTextEdit = QTextEdit()
        self.descriptionTextEdit.setReadOnly(True)
        self.descriptionTextEdit.setMinimumSize(QSize(0, heightSize))
        self.descriptionTextEdit.setMaximumSize(QSize(16777215, heightSize))
        self.descriptionTextEdit.setText(data['description'])
        self.descriptionTextEdit.setObjectName(description_object)
        self.descriptionTextEdit.setStyleSheet(styleSheet)
        self.descriptionTextEdit.setFont(font)
        verticalLayout.addWidget(self.descriptionTextEdit)

        return widget

    def nutritionWidget(self, data):
        '''

        :return:
        '''
        object = data['id'] + '_nutritionWidgetObject'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=object,
                                                         background_color=self.color.get_value(),
                                                         border_radius=0)

        widget = self.sample_widget.widget_def(set_object_name=object, set_styleSheet=styleSheet)
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        nutri_object = 'nutriLabelObject'
        styleSheet = self.labelStyleSheet.replace(self.sampleObjectNmae, nutri_object)
        nutritop_label = self.sample_widget.label(set_text='Nutrition',
                                                  set_alighment=self.sample_widget.center_alignment,
                                                  set_object_name=nutri_object, set_styleSheet=styleSheet)
        font = self.font
        font.setPointSize(15)
        nutritop_label.setFont(font)
        verticalLayout.addWidget(nutritop_label)

        verticalLayout.addWidget(self.nutritionListWidget(data))

        return widget

    def nutritionListWidget(self, data):
        height = 150
        widget = self.sample_widget.widget_def(min_size=(0, height), max_size=(16777215, height))
        horizontalLayout = self.sample_widget.horizontal_layout(parent_self=widget, set_spacing=15)
        scrollArea = self.sample_widget.scrollArea(parent_self=widget)
        horizontalLayout.addWidget(scrollArea)
        scrollArea.setWidgetResizable(True)
        widget_object = 'scrollAreaWidgetContents'
        styleSheet = self.sample_widget.styleSheet_def(obj_name=widget_object,
                                                       background_color=self.color.get_value(),
                                                       border_radius=0)

        scrollAreaWidgetContents = self.sample_widget.widget_def(set_object_name=widget_object,
                                                                 set_styleSheet=styleSheet)

        scrollArea.setWidget(scrollAreaWidgetContents)
        self.nutrition_horizontalLayout_ = self.sample_widget.horizontal_layout(parent_self=scrollAreaWidgetContents,
                                                                                set_spacing=15)

        for key, value in data['nutrition'].items():
            buttonObject = key + '_nutritionButton'
            text = key + ' \n' + str(value)
            styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonObject,
                                                           background_color=self.backgroundColor.get_value(),
                                                           border_radius=50)
            button = self.sample_widget.pushButton(set_text=text, set_object_name=buttonObject,
                                                   set_styleSheet=styleSheet,
                                                   min_size=(100, 100), max_size=(100, 100))
            font = self.font
            font.setPointSize(10)
            button.setFont(font)
            self.nutrition_horizontalLayout_.addWidget(button)

        '''
        for each in range(0, 4):
            buttonObject = 'nutritionButton'
            styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonObject,
                                                           background_color=self.backgroundColor.get_value(),
                                                           border_radius=50)
            button = self.sample_widget.pushButton(set_text='Nutrition', set_object_name=buttonObject,
                                                   set_styleSheet=styleSheet,
                                                   min_size=(100, 100), max_size=(100, 100))
            self.nutrition_horizontalLayout_.addWidget(button)
        '''
        return widget

    def mealTabWidget(self, data):
        '''

        :return:
        '''
        height = 500
        widget = self.sample_widget.widget_def(min_size=(0, height), max_size=(16777215, height))
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        self.meal_tabWidget = QTabWidget()
        verticalLayout.addWidget(self.meal_tabWidget)

        self.update_tabWidget(dic_val=data)

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
        # lineEdit.textChanged.connect(self.lineEditTextChanged)
        verticalLayout.addWidget(lineEdit)

        return widget

    def nutrition_update(self, dic):
        '''

        :return:
        '''
        self.help_class.clearLayout(self.nutrition_horizontalLayout_)
        nutrition = dic['nutrition']
        for each in nutrition:
            buttonObject = each + '_nutritionButton'
            text = each + ' \n' + str(nutrition[each])
            styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonObject,
                                                           background_color=self.backgroundColor.get_value(),
                                                           border_radius=50)
            button = self.sample_widget.pushButton(set_text=text, set_object_name=buttonObject,
                                                   set_styleSheet=styleSheet,
                                                   min_size=(100, 100), max_size=(100, 100))
            self.nutrition_horizontalLayout_.addWidget(button)

    def ingredientItemWidget(self, ingredient):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setColumnCount(3)
        treeWidget.setHeaderLabels(['Item', 'Quantity', 'Weight'])
        verticalLayout.addWidget(treeWidget)

        for each in ingredient:
            item = QTreeWidgetItem(treeWidget)
            item.setText(0, each['item'])
            item.setText(1, each['quantity'])
            weight = each['weight']['value'] + ' ' + each['weight']['unit']
            item.setText(2, weight)
            treeWidget.addTopLevelItem(item)

        return widget

    def equipment_def(self, equipment):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setColumnCount(2)
        treeWidget.setHeaderLabels(['name', 'description'])
        verticalLayout.addWidget(treeWidget)

        for each in equipment:
            item = QTreeWidgetItem(treeWidget)
            item.setText(0, each['name'])
            item.setText(1, each['description'])
            treeWidget.addTopLevelItem(item)

        return widget

    def tips_def(self, tips):
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget, setHeaderHidden=True)
        treeWidget.setColumnCount(1)
        verticalLayout.addWidget(treeWidget)

        for each in tips:
            item = QTreeWidgetItem(treeWidget)
            item.setText(0, each)
            treeWidget.addTopLevelItem(item)

        return widget

    def variations_def(self, variation):
        '''

        :param variation:
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setColumnCount(1)
        treeWidget.setHeaderLabels(['Variation'])
        verticalLayout.addWidget(treeWidget)

        for each in variation:
            item = QTreeWidgetItem(treeWidget)
            item.setText(0, each)
            treeWidget.addTopLevelItem(item)

        return widget

    def storage_def(self, storage):
        '''

        :param storage:
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setColumnCount(2)
        treeWidget.setHeaderLabels(['Storage', 'Duration'])
        verticalLayout.addWidget(treeWidget)

        for key, value in storage.items():
            item = QTreeWidgetItem(treeWidget)
            item.setText(0, key)
            item.setText(1, value)
            treeWidget.addTopLevelItem(item)

        return widget

    def presentation_def(self, presentation):
        '''

        :param presentation:
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setColumnCount(1)
        treeWidget.setHeaderLabels(['Presentation'])
        verticalLayout.addWidget(treeWidget)

        for each in presentation:
            item = QTreeWidgetItem(treeWidget)
            item.setText(0, each)
            treeWidget.addTopLevelItem(item)

        return widget

    def allergy_def(self, allergy):
        '''

        :param allergy:
        :return:
        '''
        widget = self.sample_widget.widget_def()
        verticalLayout = self.sample_widget.vertical_layout(parent_self=widget, set_spacing=15)

        treeWidget = self.sample_widget.treeWidget(parent_self=widget)
        treeWidget.setColumnCount(1)
        treeWidget.setHeaderLabels(['Allergy'])
        verticalLayout.addWidget(treeWidget)

        for each in allergy:
            item = QTreeWidgetItem(treeWidget)
            item.setText(0, each)
            treeWidget.addTopLevelItem(item)

        return widget

    def update_tabWidget(self, dic_val):
        '''

        :return:
        '''


        self.ingredientItemWidget(ingredient=dic_val['ingredients'])

        # INGREDIENT TAB
        self.meal_tabWidget.addTab(self.ingredientItemWidget(ingredient=dic_val['ingredients']), 'Ingredients')

        # EQUIPMENT TAB
        self.meal_tabWidget.addTab(self.equipment_def(equipment=dic_val['equipment']), 'Equipment')

        # TIPS TAB
        self.meal_tabWidget.addTab(self.tips_def(tips=dic_val['tips']), 'Tips')

        # VARIATION TAB
        self.meal_tabWidget.addTab(self.variations_def(variation=dic_val['variations']), 'Variations')

        # STORAGE TAB
        self.meal_tabWidget.addTab(self.storage_def(storage=dic_val['storage']), 'Storage')

        # PRESENTATION TAB
        self.meal_tabWidget.addTab(self.presentation_def(presentation=dic_val['presentationTips']), 'Presentation')

        # ALLERGY TAB
        self.meal_tabWidget.addTab(self.allergy_def(allergy=dic_val['allergens']), 'Allergy')

    def update_(self, dic_val):
        '''

        :return:
        '''
        print('thi sis the update')

        # NUTRITION UPDATE
        self.nutrition_update(dic=dic_val)

        # TAB WIDGET UPDATE
        self.update_tabWidget(dic_val=dic_val)






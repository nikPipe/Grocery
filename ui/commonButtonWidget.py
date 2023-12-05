
from functools import partial
import random

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable

sample_widget_template_class = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()

color_class = sample_color_variable.COLOR_VARIABLE()



color__ = color_class.setColorVal(r=36, g=36, b=36)
backgroundColor = color_class.setColorVal(r=179, g=179, b=179)
width = 200
height = 200
width_ = width
height_ = 100
font = QFont()
font.setBold(True)
font.setPointSize(10)

def commonWidget(dict):
    """
    @param parent: QWidget
    @return: QWidget
    """
    objectName = dict['id'] + '_object'
    widget = sample_widget_template_class.widget_def(min_size=(width, height), max_size=(width, height),
                                                        set_object_name=objectName)
    verticallaout = sample_widget_template_class.vertical_layout(parent_self=widget, set_contents_margins=(0, 0, 0, 0),
                                                                    set_spacing=0)

    #NAME OBJECT
    id = dict['id']
    name = dict['name']

    label_object = id + '_name_object'
    styleSheet = sample_widget_template_class.styleSheet_def(obj_name=label_object,
                                                                color=color_class.white_color.get_value(),
                                                                border_radius=20)
    label = sample_widget_template_class.label(set_text=name, set_alighment=sample_widget_template_class.center_alignment,
                                                    set_styleSheet=styleSheet, set_object_name=label_object)
    font_ = font
    font_.setPointSize(12)
    label.setFont(font_)
    verticallaout.addWidget(label)



    image = dict['images']['main']
    time = 'MealTime: ' + dict['time']['totalTime']['value'] + ' ' + dict['time']['totalTime']['unit']

    pushButton_object = id + '_object'
    styleSheet = sample_widget_template_class.styleSheet_def(obj_name=pushButton_object,
                                                             background_color=backgroundColor.get_value(),
                                                             border_radius=20)


    pushButton = sample_widget_template_class.pushButton(set_text='', min_size=(width_, height_), max_size=(width_, width_),
                                               set_styleSheet=styleSheet, set_object_name=pushButton_object,
                                               set_icon=image, set_icon_size=(width_, height_))
    pushButton.setFont(font)
    verticallaout.addWidget(pushButton)

    #TIME LABEL
    label_object = id + '_time_label_object'
    styleSheet = sample_widget_template_class.styleSheet_def(obj_name=label_object,
                                                             color=color_class.white_color.get_value(),
                                                                border_radius=20)
    label = sample_widget_template_class.label(set_text=time, set_alighment=sample_widget_template_class.center_alignment,
                                                  set_styleSheet=styleSheet, set_object_name=label_object)
    label.setFont(font)
    verticallaout.addWidget(label)

    verticallaout.addWidget(label_button_def(dict))

    return widget

def label_button_def(dict):
    '''

    :return:
    '''
    widget = sample_widget_template_class.widget_def()
    gridLayout = sample_widget_template_class.grid_layout(parent_self=widget, set_spacing=0, set_contents_margins=(0, 0, 0, 0))

    id = dict['id']
    name = dict['name']

    label_object = id + '_label_object'
    styleSheet = sample_widget_template_class.styleSheet_def(obj_name=label_object,
                                                             color=color_class.white_color.get_value(),
                                                             border_radius=20)
    label = sample_widget_template_class.label(set_text=name, set_alighment=sample_widget_template_class.center_alignment,
                                               set_styleSheet=styleSheet, set_object_name=label_object)
    label.setFont(font)
    gridLayout.addWidget(label, 0, 0, 1, 1)

    size = 20
    pushButton_object = id + '_pushButton_object'
    if 'Non-Vegetarian' in dict['dietTypes'] or 'Non-Vegetarian' in dict['dietTypes'] or 'Pescatarian' in dict['dietTypes'] or 'Pescatarian' in dict['dietTypes']:
        color = color_class.red_color.get_value()
    else:
        color = color_class.green_color.get_value()


    styleSheet_ = sample_widget_template_class.styleSheet_def(obj_name=pushButton_object,
                                                              background_color=color,
                                                              border_radius=20)
    pushButton = sample_widget_template_class.pushButton(set_text='', min_size=(size, size),
                                                            max_size=(size, size),
                                                            set_styleSheet=styleSheet_,
                                                            set_object_name=pushButton_object)
    pushButton.setFont(font)
    gridLayout.addWidget(pushButton, 0, 1, 1, 1)

    #ADD TO CALENDER
    size = 30
    pushButton_object = id + '_addToCalender_pushButton_object'
    addToCalender = sample_widget_template_class.pushButton(set_text='', min_size=(size, size),
                                                            max_size=(size, size), set_object_name=pushButton_object)
    addToCalender.setFont(font)
    gridLayout.addWidget(addToCalender, 0, 2, 1, 1)



    return widget









from functools import partial

from ui.import_module import *
from ui.sampleWidget import sample_widget_template
from ui.sampleWidget import styleSheet, sample_color_variable
from data import help

sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
styleSheet_class = styleSheet.STYLESHEET()
color_class = sample_color_variable.COLOR_VARIABLE()
help_class = help.Help()

def label_def(objName, color, val=40, name=''):
    '''

    :return:
    '''
    objectName = objName
    first_name_styleSheet = sample_widget.styleSheet_def(obj_name=objectName,
                                                              color=color,
                                                              font_size=val, )

    first_name = sample_widget.label(set_object_name=objectName,
                                          set_styleSheet=first_name_styleSheet,
                                          set_text=name, set_alighment=sample_widget.center_alignment)

    font = QFont()
    font.setBold(True)
    font.setPointSize(val)
    first_name.setFont(font)

    return first_name


def button_def(objName, color, backgroundColor='', val=40, name='', connect=None):
    '''

    :return:
    '''
    objectName = objName


    first_name_styleSheet = sample_widget.styleSheet_def(obj_name=objectName,
                                                                     background_color=backgroundColor,
                                                                     color = color,
                                                                     font_size=val,
                                                                     border_radius=10)

    first_name = sample_widget.pushButton(set_object_name=objectName,
                                          set_styleSheet=first_name_styleSheet,
                                          set_text=name)

    font = QFont()
    font.setBold(True)
    font.setPointSize(val)
    first_name.setFont(font)

    if connect:
        first_name.clicked.connect(connect)



    return first_name


def lineEdit_def(objName, color, backgroundColor='', val=40, name='', connect=None):
    '''

    :return:
    '''
    objectName = objName
    first_name_styleSheet = sample_widget.styleSheet_def(obj_name=objectName,
                                                                        background_color=backgroundColor,
                                                                        color = color,
                                                                        font_size=val,
                                                                        border_radius=10)

    first_name = sample_widget.line_edit(set_object_name=objectName,
                                             set_styleSheet=first_name_styleSheet,
                                             set_text=name)

    font = QFont()
    font.setBold(True)
    font.setPointSize(val)
    first_name.setFont(font)

    if connect:
        first_name.textChanged.connect(connect)

    return first_name


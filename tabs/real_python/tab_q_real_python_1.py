#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---- tof
"""
# this material is used for selection access to the tab which must
# be named tab_...python among other things

KEY_WORDS:      rh
CLASS_NAME:     RealPython1Tab
WIDGETS:        QHBoxLayout QVBoxLayout QGridLayout QFormLayout
STATUS:         June 2025  brand new test
TAB_TITLE:      RP: python-pyqt-gui-calculator
DESCRIPTION:    RP: Python and PyQt: Building a GUI Desktop Calculator
HOW_COMPLETE:   25  #  AND A COMMENT

try this in a tab
Python and PyQt: Building a GUI Desktop Calculator – Real Python
https://realpython.com/python-pyqt-gui-calculator/

Python and PyQt: Building a GUI Desktop Calculator


--- but these are for main window that i do not want to do now, model after ??? that i already have
Python and PyQt: Creating Menus, Toolbars, and Status Bars – Real Python
https://realpython.com/python-menus-toolbars/



"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
# --------------------------------


import inspect
import subprocess
import sys
import time
from datetime import datetime
from functools import partial
from subprocess import PIPE, STDOUT, Popen, run

import wat
from PyQt5 import QtGui
from PyQt5.QtCore import (QDate,
                          QDateTime,
                          QModelIndex,
                          QSize,
                          Qt,
                          QTime,
                          QTimer)
from PyQt5.QtGui import QColor, QPalette, QTextCursor, QTextDocument
# sql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
# widgets biger
# widgets -- small
# layouts
from PyQt5.QtWidgets import (QAction,
                             QFormLayout,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDateEdit,
                             QDateTimeEdit,
                             QGridLayout,
                             QGroupBox,
                             QHBoxLayout,
                             QLabel,
                             QLineEdit,
                             QListWidget,
                             QListWidgetItem,
                             QMainWindow,
                             QMenu,
                             QMessageBox,
                             QPushButton,
                             QRadioButton,
                             QSizePolicy,
                             QTableView,
                             QTableWidget,
                             QTableWidgetItem,
                             QTabWidget,
                             QTextEdit,
                             QTimeEdit,
                             QVBoxLayout,
                             QWidget)

#import parameters

import utils_for_tabs as uft
import wat_inspector
import tab_re_base

# ---- end imports

print_func_header   = uft.print_func_header

def greet(name, msg ):

    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello, {name}")

#  --------
class RealPython1Tab( tab_re_base.TabReBase ):
    """
    Reference examples for QPushButton


    this is also the place for documentation on the methods normally found
    in a tab_.... file and should display its naming and other coding conventions
    other tab_xxx files may not be as well commented, you should be familiar with
    the conventions and be able to read the code.
    """
    def __init__(self):
        """
        set up the tab

        this is pretty much boiler plate for a tab
        """
        super().__init__()
        self.module_file        = __file__      # save for help file usage

        # modify to match the number of mutate methods in this module
        self.mutate_dict[0]     = self.mutate_0
        # self.mutate_dict[1]     = self.mutate_1
        # self.mutate_dict[2]     = self.mutate_2
        # #self.mutate_dict[3]     = self.mutate_3

        self.build_dict[0]      = self.build_gui_widgets_0
        self.build_dict_msg[0]  = self.build_gui_msg_0

        self.build_dict[1]      = self.build_gui_widgets_1
        #self.build_dict_msg[1]  = self.build_gui_msg_1

        self.build_dict[2]      = self.build_gui_widgets_2
        #self.build_dict_msg[2]  = self.build_gui_msg_2

        self.build_dict[3]      = self.build_gui_widgets_3
        #self.build_dict_msg[3]  = self.build_gui_msg_3
        self.build_dict[4]      = self.build_gui_widgets_4

        # self.mutate_dict[3]     = self.mutate_3
        # self.mutate_dict[4]     = self.mutate_4

        # self._build_gui_widgets = self.
        # self._build_gui()
        self.post_init( )


    def build_gui_widgets_0( self,   ):
        """
        h_layout.py
        Horizontal layout example.


        content of the excercise
        """

        main_layout     = self.main_layout
        layout          = QHBoxLayout()
        main_layout.addLayout( layout )

        layout.addWidget(QPushButton("Left"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Right"))

        self.post_build_msg  = [ "code from build_gui_widgets_0",
                                 "Like RP h_layout.p" ]

    #-----------------------
    def build_gui_msg_0( self, ):
        """
        messages for build_gui_widgets_n

        not part of excercise, but message about the code
        """
        self.append( "code from build_gui_widgets_0" )
        msg    = "Like RP h_layout.py"
        self.append_msg( msg,)

    #-----------------------
    def build_gui_widgets_1( self, ):
        """
        v_layout.py


        Vertical layout example.
        content of the excercise
        """
        main_layout     = self.main_layout
        layout          = QVBoxLayout()
        main_layout.addLayout( layout )

        layout.addWidget(QPushButton("Top 2"))
        layout.addWidget(QPushButton("Center 3"))
        layout.addWidget(QPushButton("Bottom 4"))

        self.post_build_msg  = [ "code from build_gui_widgets_1",
                                 "Like RP v_layout.p" ]

    #-----------------------
    def build_gui_msg_1xxx( self, ):
        """
        messages for build_gui_widgets_n

        not part of excercise, but message about the code
        """
        self.append( "code from build_gui_widgets_0" )
        msg    = "Like RP v_layout.py"
        self.append_msg( msg,)


    def build_gui_widgets_2( self, ):
        """
        g_layout.py


        Grid layout example
        content of the excercise
        """
        main_layout     = self.main_layout
        layout = QGridLayout()
        main_layout.addLayout( layout )

        layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
        layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
        layout.addWidget(QPushButton("Button (0, 2)"), 0, 2)
        layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
        layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
        layout.addWidget(QPushButton("Button (1, 2)"), 1, 2)
        layout.addWidget(QPushButton("Button (2, 0)"), 2, 0)
        layout.addWidget(
               QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2
                   )

        # part of framework msg function
        self.post_build_msg  = [ "code from build_gui_widgets_2",
                                 "Like RP g_layout.py" ]

    #-----------------------
    def build_gui_msg_2xxx( self, ):
        """
        messages for build_gui_widgets_n


        """
        self.append_function_msg( "code from build_gui_widgets_0" )
        msg    = "Like RP g_layout.py"
        self.append_msg( msg,)


    def build_gui_widgets_3( self, ):
        """

        content of the excercise
        """
        main_layout     = self.main_layout


        layout = QFormLayout()

        main_layout.addLayout( layout )

        # widgets like RP
        layout.addRow( "Name:",      QLineEdit())
        layout.addRow( "Age:",       QLineEdit())
        layout.addRow( "Job:",       QLineEdit())
        layout.addRow( "Hobbies:",   QLineEdit())

        self.post_build_msg  = [ "code from build_gui_widgets_3",
                                 "Like RP f_layout.py" ]
# signals_slots.py



    def build_gui_widgets_4( self, ):
        """
        Signals and slots example.
        signals_slots.py


        content of the excercise
        """
        main_layout     = self.main_layout


        layout = QVBoxLayout()

        main_layout.addLayout( layout )


        #window.setWindowTitle("Signals and slots")


        widget = QPushButton("Greet")
        # widget.clicked.connect(greet)
        widget.clicked.connect( partial(greet, "World!"))


        layout.addWidget(widget)
        widget         = QLabel("")
        self.msg_label = widget
        layout.addWidget( widget )

        self.post_build_msg  = [ "code from build_gui_widgets_4",
                                 "signals_slots.py" ]


    # #-----------------------
    # def build_gui_msg_3( self, ):
    #     """
    #     messages for build_gui_widgets_n

    #     not part of excercise, but message about the code
    #     """
    #     self.append_function_msg( "code from build_gui_widgets_3" )
    #     msg    = "Like RP v_layout.py"
    #     self.append_msg( msg,)



    # # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets
            these mutations will try to mimic a typical default state
            of a widget for the first push button the
            second will not be modified by mutate_0

        this is important content for the widgets referenced on this tab
        read the code for more insight, note messages to app and comments
        """
        pass
        #self.append_function_msg( "mutate_0()" )


    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets

        this is important content for the widgets referenced on this tab
        read the code for more insight, note messages to app and comments
        """
        self.append_function_msg( "mutate_1()" )

    #     #self.append_msg( tab_base.DONE_MSG )
    # def greet(self ):
    #     if self.msgLabel.text():
    #         self.msgLabel.setText("")
    #     else:
    #         self.msgLabel.setText("Hello, World!")

    def greet_with_arg(self, name):
    if msg.text():
        self.msg_label.setText("")
    else:
        self.msg_label.setText(f"Hello, {name}")


    # ------------------------
    def inspect(self):
        """
        the usual

        Allows the user to inspect local and global variables using
        the wat_inspector

        this is pretty much boiler plate for a tab
        """
        self.append_function_msg( tab_re_base.INSPECT_MSG )

        # we set local variables to make it handy to inspect them
        self_layout    = self.layout


        wat_inspector.go(
             msg            = "for your inspection, inc. locals and globals",
             a_locals       = locals(),
             a_globals      = globals(), )

        self.append_msg( tab_re_base.DONE_MSG )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tab's code

        this is pretty much boiler plate for a tab
        """
        self.append_function_msg( tab_re_base.BREAK_MSG )

        breakpoint()

        self.append_msg( tab_re_base.DONE_MSG )

# ---- eof

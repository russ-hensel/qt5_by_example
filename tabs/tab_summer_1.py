#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ---- tof

"""
self.help_file_name     =  "qsql_relational_table_model_tab_2.txt"

KEY_WORDS:      spliter inspired by summer news reader new_base split
CLASS_NAME:     Summer_1_Tab
WIDGETS:        QSplitter
STATUS:         runs_correctly_5_10      demo_complete_2_10   !! review_key_words   !! review_help_0_10
TAB_TITLE:      QSplitter

"""



"""
ideas from from:
 newsreader.pyw

Rapid GUI Programming with Python and Qt:
The Definitive Guide to PyQt Programming
by Mark Summerfield

ISBN: 0132354187



"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #qt_fitz_book.main()
# --------------------


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
from PyQt5.QtGui import QColor, QIcon, QPalette, QTextCursor, QTextDocument
# sql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
# widgets biger
# widgets -- small
# layouts
from PyQt5.QtWidgets import (QAction,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDateEdit,
                             QDateTimeEdit,
                             QDial,
                             QDoubleSpinBox,
                             QFontComboBox,
                             QGridLayout,
                             QGroupBox,
                             QHBoxLayout,
                             QLabel,
                             QLCDNumber,
                             QLineEdit,
                             QListWidget,
                             QListWidgetItem,
                             QMainWindow,
                             QMenu,
                             QMessageBox,
                             QProgressBar,
                             QPushButton,
                             QRadioButton,
                             QSizePolicy,
                             QSlider,
                             QSpinBox,
                             QSplitter,
                             QTableView,
                             QTableWidget,
                             QTableWidgetItem,
                             QTabWidget,
                             QTextBrowser,
                             QTextEdit,
                             QTimeEdit,
                             QVBoxLayout,
                             QWidget)

import parameters
#import qt_widgets
import utils_for_tabs as uft
import wat_inspector
import tab_base


# ---- end imports



#  --------
class Summer_1_Tab( tab_base.TabBase  ) :
    def __init__(self):
        """
        the usual
        """
        super().__init__()
        self.help_file_name     = ( self.__class__.__name__ + ".txt" ).lower()

        # self.help_file_name     =  "build_from_classname.txt"
        self.mutate_dict[0]     = self.mutate_0
        self.mutate_dict[1]     = self.mutate_1
        # self.mutate_dict[2]    = self.mutate_2
        # self.mutate_dict[3]    = self.mutate_3
        # self.mutate_dict[4]    = self.mutate_4
        self._build_gui()





    # # -------------------------------
    # def _build_gui(self,   ):
    #     """
    #     layouts
    #         a vbox for main layout
    #         h_box for or each row of buttons
    #     """
    #     tab_page      = self
    #     layout        = QVBoxLayout( tab_page )

    #----------------------------
    def _build_gui_widgets(self, main_layout  ):
        """
        the usual, build the gui with the widgets of interest
        and the buttons for examples
        """
        layout              = QVBoxLayout(   )

        main_layout.addLayout( layout )
        #button_layout        = QHBoxLayout(   )



#-----------------
        self.groupsList    = QListWidget()
        self.messagesList  = QListWidget()
        self.messageView   = QTextBrowser()

        self.messageSplitter = QSplitter(Qt.Vertical)
        self.messageSplitter.addWidget( self.messagesList )
        self.messageSplitter.addWidget( self.messageView)

        # outer most splitter
        self.mainSplitter   = QSplitter(Qt.Horizontal)
        self.mainSplitter.addWidget(self.groupsList)
        self.mainSplitter.addWidget(self.messageSplitter)


        #self.setCentralWidget(self.mainSplitter)
        layout.addWidget( self.mainSplitter )

        self.mainSplitter.setStretchFactor(0, 1)
        self.mainSplitter.setStretchFactor(1, 3)
        self.messageSplitter.setStretchFactor(0, 1)
        self.messageSplitter.setStretchFactor(1, 2)


        # ---- new row, standard buttons
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )


        widget = QPushButton("mutate\n")
        self.button_ex_1         = widget
        widget.clicked.connect( lambda: self.mutate( ) )
        button_layout.addWidget( widget )


        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )


    # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_0" )

        msg    = "so far not implemented "
        self.append_msg( msg, clear = False )

        self.append_msg( "mutate_0 done" )

    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_1" )

        msg    = "so far not implemented "
        self.append_msg( msg, clear = False )

        self.append__msg( "breakpoint done" )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        self.append_function_msg(  "inspect" )

        #self_widgets_list   = self.widgets_list
        wat_inspector.go(
             msg            = "see self_widgets_list",
             a_locals       = locals(),
             a_globals      = globals(), )
        self.append_msg( "mutate_0 done" )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        self.append_function_msg(  "breakpoint" )

        breakpoint()
        self.append_msg( "breakpoint done" )

# ---- eof
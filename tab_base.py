#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof


"""



"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #qt_fitz_book.main()
# --------------------


import inspect
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from functools import partial
from subprocess import PIPE, STDOUT, Popen, run

import wat
from PyQt5 import QtGui
from PyQt5.QtCore import (QAbstractListModel,
                          QAbstractTableModel,
                          QDate,
                          QDateTime,
                          QModelIndex,
                          QSize,
                          Qt,
                          QTime,
                          QTimer)
from PyQt5.QtGui import QColor, QImage, QPalette, QTextCursor, QTextDocument, QIcon
# sql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
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

                             QLineEdit,
                             QListView,
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
                             QTableView,
                             QTableWidget,
                             QTableWidgetItem,
                             QTabWidget,
                             QTextEdit,
                             QTimeEdit,
                             QVBoxLayout,
                             QWidget)

import parameters
#import qt_widgets
import utils_for_tabs as uft
import wat_inspector
import global_vars
# ---- imports neq qt
import logging

# ---- end imports



basedir = os.path.dirname(__file__)

tick    = QImage(os.path.join("tick.png"))

logger          = logging.getLogger( )

# Color scale, which is taken from colorbrewer2.org.
# Color range -5 to +5; 0 = light gray
COLORS = [
    "#053061",
    "#2166ac",
    "#4393c3",
    "#92c5de",
    "#d1e5f0",
    "#f7f7f7",
    "#fddbc7",
    "#f4a582",
    "#d6604d",
    "#b2182b",
    "#67001f",
]



#  --------
class TabBase( QWidget ) :
    def __init__(self):
        """
        some var for later use
        """
        super().__init__()

        self.help_file_name     =  "unknown.txt"
        #self._build_model()

        self.mutate_dict    = {}
        self.mutate_ix      = 0
        # _build_gui(self,   ): call from child

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of widgets
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        self._build_gui_top(     layout )
        self._build_gui_widgets( layout )
        self._build_gui_bot(     layout )

    # -------------------------------
    def _build_gui_top( self, layout ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of widgets
        """
        # ---- new row
        row_layout          = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        widget              = QLabel( "classes...... on this tab" )
        self.class_widget   = widget  # widget showin calsses or widgets on tab
        row_layout.addWidget( widget,   )

    # -------------------------------
    def _build_gui_widgetsssss(self, layout  ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of widgets
        """
        # ---- new row
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        # widget    =  self.view
        # row_layout.addWidget( widget,   )

        # # ---- new row,
        # row_layout = QHBoxLayout(   )
        # layout.addLayout( row_layout,  )

        # ---- PB
        widget = QPushButton("select_all\n")
        #widget.clicked.connect( self.select_all  )
        row_layout.addWidget( widget,   )


        # ---- "
        widget = QPushButton("select_with_where\n" )
        #widget.clicked.connect( self.select_with_where   )
        row_layout.addWidget( widget,   )



        # ---- self.inspect
        widget = QPushButton("inspect\n")
        #widget.clicked.connect( self.inspect    )
        row_layout.addWidget( widget,   )

        # ---- PB self.breakpoint
        widget = QPushButton("breakpoint\n")
        #widget.clicked.connect( self.breakpoint    )
        row_layout.addWidget( widget,   )

    # -------------------------------
    def _build_gui_bot(self, layout  ):
        """
        make the bottom of the gui, mostly the large
        message widget
        layouts
            a vbox for main layout
        """
        # ---- new row
        row_layout      = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        # ----
        widget              = QTextEdit("load\nthis should be new row ")
        self.msg_widget     = widget
        #widget.clicked.connect( self.load    )
        row_layout.addWidget( widget,   )


    # ------------------------------------
    def mutate( self ):
        """
        read it

        """
        # print_func_header( "mutate" )

        # self.append_function_msg( "mutate" )

        max_ix          = len( self.mutate_dict)
        self.mutate_dict[ self.mutate_ix ]()
        self.mutate_ix   += 1
        if self.mutate_ix >= max_ix:
            self.mutate_ix = 0



    #----------------------------
    def clear_msg( self,  ):
        """
        read it --

        """
        self.msg_widget.clear()

    #----------------------------
    def append_function_msg( self, msg, clear = True ):
        """
        read it --
            and print to console
        msg is just the name of the function
        """
        msg     = f"----==== {msg} ====----"
        if clear:
            self.clear_msg(  )

        self.msg_widget.append( msg )
        print( msg )


    #----------------------------
    def append_msg( self, msg, clear = False ):
        """
        read it --
            and print to console
        """
        if clear:
            self.clear_msg(   )
        self.msg_widget.append( msg )
        print( msg )

    # # ------------------------
    # def inspect(self):
    #     """
    #     the usual
    #     """
    #     print_func_header( "inspect" )

    #     self_model         = self.model
    #     self_view     = self.view

    #     wat_inspector.go(
    #          msg            = "locals for model and view",
    #          a_locals       = locals(),
    #          a_globals      = globals(), )

    # # ------------------------
    # def breakpoint(self):
    #     """
    #     each tab gets its own function so we break in that
    #     tabs code
    #     """
    #     print_func_header( "breakpoint" )

    #     breakpoint()

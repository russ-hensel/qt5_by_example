#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---- tof
"""

tab_groupbox.py

self.help_file_name     =  "group_widget_tab.txt"

KEY_WORDS:      grid layout table new   new tab base stagetwo
CLASS_NAME:     GridLayoutTab
WIDGETS:        GridLayout
STATUS:         runs_correctly_5_10      demo_complete_2_10   !! review_key_words   !! review_help_0_10
TAB_TITLE:      GridLayout

"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #qt_widgets.main( )
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
from PyQt5.QtGui import QColor, QPalette, QTextCursor, QTextDocument

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel

from PyQt5.QtWidgets import (QAction,
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

import parameters
import tab_base
import utils_for_tabs as uft
import wat_inspector
import tab_base

# ---- end imports


# these must be defined at import time in uft
INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header

# ----------------------------
class GridLayoutTab( tab_base.TabBase  ) :
    def __init__(self):
        """
        the usual
            grid_layout_tab.GridLayoutTab
        """
        super().__init__()

        self.help_file_name     =  "grid_layout_tab.txt"

        self.mutate_dict[0]    = self.mutate_0
        self.mutate_dict[1]    = self.mutate_1
        # self.mutate_dict[2]    = self.mutate_2
        # self.mutate_dict[3]    = self.mutate_3
        # self.mutate_dict[4]    = self.mutate_4

        self._build_gui()


    def _build_gui_widgets(self, main_layout  ):
        """
        the usual, build the gui with the widgets of interest
        and the buttons for examples
        """
        layout              = QGridLayout(   )

        main_layout.addLayout( layout )
        button_layout        = QHBoxLayout(   )

    # # ----------------------------
    # def _build_gui(self,   ):
    #     """
    #     the usual
    #     """

    #     tab_page      = self

    #     layout        = QGridLayout( tab_page )

        ix_row        = 1
        ix_col        = 0

        row_span      = 1 # default is 1
        col_span      = 1 # default is 1

        # rowSpan: (Optional) The number of rows the widget should span. Defaults to 1.
        # columnSpan: (Optional) The number of columns the widget should span. Defaults to 1.

        for ix_row  in range( 0, 6 ):
            for ix_col in range( 0,4 ):
                widget = QPushButton(f"r{ix_row} c{ix_col}")
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        for ix_row  in range( 0, 6, 2 ):
            for ix_col in range( 4, 6 ):
                row_span      = 2
                col_span      = 1
                widget = QPushButton(f"r{ix_row} c{ix_col}")
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        ix_row   += 2
        button_layout  = QHBoxLayout()
        layout.addLayout( button_layout, ix_row, 0, row_span, 6 )


        widget = QPushButton("mutate\n")
        #self.button_ex_1         = widget
        widget.clicked.connect( lambda: self.mutate( ) )
        button_layout.addWidget( widget )



        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )




    # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_0" )

        msg    = "so far not implemented "
        self.append_msg( msg, clear = False )

    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_1" )
        msg    = "so far not implemented "
        self.append_msg( msg, clear = False )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        self.append_function_msg( "inspect" )

        # make some locals for inspection
        wat_inspector.go(
             msg            = "gridlayouttab",
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        keep this in each object so user breaks into that object
        """
        self.append_function_msg( "breakpoint" )

        breakpoint()


# ---- eof
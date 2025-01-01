#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---- tof
"""

tab_groupbox.py

self.help_file_name     =  "group_widget_tab.txt"

KEY_WORDS:      grid layout table
CLASS_NAME:     GridLayoutTab
WIDGETS:        GridLayout
STATUS:         works
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

import utils_for_tabs as uft
import wat_inspector

# ---- end imports


# these must be defined at import time in uft
INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header

# ----------------------------
class GridLayoutTab( QWidget ) :
    def __init__(self):
        """
        the usual
            grid_layout_tab.GridLayoutTab
        """
        super().__init__()
        self._build_gui()
        self.help_file_name     =  "grid_layout_tab.txt"

    # ----------------------------
    def _build_gui(self,   ):
        """
        the usual
        """

        tab_page      = self

        layout        = QGridLayout( tab_page )

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

        return tab_page

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

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
        print_func_header( "breakpoint" )

        breakpoint()


# ---- eof
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof
"""
tab_qlist.py


KEY_WORDS:      list widget
CLASS_NAME:     QListWidgetTab
WIDGETS:        QListWidget
STATUS:         works
TAB_TITLE:      QListWidgetTab


"""


# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_widgets
    qt_widgets.main( )
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

INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header

#  --------
class QListWidgetTab( QWidget ) :
    def __init__(self):
        """
        the usual
        tab_list_widget.py
        """
        super().__init__()
        self._build_gui()
        self.help_file_name      =  "list_widget_tab.txt"

    #-----------------------------------------------
    def _build_gui(self,   ):
        """
        the usual
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        button_layout = QHBoxLayout( )

        # ---- QListWidget
        widget              = QListWidget(    )
        self.list_widget_1  = widget
        widget.setGeometry( 50, 50, 200, 200 )
        layout.addWidget( widget )

        widget.itemClicked.connect( self.list_clicked )

        values    =  [ "one", "two"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )

        widget.clear()

        values    =  [ "oneish", "twoish"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )
            index_to_select = 2
            widget.setCurrentRow(index_to_select)

        # --- buttons
        layout.addLayout( button_layout,  )

        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    # --------------------
    def list_clicked( self, item ):
        """
        when the list is clicked get the text
        """
        print_func_header( "list_clicked" )

        widget        = self.list_widget_1
        row           = widget.row(item)

        text = item.text()

        print(f"Clicked row: {row}, text: {text}")

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_list_widget_1  = self.list_widget_1
        wat_inspector.go(
             msg            = "from inspect method",
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        print_func_header( "breakpoint" )

        breakpoint()


# ---- eof
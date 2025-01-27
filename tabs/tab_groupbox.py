#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof
"""

tab_groupbox.py

self.help_file_name     =  "group_widget_tab.txt"

KEY_WORDS:      group collect widgets
CLASS_NAME:     QGroupBoxTab
WIDGETS:        QGroupBox
STATUS:         works
TAB_TITLE:      QGroupBox


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

# ---- imports neq qt




# ---- end imports



INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header


#  --------
class QGroupBoxTab( QWidget ) :
    def __init__(self):
        """
        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py
        tab_groupbox.py
        """
        super().__init__()
        self._build_gui()

    def _build_gui(self,   ):
        """
        build the gui
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        # ---- QGroupBox
        #groupbox   = QGroupBox()  # no title
        groupbox   = QGroupBox( "QGroupBox 1" )   # version with title

        groupbox.setStyleSheet("""
            QGroupBox {
                border: 2px solid blue;
                border-radius: 10px;
                margin-top: 15px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px;
                background-color: white;
            }
        """)

        layout.addWidget( groupbox )
        layout_b     = QHBoxLayout( groupbox  )

        self.build_gui_in_groupbox( layout_b )

        button_layout = layout # needs fixing

        # ---- PB inspect
        widget          = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        clear_button    = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    # ---------------------------
    def build_gui_in_groupbox( self, layout ):
        """
        this is a bit of gui built inside another groupbos = QGroupBox()
        """
        widget = QPushButton("do_nothing\n")
        #widget.clicked.connect(  self.show_values  )
        layout.addWidget( widget )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection
        my_tab_widget = self
        #parent_window = self.parent( ).parent( ).parent().parent()

        wat_inspector.go(
             msg            = "self.text_edit from inspect method",
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

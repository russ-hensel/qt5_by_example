#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof
"""
based lousely on
... /book_pyqt5_src/basic/widgets_2c.py


KEY_WORDS:      some stuff from the m fitz book lables with images
CLASS_NAME:     Fitz_2_Tab
WIDGETS:        QPixmap QLabel
STATUS:         works
TAB_TITLE:      Lable with Image


"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main_qt
    #main.main()
# --------------------



import inspect
import os
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
from PyQt5.QtGui import QColor, QPalette, QPixmap, QTextCursor, QTextDocument
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

# ---- imports neq qt




# ---- end imports

print_func_header   = uft.print_func_header

#  --------
class Fitz_2_Tab( QWidget ) :
    def __init__(self):
        """
        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py
        tab_misc_widgets.py
        """
        super().__init__()
        self._build_gui()
        self.mutate_ix   = 0
        self.help_file_name      =  "fitz_2_tab.txt"

    # -------------------------------
    def _build_gui(self,   ):
        """
        added some size control
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        # ---- fitz code here
        basedir = os.path.dirname(__file__)

        widget = QLabel("Hello")

        # # tag::scaledContents[]
        widget.setPixmap( QPixmap( "a_cat.jpg" ) )
        widget.setPixmap( QPixmap( "bird_house.jpg" ))

        # for some photos you may loose control of size this whould fix
        widget.setMinimumSize( 100, 75)  # Minimum width: 100px, Minimum height: 75px
        widget.setMaximumSize( 400, 300)  # Maximum width: 400px, Maximum height: 300px

        chat_says = """
        Summary of Methods:

            setFixedSize(width, height): Sets a fixed size.
            setMinimumSize(width, height): Sets a minimum size.
            setMaximumSize(width, height): Sets a maximum size.
            setSizePolicy(policy_horizontal, policy_vertical): Sets resizing behavior.
            resize(width, height): Sets the initial size of the QLabel.

        """

        #widget.setPixmap( QPixmap( "otjex.jpg" ) )
        #widget.setPixmap( QPixmap(os.path.join( basedir, "a_cat.jpg")) )
        widget.setScaledContents(True)
        # widget.setGeometry( 50, 50, 50, 50 ) #
        layout.addWidget( widget )

        # ---- new row, standard buttons
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_widgets_list   = self.widgets_list
        wat_inspector.go(
             msg            = "see self_widgets_list",
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

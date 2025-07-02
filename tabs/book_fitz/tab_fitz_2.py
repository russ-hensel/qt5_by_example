#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof
"""
based lousely on
... /book_pyqt5_src/basic/widgets_2c.py


KEY_WORDS:      some stuff from the m fitz book lables with images     new tab
CLASS_NAME:     Fitz_2_Tab
WIDGETS:        QPixmap QLabel
STATUS:         ** runs   !! runs_correctly      demo_complete_0_10
TAB_TITLE:      Lable with Image
HOW_COMPLETE:   5  #  AND A COMMENT


"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
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
import tab_base



# ---- end imports

#  --------
class Fitz_2_Tab(  tab_base.TabBase ) :
    def __init__(self):
        """
        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py
        tab_misc_widgets.py
        """
        super().__init__()

        self.mutate_dict[0]    = self.mutate_0
        self.mutate_dict[1]    = self.mutate_1
        # self.mutate_dict[2]    = self.mutate_2
        # self.mutate_dict[3]    = self.mutate_3
        # self.mutate_dict[4]    = self.mutate_4

        self.help_file_name = "fitz_2_tab.txt"
        self._build_gui()

    # -------------------------------
    def _build_guixxxxx(self,   ):
        """
        added some size control
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

    def _build_gui_widgets(self, main_layout  ):
        """
        the usual, build the gui with the widgets of interest
        and the buttons for examples
        """
        layout              = QVBoxLayout(   )

        main_layout.addLayout( layout )
        button_layout        = QHBoxLayout(   )

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

        widget = QPushButton("mutate\n")
        self.button_ex_1         = widget
        widget.clicked.connect( lambda: self.mutate( ) )
        button_layout.addWidget( widget )

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
        self.append_function_msg( "breakpoint" )

        breakpoint()

# ---- eof

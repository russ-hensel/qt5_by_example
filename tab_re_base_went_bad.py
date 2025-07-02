#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof


"""
Base class for demo tabs  -- a second version plan to descent then override

this is pretty much infrastructure for the application
not part of the widget examples

"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #qt_fitz_book.main()
# --------------------


#import inspect
#import json
import os
#import subprocess
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

DONE_MSG        = ( "<<-- done\n" )
INSPECT_MSG     = ( "inspect()"  )
BREAK_MSG       = ( "breakpoint()" )

# tab_base.DONE_MSG

#  --------
class TabReBase( QWidget ):
    def __init__(self):
        """
        some var for later use
        """
        super().__init__()

        self.help_file_name     =  "unknown.txt"
        #self._build_model()

        self.mutate_dict    = {}

        self.mutate_ix      = 0

        self.build_dict     = {}  # a list would suffice
        self.build_ix       = 0

        self.tab_layout     = None
        #self.help_file_set  = set()
        # _build_gui(self,   ): call from child

    #------------------------
    def post_init(self):
        """
        more init after child
        """
        # max_build_dict   = len( )
        self.set_help_file_name()
        self.next_gui_build()


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

    # -------------------------------
    def build_gui_last_buttons(self, row_layout  ):
        """
        self.build_gui_last_buttons(  row_layout  )
        """
        # ---- mutate
        widget = QPushButton("rebuild-\ngui")

        connect_to          = self.next_gui_build
        widget.clicked.connect( connect_to )
        row_layout.addWidget( widget )

        # ---- PB inspect
        widget              = QPushButton("wat\ninspect")
        connect_to          = self.inspect
        widget.clicked.connect( connect_to )
        row_layout.addWidget( widget )

        # ---- PB breakpoint
        widget              = QPushButton("breakpoint-\ndebug")
        connect_to          = self.breakpoint
        widget.clicked.connect( connect_to )
        row_layout.addWidget( widget )

    def replace_top_layout( self ):
        """

        :return: DESCRIPTION
        :rtype: TYPE

        """

        # Assuming tab_page is the parent widget (e.g., a QWidget or QTabWidget page)
        # and layout is the current QVBoxLayout
        # tab_page      = self
        # layout        = QVBoxLayout( tab_page )
        # self.tab_layout = layout
        # Step 1: Delete all widgets in the existing layout

        layout   = self.tab_layout
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)  # Remove the item at index 0
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()  # Schedule the widget for deletion
                # If the item is a layout, recursively delete its widgets
                elif item.layout() is not None:
                    def clear_layout(sub_layout):
                        while sub_layout.count():
                            sub_item = sub_layout.takeAt(0)
                            sub_widget = sub_item.widget()
                            if sub_widget is not None:
                                sub_widget.deleteLater()
                            elif sub_item.layout() is not None:
                                clear_layout(sub_item.layout())
                    clear_layout(item.layout())
                    item.layout().deleteLater()

            # Step 2: Delete the old layout
            layout.deleteLater()

        # Step 3: Create and set a new layout
        # new_layout = QVBoxLayout(tab_page)
        # tab_page.setLayout(new_layout)
        tab_page            = self
        layout              = QVBoxLayout(tab_page )
        self.tab_layout     = layout
        self.main_layout    = layout   # bit of confusion here

    # Now you can add new widgets to new_layout


    # ------------------------------------
    def set_help_file_name( self,   ):
        """
         read it
             check for dups and warn !!

         !! move help file to the dir where the class file is


         """

        splits                 = self.module_file .split( "/" )
        #self.help_file_name    = splits[ 1 ].replace( ".", "__") + ".txt"
        #self.help_file_name    = splits[ 1 ] + ".txt"

        file_path           = "/".join( splits[ 0:-1 ]  )
        print( f"{file_path =}" )
        file_name           = splits[ -1 ].split( "." )[0] + ".txt"
        print( f"{file_name =}" )
        #file_name           =  file_path + "/help/" + file_name
        file_name           =  file_path +  "/" + file_name
        print( f"{file_name =}" )

        self.help_file_name =  file_name

        msg    = (f"tab_checkbox.set_help_file_name() we have a "
                  f"help file {self.help_file_name = } ")
        logging.debug( msg )

    # ------------------------------------
    def next_gui_build( self ):
        """

        :return: DESCRIPTION
        :rtype: TYPE

        """
        # max_build_dict   = len( self.build_dict )

        self.replace_top_layout()
        layout     =  self.tab_layout

        self._build_gui_top( layout )

        self.build_dict[ self.build_ix ]()

        row_layout = QHBoxLayout()
        layout.addLayout( row_layout )
        self.build_gui_last_buttons( row_layout )

        self._build_gui_bot( layout )

        # ready for next post increment
        self.build_ix   += 1
        if self.build_ix >= len( self.build_dict ):
            self.build_ix = 0

    # ------------------------------------
    def mutate( self ):
        """
        read it
            may not be used may come back
            loop throug the mutate functions
        """
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

# ---- eof
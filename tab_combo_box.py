#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KEY_WORDS:      combo box or drop down list bos
CLASS_NAME:     QComboBoxTab
WIDGETS:        QComboBox
STATUS:         works
TAB_TITLE:      QComboBox
TAB_HELP:       combo_box_widget_tab.txt


self.help_file_name     =  "combo_box_widget_tab.txt"
/mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example/docs/combo_box_widget_tab.txt
"""
# ---- tof
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #main.main()
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

print_func_header =  uft.print_func_header

#  --------
class QComboBoxTab( QWidget ) :
    def __init__(self):
        """
        """
        super().__init__()
        self.help_file_name     =  "combo_box_widget_tab.txt"
        self._build_gui()

    # ---- combo tab ------------------------------------------------
    def _build_gui(self,   ):
        """
        all build on a local QWidget
        count : const int
        currentData : const QVariant
        currentIndex : int
        currentText : QString
        duplicatesEnabled : bool
        editable : bool
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        button_layout = QHBoxLayout(   )
        sub_layout    = QHBoxLayout(   )

        # ---- for combo_1
        layout.addLayout( sub_layout )

        widget          = QLabel("combo_1 -> ( non-editable ) -> ")
        sub_layout.addWidget( widget )

        # ---- combo_1
        widget        = QComboBox()
        self.combo_1  = widget

        widget.addItem('Zero')
        widget.addItem('One')
        widget.addItem('Two')
        widget.addItem('Three')
        widget.addItem('Four')

        widget.setCurrentIndex( 2 )   # set index

        # these work but in some case seem only to work with a lambda
        widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        widget.currentTextChanged.connect(  self.combo_currentTextChanged  )

        #widget.currentTextChanged.connect(self.current_text_changed)
        widget.setMinimumWidth( 200 )

        sub_layout.addWidget( widget )

        # ---- combo_2
        sub_layout    = QHBoxLayout(   )
        layout.addLayout( sub_layout )

        widget          = QLabel("combo_2 -> (editable) ->")
        sub_layout.addWidget( widget )

        widget        = QComboBox()
        self.combo_2  = widget

        widget.addItem('Zeroxx')
        widget.addItem('One')
        widget.addItem('Two')
        widget.addItem('Three')
        widget.addItem('Four')
        #widget.editable( True )
        widget.setEditable( True )   # if is edited then value does not match index

        widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        widget.currentTextChanged.connect(  self.combo_currentTextChanged  )

        #widget.currentTextChanged.connect(self.current_text_changed)
        widget.setMinimumWidth( 200 )

        sub_layout.addWidget( widget )

        # ---- buttons
        layout.addLayout ( button_layout )
        # --- buttons
        label       = "combo\n_reload"
        widget = QPushButton( label )
        widget.clicked.connect( self.combo_reload )

        button_layout.addWidget( widget )

        # ---- PB mutate
        label       = "mutate\n"
        widget = QPushButton( label )
        widget.clicked.connect( self.mutate )

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

    # --------
    def show_combo_values(self):
        """
        what it says
        """
        print_func_header( "show_combo_values" )

        print( "show_combo_values")
        # ia_qt.q_combo_box( self.combo_1, "this is the first combobox from 1" )
        # current_text         = self.combo_1.currentText()
        # index                = self.combo_1.currentIndex()
        # msg   = ( f"\ncombo_1:"
        #           f"\n    current_text       = {current_text}"
        #           f"\n    index              = {index}"
        # )
        # print( msg )

        # current_text         = self.combo_2.currentText()
        # index                = self.combo_2.currentIndex()
        # index_text           = self.combo_2.itemText( index )
        # index_valid          = current_text == index_text
        # msg   = ( f"\ncombo_2:"
        #           f"\n    current_text       = {current_text}"
        #           f"\n    index              = {index}"
        #           f"\n    index_text         = {index_text}"
        #           f"\n    index_valid        = {index_valid}"
        # )
        # print( msg )
        # self.print_combo_values( self.combo_2 )
        #ia_qt.q_combo_box( self.combo_2, "this is the second combobox from 1" )


    # # add this to ia_qt
    # def print_combo_values(self, combo_box ):
    #     """Prints all items in the QComboBox and the value of a specific index."""
    #     # Get all values
    #     all_items = [ combo_box.itemText(i) for i in range( combo_box.count())]
    #     print(f"All items in the QComboBox: {all_items}")

    #     # Get value at a specific index (e.g., index 2)
    #     specific_index = 2
    #     if specific_index <   combo_box.count():
    #         value_at_index =  combo_box.itemText( specific_index )
    #         print(f"Value at index {specific_index}: {value_at_index}")
    #     else:
    #         print(f"Index {specific_index} is out of range.")



    # -----------------------
    def conbo_signal(self, arg ):
        """
                activated(int index)
        void 	currentIndexChanged(int index)
        void 	currentTextChanged(const QString &text)
        void 	editTextChanged(const QString &text)
        void 	highlighted(int index)
        void 	textActivated(const QString &text)
        void 	textHighlighted(const QString &text)
        """
        print_func_header( "conbo_signal" )

        print( f"conbo_signal {arg}")

    # -----------------------
    def conbo_currentIndexChanged(self, arg ):
        """
        what it says
        """
        print_func_header( "conbo_currentIndexChanged" )


    # -----------------------
    def combo_currentTextChanged(self, arg ):
        """
               activated(int index)
        void 	currentIndexChanged(int index)
        void 	currentTextChanged(const QString &text)
        void 	editTextChanged(const QString &text)
        void 	highlighted(int index)
        void 	textActivated(const QString &text)
        void 	textHighlighted(const QString &text)
        """
        print_func_header( "combo_currentTextChanged" )
        print( f"combo_currentTextChanged {arg}")

    # --------------------------
    def combo_reload(self,   ):
        """
        notice order of events
        """
        print_func_header( "combo_reload" )

        print( f"combo_reload { '' }clear next --------", flush = True )
        values         =  [ "1_reload", "2", "3", "4", ]
            # what do i get I get a dict of lists, I need all the keys
        widget         = self.combo_1
        widget.clear()       # delete all items from Combobox
        print( f"combo_reload end clear / next addItems", flush = True )
        widget.addItems( values )


    # --------------------------
    def inspect_old( self, arg  ):
        """
        count : const int
        currentData : const QVariant
        currentIndex : int
        currentText : QString
        duplicatesEnabled : bool
        editable : bool
        """
        print_func_header( "inspect_old" )
        print( f"combo_info { '' }  --------", flush = True )

        widget         = self.combo_1

        info           = widget.count()
        msg            = f"widget.count() {info}"
        print( msg )

        info           = widget.currentData()    # seem to always get None
        msg            = f"widget.currentData() {info}"
        print( msg )

        # qt5 not working for me
        # info           = widget.editable
        # msg            = f".editable {info}"
        # print( msg )

        info           = widget.currentText()  # is good
        msg            = f".currentText() {info}"
        print( msg )

        info           = widget.currentIndex()
        msg            = f".currentIndex() {info}"
        print( msg )

        info           = widget.placeholderText()
        msg            = f".placeholderText() {info}"
        print( msg )

        self.show_combo_values()   # move this code here


        print( f"combo_info end { '' } --------", flush = True )

    # ----
    def mutate(self,   ):
        """
        what it says
        """
        print_func_header( "mutate" )

        print( "\n>>>>mutate   -- to do more "   )
        self.combo_1.setCurrentIndex( 2 )

        self.combo_2.setCurrentText( "2" )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection
        my_tab_widget = self
        combo_1       = self.combo_1
        combo_2       = self.combo_2
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

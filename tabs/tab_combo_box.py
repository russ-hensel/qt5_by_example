#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KEY_WORDS:      combo box or drop down list box return pressed editable press ddl   new tab
CLASS_NAME:     QComboBoxTab
WIDGETS:        QComboBox
STATUS:         works  5/10
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
import tab_base
# ---- imports neq qt

# ---- end imports



#  --------
class QComboBoxTab( tab_base.TabBase  ) :
    def __init__(self):
        """
        """
        super().__init__()
        self.help_file_name     =  "combo_box_widget_tab.txt"

        self.mutate_dict[0]    = self.mutate_0
        self.mutate_dict[1]    = self.mutate_1
        # self.mutate_dict[2]    = self.mutate_2
        # self.mutate_dict[3]    = self.mutate_3
        # self.mutate_dict[4]    = self.mutate_4

        self._build_gui()

    # ----------------------------------------------
    def _build_gui_widgets(self, main_layout  ):
        """
        all build on a local QWidget
        count : const int
        currentData : const QVariant
        currentIndex : int
        currentText : QString
        duplicatesEnabled : bool
        editable : bool
        """


        # tab_page      = self
        # layout        = QVBoxLayout( tab_page )
        # button_layout = QHBoxLayout(   )
        # sub_layout    = QHBoxLayout(   )

        # ---- for combo_1
        layout        = QVBoxLayout(   )
        main_layout.addLayout( layout )

        sub_layout    = QHBoxLayout(   )

        layout.addLayout( sub_layout )

        widget          = QLabel("combo_1 -> ( non-editable ) -> ")
        sub_layout.addWidget( widget )

        # ---- combo_1
        widget        = QComboBox()
        self.combo_1  = widget

        a_list        = ['Zero',
                         'One',
                         'Two',
                         'Three',
                         'Four' ]

        widget.addItems( a_list )
        # think there is a way to add all at once  widget.insertItems( values ) or addItems()
        # widget.addItem('Zero')
        # widget.addItem('One')
        # widget.addItem('Two')
        # widget.addItem('Three')
        # widget.addItem('Four')

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
        widget.setEditable( True )
        widget.lineEdit().returnPressed.connect( self.conbo_return )

        widget.addItem('Zeroxx')
        widget.addItem('One')
        widget.addItem('Two')
        widget.addItem('Three')
        widget.addItem('Four')

        widget.setEditable( True )   # if is edited then value does not match index

        widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        widget.currentTextChanged.connect(  self.combo_currentTextChanged  )

        #widget.currentTextChanged.connect(self.current_text_changed)
        widget.setMinimumWidth( 200 )

        sub_layout.addWidget( widget )

        # ---- buttons
        button_layout = QHBoxLayout(   )
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
        self.append_function_msg( "show_combo_values" )

        self.append_msg( "show_combo_values")
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
    def conbo_return(self, arg ):
        """

        """
        self.append_function_msg( "conbo_signal" )

        #print( f"conbo_signal {arg}")

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
        self.append_function_msg( "conbo_signal" )

        print( f"conbo_signal {arg}")

    # -----------------------
    def conbo_currentIndexChanged(self, arg ):
        """
        what it says
        """
        self.append_function_msg( "conbo_currentIndexChanged" )

        self.append_function_msg( "conbo_currentIndexChanged -- and get text" )

        self.append_msg( f"{self.combo_1.currentText( ) = }" )



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
        self.append_function_msg( "combo_currentTextChanged" )
        self.append_msg( f"combo_currentTextChanged {arg = }")
        self.append_msg( f"combo_currentTextChanged done")


    # --------------------------
    def combo_reload(self,   ):
        """
        notice order of events
        """
        self.append_function_msg( "combo_reload" )

        self.append_msg( f"combo_reload { '' }clear next --------", flush = True )
        values         =  [ "1_reload", "2", "3", "4", ]
            # what do i get I get a dict of lists, I need all the keys
        widget         = self.combo_1
        widget.clear()       # delete all items from Combobox
        self.append_msg( f"combo_reload end clear / next addItems", flush = True )
        widget.addItems( values )
        self.append_msg( f"combo_reload done")

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
        self.append_function_msg( "inspect_old" )
        self.append_msg( f"combo_info { '' }  --------", flush = True )

        widget         = self.combo_1

        info           = widget.count()
        msg            = f"widget.count() {info}"
        self.append_msg( msg )

        info           = widget.currentData()    # seem to always get None
        msg            = f"widget.currentData() {info}"
        self.append_msg( msg )

        # qt5 not working for me
        # info           = widget.editable
        # msg            = f".editable {info}"
        # print( msg )

        info           = widget.currentText()  # is good
        msg            = f".currentText() {info}"
        self.append_msg( msg )

        info           = widget.currentIndex()
        msg            = f".currentIndex() {info}"
        self.append_msg( msg )

        info           = widget.placeholderText()
        msg            = f".placeholderText() {info}"
        self.append_msg( msg )

        self.show_combo_values()   # move this code here


        self.append_msg( f"combo_info end { '' } --------", flush = True )

    # ----
    def mutate_old(self,   ):
        """
        what it says
        new mutate may be in base class
        """
        self.append_function_msg( "mutate old" )

        self.append_msg( "\n>>>>mutate   -- to do more "   )
        self.combo_1.setCurrentIndex( 2 )
        self.combo_2.setCurrentText( "2" )

        msg     = f"{self.combo_1.currentText =}"
        self.append_msg( msg  )

        self.append_msg( "mutate_old done" )

    # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_0" )

        msg    = 'combo_2.lineEdit().setText( "mutate_0" )  '
        self.append_msg( msg, clear = False )
        self.combo_2.lineEdit().setText( "mutate_0" )

        msg     = f"{self.combo_1.currentText =}"
        self.append_msg( msg  )

        self.append_msg( "mutate_0 done" )

    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_1" )

        msg    = 'combo_2.setCurrentText( "2" )'
        self.append_msg( msg, clear = False )
        self.combo_2.setCurrentText( "2" )

        msg    = 'combo_1.setCurrentIndex( 2 )'
        self.append_msg( msg, clear = False )
        self.combo_1.setCurrentIndex( 2 )

        self.append_msg( "mutate_1 done" )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        self.append_function_msg( "inspect" )

        # make some locals for inspection
        my_tab_widget = self
        combo_1       = self.combo_1
        combo_2       = self.combo_2
        wat_inspector.go(
             msg            = "self.text_edit from inspect method",
             a_locals       = locals(),
             a_globals      = globals(), )

        self.append_msg( "-- done" )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        self.append_function_msg( "breakpoint" )

        breakpoint()

        self.append_msg( "-- done" )
# ---- eof
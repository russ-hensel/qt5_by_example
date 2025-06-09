#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KEY_WORDS:      QLineEdit line edit lineedit
CLASS_NAME:     QLineEditTab
WIDGETS:        QLineEdit
STATUS:         look at misc widget.... and see what we can extract
TAB_TITLE:      QLineEdit



TAB_HELPxx:       combo_box_widget_tab.txt


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


# ---- end imports


#  --------
class QLineEditTab( tab_base.TabBase  ) :
    def __init__(self):
        """
        """
        super().__init__()
        self.help_file_name     =  "lable_widget_tab.txt"
        self.module_file       = __file__
        self.mutate_dict[0]    = self.mutate_0
        self.mutate_dict[1]    = self.mutate_1
        self.mutate_dict[2]    = self.mutate_2
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
        # ----
        layout        = QVBoxLayout(   )
        main_layout.addLayout( layout )

        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout )

        # ---- line edit
        widget              = QLineEdit( "line_edit_0 ")
        self.line_edit_0    = widget

        # these work but in some case seem only to work with a lambda
        # widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        # widget.currentTextChanged.connect(  self.combo_currentTextChanged  )

        #widget.currentTextChanged.connect(self.current_text_changed)
        widget.setMinimumWidth( 200 )

        row_layout.addWidget( widget )

        # ---- label_1
        widget              = QLineEdit(  "line_edit_1")
        self.line_edit_1    = widget

        # these work but in some case seem only to work with a lambda
        # widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        # widget.currentTextChanged.connect(  self.combo_currentTextChanged  )

        #widget.currentTextChanged.connect(self.current_text_changed)
        widget.setMinimumWidth( 200 )

        row_layout.addWidget( widget )


        # ---- buttons
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout )

        # ---- build_gui_last_buttons
        self.build_gui_last_buttons( layout )

    # -----------------------
    def conbo_return(self, arg ):
        """

        """
        self.append_function_msg( "conbo_signal" )
        self.append_msg( "/n" )
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

        self.append_msg( f"conbo_signal {arg = }")
        self.append_msg( "/n" )

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

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_0" )
        msg       = f"{self.line_edit_1.text() = }"
        self.line_edit_1.setReadOnly( False )
        msg      = "line_edit_1.setReadOnly( False )"
        self.line_edit_1.setText( msg )   # vs text()
        self.append_msg( msg )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_1" )


        self.line_edit_1.setReadOnly( True )
        msg      = "line_edit_1.setReadOnly( True )"
        self.line_edit_1.setText( msg )   # vs text()
        self.append_msg( msg )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_2( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_2-- nothing so far " )

        # msg    = 'combo_2.setCurrentText( "2" )'
        # self.append_msg( msg, clear = False )
        # self.combo_2.setCurrentText( "2" )

        # msg    = 'combo_1.setCurrentIndex( 2 )'
        # self.append_msg( msg, clear = False )
        # self.combo_1.setCurrentIndex( 2 )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        self.append_function_msg( "inspect" )

        # make some locals for inspection
        my_tab_widget      = self
        self_line_edit_0   = self.line_edit_0
        self_line_edit_1   = self.line_edit_1

        wat_inspector.go(
             msg            = "from tab inspect... ",
             a_locals       = locals(),
             a_globals      = globals(), )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        self.append_function_msg( "breakpoint" )

        breakpoint()

        self.append_msg( tab_base.DONE_MSG )


# ---- eof
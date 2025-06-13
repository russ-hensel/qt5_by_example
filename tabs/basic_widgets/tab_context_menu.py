#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---- tof
"""

tab_context_menu.py

KEY_WORDS:      context menu connect qq
CLASS_NAME:     ContextMenuTab
WIDGETS:        QContextMenu
STATUS:
TAB_TITLE:      QContextMenu


"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #main.main()
# --------------------------------


import inspect
import subprocess
import sys
import time
from datetime import datetime
from functools import partial
from subprocess import PIPE, STDOUT, Popen, run

import wat

from PyQt5 import QtCore
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

#import parameters

import utils_for_tabs as uft
import wat_inspector
import tab_base

# ---- end imports

print_func_header   = uft.print_func_header

#  --------
class ContextMenuTab( tab_base.TabBase ):
    """
    Now i have a doc string.


    see
    """
    def __init__(self):
        """
        mostly for buttons
        """
        super().__init__()
        self.module_file       = __file__      # save for help file usage
        self.mutate_dict[0]    = self.mutate_0
        self.mutate_dict[1]    = self.mutate_1
        self.mutate_dict[2]    = self.mutate_2
        self.mutate_dict[3]    = self.mutate_3
        # self.mutate_dict[4]    = self.mutate_4
        self._build_gui()

    def _build_gui_widgets( self, main_layout ):
        """
        the usual, build the gui with the widgets of interest

        """
        layout              = QVBoxLayout()
        main_layout.addLayout( layout )

        # too clever ??
        main_layout.addLayout( layout := QVBoxLayout() )

        #button_layout        = QHBoxLayout(   )

        # main_layout.addLayout( layout )
        # button_layout        = QHBoxLayout(   )

        # ---- new row c
        row_layout          = QHBoxLayout(   )
        layout.addLayout( row_layout )

        # ---- New Row button_1 and _2
        row_layout          = QHBoxLayout(   )
        layout.addLayout( row_layout )



        # ---- the QTextEdit
        widget       = QTextEdit()
        # layout.addWidget(text_edit, 4, 0, 1, 3)  # Row 4, Column 0, RowSpan 1, ColumnSpan 3
        self.text_edit  = widget

        print( f"{widget.minimumSize( ) =} ")
        widget.setMinimumHeight( 100 )
        # print(  ia_qt.q_text_edit( text_edit, msg = "QTextEditTab.text_edit" ) )
        self.set_custom_context_menu( widget )


        row_layout.addWidget( widget,  )


        # ---- new row, standard buttons
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )

        self.button_ex_1         = widget

        self.build_gui_last_buttons( button_layout )

    def clear_context_menu(self, widget ):
        # Option 1: Revert to default context menu
        widget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        # Option 2: Disable context menu entirely
        # self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)


    #----------------------------
    def set_custom_context_menu( self, widget ):
        """
        what it says
        """
        widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        widget.customContextMenuRequested.connect(self.show_context_menu)
        self.context_widget   = widget # for later use in menu

    #----------------------------
    def foo(self):
            # Example function to be called from context menu
            msg   = ("Foo action triggered!")
            self.append_msg( msg )


    def show_context_menu( self, pos):
        """
        refactor to action instead of all the named ones

        """
        widget = self.context_widget
        menu   = QMenu( widget )   # maybe widget ??

        # Add standard actions
        undo_action = menu.addAction("Undo")
        undo_action.triggered.connect(widget.undo)
        menu.addSeparator()

        cut_action = menu.addAction("Cut")
        cut_action.triggered.connect(widget.cut)
        copy_action = menu.addAction("Copy")
        copy_action.triggered.connect(widget.copy)
        paste_action = menu.addAction("Paste")
        paste_action.triggered.connect(widget.paste)
        menu.addSeparator()

        select_all_action = menu.addAction("Select All")
        select_all_action.triggered.connect(widget.selectAll)
        menu.addSeparator()

        # Add custom action
        foo_action = menu.addAction("Foo")
        foo_action.triggered.connect(self.foo)

        # Enable/disable actions based on context
        cursor = widget.textCursor()
        has_selection = cursor.hasSelection()
        can_undo = widget.document().isUndoAvailable()
        can_paste = QApplication.clipboard().text() != ""

        undo_action.setEnabled(can_undo)
        cut_action.setEnabled(has_selection)
        copy_action.setEnabled(has_selection)
        paste_action.setEnabled(can_paste)

        # Show the context menu
        menu.exec_(widget.mapToGlobal(pos))


    #----------------------------
    def get_button_style_sheet( self ):
        """
        what it says
        """
        return """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """

    # ------------------------------------
    def signal_sent( self, msg ):
        """
        when a signal is sent, use find
        """
        self.append_function_msg( "signal_sent" )
        # msg   = f"{function_nl}signal_sent"
        # print( msg )
        self.append_msg( f"signal_sent {msg}" )

        self.append_msg( "<<-- done" )

    # ------------------------------------
    def put_in_clipboard( self, a_string ):
        """
        what it says:
        """
        self.append_function_msg( "put_in_clipboard" )

        clipboard = QApplication.clipboard()

        # Set a string into the clipboard
        clipboard.setText( a_string )
        self.append_msg(  f"put_in_clipboard { a_string = }" )

        get_text_out   =   clipboard.text()

        self.append_msg( "<<-- done" )

    # ------------------------------------
    def clear_values( self ):
        """
        There is much more info to show
        """
        self.append_msg( "clear_values" )

        self.append_msg(  "\n\nclear_values")
        self.append_msg(  "clear_values self.line_edit_1 " )  # setText()   ??
        self.line_edit_1.setText( "" )
        # print( f"{self.little_widget_line_edit_1.isEnabled() = }" )  # setEnabled()
        # print( f"{self.little_widget_qlabel_1.text() = }" )  # setText() ??
        self.append_msg( "<<-- done" )

    # ------------------------------------
    def set_values( self ):
        """
        What it says
        """
        self.append_function_msg( "set_values" )

        self.append_msg(  "set_values  self.line_edit_1 " )  # setText()   ??
        self.line_edit_1.setText( "xxxxx" )
        # print( f"{self.little_widget_line_edit_1.isEnabled() = }" )  # setEnabled()
        # print( f"{self.little_widget_qlabel_1.text() = }" )  # setText() ??
        self.append_msg( "<<-- done" )

    # ------------------------------------
    def pb_1_clicked( self ):
        """
        What it says
        """
        self.append_msg( "pb_1_clicked" )
        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def pb_2_clicked( self ):
        """
        What it says
        """
        self.append_msg( "pb_2_clicked" )

        self.append_msg( "<<-- done" )

    # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets


        """
        self.append_function_msg( "mutate_0" )

        widget    = self.text_edit

        msg       = "clear custom context menu"
        self.append_msg( msg, )
        self.clear_context_menu( widget )

        msg    = "use setMinimumHeight() "
        self.append_msg( msg )
        widget.setMinimumHeight( 100 )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_1" )
        # msg    = "begin implementation"
        # self.append_msg( msg, clear     = False )

        widget    = self.text_edit

        msg       = "set custom context menu"
        self.append_msg( msg, clear = False )
        self.set_custom_context_menu( widget )


        msg    = "use setMinimumHeight() "
        self.append_msg( msg )
        widget.setMinimumHeight( 200 )


        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_2( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_2" )


        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_3( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_3" )

        msg    = "...."
        self.append_msg( msg, clear = False )




        self.append_msg( tab_base.DONE_MSG )

    # ---- connects -----------------------
    # --------------------------
    def return_pressed( self ):
        """
        what is says
        """
        self.append_function_msg( "return_pressed" )

        self.append_msg( "\n" )



    # ------------------------
    def inspect(self):
        """
        the usual
        """
        self.append_function_msg( tab_base.INSPECT_MSG )

        self_q_push_button_1    = self.q_push_button_1
        self_q_push_pbutton_2   = self.q_push_pbutton_2

        wat_inspector.go(
             msg            = "variables for inspection ",
             a_locals       = locals(),
             a_globals      = globals(), )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tabs code
        """
        self.append_function_msg( tab_base.BREAK_MSG )

        breakpoint()

        self.append_msg( tab_base.DONE_MSG )

# ---- eof

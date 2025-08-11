#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---- tof
"""
# metadata here including WIKI_LINK as Constant ( not comment )
# this material is used for selection access to the tab module which must
# be named tab_....py     among other things

KEY_WORDS:      russ
CLASS_NAME:     RussTextEditTab
WIDGETS:        QTextEdit
STATUS:         brand new
TAB_TITLE:      RussTextEdit / Experiment
DESCRIPTION:    Experiment with extending a text edit
HOW_COMPLETE:   20  #  AND A COMMENT -- <10 major probs  <15 runs but <20 fair not finished  <=25 not to shabby
"""
WIKI_LINK      =  "https://github.com/russ-hensel/qt5_by_example/wiki/What-We-Know-About-QPushButtons"

"""
Some Notes:




"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
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



# -------------------------------
class RussEditBase(  ):
    """


    """
    def __init__(self,
                 parent                 = None, ):

        self.up_button              = None
        self.dn_button              = None
        self.search_text_widget     = None
        self.last_position          = 0
        self.set_custom_context_menu(   )

    def make_search_wigets( self, ):
        """
        search_text_widget,  up_button,  dn_button  =  text_edit.make_search_wigets(  )
        """
        widget      = QPushButton( "Up✓")
        self.up_button  = widget
        widget.clicked.connect(  self.search_up  )

        widget      = QPushButton( "Down")
        self.dn_button  = widget
        widget.clicked.connect(  self.search_down )

        widget      = QLineEdit()
        self.search_text_widget   = widget


        return self.search_text_widget, self.up_button, self.dn_button


    # ---------------------
    def search_down( self,   ):
        """
        search for text see search up
            case insensitive
        """
        text_edit   = self
        search_text = self.search_text_widget.text()
        if search_text:
            cursor = text_edit.textCursor()
            cursor.setPosition( self.last_position )
            found = text_edit.find( search_text )

            if found:
                self.last_position = text_edit.textCursor().position()
                text_edit.ensureCursorVisible()  # Scroll to the found text

            else:
                # grok code
                self.last_position = 0
                cursor.setPosition(self.last_position)
                text_edit.setTextCursor(cursor)
                text_edit.ensureCursorVisible()  # Optional: Scroll to top if reset

    # ---------------------
    def search_up( self,  ):
        """case insensitive
        for an text edit search for a string
        the line_edit contains the string that is the target
        direction of search is up
        case insensitive
        may need to protect against trying to start beyond end !!
        as user may have deleted some text

        """
        text_edit   = self
        search_text = self.search_text_widget.text()
        if search_text:
            cursor = text_edit.textCursor()
            cursor.setPosition( self.last_position )

            found = text_edit.find( search_text, QTextDocument.FindBackward )

            if found:
                self.last_position = text_edit.textCursor().position()
                text_edit.ensureCursorVisible()  # Scroll to the found text

            else:
                self.last_position = text_edit.document().characterCount()
                cursor.setPosition( self.last_position )
                text_edit.setTextCursor(cursor)
                text_edit.ensureCursorVisible()  # Optional: Scroll to top if reset


    #----------------------------
    def set_custom_context_menu( self, ):
        """
        what it says
        """
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect( self.show_context_menu )


    # ---------------------------------------
    def show_context_menu( self, pos ):
        """
        from chat, refactor please !!
        !! needs extension

        """
        widget      = self
        menu        = QMenu( widget )

        # Add standard actions
        undo_action = menu.addAction("Undo")
        undo_action.triggered.connect(widget.undo)
        menu.addSeparator()

        cut_action = menu.addAction("Cut")
        cut_action.triggered.connect(widget.cut)

        copy_action = menu.addAction("Copy")
        # copy_action.triggered.connect(widget.copy)

        paste_action = menu.addAction("Paste")
        paste_action.triggered.connect( widget.paste )
        #menu.addSeparator()

        # ---- "Smart Paste"
        foo_action = menu.addAction("Smart Paste")
        #foo_action.triggered.connect(self.smart_paste_clipboard )
        menu.addSeparator()

        # ---- "Strip Sel"
        foo_action = menu.addAction("Strip Sel")
        #foo_action.triggered.connect( self.strip_lines_in_selection)
        #menu.addSeparator()

        # ---- "RStrip Sel"
        foo_action = menu.addAction("RStrip Sel")
        #foo_action.triggered.connect( self.strip_eol_lines_in_selection )
        #menu.addSeparator()

        # ---- ""Update Markup""
        foo_action = menu.addAction("Update Markup")
        #foo_action.triggered.connect( self.update_markup )
        menu.addSeparator()

        # ---- "Open Urls"
        foo_action = menu.addAction("Open Urls")
        #foo_action.triggered.connect( self.goto_urls_in_selection )
        menu.addSeparator()


        select_all_action = menu.addAction("Select All")
        select_all_action.triggered.connect(widget.selectAll)

        # ---- >>   go
        menu_action = menu.addAction(">>   go ...")
        #menu_action.triggered.connect( self.cmd_exec )
        menu.addSeparator()


        # Enable/disable actions based on context
        cursor = widget.textCursor()
        has_selection   = cursor.hasSelection()
        can_undo        = widget.document().isUndoAvailable()
        can_paste       = QApplication.clipboard().text() != ""

        undo_action.setEnabled(can_undo)
        cut_action.setEnabled(has_selection)
        copy_action.setEnabled(has_selection)
        paste_action.setEnabled(can_paste)
        foo_action.setEnabled(can_paste)

        # Show the context menu
        menu.exec_(widget.mapToGlobal(pos))



# -------------------------------
class RussTextEdit( QTextEdit, RussEditBase ):
    """

    """
    def __init__(self,
                 parent                 = None, ):

        # Initialize QTextEdit properly
        QTextEdit.__init__( self, parent )  # Call QTextEdit constructor with parent

#  --------
class RussTextEditTab( tab_base.TabBase ):
    """
    Reference examples for QPushButton


    this is also the place for documentation on the methods normally found
    in a tab_.... file and should display its naming and other coding conventions
    other tab_xxx files may not be as well commented, you should be familiar with
    the conventions and be able to read the code.
    """
    def __init__(self):
        """
        set up the tab

        this is pretty much boiler plate for a tab
        """
        super().__init__()
        self.module_file        = __file__      # save for help file usage

        global WIKI_LINK
        self.wiki_link          = WIKI_LINK

        # modify to match the number of mutate methods in this module
        self.mutate_dict[0]     = self.mutate_0
        self.mutate_dict[1]     = self.mutate_1
        # self.mutate_dict[2]     = self.mutate_2
        # self.mutate_dict[3]     = self.mutate_3
        # self.mutate_dict[4]     = self.mutate_4

        self._build_gui()


    #----------------------------
    def _build_gui_widgets(self, main_layout  ):
        """
        the usual, build the gui with the widgets of interest
        and the buttons for examples
        """
        layout              = QGridLayout(   )

        main_layout.addLayout( layout )
        # button_layout        = QHBoxLayout(   )

        # ---- the QTextEdit
        #text_edit       = QTextEdit()
        text_edit       = RussTextEdit()
        # layout.addWidget(text_edit, 4, 0, 1, 3)  # Row 4, Column 0, RowSpan 1, ColumnSpan 3
        self.text_edit  = text_edit

        print( f"{text_edit.minimumSize( ) =} ")
        text_edit.setMinimumHeight( 100 )
        # print(  ia_qt.q_text_edit( text_edit, msg = "QTextEditTab.text_edit" ) )

        ix_row     = 0
        ix_col     = 0
        row_span   = 1
        col_span   = 3

        layout.addWidget( text_edit, ix_row, ix_col, row_span, col_span )  # rowSpan, columnSpan Alignment  # args are
            # widget: The widget you want to add to the grid.
            # row: The row number where the widget should appear (starting from 0).
            # column: The column number where the widget should appear (starting from 0).
            # rowSpan (optional): The number of rows the widget should span (default is 1).
            # columnSpan (optional): The number of columns the widget should span (default is 1).
            # alignment (optional): The ali

        search_text_widget,  up_button,  dn_button  =  text_edit.make_search_wigets(  )

        ix_row     += 1
        ix_col     = 0
        row_span   = 1
        col_span   = 1

        layout.addWidget( search_text_widget, ix_row, ix_col, row_span, col_span )

        #ix_row     += 1
        ix_col     += 1
        row_span   = 1
        col_span   = 1

        layout.addWidget( up_button, ix_row, ix_col, row_span, col_span )

        #ix_row     += 1
        ix_col     += 1
        row_span   = 1
        col_span   = 1

        layout.addWidget( dn_button, ix_row, ix_col, row_span, col_span )

        # # ---- search
        # ix_row     += 1
        # ix_col     = 0
        # row_span   = 1
        # col_span   = 1

        # widget             = QLineEdit()
        # self.line_edit     = widget

        # # ---- see if these are legal
        # #widget.setHeight( 10 )   # ng
        # widget.setText( "Python")
        # # widget.append(  "append a bit" )
        # widget.setReadOnly( False )  # but this is default
        # # too soon to call
        #self.set_custom_context_menu( widget )


        # widget.maximumHeight(…) # maximumHeight(self) -> int
        # widget.maximumSize(…) # maximumSize(self) -> QSize
        # widget.maximumViewportSize(…) # maximumViewportSize(self) -> QSize
        # widget.maximumWidth(  ) # maximumWidth(self) -> int


        # ---- new row
        button_layout = QHBoxLayout( )
        ix_row    += 1
        layout.addLayout ( button_layout, ix_row, ix_col, row_span,  col_span )


        # ---- new row
        button_layout = QHBoxLayout(   )
        ix_row    += 1
        layout.addLayout ( button_layout, ix_row, ix_col, row_span,  col_span )


        self.build_gui_last_buttons( button_layout )




    #----------------------------
    def get_button_style_sheet( self ):
        """
        what it says

        when applied to a button changes a bit of its appearance

        this is important content for the widgets referenced on this tab
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
        # i do not know what the default state, perhaps wat_inspector can tell
    # ------------------------------------
    def signal_sent( self, msg ):
        """
        when a signal is sent, use find ???

        this is important content for the widgets referenced on this tab
        """
        self.append_function_msg( "signal_sent()" )
        # msg   = f"{function_nl}signal_sent"
        # print( msg )
        self.append_msg( f"signal_sent {msg}" )

        self.append_msg( tab_base.DONE_MSG )

    # ---- connects signals...   --------
    # --------------------------
    def return_pressed( self ):
        """
        what is says  -- not connected, delete?

        this is important content for the widgets referenced on this tab
        """
        self.append_function_msg( "return_pressed()" )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def pb_1_clicked( self ):
        """
        What it says

            this function may be connected to a button normally
            q_push_button_1

        this is important content for the widgets referenced on this tab
        """
        self.append_msg( "pb_1_clicked()" )
        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def pb_2_clicked( self ):
        """
        What it says

            this function may be connected to a button normally
            q_push_button_1

        this is important content for the widgets referenced on this tab
        """
        self.append_msg( "pb_2_clicked()" )

        self.append_msg( tab_base.DONE_MSG  )

    # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets
            these mutations will try to mimic a typical default state
            of a widget for the first push button the
            second will not be modified by mutate_0

        this is important content for the widgets referenced on this tab
        read the code for more insight, note messages to app and comments
        """
        self.append_function_msg( "mutate_0()" )
        return

        # ---- change widget
        msg    = "for q_push_button_1 we more or less reset it"
        self.append_msg( msg, clear = False )
            # we use a local variable because it reduces the amount of code
            # and does not run any slower
            # we use this local variable idea in many places
        widget          = self.q_push_button_1
        widget.setText( "text set in mutate_0()" )
        widget.width     = 300
        widget.setToolTip( None )
        widget.setStyleSheet( "" )

        # ---- change widget
        msg    = "for q_push_button_2 no mutations"
        self.append_msg( msg, )

        widget          = self.q_push_button_2
        # self.q_push_button_1.setDisabled( True )
        # self.q_push_button_2.setDisabled( False )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets

        this is important content for the widgets referenced on this tab
        read the code for more insight, note messages to app and comments
        """
        self.append_function_msg( "mutate_1()" )
        return
        # msg    = "begin implementation"
        # self.append_msg( msg, clear     = False )
        # for self.q_push_button_1

        msg    = "mess with q_push_button_1"
        self.append_msg( msg, )

        widget        = self.q_push_button_1
            # it is often convenient to use a local variable,
            # you will see this a lot in our code, it does not seem to
            # be typical but we think it should be

        msg    = "q_push_button_1 set a tooltip"
        self.append_msg( msg, )

        widget.setToolTip( "this is a tool tip" )
        widget.setText( "text set in \nmutate_1()" )
            # note \n
        widget.width     = 200

        # ---- change widget
        msg    = "some changes to q_push_button_2"
        self.append_msg( msg, clear = False )

        # ---- self.q_push_button_2
        widget        = self.q_push_button_2
        # msg    = "setChecked(True )"
        # self.append_msg( msg, )


        # msg        = f"{self.q_push_button_1.isChecked() = } "
        # self.append_msg( msg, )


        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_2( self ):
        """
        read it -- mutate the widgets

        this is important content for the widgets referenced on this tab
        read the code for more insight, note messages to app and comments
        """
        self.append_function_msg( "mutate_2()" )
        return

        msg    = "change some attributes..."
        self.append_msg( msg,  )


        widget     = self.q_push_button_1
        self.q_push_button_1.setText( "one line")
        self.q_push_button_1.width     = 500
        self.q_push_button_1.setVisible( False )

        msg    = "q_push_button_1 mess with checkable enabled..."
        self.append_msg( msg,  )

        self.q_push_button_1.setCheckable( True )
        self.q_push_button_1.setChecked( True )
        self.q_push_button_1.setDisabled( True )

        self.q_push_button_1.setVisible( True )

        # next does not seem to work
        self.q_push_button_1.setCheckable( True )

        # ---- change widget
        msg    = "some changes to q_push_button_2"
        self.append_msg( msg, clear = False )

        widget     = self.q_push_button_2
        widget.setCheckable( True )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_3( self ):
        """
        read it -- mutate the widgets

        this is important content for the widgets referenced on this tab
        read the code for more insight, note messages to app and comments
        """
        self.append_function_msg( "mutate_3()" )
        return

        msg    = "re-enable some stuff -- change attributes"
        self.append_msg( msg, clear = False )

        # ---- first widget
        widget      = self.q_push_button_1
        self.q_push_button_1.setText( "one line")
        self.q_push_button_1.width     = 500
        self.q_push_button_1.setDisabled( False )
        self.q_push_button_1.setVisible( True )
        self.q_push_button_1.setCheckable( True )
        self.q_push_button_1.toggle()

        msg    = "add menu to q_push_button_1"
        self.append_msg( msg, clear = False )

        menu                = QMenu(self)
        menu.addAction("Option 1")
        menu.addAction("Option 2")
        widget.setMenu( menu )

        # ---- change widget
        widget      = self.q_push_button_2
        msg         = "\nsome changes to q_push_button_2"
        self.append_msg( msg, clear = False )

        msg    = "q_push_button_2 mess with style sheet... hover ... color "
        self.append_msg( msg,  )

        widget.setCheckable( False )
        widget.setStyleSheet( self.get_button_style_sheet() )
        msg     = f"get style sheet from widget \n {widget.styleSheet()}"
        self.append_msg( msg,  )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_4( self ):
        """
        read it -- mutate the widgets

        this is important content for the widgets referenced on this tab
        """
        self.append_function_msg( "mutate_4()" )
        return

        msg    = "undo many of earlier mutations"
        self.append_msg( msg, clear = False )

        widget      = self.q_push_button_1
        self.q_push_button_1.setText( "one line")
        self.q_push_button_1.width     = 500
        self.q_push_button_1.setDisabled( False )
        self.q_push_button_1.setVisible( True )
        self.q_push_button_1.setCheckable( True )

        # seems to make togable, how to turn off
        #self.q_push_button_1.toggle()

        msg    = "add menu to q_push_button_1"
        self.append_msg( msg, clear = False )
        menu                = QMenu(self)
        menu.addAction("Menu Option 1")
        menu.addAction("Menu Option 2")
        # try to clear the menu
        widget.setMenu( None )

        # ---- change widget
        widget      = self.q_push_button_2
        msg         = "some changes to q_push_button_2"
        self.append_msg( msg, clear = False )

        widget.setStyleSheet("")
            # no style sheet

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------
    def inspect(self):
        """
        the usual

        Allows the user to inspect local and global variables using
        the wat_inspector

        this is pretty much boiler plate for a tab
        """
        self.append_function_msg( tab_base.INSPECT_MSG )

        # we set local variables to make it handy to inspect them
        self_q_push_button_1    = self.q_push_button_1
        self_q_push_button_2    = self.q_push_button_1

        wat_inspector.go(
             msg            = "for your inspection, some locals and globals",
             a_locals       = locals(),
             a_globals      = globals(), )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------
    def breakpoint(self):
        """
        each tab gets its own function so we break in that
        tab's code

        this is pretty much boiler plate for a tab
        """
        self.append_function_msg( tab_base.BREAK_MSG )

        breakpoint()

        self.append_msg( tab_base.DONE_MSG )

# ---- eof

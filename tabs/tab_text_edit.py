#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---- tof
"""
KEY_WORDS:      Example of a text edit for string input
CLASS_NAME:     QTextEditTab
WIDGETS:        QTextEdit
STATUS:         works
TAB_TITLE:      QTextEdit
"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main

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
class QTextEditTab( QWidget ) :
    def __init__(self):
        """
        the usual
        tab_text_edit.py
        """
        super().__init__()
        self._build_gui()
        # State variable to track search position
        self.last_position = 0

    #  --------
    def _build_gui(self,   ):
        """
        the usual
        """
        tab_page      = self
        layout        = QGridLayout( tab_page )

        # ---- the QTextEdit
        text_edit       = QTextEdit()
        # layout.addWidget(text_edit, 4, 0, 1, 3)  # Row 4, Column 0, RowSpan 1, ColumnSpan 3
        self.text_edit  = text_edit

        print( f"{text_edit.minimumSize( ) =} ")
        text_edit.setMinimumHeight( 100 )
        # print(  ia_qt.q_text_edit( text_edit, msg = "QTextEditTab.text_edit" ) )

        ix_row     = 0
        ix_col     = 0
        row_span   = 1
        col_span   = 1

        layout.addWidget( text_edit, ix_row, ix_col, row_span, col_span )  # rowSpan, columnSpan Alignment  # args are
            # widget: The widget you want to add to the grid.
            # row: The row number where the widget should appear (starting from 0).
            # column: The column number where the widget should appear (starting from 0).
            # rowSpan (optional): The number of rows the widget should span (default is 1).
            # columnSpan (optional): The number of columns the widget should span (default is 1).
            # alignment (optional): The ali

        # ----- search
        ix_row     += 1
        ix_col     = 0
        row_span   = 1
        col_span   = 1

        widget             = QLineEdit()
        self.line_edit     = widget

        # ---- see if these are legal
        #widget.setHeight( 10 )   # ng
        widget.setText( "widget.setText ")
        # widget.append(  "append a bit" )
        widget.setReadOnly( True )

        chat = """
Font Settings:

    setFont(QFont): Sets the default font for the editor.
    setFontPointSize(float): Sets the font size.
    setFontFamily(str): Sets the font family.

Color Settings:

    setTextColor(QColor): Sets the text color.
    setTextBackgroundColor(QColor): Sets the background color of the text.
    setPalette(QPalette): Adjusts the editor's color palette.

Alignment:

    setAlignment(Qt.AlignmentFlag): Aligns the text (e.g., Qt.AlignLeft, Qt.AlignRight).

Read-Only Mode:

    setReadOnly(bool): Makes the editor read-only (e.g., for displaying text only).

Line Wrapping:

    setLineWrapMode(QTextEdit.LineWrapMode): Controls text wrapping.
        Options: NoWrap, WidgetWidth, etc.
    setWordWrapMode(QTextOption.WrapMode): Adjusts word wrapping behavior.

Cursor Control:

    setTextCursor(QTextCursor): Sets the current text cursor.
    textCursor(): Retrieves the current cursor.
    moveCursor(QTextCursor.MoveOperation): Moves the cursor (e.g., QTextCursor.Start, QTextCursor.End).

Scrollbars:

    setVerticalScrollBarPolicy(Qt.ScrollBarPolicy): Controls vertical scrollbar visibility (e.g., Qt.ScrollBarAlwaysOn).
    setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy): Controls horizontal scrollbar visibility.

Undo/Redo:

    setUndoRedoEnabled(bool): Enables or disables undo/redo.
    undo(): Undoes the last action.
    redo(): Redoes the last undone action.
"""


        # widget.maximumHeight(…) # maximumHeight(self) -> int
        # widget.maximumSize(…) # maximumSize(self) -> QSize
        # widget.maximumViewportSize(…) # maximumViewportSize(self) -> QSize
        widget.maximumWidth(  ) # maximumWidth(self) -> int

        widget.setPlaceholderText( "Enter search text" )
        layout.addWidget( widget, ix_row, ix_col, row_span,  col_span )

        #ix_row     += 1
        ix_col     += 1
        row_span   = 1
        col_span   = 1
        widget           = QPushButton("Down")
        self.down_button = widget
        widget.clicked.connect(self.search_down)
        layout.addWidget( widget, ix_row, ix_col, row_span,  col_span )

        ix_col     += 1
        widget           = QPushButton("Up")
        self.up_button   = widget
        widget.clicked.connect( self.search_up )
        layout.addWidget( widget, ix_row, ix_col, row_span,  col_span )

        # ---- lower buttons
        ix_row     += 1
        ix_col     = 0
        row_span   = 1
        col_span   = 1
        button_layout = QHBoxLayout(   )
        layout.addLayout ( button_layout, ix_row, ix_col, row_span,  col_span )
            # if you have row_span you need col_span, only positional

        # ---- PB set_text\n_ver_1
        widget = QPushButton( "set_text\n_ver_1" )
        widget.clicked.connect(  self.set_text_ver_1 )
        #widget.setMaximumWidth(150)
        button_layout.addWidget( widget,   )

        # ---- PB set_text\n_ver_2
        widget = QPushButton( "set_text\n_ver_2" )
        widget.clicked.connect(  self.set_text_ver_2 )
        #widget.setMaximumWidth(150)
        button_layout.addWidget( widget,   )

        widget = QPushButton("insert_text\n")
        widget.clicked.connect( self.insert_text  )
        button_layout.addWidget( widget,  )

        # ---- PB clear_text
        widget = QPushButton("clear\n_text")
        widget.clicked.connect( self.clear_text )
        button_layout.addWidget( widget,   )

         # ---- PB copy_all_text
        widget = QPushButton( "copy_all\n_text" )
        widget.clicked.connect( self.copy_all_text  )
        button_layout.addWidget( widget,   )
        # ---- PB
        widget = QPushButton( "copy_line_of_text\n" )
        widget.clicked.connect(lambda: self.copy_line_of_text( text_edit ))
        button_layout.addWidget( widget,   )

        # ---- PB
        widget = QPushButton( "copy_n_lines\n_of_text" )
        widget.clicked.connect(lambda: self.copy_n_lines_of_text( text_edit, 5 ))
        button_layout.addWidget( widget,   )

        # ---- PB
        widget = QPushButton("copy_selected\n_text")
        widget.clicked.connect( self.copy_selected_text )
        button_layout.addWidget( widget,   )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    # ---------------  end of button actions and class
    # ---------------------------------------
    def display_string( self, a_string, update_now = False ):
        """
        !! we may phase out for print_string  or the reverse ??
             make one call the other
        print to message area, with scrolling and
        log if we are configured for it

        parameters.gui_text_log_fn    = False  # "gui_text.log"
                                               # a file name or something false


        parameters.log_gui_text       = False # True or false to log text
        parameters.log_gui_text_level = 10    # logging level for above

        !! add parameter clear_msg = True or false

        """
        """
        what it says
        """
        print_func_header( "display_string" )

        print(  f"in display_string, with a_string = {a_string}")
        # return
        #   try  !!!  QTextEdit.clear()
        cursor = self.text_edit.textCursor()
        # cursor.movePosition( QTextCursor::End )
        cursor.insertText( a_string )

    #  --------
    def print_message(self, text):
        """
        what is says
        """
        print_func_header( "print_message" )

        print("Button clicked:", text)

    #  --------
    def clear_text( self ):
        """
        """
        print_func_header( "clear_text" )

        self.text_edit.clear()

    #  --------
    def copy_text(self, text_edit):
        """
        what is says
        """
        print_func_header( "copy_text" )

        print( "QTextEditTab.copy_text"   )
        selected_text      = text_edit.toPlainText()
        QApplication.clipboard().setText(selected_text)
        print(  f" copy_text -> {selected_text }" )


    #  --------
    def copy_all_text( self, text_edit ):
        """
        what it says
        """
        print_func_header( "copy_all_text" )

        # text_edit not used
        all_text = self.text_edit.toPlainText()
        print( f"{all_text = }")

        self.copy_all_text_b( None )

        return all_text  # return not used

    #  --------
    def copy_all_text_b( self, text_edit ):
        """
        what it says
        """
        print_func_header( "copy_all_text_b" )

        text_edit   = self.text_edit
        # Save current cursor position
        cursor      = text_edit.textCursor()
        original_position = cursor.position()

        # Select all text and copy to the clipboard
        text_edit.selectAll()
        text_edit.copy()   # think goes to clipboard

        all_text = self.text_edit.toPlainText()

        # Restore cursor to its original position
        cursor.setPosition(original_position)
        text_edit.setTextCursor(cursor)

        print( "all text copied to clipboard" )

        return  all_text

    # ----
    def set_text_ver_1(self,  ):
        """
        what is says
        """
        print_func_header( "set_text_ver_1" )

        a_string    = 1 * (

        """
        More than 20 years have passed since I authored the Python
 e of the most popular
programming languages in the world. Python programmers also
have a wealth of information at their fingertips in the form of
advanced editors, IDEs, notebooks, web pages, and more. In fact,
there’s probably little need to consult a reference book when almost
any reference material you might want can be conjured to appear
before your eyes with the touch of a few keys.

        """ )

        self.text_edit.setText( a_string )
    # ----
    def set_text_ver_2(self,  ):
        """
        what is says
        """
        print_func_header( "set_text_ver_2" )

        a_string    = 22  * (

        """
        HOMEXCEL Sponges Kitchen 24pcs, Non-Scratch Scrub Dish Sponges,
        Safe on Non-Stick Cookware,Dual Sided Cleaning Sponges
        for Kitchen,Household,Bathroom and More

        """ )

        self.text_edit.setText( a_string )

    # ----------
    def set_textxxx(self, a_string ):
        """
        """
        print_func_header( "set_text_ver_2" )

        text_edit       = self.text_edit
        text_edit.clear()
        cursor          = text_edit.textCursor()
        cursor.insertText(a_string)

    # ----
    def delete_text(self, text_edit):
        """
        """
        print_func_header( "delete_text" )

        text_edit.clear()

    # ----
    def insert_text( self, ):
        """
        insert text at the cursor position
        """
        print_func_header( "insert_text" )

        a_string  = ( """>>---- so here is a bit
of text the we will
           ------------------> insert
at the cursor ----<<""")

        text_edit       = self.text_edit
        cursor          = text_edit.textCursor()
        cursor.insertText( a_string )

    #----------------------------
    def copy_selected_text(self,  ):
        """
        """
        print_func_header( "copy_selected_text" )

        text_edit       = self.text_edit
        selected_text   = text_edit.textCursor().selectedText()
        QApplication.clipboard().setText( selected_text )

        # to paste get the text with QApplication.clipboard().text()
        #clipboard = QApplication.clipboard()

        print(  f"   -> {selected_text = } now in clipboard" )

    #----------------------
    def copy_n_lines_of_text(self, text_edit, num_lines ):
        """
        copy some number of lines of text to clipboard

        """
        print_func_header( "copy_n_lines_of_text" )

        cursor = text_edit.textCursor()

        # Save the original cursor position
        original_position = cursor.position()

        # Move to the start of the current line
        cursor.movePosition(cursor.StartOfLine)

        # List to store the next lines
        lines = []

        # Collect the next `num_lines` lines
        for _ in range( num_lines ):
            # Select the line from the start to the end
            cursor.movePosition(cursor.EndOfLine, cursor.KeepAnchor)
            line_text = cursor.selectedText()

            # Add the selected line to the list
            lines.append(line_text)

            # Move to the start of the next line
            cursor.movePosition(cursor.Down)

        # Restore the original cursor position
        cursor.setPosition(original_position)
        text_edit.setTextCursor(cursor)

        # Print or return the list of lines
        print(f"Next {num_lines} lines:", lines)
        return lines

    #----------------------
    def copy_line_of_text(self, arg ):
        """
        chat:
        With a QTextWidge holding some text:
        from the cursor position copy the text from the
        beginning of the line to the end of the line.
        """
        print_func_header( "copy_line_of_text" )

        text_edit           = self.text_edit
        cursor              = text_edit.textCursor()
        # Save the original cursor position
        original_position   = cursor.position()
        cursor.movePosition( cursor.StartOfLine )

        # Select the text from the beginning to the end of the line
        cursor.movePosition(cursor.EndOfLine, cursor.KeepAnchor)
        selected_text = cursor.selectedText()
        # print(f"Copied text: {selected_text = }")

        # Optionally, copy to the system clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(selected_text)

        # Restore the original cursor position
        cursor.setPosition(original_position)
        self.text_edit.setTextCursor(cursor)

        print(f"Copied text: {selected_text = }")

    # ---------------------
    def search_down(self):
        """
        think i want no print for this
        search from current cursor down in text field
        """
        search_text = self.line_edit.text()
        if search_text:
            cursor = self.text_edit.textCursor()
            cursor.setPosition(self.last_position)
            found = self.text_edit.find(search_text)

            if found:
                self.last_position = self.text_edit.textCursor().position()
            else:
                # Reset position if end is reached and no match
                self.last_position = 0

    # ---------------------
    def search_up(self):
        """
        think i want no print for this
        search from current cursor up in text field
        """
        search_text = self.line_edit.text()
        if search_text:
            cursor = self.text_edit.textCursor()
            cursor.setPosition( self.last_position )
            # Use QTextDocument.FindBackward for backward search
            found = self.text_edit.find(search_text, QTextDocument.FindBackward)

            if found:
                self.last_position = self.text_edit.textCursor().position()
            else:
                # Reset position if start is reached and no match
                self.last_position = self.text_edit.document().characterCount()

    # ---------------------
    def inspect_widget(self,  ):
        """
        in a QTextEdit how do i find the position of the cursor
        move the cursor to some position, move the cursor to the top, or bottom
        """
        print_func_header( "inspect" )

        print( "\n >>>> inspect_widget.inspect_widget  -- to do "   )
        print( "some cursor stuff in copy__")
        # print( f"copy_all_text {self.copy_all_text( self.text_edit )}" )

    # ----
    def change_widget(self, text_edit ):
        """
        in a QTextEdit how do i find the position of the cursor
        move the cursor to some positext_edit.show()tion, move the cursor to the top, or bottom

        # Move the cursor by 5 characters while keeping the selection
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 5)

        # Apply the modified cursor to the QTextEdit to reflect the selection
        text_edit.setTextCursor(cursor)
        """
        print_func_header( "change_widget" )

        print( "\n>>>>change_widget   -- to do "   )
        print( "some cursor stuff in copy__")

        # Ensure that the cursor is visible and the widget scrolls to it
        text_edit.ensureCursorVisible()

        cursor = text_edit.textCursor()
        cursor.setPosition(10)  # Moves the cursor to position 10 in the text
        text_edit.setTextCursor(cursor)
        # Move the cursor by 5 characters while keeping the selection
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 5)
        # Apply the modified cursor to the QTextEdit to reflect the selection
        text_edit.setTextCursor(cursor)
        text_edit.show()
        # time.sleep( 1 )

        # cursor = text_edit.textCursor()
        # cursor.movePosition(QTextCursor.Start)   # .End
        # text_edit.setTextCursor(cursor)
        # time.sleep( 1 )

        # print( "cursor to end ")
        # cursor = text_edit.textCursor()
        # cursor.movePosition(QTextCursor.End)   # .End
        # text_edit.setTextCursor(cursor)

        # # Move cursor to position 100
        # cursor = text_edit.textCursor()
        # cursor.setPosition(100)
        # text_edit.setTextCursor(cursor)

        print( "\n>>>>change_widget   -- to do "   )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection
        local_self            = self
        #parent_window = self.parent( ).parent( ).parent().parent()
        local_self_text_edit  = self.text_edit
        wat_inspector.go(
             msg            = "inspect ",
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

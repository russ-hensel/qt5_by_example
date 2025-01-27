#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ---- tof
"""
Created on Fri Jan 10 16:32:00 2025
text edit extensions

        features to add

            have it created the edit need method
                 for it and change the inti
                 _obj   = TextEditExt( parameters )
                  self.text_edit = TextEcitExt.build_text_edit()

                  then build other stuff

            block indent and outdent

        widget                  = QLineEdit()
        self.line_edit          = widget
        widget.setPlaceholderText("Enter search text")
        button_layout.addWidget( widget, )

        # Buttons
        widget                  = QPushButton("Down")
        self.down_button        = widget
        widget.clicked.connect(self.search_down)
        button_layout.addWidget( widget,   )

        widget           = QPushButton("Up")
        self.up_button   = widget
        widget.clicked.connect(self.search_up)
        button_layout.addWidget( widget,   )

text_edit_ext.    ( )


"""

# ---- Qt
from PyQt5.QtGui import QIntValidator, QStandardItem, QStandardItemModel, QTextCursor
from PyQt5.QtCore import QDate, QModelIndex, Qt, QTimer, pyqtSlot
from PyQt5.QtGui import QTextCursor, QTextDocument

# ---- begin pyqt from import_qt.py
#from PyQt5.QtGui import QIntValidator, QStandardItem, QStandardItemModel, QTextCursor


# ---- QtSql


from PyQt5.QtWidgets import (QAction,
                             QActionGroup,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDateEdit,
                             QDockWidget,
                             QFileDialog,
                             QFrame,
                             QGridLayout,
                             QHBoxLayout,
                             QInputDialog,
                             QLabel,
                             QLineEdit,
                             QListWidget,
                             QMainWindow,
                             QMdiArea,
                             QMdiSubWindow,
                             QMenu,
                             QMessageBox,
                             QPushButton,
                             QSpinBox,
                             QTableView,
                             QTabWidget,
                             QTextEdit,
                             QVBoxLayout,
                             QWidget)

import webbrowser
# ---- local imports
from app_global import AppGlobal
import exec_qt      #


MARKER              = ">>"
EXEC_RUNNER         = None  # setup below
# TEXT_EXT            = None


class TextEditExt( object ):
    """
    About this class.....
    self.text_edit_ext_obj         = text_edit_ext.TextEditExt( AppGlobal.parameters, entry_widget)
    """
    #----------- init -----------
    def __init__(self, parameters, text_edit  ):
        """
        Usual init see class doc string
        """
        # this is the constructor run when you create
        # like  app = AppClass( 55 )
        self.parameters       = parameters
        self.text_edit        = text_edit

    # ------------------------------------------
    def get_template_ddl_values(self):
        """
        get the list of dropdown value from the
        parameter templates

        """
        values              = []
        text_templates      = self.parameters.text_templates
        for i_key, i_value in text_templates.items( ):
            values.append( i_key )

        return values

    # ---------------------------------
    def get_template_by_key( self, key ):
        """
        what it says
            when a dropdown needs a text item

        """

        text_templates      = self.parameters.text_templates
        text                = text_templates[ key ]

        return text

    # ---------------------------------
    def build_up_template_widgets( self,   ):
        """
        what it says
            perhap we should change to create
            and even return its button ??
            ddl_widget,  ddl_button_widget  =    self.tex_....build_up_template_widgets
        """

        #self.text_edit_ext_obj.set_up_widget( widget )
        # ---- combo
        widget              = QComboBox()
        self.ddl_widget     = widget
        #self.text_edit_ext_obj.set_up_widget( widget )
        values              = self.get_template_ddl_values()
        widget.addItems( values )
        widget.setCurrentIndex( 0 )
        widget.setMinimumWidth( 200 )

        # # these work but in some case seem only to work with a lambda
        # widget.currentIndexChanged.connect( self.conbo_currentIndexChanged )
        # widget.currentTextChanged.connect(  self.combo_currentTextChanged  )
        #widget.currentTextChanged.connect(self.current_text_changed)

        # ---- button
        label                   = "Paste Template"
        widget                  = QPushButton( label )
        self.ddl_button_widget  = widget
        #connect_to         = functools.partial( text_edit_ext.qt_exec, entry_widget )
        connect_to         = self.paste_template
        widget.clicked.connect( connect_to )

        return ( self.ddl_widget, self.ddl_button_widget )

    #-----------------------------------
    def paste_template ( self, ):
        """
        what it says
        """
        key    = self.ddl_widget.currentText( )
        text   = self.get_template_by_key( key )
        #rint( "this is the text we need to paste")
        #rint( text )
        self.insert_text_at_cursor( text )

    #-----------------------------------
    def paste_clipboard( self, ):
        """
        what it says
        """
        text    = QApplication.clipboard().text( )
        print( "this is the text we need to paste from clipboard")
        print( text )
        self.insert_text_at_cursor( text )

    # ------------------------
    def insert_text_at_cursor( self, text ):
        """
        insert text at the cursor position
        """
        text_edit       = self.text_edit
        cursor          = text_edit.textCursor()
        cursor.insertText( text )


# ------------------------
def get_snippet_lines( text_edit, do_undent = True  ):
    """
    title is line 0
    often for code
    assume cursor in the body
    but there is a built in find function

    # ---- top of text
    >beginmarker    anything else on line

    >>py this is a title
    print( 1 )
    for ix in range( 10, 15 ):
        print( ix )

    >beginmarker    anything else on line

    # ---- end  of text

    start scanning up:
        stop if hit begin marker or top ( or blank lines?

    now scan down and collect lines ( rstripped, no spaces no \n )

        stop if  n_blank lines
        marker
        or end of text
    """
    lines                   = []
    cursor                  = text_edit.textCursor()
    consective_blank_lines  = 0
    original_position       = cursor.position()
    cursor.movePosition( cursor.StartOfLine )
    prior_start_of_line     = cursor.position()

    # ---- upward scan
    for ix in range( 20 ):

        cursor.movePosition( QTextCursor.StartOfLine )
        cursor.movePosition(cursor.EndOfLine, cursor.KeepAnchor )
        selected_text = cursor.selectedText()

        selected_text   = selected_text.rstrip()
        if   selected_text == "":
            consective_blank_lines  += 1

        else:
             consective_blank_lines  = 0

        if selected_text.strip().lower().startswith( MARKER ):
            #rint( f"hit the top of marked text {ix =}")
            break # leave curor at begin of marker line

        # lines.append( selected_text  )

        cursor.movePosition( cursor.Up )
        cursor.movePosition( QTextCursor.StartOfLine )
        position       = cursor.position()
        if position == prior_start_of_line:
            print( f"is error !! hit the top of all text {ix =}")
            break
        else:
            prior_start_of_line  = position

    # now at top of text
    #rint( f"found the top of  text {ix =}")

    # ---- start down collecting lines
    consective_blank_lines  = 0
    on_top_line             = True
    for ix in range( 20 ):
        cursor.movePosition( cursor.EndOfLine, cursor.KeepAnchor )
        selected_text   = cursor.selectedText()
        selected_text   = selected_text.rstrip()

        if   selected_text == "":
            consective_blank_lines  += 1

        else:
             consective_blank_lines  = 0

        if consective_blank_lines  > 3:
            msg = f"scan down blank line limit {consective_blank_lines}"
            #rint( msg )
            break

        # hot on firs line down
        if not on_top_line and selected_text.strip().lower().startswith( MARKER ):
            #rint( f"hit the next line of marked text {ix =}")
            break # leave curor at begin of marker line
        else:
            on_top_line = False

        lines.append( selected_text  )

        # Move to the start of the next line 2 steps
        cursor.movePosition(cursor.Down)
        cursor.movePosition(QTextCursor.StartOfLine)
        position       = cursor.position()

        if position == prior_start_of_line:
            #rint( f"hit the end of text {ix =} ")
            break

        else:
            prior_start_of_line  = position

    if do_undent:
        lines   = undent_lines( lines )

    return lines

# ---------------------
def search_downxxxx( line_edit, text_edit ):
    """
    search for text
        case insensitive
    """
    search_text = line_edit.text()
    if search_text:
        cursor = text_edit.textCursor()
        #cursor.setPosition( self.last_position )
            # this last position stuff did not seem to do anything
        found = text_edit.find(search_text)

        if found:
            pass
            # self.last_position = self.text_edit.textCursor().position()

        else:
            pass
            # Reset position if end is reached and no match
            # self.last_position = 0

# ---------------------
def search_down(self):
    """
    search for text see search up
        case insensitive
    """
    search_text = self.line_edit.text()
    if search_text:
        cursor = self.text_edit.textCursor()
        cursor.setPosition( self.last_position )
        found = self.text_edit.find(search_text)

        if found:
            self.last_position = self.text_edit.textCursor().position()

        else:
            # Reset position if end is reached and no match
            self.last_position = 0


# ---------------------
def search_up( line_edit, text_edit ):
    """case insensitive
    for an text edit search for a string
    the line_edit contains the string that is the target
    direction of search is up
    case insensitive
    """
    search_text = line_edit.text()
    if search_text:
        cursor = text_edit.textCursor()
        #cursor.setPosition( self.last_position )
        # Use QTextDocument.FindBackward for backward search
        found = text_edit.find(search_text, QTextDocument.FindBackward )

        # if found:
        #     self.last_position = self.text_edit.textCursor().position()
        # else:
        #     # Reset position if start is reached and no match
        #     self.last_position = self.text_edit.document().characterCount()

#  --------
def copy_all_text( self, text_edit ):
    """
    what it says
        copy into clipboard
    """
    # Save current cursor position
    cursor = text_edit.textCursor()
    original_position = cursor.position()

    text_edit.selectAll()
    text_edit.copy()   # goes to clipboard
    all_text = self.text_edit.toPlainText()

    # Restore cursor
    cursor.setPosition(original_position)
    text_edit.setTextCursor(cursor)
    return  all_text

# ------------------------
def undent_lines( lines ):
    """
    delete leading spaces ( as per code )
    then return as a multiline string  that is a list of strings
        lines   is a list of lines


    """
    new_lines            = []
    if len( lines ) == 0:
        return new_lines

    num_leading_spaces   = len( lines[0] ) - len( lines[0].lstrip(' ') )
    #rint( f"{num_leading_spaces = }")
    leading_spaces       = " " * num_leading_spaces

    for i_line in lines:
        if i_line.startswith( leading_spaces ):
            i_line   = i_line[ num_leading_spaces : ]
        new_lines.append( i_line )

    return new_lines

# ------------------------
def qt_exec( text_edit ):
    """
    execute in a qt window from code in text_edit
    this is like the wat inspector but is not it
    >>

    for ix in range( 1, 5):
        print( ix )

    >>

    print( "hi there" )


    """
    code_lines       = get_snippet_lines( text_edit  )
    print( code_lines )
    code_lines       = undent_lines(code_lines)
    #rint( f"{code_lines = }")
    code    = "\n".join( code_lines[ 1:] )  # title in line 0 !!
    #rint( code )
    global   EXEC_RUNNER
    if EXEC_RUNNER is None:
        EXEC_RUNNER      = exec_qt.ExecRunner( AppGlobal.q_app  )

    EXEC_RUNNER.create_window(
                code       = code,
                a_locals   = locals(),
                a_globals  = globals(),
                msg        = "my code message" )


# ------------------------
def cmd_exec( text_edit ):
    """
    execute command parsed out of text

    py
    sh
    url
    shell
    text
    idle

    """
    code_lines       = get_snippet_lines( text_edit  )
    print( code_lines )
    code_lines       = undent_lines(code_lines)
    splits           = code_lines[0].split()
    if splits[0] == ">>":
        splits = splits[1:]        # toss the >>
    if splits[0].startswith( ">>" ):
        splits[0]  = splits[0][ 2: ]  # again toss the >>

    cmd         = splits[0].lower()
    cmd_args    = splits[ 1:]

    print( f"{cmd = } \n {cmd_args = }")

    if   cmd == "py":
        code    = "\n".join( code_lines[ 1:] )  # title in line 0 !!
        msg     = " ".join( cmd_args )
        if msg == "":
            msg  = "execute some python code"
        #rint( code )
        global   EXEC_RUNNER
        if EXEC_RUNNER is None:
            EXEC_RUNNER      = exec_qt.ExecRunner( AppGlobal.q_app  )

        EXEC_RUNNER.create_window(
                    code       = code,
                    a_locals   = locals(),
                    a_globals  = globals(),
                    msg        = msg,
                    autorun    = True )

    elif cmd == "idle":
        pass
    elif cmd == "text":
         filename     = cmd_args[0]
         AppGlobal.os_open_txt_file( filename )

    elif cmd == "url":
        filename     = cmd_args[0]
        webbrowser.open( filename, new = 0, autoraise = True )

    elif cmd == "idle":
        pass
    elif cmd == "idle":
        pass
    else:
        print( f"{cmd = } \n {cmd_args = }")
    # next case based on command cmd

# # ------------------------
# def cmd_exec( text_edit ):
#     """
#     execute command parsed out of text


#     """

# ---- eof





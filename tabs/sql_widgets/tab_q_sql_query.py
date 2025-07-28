#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof

"""
self.help_file_name     =  "sql_query_model_tab.txt"

KEY_WORDS:      sql query select insert delete update      rh dc
CLASS_NAME:     QSqlQueryTab
WIDGETS:        QSqlQuery
STATUS:         works
TAB_TITLE:      QSqlQuery / Reference
DESCRIPTION:    A reference for the QSqlQuery widget -- non visual sql
HOW_COMPLETE:   20  #  AND A COMMENT

this guy mixes up the qsql and my utilities or extensions, it should be split up

What We Know About QSqlQuery · russ-hensel/qt5_by_example Wiki
https://github.com/russ-hensel/qt5_by_example/wiki/What-We-Know-About-QSqlQuery


"""
WIKI_LINK      =  "https://github.com/russ-hensel/qt5_by_example/wiki/What-We-Know-About-QSqlQuery"

# --------------------
if __name__ == "__main__":
    #----- run the full app
    """
    import qt_sql_widgets
    qt_sql_widgets.main()
    """
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
                             QHeaderView,
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
import qt_table_model
import global_vars
import utils_for_tabs as uft
import wat_inspector
import qsql_utils
import tab_base

# ---- end imports


INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header

print( "==================================mover rename into databasetab ")

#-----------------------------------------------
"""
2025-07-22:DAV: SQLError forked from libs/qsql_utils.py SQLError

"""
class SQLError( Exception ):
    """
    raise SQLError( why, errors )
    """
    def __init__(self, why, errors = "not given"):
        """

        I really do not know what I am doing here, works
        but fix in future

        """

        # Call the base class constructor with the parameters it needs
        super( ).__init__( why )
        self.why    = why
        # Now for your custom code...
        self.errors = errors



#-----------------------------------------------
class QSqlQueryTab( tab_base.TabBase ):
    """

    """
    def __init__(self, ):
        """
        """
        super().__init__( )
        self.module_file        = __file__      # save for help file usage

        global WIKI_LINK
        self.wiki_link          = WIKI_LINK

        self.mutate_dict[0]     = self.mutate_0
        self.mutate_dict[1]     = self.mutate_1
        # self.mutate_dict[2]    = self.mutate_2
        # self.mutate_dict[3]    = self.mutate_3
        # self.mutate_dict[4]    = self.mutate_4
        self._build_gui()

    def _build_gui_widgets( self, main_layout ):
        """
        the usual, build the gui with the widgets of interest

        note that this is mostly buttons to activate the widget(s) of interest
        """
        # layout              = QHBoxLayout()
        # main_layout.addLayout( layout )

        # too clever ??
        main_layout.addLayout( layout := QHBoxLayout() )

        widget = QPushButton( "select_\nand_print" )
        widget.clicked.connect( self.select_and_print  )
        layout.addWidget( widget, )

        widget = QPushButton( "select_and\n_print_error" )
        widget.clicked.connect( self.select_and_print_error  )
        layout.addWidget( widget, )

        widget = QPushButton( "insert_\ndata" )
        widget.clicked.connect( self.insert_data  )
        layout.addWidget( widget,   )

        widget = QPushButton( "delete_\ndata" )
        widget.clicked.connect( self.delete_data  )
        layout.addWidget( widget,   )

        # ---- new row, for build_gui_last_buttons
        button_layout = QHBoxLayout(   )
        main_layout.addLayout( button_layout, )

        self.build_gui_last_buttons( button_layout )

    #-----------------------------------------------
    def select_and_print( self ):
        """
        select data then loop through with a print
        test qsql_utils
        """
        msg = ( "select_and_print()\n" )
        print_func_header( msg )
        self.append_msg( msg )

        sql     = """
            SELECT
                id,
                name,
                frequency
                FROM book_club
            """

        query      = QSqlQuery( global_vars.EX_DB )

        query_ok   =  qsql_utils.query_exec_error_check( query = query, sql = sql, raise_except = True )

        msg      = ("book_club table:")
        self.append_msg( msg )

        while query.next():
            a_id        = query.value(0)
            name        = query.value(1)
            frequency   = query.value(2)

            msg      = (f"ID: {a_id = }  { name = }  {frequency = }  ")
            self.append_msg( msg )

    #-----------------------------------------------
    def query_exec_error_check( self, query, sql = None, raise_except = True ):
        """
        2025-07-22:DAV: query_exec_error_check() forked from libs/qsql_utils.py query_exec_error_check()
    
        """
        query_ok    = True
        if sql is None:
            result  = query.exec_( )  # sql already in the query
        else:
            result  = query.exec_( sql )
    
        if not result:
            query_ok        = False
            error_txt       =  query.lastError().text()
            loc             = "query_exec_error_check"
            debug_msg        = f"{loc} >>> error sql = { sql } \n lastError = {error_txt = }"
            # logging.debug( debug_msg )
            # dialog          =  DisplaySQLError( parent = None, title = "SQL Error", msg = debug_msg )
            # if dialog.exec_() == QDialog.Accepted:
            #    pass
            raise SQLError( "sqlerror", debug_msg )
            msg = ( debug_msg )
            print_func_header( msg )
            self.append_msg( msg )
    
        else:
            pass
            #rint("Query executed successfully.")
        return query_ok
        
    
    #-----------------------------------------------
    def select_and_print_error( self ):
        """
        select data then loop through with a print
        test qsql_utils
        """
        print_func_header( "select_and_print_error() -- should throw error and exception " )

        sql     = """
            SELECT
                iddddddd,
                name,
                frequency
                FROM book_club
            """

        query      = QSqlQuery( global_vars.EX_DB )

        # FIXME: pull code out of qsql_utils and post here directly --
        # this should never refer to libs/qsql_utils.py
        # because the learner doesn't need to be jumping around.
        """
        query_ok   =  qsql_utils.query_exec_error_check(   query = query, sql = sql, raise_except = True )
        """
        query_ok   =  self.query_exec_error_check(   query = query, sql = sql, raise_except = True )

        msg      = ("book_club table:")
        self.append_msg( msg )

        while query.next():
            a_id        = query.value(0)
            name        = query.value(1)
            frequency   = query.value(2)

            msg      = (f"ID: {a_id = }  { name = }  {frequency = }  ")
            self.append_msg( msg )

    #-----------------------------------------------
    def insert_data( self ):
        """
        also see the tab_qsql_database.py  populate_book_club_table
        this uses bind variables, probably the safeest way to execute sql
        """
        msg = ( "insert_data()\n" )
        self.append_msg( msg )
        
        query = QSqlQuery(  global_vars.EX_DB  )

        table_data = [
            ("History",      "weekly"    ),
            ("Adventure",    "weekly"    ),
            ("Easterns",      "monthly"   ),
            ("Physics",      "daily"     ),
        ]

        for name, frequency in table_data:
            # this only one way to bind
            sql     = """INSERT INTO book_club (
                name,
                frequency  )
                VALUES (?, ? )
            """

            query.prepare( sql )
            query.addBindValue( name )
            query.addBindValue( frequency )
            query.exec()
        msg = ("added 4 things:")
        self.append_msg( msg )
        self.append_msg( f"added: {table_data}   " )

    #-----------------------------------------------
    def delete_data( self ):
        """

        FIXME:
        """
        print_func_header( "insert_data()" )
        msg = ( "delete_data()\n" )
        self.append_msg( msg )
        
        query = QSqlQuery(  global_vars.EX_DB  )
        
        sql     = """
            DELETE FROM book_club
            WHERE name = "Biography";
        """
        
        query.prepare( sql )
        query.exec()

    # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets


        """
        self.append_function_msg( "mutate_0()" )

        # msg    = "initial mutate"
        # self.append_msg( msg, clear = False )

        # self.q_push_button_1.setDisabled( True )
        # self.q_push_button_2.setDisabled( False )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_1()" )
        # msg    = "begin implementation"
        # self.append_msg( msg, clear     = False )
        # widget        = self.q_push_button_1
        # widget.setText( "two\nlines")
        # widget.width     = 200

        # self.q_push_button_1.setText( "two\nlines")
        # self.q_push_button_1.width     = 200
        # self.q_push_button_1.setDisabled( True )
        # self.q_push_button_1.setToolTip( "this is a tool tip" )
        # self.q_push_button_1.setVisible( True )

        # msg    = "setChecked(True )"
        # self.append_msg( msg, )
        # self.q_push_button_1.setCheckable( True )
        # self.q_push_button_1.setChecked(True )

        # msg        = f"{self.q_push_button_1.isChecked() = } "
        # self.append_msg( msg, )

        self.append_msg( tab_base.DONE_MSG )


    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect()" )

        # make some locals for inspection
        the_global_ex_db   =  global_vars.EX_DB
        # parent_window = self.parent( ).parent( ).parent().parent()
        # a_db          = parent_window.sample_db
        # model         = self.people_model
        # view          = self.people_view
        wat_inspector.go(
             msg            = "inspect...",
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        the usual
        """
        print_func_header( "breakpoint()" )

        breakpoint()


# ---- eof
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof

"""
self.help_file_name     =  "sql_query_model_tab.txt"

KEY_WORDS:      sql query select insert delete update  error qsql_utils
CLASS_NAME:     QSqlQueryTab
WIDGETS:        QSqlQuery
STATUS:         works
TAB_TITLE:      QSqlQueryTab


this guy mixes up the qsql and my utilities or extensions, it should be split up



"""


# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_sql_widgets
    qt_sql_widgets.main()
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


# ---- end imports


INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header

print( "==================================mover rename into databasetab ")

#-----------------------------------------------
class QSqlQueryTab( QWidget ):
    """
    Yes, you can use a QSqlQueryModel to loop through all the rows of a
    database table. While QSqlQueryModel is primarily a model class for
    displaying read-only data in views like QTableView, you can
    still access the data pro grammatically by iterating through the rows and columns.

    Here’s an example of how to use QSqlQueryModel to loop through each row in the table.
    """
    def __init__(self, ):
        """
        """
        super().__init__( )
        self.help_file_name     =  "sql_query_model_tab.txt"
        self.build_tab()

    #-----------------------------------------------
    def build_tab(self,   ):
        """
        build the tab gui ...
        """
        tab_page            = self

        #layout        = QVBoxLayout( tab_page )
        layout        = QVBoxLayout( tab_page )
        button_layout = QHBoxLayout(   )

        layout.addLayout( button_layout )

        widget = QPushButton( "select_\nand_print" )
        widget.clicked.connect( self.select_and_print  )
        button_layout.addWidget( widget,   )


        widget = QPushButton( "select_and\_print_error" )
        widget.clicked.connect( self.select_and_print_error  )
        button_layout.addWidget( widget,   )


        widget = QPushButton( "insert_\ndata" )
        widget.clicked.connect( self.insert_data  )
        button_layout.addWidget( widget,   )

        widget = QPushButton( "delete_\ndata" )
        widget.clicked.connect( self.insert_data  )
        button_layout.addWidget( widget,   )

        widget = QPushButton( "delete_\ndata" )
        widget.clicked.connect( self.delete_data  )
        button_layout.addWidget( widget,   )

        # ---- PB inspect
        widget              = QPushButton("inspect\n")
        connect_to          = self.inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB breakpoint
        widget              = QPushButton("breakpoint\n ")
        connect_to          = self.breakpoint
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

    #-----------------------------------------------
    def select_and_print( self ):
        """
        select data then loop through with a print
        test qsql_utils
        """
        print_func_header( "select_and_print" )

        sql     = """
            SELECT
                id,
                name,
                frequency
                FROM book_club
            """

        query      = QSqlQuery( global_vars.EX_DB )

        query_ok   =  qsql_utils.query_exec_error_check(   query = query, sql = sql, raise_except = True )

        print("book_club table:")

        while query.next():
            a_id        = query.value(0)
            name        = query.value(1)
            frequency   = query.value(2)

            print(f"ID: {a_id = }  { name = }  {frequency = }  ")


    #-----------------------------------------------
    def select_and_print_error( self ):
        """
        select data then loop through with a print
        test qsql_utils
        """
        print_func_header( "select_and_print_error -- should throw error and exception " )

        sql     = """
            SELECT
                iddddddd,
                name,
                frequency
                FROM book_club
            """

        query      = QSqlQuery( global_vars.EX_DB )

        query_ok   =  qsql_utils.query_exec_error_check(   query = query, sql = sql, raise_except = True )

        print("book_club table:")

        while query.next():
            a_id        = query.value(0)
            name        = query.value(1)
            frequency   = query.value(2)

            print(f"ID: {a_id = }  { name = }  {frequency = }  ")

    #-----------------------------------------------
    def insert_data( self ):
        """
        also see the tab_qsql_database.py  populate_book_club_table
        this uses bind variables, probably the safeest way to execute sql
        """
        print_func_header( "insert_data" )

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

        # !! do we ever execute

    #-----------------------------------------------
    def delete_data( self ):
        """

        """
        print_func_header( "insert_data" )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

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
        print_func_header( "breakpoint" )

        breakpoint()


# ---- eof
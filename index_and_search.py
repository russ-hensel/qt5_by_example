#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build the database to search for tabs
"""

# ---- tof

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    # import qt_search
    # qt_search.main()
# --------------------

import inspect
import os
import sqlite3 as lite
import subprocess
import sys
from functools import partial
from pathlib import Path
from platform import python_version
from subprocess import PIPE, STDOUT, Popen, run

import key_word_indexer
#from app_global import AppGlobal
from PyQt5 import QtGui
from PyQt5.QtCore import (QDate,
                          QModelIndex,
                          QSize,
                          QSortFilterProxyModel,
                          Qt,
                          QTimer)
# sql
from PyQt5.QtSql import (QSqlDatabase,
                         QSqlField,
                         QSqlQuery,
                         QSqlQueryModel,
                         QSqlRecord,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlRelationalTableModel,
                         QSqlTableModel)
from PyQt5.QtWidgets import (QAbstractItemView,
                             QAction,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDataWidgetMapper,
                             QDateEdit,
                             QDialog,
                             QDoubleSpinBox,
                             QFormLayout,
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
                             QSpinBox,
                             QStyledItemDelegate,
                             QTableView,
                             QTableWidget,
                             QTableWidgetItem,
                             QTabWidget,
                             QTextEdit,
                             QVBoxLayout,
                             QWidget)

import global_vars
import parameters
import utils_for_tabs as uft
import wat_inspector

# ---- ---- local imports
print_func_header  = uft.print_func_header

# -----------------------------
def delete_db_file( file_name ):
    """
    will delete any file, but intended for db file
    """
    exists    = str( os.path.isfile( file_name ) )
    print( f"{file_name} exists {exists}" )

    if exists:
        try:
            os.remove( file_name )   # error if file not found
            print(f"removed {file_name} "  )

        except OSError as error:
            print( error )
            print( f"os.remove threw error on file {file_name}")

    else:
        print( f"file already gone  {file_name}                ")

# -------------------------------------
class TabDBBuilder():
    """
    this will create
    """
    #-------------------
    def __init__( self ):
        """
        The usual
        """
        self.db    = None
        self.reset()

        global_vars.set_tab_db( self.db  )
        global_vars.set_tab_db_builder( self  )

    #------------
    def reset( self, ):
        """
        Reset and rebuild the db
        """
        self.create_connection()
        self.create_populate_tables()

    #------------
    def create_connection( self, ):
        """
        Create a SQLite database connection.
        """
        if self.db is not None:
            self.db.close()
            self.db    = None  # or delete?

        db_file_name             = parameters.PARAMETERS.tab_db_file_name

        if db_file_name !=  ':memory:':
            # delete for a fresh start
            pass
            delete_db_file( db_file_name )

        db              = QSqlDatabase.addDatabase( parameters.PARAMETERS.tab_db_type, "tab_db" )
        db.setDatabaseName( db_file_name )
        self.db         = QSqlDatabase.database( "tab_db" )  # may need to do neare to use lets see

        if not db.open():
            print("IndexDB Error: Unable to establish a database connection.")
            return False
        return True

    # ---------------------------
    def create_populate_tables( self, ):
        """
        Create  tables.and populate with a bit of data
        """
        self.create_tab_table()
        self.create_tab_key_word_table()

        file_list     = self.find_doc_files()
        self.add_docs_to_db( file_list  )

        self.populate_key_word_table()

        self.query_print_tab()

    # ---------------------------
    def create_tab_table( self, ):
        """
        Create table
        ."""
        query   = QSqlQuery( self.db )

        sql     = """
            CREATE TABLE tabs (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_file_name   TEXT,
                name            TEXT,
                tab_title       TEXT,
                module          TEXT,
                class           TEXT,
                widgets         TEXT,
                key_words       TEXT
            )
        """

        if not query.exec_(sql):
            print("Error executing query:", query.lastError().text())
        else:
            pass
            #rint("Query executed successfully.")

    # ---------------------------
    def create_tab_key_word_table( self, ):
        """
        Create table
        ."""
        query   = QSqlQuery( self.db )

        sql     = """
            CREATE TABLE tabs_key_word (
                id              INTEGER,
                key_word        TEXT
            )
        """

        if not query.exec_(sql):
            print("create_tab_key_words_table Error executing query:", query.lastError().text())
        else:
            pass
            #rint("create_tab_key_words_table Query executed successfully.")

    #------------
    def find_doc_files( self, ):
        """
        find the object files and make a list
           may later need to use .name or .stem
        """
        directory_list      = parameters.PARAMETERS.dir_for_tabs
        file_list           = []
        #i_directory    = Path( "./" )
        for i_directory in directory_list:
            i_directory = Path( i_directory )

            i_file_list    = [file  for file in i_directory.glob('tab*.py')  ]
                    # not .stem or .name whic may be needed later

            file_list      = file_list + i_file_list
        for ix, i_file in enumerate( file_list ):
            pass
            #rint( ix, i_file)

        return file_list

    #------------
    def add_docs_to_db( self, doc_file_list  ):
        """
        add data from all the docs in doc_file_list to
        the database
        """
        for ix, i_doc in enumerate( doc_file_list ):
            doc_data  = self.get_doc_data( i_doc )
            # if str( i_doc ) == "tab_box_layout.py":
            #     pass
            #     #breakpoint()
            # must ave at least module and class

            # tab_title                   = doc_data[ "tab_title" ].strip()
            # tab_title.replace( "/", "\n")

            # tab_title                   = doc_data[ "tab_title" ].strip()

            # tab_title                   =  eval( "'" + tab_title + "'" )
            # doc_data[ "tab_title" ]     = tab_title

            module       = doc_data[ "module" ].strip()
            class_name   = doc_data[ "class_name" ].strip()
            if not bool( class_name ) or not bool( module ):
                continue

            self.doc_data_to_db( doc_data )

    #------------
    def doc_data_to_db( self, doc_data ):
        """
        add a doc data to the db
        """
        query = QSqlQuery( self.db )

        table_data = [
            ( str( doc_data[ "doc_file_name"] ),
              "name??",
              doc_data[ "tab_title"],
              doc_data[ "module"],
              doc_data[ "class_name"],
              doc_data[ "widgets"],
              doc_data[ "key_words"],
            ),
        ]

        for doc_file_name, name,  tab_title, module, class_name, widgets, key_words in table_data:
            # this only one way to bind
            sql     = """INSERT INTO tabs (
                doc_file_name,
                name,
                tab_title,
                module ,
                class,
                widgets,
                key_words
                )
            VALUES ( ?, ?, ?, ?, ?, ?, ? )
            """
            query.prepare( sql )
            query.addBindValue( doc_file_name )
            query.addBindValue( name )
            query.addBindValue( tab_title )
            query.addBindValue( module )
            query.addBindValue( class_name )
            query.addBindValue( widgets )
            query.addBindValue( key_words )

            result   = query.exec_()
            if not result:
                print("doc_data_to_db Error executing query:", query.lastError().text())
                1/0
            else:
                pass
                #rint("doc_data_to_db Query executed successfully.")

    #------------
    def get_doc_data( self, file_name ):
        """
        beware file_name really file_name_path
        read the doc data into a dict strings?
        file_name think string or path
        change to with
        """
        #rint( f"get_doc_data {file_name = }")
        #rint( "could make a loop to do this maybe a comp !!")

        doc_data_items       = [ "doc_file_name",
                                  "class_name",    "tab_title",
                                  "key_words",     "widgets" ] # omit doc_file_name

        doc_data    = {}
        doc_data[ "module"  ]    = str( file_name )[ :-3 ]
        for i_doc_item in doc_data_items:
            doc_data[ i_doc_item ] = ""

        doc_data[ "doc_file_name" ] = file_name

        a_file  = open( file_name, 'r', encoding = "utf8", errors = 'ignore' )

        for ix, i_line in enumerate( a_file ):

            i_line    = i_line.rstrip('\n')   # this i think is the best way --- think is arg to have python strip
            i_line    = i_line.strip()
            #rint( f"reading line no {ix} =  {i_line }")


            if i_line.startswith( "KEY_WORDS:"):
                    i_line    = i_line[ 10: ].strip()
                    doc_data[ "key_words" ] = doc_data[ "key_words" ] + " " + i_line

            # if i_line.startswith( "MODULE:"):
            #         i_line    = i_line[ len("MODULE:" ): ].strip()
            #         doc_data[ "module" ] = doc_data[ "module" ] + " " + i_line

            key         = "class_name"
            if i_line.startswith(  f"{key.upper()}:"):
                    i_line    = i_line[ len(key) + 1 : ].strip()
                    doc_data[ key ] = doc_data[ key ] + " " + i_line

            key         = "widgets"
            if i_line.startswith(  f"{key.upper()}:"):
                    i_line    = i_line[ len(key) + 1 : ].strip()
                    doc_data[ key ] = doc_data[ key ] + " " + i_line

            key         = "tab_title"
            if i_line.startswith(  f"{key.upper()}:"):
                    i_line    = i_line[ len(key) + 1 : ].strip()
                    doc_data[ key ] = doc_data[ key ] + " " + i_line

            if ix > 20:   # line limit
                #rint( "break on ix .....")
                break

        a_file.close()

        #rint( f"{doc_data = }")

        return doc_data

    #------------
    def populate_key_word_table ( self, ):
        """
        Populate
        """
        print_func_header( "populate_key_word_table" )

        a_kwi     = key_word_indexer.KeyWordIndexer( db             = self.db,
                                                    table_name      = "tabs",
                                                    kw_table_name   = "tabs_key_word"   )
        a_kwi.loop_thru()

    #------------
    def query_print_tab( self, ):
        """
        Print out the table
        """
        print_func_header( "query_print_tab" )

        query           = QSqlQuery( self.db )

        #rint("tab table")

        sql   = "SELECT id, module, class, widgets, key_words FROM tabs"

        if not query.exec_( sql ):  # Check if execution failed
            print("Error executing query:", query.lastError().text())


        while query.next():
            a_id                = query.value(0)
            module              = query.value(1)
            a_class             = query.value(2)
            #rint(f"ID: {a_id},  {module = },   {a_class = }")

# ---- useless object but requred delete it later
class IndexSearch(   ):
    def __init__(self):
        """
        pass
        """
        pass
        self.build_stuff()

    def build_stuff( self ):
        pass
        self.index_db     = TabDBBuilder( )
        return self.index_db.db


# ---- eof
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 KEY_WORDS:      data mapper moves data from a model to a form crud sql
 CLASS_NAME:     DataMapperTab
 WIDGETS:        QSqlTableModel QDataWidgetMapper
 STATUS:         works
 TAB_TITLE:      DataMapper
 TAB_HELP:       data_mapper_tab.txt


self.help_file_name     =  "data_mapper_tab.txt"

 /mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example/docs//mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example/docs/data_mapper_tab.txt
"""


# ---- tof

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main

# --------------------

import inspect
#from   ex_qt import ia_qt
#import ia_qt
import subprocess
import sys
#import adjust_path
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
# widgets bigger
# widgets -- small
# layouts
from PyQt5.QtWidgets import (QAction,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDataWidgetMapper,
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
                             QStyledItemDelegate,
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
import global_vars
# ---- end imports

print_func_header   = uft.print_func_header

#-----------------------------------------------
class DataMapperTab( QWidget ):
    """
    here build a tab in its own class to hide its variables
    and have its own namespace

    """
    def __init__(self, ):
        """
        the usual
        """
        super().__init__( )
        self.help_file_name     =  "data_mapper_tab.txt"
        # Create a QSqlTableModel and set it to the people table
        model       = QSqlTableModel( self, global_vars.EX_DB  )
        self.model  = model
        model.setTable( 'employee' )
        model.select()
        self.row_index = 1

        self.build_tab()

    #-----------------------------------------------
    def build_tab(self,   ):
        """
        the usual widget construct and init
        """
        tab_page        = self
        layout          = QVBoxLayout( tab_page )

        button_layout = QHBoxLayout( tab_page )

        # Create QLineEdit widgets
        self.name_edit          = QLineEdit(self)
        self.dob_edit           = QLineEdit(self)
        self.occupation_edit    = QLineEdit(self)

        # Add labels and line edits to the layout
        layout.addWidget(QLabel("Name"))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("Date of Birth"))
        layout.addWidget(self.dob_edit)
        layout.addWidget(QLabel("Occupation"))
        layout.addWidget(self.occupation_edit)

        layout.addLayout( button_layout )

        # ----
        self.submit_button = QPushButton('select')
        self.submit_button.clicked.connect(self.submit_changes)
        button_layout.addWidget(self.submit_button)

        # ----
        self.submit_button = QPushButton('submit_changes')
        self.submit_button.clicked.connect(self.submit_changes)
        button_layout.addWidget(self.submit_button)

        # ---- QPushButton
        widget = QPushButton("goto_next")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.goto_next( ) )
        button_layout.addWidget( widget )

        # ---- QPushButton
        widget = QPushButton("goto_prior")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.goto_prior( ) )
        button_layout.addWidget( widget )

        # ---- data mapper
        # Set up QDataWidgetMapper
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)

        # Map the fields to the respective columns
        self.mapper.addMapping(self.name_edit,       1)  # Column 1: "name"
        self.mapper.addMapping(self.dob_edit,        2)   # Column 2: "dob"
        self.mapper.addMapping(self.occupation_edit, 3)  # Column 3: "occupation"

        # Set the row to display and map data to the widgets
        self.mapper.setCurrentIndex( self.row_index )

        # ---- new row, standard buttons
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )



    # def create_tab_connection( self ):
    #     # Setup a connection to an SQLite database (for example)
    #     db = QSqlDatabase.addDatabase('QSQLITE')
    #     self.db    = db
    #     db.setDatabaseName(':memory:')  # In-memory database, for demo purposes
    #     if not db.open():
    #         print("Unable to open database")
    #         return False

    #     # Create a sample table and insert data
    #     query = db.exec_("""
    #         CREATE TABLE people (
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             name TEXT,
    #             dob TEXT,
    #             occupation TEXT
    #         );
    #     """)

    #     query = db.exec_("""
    #         INSERT INTO people (name, dob, occupation) VALUES
    #         ('Alice', '1990-04-20', 'Engineer'),
    #         ('Bob', '1985-11-30', 'Designer'),
    #         ('Charlie', '1992-06-15', 'Developer');
    #     """)

    #     return True


    # -----------------------------
    def submit_changes(self):
        """
        Submit changes back to the database.
        """
        print_func_header( "submit_changes" )

        # Submit the changes to the model and the database
        self.mapper.submit()
        if self.model.submitAll():
            print("Changes submitted successfully!")
        else:
            print(f"Error submitting changes: {self.model.lastError().text()}")

    # -----------------------------
    def goto_next(self):
        """
        readme
        """
        print_func_header( "goto_next" )

        self.row_index += 1
        self.mapper.setCurrentIndex( self.row_index )
        print( f"{self.row_index = }")

    # -----------------------------
    def goto_prior(self):
        """
        readme
        """
        print_func_header( "goto_prior" )

        self.row_index -= 1
        self.mapper.setCurrentIndex( self.row_index )
        print( f"{self.row_index = }")

    #-----------------------------------------------
    def create_tab_connection( self ):
        # Setup a connection to an SQLite database (for example)
        pass

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        #self_widgets_list   = self.widgets_list
        wat_inspector.go(
             msg            = "tbd",
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


# ---- eof

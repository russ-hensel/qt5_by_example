#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:55:08 2024

tab_qsql_table_model.

self.help_file_name     =  "qsql_table_model_tab.txt"

KEY_WORDS:      sql query of a single table crud select insert update delete zz
CLASS_NAME:     QSqlTableModelTab
WIDGETS:        QSqlTableModel QTableView
STATUS:         works
TAB_TITLE:      QSqlTableModel



"""
# ---- tof

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #main.main()
# -------------------


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


import info_about
import utils_for_tabs as uft
import wat_inspector
import global_vars

# ---- end imports


INDENT              = uft.INDENT
print_func_header   =  uft.print_func_header

#-----------------------------------------------
class QSqlTableModelTab( QWidget ):
    """
    QSqlTableModel
        and  QTableView
    """
    def __init__(self, ):
        """
        """
        super().__init__( )
        self.help_file_name     =  "qsql_table_model_tab.txt"
        self._build_model()
        self._build_gui()
        self.ix_id_list         = 0

        self.id_list            = [ 1000, 1001, 1002, 1003, 1004, 3 ]
            # use for prior next
        self.select_all()

    # ------------------------------
    def _build_gui( self,   ):
        """
        What it says
        """
        tab_page       = self

        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

        layout.addWidget( self.people_view   )

        layout.addWidget( self.phone_view    )

        # --- buttons
        row_layout      = QHBoxLayout(   )
        layout.addLayout( row_layout )

        # ---- PB select_all
        widget              = QPushButton("select_all\n")
        connect_to          = self.select_all
        widget.clicked.connect( connect_to )
        row_layout.addWidget( widget )

        label       = "<<prior\n"
        widget      = QPushButton( label )
        connect_to  = partial( self.prior_next, -1 )
        widget.clicked.connect( connect_to )
        row_layout.addWidget( widget )


        label       = "next>>\n"
        widget      = QPushButton( label )
        connect_to  = partial( self.prior_next, 1 )
        widget.clicked.connect( connect_to )
        row_layout.addWidget( widget )


        # ---- PB get_selected_rows
        widget              = QPushButton("get_selected_rows\n")
        widget.clicked.connect( self.get_selected_rows )
        row_layout.addWidget( widget )

        # ---- PB get_data_values
        widget              = QPushButton("get_data_values\n")
        widget.clicked.connect( self.get_data_values )
        row_layout.addWidget( widget )

        # ---- PB inspect
        widget              = QPushButton("inspect\n")
        connect_to          = self.inspect
        widget.clicked.connect( connect_to )
        row_layout.addWidget( widget )

        # ---- PB breakpoint
        widget              = QPushButton("breakpoint\n ")
        connect_to          = self.breakpoint
        widget.clicked.connect( connect_to )
        row_layout.addWidget( widget )

    # ------------------------------
    def _build_model( self,   ):
        """
        build model and views if used here

        """
        # ---- people
        model                  = QSqlTableModel( self, global_vars.EX_DB   )
        self.people_model      = model
        model.setTable('people')

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .

        model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.people_view        = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        view.setSelectionBehavior( QTableView.SelectRows )
        view.clicked.connect( self._people_view_clicked  )

        # ---- people_phones
        model                  = QSqlTableModel( self, global_vars.EX_DB  )
        self.phone_model       = model
        model.setTable( 'people_phones' )

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.phone_view         = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        #view.setSelectionBehavior( QTableView.SelectRows )
        #view.clicked.connect( self._view_clicked  )

            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
       #  model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

    # ------------------------
    def get_selected_rows(self, index,   ):
        """ """
        print_func_header( "get_selected_rows" )

        print( "looking at the people view ")
        view            = self.people_view
        # Assuming `view` is your QTableView
        selection_model = view.selectionModel()
        if selection_model:
            selected_indexes = selection_model.selectedRows()  # Get the selected rows

            for index in selected_indexes:
                row = index.row()  # Get the row number
                print(f"Selected row: {row = }")

    # ------------------------
    def get_data_values(self,    ):
        """ """
        print_func_header( "get_data_values" )

        row             = 1
        column          = 1
        print( "for now not selectd by by x,y {x = } {y = }")

        model           = self.people_model


        # Retrieve the QModelIndex for the specified cell
        index   = model.index(row, column)

        # Get the data from the model at the specified index
        value = model.data(index)
        print( f"Value at row {row },  {column = }: {value = }" )

        # using column name
        column_name = "name"

        # Get the column index for the column name
        column = model.fieldIndex( column_name )

        if column == -1:
            print(f"Column '{column_name}' not found in the model.")
        else:
            # Retrieve the QModelIndex for the specified cell
            index = model.index(row, column)

            # Get the data from the model at the specified index
            value = model.data(index)
            print( f"Value at row {row}, column '{column_name}': {value}")

    # ------------------------
    def _people_view_clicked(self, index,   ):
        """ """
        print_func_header( "_people_view_clicked" )

        view    = self.people_view
        msg     = f"_view_clicked {index} "
        print( msg )
        msg     = f"{INDENT}{view = } there is much to explore here, row, column, values"
        print( msg )

        msg     = f"{INDENT}{index} {index.row() = } {index.column() = } "
        print( msg )

        model           = self.people_model
        people_model    = model
        no_rows         = model.rowCount()

        msg     = f"{INDENT}{model.rowCount() = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        age_ix       = 2
        age          = model.data( model.index( row_ix, age_ix ) )

        msg     = f"{INDENT}extracted data {age = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        key_ix       = 0 # column may have been hidden
        key          = model.data( model.index( row_ix, key_ix ) )

        msg     = f"{INDENT}extracted data {key = }   "
        print( msg )

        msg     = f"{INDENT}phones are now displayed for for the person clicked on"
        print( msg )

        # ---- sync up second model with row clicked in first
        phone_model     = self.phone_model
        phone_model.setFilter( f"person_id = {key}" )
        phone_model.select()

    # -----------------------
    def delete_selected_record(self):
        """
        !!What it says
        """
        print_func_header( "delete_selected_record" )


    # --------------------------
    def prior_next( self, delta  ):
        """
        What it says
        delta may be positive or negative
        """
        print_func_header( f"prior_next {delta = }" )

        ix                     = self.ix_id_list
        our_list               = self.id_list
        max                    = len( our_list )

        new_ix                 = ix + delta

        if   new_ix < 0:
            print( "wrap to max ix")
            new_ix  = max - 1

        elif new_ix >= max:
            print( "wrap to ix = 0")
            new_ix  = 0

        self.ix_id_list   = new_ix
        #return new_ix

        self.select_by_id( our_list[ new_ix ]  )


    # --------------------------
    def select_by_id( self, a_id   ):
        """
        What it says
        taken from stuff and simplifed
        """
        print_func_header( f"select_by_id for people {a_id = }" )

        record   = None
        model    = self.people_model

        #ia_qt.q_sql_query_model( model, "select_record 1" )
        model.setFilter( f"id = {a_id}" )
        model.select()
        #ia_qt.q_sql_query_model( model, "select_record 2" )

        print( f"{INDENT}select_by_id{model.rowCount() = }  ")

        print( info_about.get( model, msg = "select_by_id post filter and select " ) )

        if model.rowCount() > 0:
            record                  = model.record(0)
            #self.id_field.setText( str(record.value("id")) )
            #self.record_to_field( record )
            #self.textField.setText(record.value("text_data"))
            #self.record_state       = RECORD_FETCHED
            self.current_id         = a_id
            print( f"people id = {a_id}")

        else:
            msg    = f"Record not found! {a_id = }"
            print( msg )


    # -----------------------
    def save(self):
        """
        !!What it says
        """
        print_func_header( "save" )

    # # ------------------------
    # def print_data(self):
    #     """ """
    #     what    = "print_data"
    #     print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    #     DB_OBJECT.query_data()

    # # ------------------------
    # def do_selections(self):
    #     """ """
    #     what    = "print_data"
    #     print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    # ------------------------
    def select_all(self):
        """ """
        print_func_header( "select_all" )

        self.people_model.setFilter( "" )
        self.people_model.select()  # Load the data into the model

        self.phone_model.setFilter( "" )
        self.phone_model.select()

    # ------------------------
    def inspect(self):
        """ """
        print_func_header( "inspect" )

        # locals for inspection
        my_tab_widget       = self
        parent_window       = self.parent( ).parent( ).parent().parent()
        #a_db                = parent_window.sample_db
        people_model        = self.people_model
        people_view         = self.people_view
        wat_inspector.go(
             msg            = "inspect QSqlTableModelTab",
             # inspect_me     = self.people_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        keep this in each object so user breaks into that object
        """
        print_func_header( "breakpoint" )

        breakpoint()


# ---- eof

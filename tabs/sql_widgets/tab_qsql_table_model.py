#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:55:08 2024

tab_qsql_table_model.

self.help_file_name     =  "qsql_table_model_tab.txt"

KEY_WORDS:      sql query of a single table crud select insert update delete zzz
CLASS_NAME:     QSqlTableModelTab
WIDGETS:        QSqlTableModel QTableView
STATUS:         runs_correctly_?_10      demo_complete_2_10   !! review_key_words   !! review_help_0_10
TAB_TITLE:      QSqlTableModel

Search
    clear

"""
# ---- tof

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
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
import tab_base
# ---- end imports


INDENT              = uft.INDENT
# print_func_header   =  uft.print_func_header

#-----------------------------------------------
class QSqlTableModelTab( tab_base.TabBase   ):
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

        self.mutate_dict[0]     = self.mutate_0
        self.mutate_dict[1]     = self.mutate_1
        # self.mutate_dict[2]    = self.mutate_2
        # self.mutate_dict[3]    = self.mutate_3
        # self.mutate_dict[4]    = self.mutate_4

        self.select_all()

    #----------------------------
    def _build_gui_widgets(self, main_layout  ):
        """
        the usual, build the gui with the widgets of interest
        and the buttons for examples
        """
        layout              = QVBoxLayout(   )

        main_layout.addLayout( layout )
        button_layout        = QHBoxLayout(   )

        layout.addWidget( self.persons_view   )

        layout.addWidget( self.phone_view    )

        # --- buttons
        row_layout      = QHBoxLayout(   )
        layout.addLayout( row_layout )

        # ---- PB select_all
        widget              = QPushButton("select_all\n")
        connect_to          = self.select_all
        widget.clicked.connect( connect_to )
        row_layout.addWidget( widget )

        label       = "clear\n"
        widget      = QPushButton( label )

        widget.clicked.connect( self.clear )
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


        # ---- mutate
        widget = QPushButton("mutate\n")
        self.button_ex_1         = widget
        widget.clicked.connect( lambda: self.mutate( ) )
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
        # ---- persons
        model                  = QSqlTableModel( self, global_vars.EX_DB   )
        self.persons_model      = model
        model.setTable('persons')

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .

        model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.persons_view        = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        view.setSelectionBehavior( QTableView.SelectRows )
        view.clicked.connect( self._persons_view_clicked  )
        view.setSortingEnabled( True )

        # ---- persons_phones
        model                  = QSqlTableModel( self, global_vars.EX_DB  )
        self.phone_model       = model
        model.setTable( 'persons_phones' )

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.phone_view         = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        view.setSortingEnabled(True)
        #view.setSelectionBehavior( QTableView.SelectRows )
        #view.clicked.connect( self._view_clicked  )

            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
       #  model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

    # ------------------------
    def get_selected_rows(self, index,   ):
        """ """
        self.append_function_msg( "get_selected_rows" )

        print( "looking at the persons view ")
        view            = self.persons_view
        # Assuming `view` is your QTableView
        selection_model = view.selectionModel()
        if selection_model:
            selected_indexes = selection_model.selectedRows()  # Get the selected rows

            for index in selected_indexes:
                row     = index.row()  # Get the row number
                msg     = ( f"Selected row: {row = }" )
                self.append_msg( msg, )
    # ------------------------
    def get_data_values(self,    ):
        """ """
        self.append_function_msg( "get_data_values" )

        row             = 1
        column          = 1
        msg    = ( f"for now not selectd by by {row = } {column = }" )
        self.append_msg( msg, )

        model           = self.persons_model


        # Retrieve the QModelIndex for the specified cell
        index   = model.index(row, column)

        # Get the data from the model at the specified index
        value = model.data(index)
        msg    =  ( f"Value at row {row },  {column = }: {value = }" )
        self.append_msg( msg, )
        # using column name
        column_name = "name"

        # Get the column index for the column name
        column = model.fieldIndex( column_name )

        if column == -1:
            msg = ( f"Column '{column_name}' not found in the model." )
            self.append_msg( msg, )
        else:
            # Retrieve the QModelIndex for the specified cell
            index = model.index(row, column)

            # Get the data from the model at the specified index
            value = model.data(index)
            msg     = ( f"Value at   {row = },   '{column_name =}': {value}" )
            self.append_msg( msg, )


    # ------------------------
    def _persons_view_clicked(self, index,   ):
        """ """
        self.append_function_msg( "_persons_view_clicked" )

        view    = self.persons_view
        msg     = f"_view_clicked {index} "
        self.append_msg( msg, )
        msg     = f"{INDENT}{view = } there is much to explore here, row, column, values"
        self.append_msg( msg, )

        msg     = f"{INDENT}{index} {index.row() = } {index.column() = } "
        self.append_msg( msg, )

        model           = self.persons_model
        persons_model    = model
        no_rows         = model.rowCount()

        msg     = f"{INDENT}{model.rowCount() = }   "
        self.append_msg( msg, )

        # extract some data
        row_ix       = index.row()
        age_ix       = 2
        age          = model.data( model.index( row_ix, age_ix ) )

        msg     = f"{INDENT}extracted data {age = }   "
        self.append_msg( msg, )

        # extract some data
        row_ix       = index.row()
        key_ix       = 0 # column may have been hidden
        key          = model.data( model.index( row_ix, key_ix ) )

        msg     = f"{INDENT}extracted data {key = }   "
        self.append_msg( msg, )

        msg     = f"{INDENT}phones are now displayed for for the persons clicked on"
        self.append_msg( msg, )

        # ---- sync up second model with row clicked in first
        phone_model     = self.phone_model
        phone_model.setFilter( f"persons_id = {key}" )
        phone_model.select()

    # -----------------------
    def delete_selected_record(self):
        """
        !!What it says
        """
        self.append_function_msg( "delete_selected_record" )

    # --------------------------
    def prior_next( self, delta  ):
        """
        What it says
        delta may be positive or negative
        """
        self.append_function_msg( f"prior_next {delta = }" )

        ix                     = self.ix_id_list
        our_list               = self.id_list
        max                    = len( our_list )

        new_ix                 = ix + delta

        if   new_ix < 0:
            msg     = ( "wrap to max ix")
            self.append_msg( msg, )
            new_ix  = max - 1

        elif new_ix >= max:
            msg     = ( "wrap to ix = 0")
            self.append_msg( msg, )
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
        self.append_function_msg( f"select_by_id for persons {a_id = }" )

        record   = None
        model    = self.persons_model

        #ia_qt.q_sql_query_model( model, "select_record 1" )
        model.setFilter( f"id = {a_id}" )
        model.select()
        #ia_qt.q_sql_query_model( model, "select_record 2" )

        msg     = ( f"{INDENT}select_by_id{model.rowCount() = }  ")
        self.append_msg( msg, )


        #print( info_about.get( model, msg = "select_by_id post filter and select " ) )
        msg     = (  info_about.INFO_ABOUT.find_info_for(  model,
                                msg = "select_by_id post filter and select " ) )
        self.append_msg( msg, )


        if model.rowCount() > 0:
            record                  = model.record(0)
            #self.id_field.setText( str(record.value("id")) )
            #self.record_to_field( record )
            #self.textField.setText(record.value("text_data"))
            #self.record_state       = RECORD_FETCHED
            self.current_id         = a_id
            msg     = ( f"persons id = {a_id}")
            self.append_msg( msg, )

        else:
            msg    = ( f"Record not found! {a_id = }" )
            self.append_msg( msg, )


    # -----------------------
    def clear(self):
        """
        !!What it says

        from ask a chat bot
        Temporary Clearing: If the goal is to temporarily hide or reset the displayed
        data without affecting the database, using setTable("") or setQuery(QSqlQuery()) is safer

        If you only want to clear the view or selected data without altering the model, you can clear the view component:

            view.clearSelection()  # Assuming `view` is your QTableView

        or bad selection


        """
        self.append_function_msg( "clear experimenting with methods persons_model" )
        # like this the best
        # try a know bad select
        model       = self.persons_model
        model.setFilter( f"id = -99" )
        model.select()


    # -----------------------
    def save(self):
        """
        !!What it says
        """
        self.append_function_msg( "save" )

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
        self.append_function_msg( "select_all" )

        self.persons_model.setFilter( "" )
        self.persons_model.select()  # Load the data into the model

        self.phone_model.setFilter( "" )
        self.phone_model.select()



    # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_0" )

        msg    = "so far not implemented "
        self.append_msg( msg, clear = False )

        self.append_msg( "mutate_0 done" )

    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_1" )

        msg    = "so far not implemented "
        self.append_msg( msg, clear = False )

        self.append_msg( "mutate_1 done" )


    # ------------------------
    def inspect(self):
        """ """
        self.append_function_msg( "inspect" )

        # locals for inspection
        my_tab_widget       = self
        parent_window       = self.parent( ).parent( ).parent().parent()
        #a_db                = parent_window.sample_db
        persons_model        = self.persons_model
        persons_view         = self.persons_view
        wat_inspector.go(
             msg            = "inspect QSqlTableModelTab",
             # inspect_me     = self.persons_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        keep this in each object so user breaks into that object
        """
        self.append_function_msg( "breakpoint" )

        breakpoint()


# ---- eof

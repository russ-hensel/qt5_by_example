#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ---- tof
"""
self.help_file_name     =  "qsql_relational_table_model_tab_2.txt"

KEY_WORDS:      table model for relational sql join crud update add insert
CLASS_NAME:     QSqlRelationalTableModelTab_2
WIDGETS:         QSqlRelationalTableModel QTableView
STATUS:         works
TAB_TITLE:       QSqlRelationalTableModel

"""

"""


tab_q_sql_relational_model_2.QSqlRelationalTableModelTab_2()

"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_sql_widgets
    qt_sql_widgets.main( )
# --------------------


# ---- imports

import inspect
import os
import subprocess
import sys
from functools import partial
from platform import python_version
from subprocess import PIPE, STDOUT, Popen, run

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

import parameters
import utils_for_tabs as uft
import wat_inspector

INDENT        = uft.INDENT
BEGIN_MARK_1  = uft.BEGIN_MARK_2
BEGIN_MARK_2  = uft.BEGIN_MARK_2

def print_func_header( what ):
    """
    what is says
    """
    #what    = "fix_me"
    print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

#-----------------------------------------------
class QSqlRelationalTableModelTab_2( QWidget ):
    """
    for widgets joining two tables
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self.relation      = ( "", "", "",  )
        self.relation      = ( "people", "id", "name" )
        self.relation      = ( "people", "id", "name, age" )
        self.relation      = ( "people", "id", "name, age, id" ) # ng
               # try to add foreigh key now broken

        self.relation      = ( "people", "id", "name, age, person_id" ) #
               # try to add foreigh key now broken

        print( f"Note option of {self.relation = }")
        self.help_file_name     =  "qsql_relational_table_model_tab_2.txt"
        self._build_model()
        self._build_gui()

        self.model.select()

    # ------------------------------
    def _build_gui( self,   ):
        """
        the usual
        """
        tab_page      = self

        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

        layout.addWidget( self.view   )

        # --- buttons
        button_layout      = QHBoxLayout(   )
        layout.addLayout( button_layout )

        # ---- PB select_for\n_all
        widget            = QPushButton( "select_for\n_all" )
        connect_to        = self.select_all
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB select\n_some
        widget            = QPushButton( "select\n_some" )
        connect_to        = self.select_some
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB select\n_some
        widget            = QPushButton( "select\n_some" )
        connect_to        = self.select_some
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB set_heading_by_number
        widget            = QPushButton( "set_heading\n_by_number" )
        widget.clicked.connect( self.set_heading_by_number )
        button_layout.addWidget( widget )

        # ---- PB sset_heading_by name
        widget            = QPushButton( "set_heading\n_by_name" )
        widget.clicked.connect( self.set_heading_by_name )
        button_layout.addWidget( widget )

        # ---- PB "get_data\n_from_model"
        widget              = QPushButton( "get_data\n_from_model" )
        connect_to          = self.get_data_from_model
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB get_selected_rows
        widget            = QPushButton("get_selected\n_rows")
        widget.clicked.connect( self.get_selected_rows )
        button_layout.addWidget( widget )

        # ---- PB delete_selected_row
        widget            = QPushButton("delete_selected\n_row")
        widget.clicked.connect( self.delete_selected_row )
        button_layout.addWidget( widget )


        # ---- PB i"insert\n_record"
        widget            = QPushButton("add\n_record")
        connect_to        = self.add_record
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB add_test_record
        widget            = QPushButton("add_test\n_record")
        widget.clicked.connect( self.add_test_record )
        button_layout.addWidget( widget )

        # ---- PB add_test_record
        widget            = QPushButton("add_via\n_chat")
        widget.clicked.connect( self.add_via_chat )
        button_layout.addWidget( widget )


        # ---- PB i"insert\n_record"
        widget            = QPushButton("update_db\n")
        connect_to        = self.update_db
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB special inspect
        widget              = QPushButton("special\ninspect")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        connect_to          = self.special_inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB inspect
        widget              = QPushButton("inspect\n")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        connect_to          = self.inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- PB breakpoint
        widget            = QPushButton("breakpoint\n")
        connect_to        = self.breakpoint
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

    # ------------------------------
    def _build_model( self,   ):
        """
        build model and views if used here

        for _1
        sql behind this should be:  old
            SELECT
                people.id,
                people.name,
                people.age,
                people.family_relation,
                people_phones.phone_number
            FROM people
            LEFT JOIN people_phones ON people.id = people_phones.person_id

        for _2  -- turn around the primary table  most of fields come from secondary table
            SELECT
                people.id,
                people.name,
                people.age,
                people.family_relation,
                people_phones.phone_number
            FROM people_phones
            LEFT JOIN people ON people.id = people_phones.person_id

        """
        model           = QSqlRelationalTableModel( self )
        self.model      = model

        model.setTable( "people_phones" )   # fields are  id  person_id  phone_number  zone

        self.relation      = ( "", "", "",  )
        self.relation      = ( "people", "id", "name" )
        self.relation      = ( "people", "id", "name, age" )
        self.relation      = ( "people", "id", "name, age, id" ) # ng
               # try to add foreigh key now broken
        self.relation      = ( "people", "id", "name, age, person_id" ) # this seems to work
                               # pepple secondary table
                                           # id column in secondary table to join on see fieldIndex below
                                               # columns in secondary table to display  id will be surpressed

               # try to add foreigh key now broken
        #debug_var   = self.model.fieldIndex( "person_id" )   # field name to number
        model.setJoinMode( QSqlRelationalTableModel.LeftJoin )  # claud thinks this might help
        model.setRelation(
            self.model.fieldIndex( "person_id" ),    # column in primary table used for join
                QSqlRelation( *self.relation )
        )

            # column_index = model.fieldIndex( "age" )  # Get the column index for "name"
            # print( f"{column_index = }")
            # model.setSort( column_index , Qt.AscendingOrder)  # seems needs to be index no

        if False:
            model.setRelation(
                self.model.fieldIndex( "person_id" ),  # column name in first table,

                QSqlRelation( "people", "id", "name, age" )
                #             table to join to in second table
                #                      column to join on  people_phone.person_id = people.id
                #                             # columns from people phones to fetch.and display display
                #                                  rest of fetch is rest of columns in primay table
                #                                        phone number zone
                #QSqlRelation("people_phones", "person_id", "phone_number, zone")
            )

        # self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
        model.setEditStrategy( QSqlRelationalTableModel.OnManualSubmit )

        # !?? mayebe not
        self.select_all()

        # ---- view
        view        = QTableView()
        self.view   = view
        view.setModel( model)

        # --- view options
        view.resizeColumnsToContents()
        view.setAlternatingRowColors(True)
        view.setSortingEnabled(True)    # for click on header
        view.setSelectionBehavior( QTableView.SelectRows )

    # ------------------------
    def get_selected_rows_dupe_delete(self, index,   ):
        """ """
        print_func_header( "get_selected_rows" )

        view            = self.view   # QTableView

        selection_model = view.selectionModel()
        if selection_model:
            selected_indexes = selection_model.selectedRows()  # Get the selected rows

            for index in selected_indexes:
                row = index.row()
                print(f"Selected row: {row = }")

    # -----------------------
    def special_inspect(self):
        """
        what it says
        """
        print_func_header( "special_inspect" )

        model           = self.model
        new_record      = model.record()
        c_names         = []
        for ix in range( 7 ):
            i_name     = new_record.fieldName( ix )
            c_names.append( i_name )
            print( f"{ix = }:   {new_record.fieldName( ix ) = } " )

        #c_names      = [ "name", "phone_number", "xxx"]
        for i_name in c_names:
            print( f"{i_name = }:   {new_record.indexOf( i_name ) = } " )

        print( "\n field index on record names ")
        for i_name in c_names:
            print( f"{i_name = }:   {model.fieldIndex( i_name ) = }" )

        print( "did this get left off ?" )
        print( f'{ model.fieldIndex( "person_id") = }' )

        for column in range(model.columnCount()):
            header   = model.headerData(column, Qt.Horizontal)
            print(f"Column {column}: {header}")

    # -----------------------
    def add_via_chat( self ):
        """
        another way is just to insert with a sqlquery thing and \
        then reselect, not what i wanted to do but pagmatic
        do i reselect I do not see it

        """

        # if query.lastError().isValid():
        #     print(query.lastError().text())
        #     return

        # # Set up the model
        # model = QSqlRelationalTableModel()
        # model.setTable("people_phones")
        # model.setRelation(model.fieldIndex("person_id"), QSqlRelation("people", "id", "name"))
        # model.select()
        print_func_header( "add_via_chat" )

                # Add a new row
        model       = self.model
        db          = model.database()
        if not db.transaction():
            print("Failed to start transaction:", db.lastError().text())


        row         = model.rowCount()  # Index for the new row
        model.insertRow(row)

        # Set values for the new row  --- does auto gen work ok

        # which table are these in the primay table  -- think only person id which is really id
        model.setData(model.index( row, model.fieldIndex( "person_id")),     1001)   # 1001 = Alice ?
        model.setData(model.index( row, model.fieldIndex( "phone_number")), "123-456-7890")
        model.setData(model.index( row, model.fieldIndex( "zone")),          "Z")

        # Debugging: Check if the row was inserted
        print("New row data before submission:")
        for col in range(model.columnCount()):
            print(f"{model.headerData(col, Qt.Horizontal)}: {model.data(model.index(row, col))}")

        # update and -- do not see select
        if not model.submitAll():
            print("add_via_chat Error saving data:", model.lastError().text())

        else:
            print("Data added successfully.")

        if not db.commit():
            print("Database commit failed:", db.lastError().text())

        # Set up a view to display the data  --- do we need this ?? try without
        # view = QTableView()
        self.view.setModel(model)

        self.view.show()

    # -----------------------
    def add_record(self):
        """
        what it says
            we need to add to primary table here: people_phones

           SELECT
               people.id,
               people.name,
               people.age,
               people.family_relation,
               people_phones.phone_number

           FROM people_phones
           LEFT JOIN people ON people.id = people_phones.person_id

        """
        1/0   # us add via chat
        print_func_header( "add_record" )

        msg             = "data for id  123  name  John Doe"
        print( msg )

        model           = self.model
        new_record      = model.record()

        """
        CREATE TABLE people_phones (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id       INTEGER,
                phone_number    TEXT,
                zone            TEXT,
                FOREIGN KEY(person_id) REFERENCES people(id) ON DELETE CASCADE
            )
        """

        # --- set values
        new_record.setValue( "id", 123)                  # appeared
        new_record.setValue( "name", "John Doe")         # nothing visible
        new_record.setValue( "age", 30)                   # nothing visible
        new_record.setValue( "family_relation", "Brother")   # nothing visible
        new_record.setValue( "phone_number", "123 456 7890")   # appeared off by column
        new_record.setValue( "zone", "Z")   # appeared wrong place

        if model.insertRecord(-1, new_record):
            pass
            # if model.submitAll():
            #     print("Record inserted and changes committed to the database.")
            # else:
            #     print("Error committing changes:", model.lastError().text())
        else:
            print("Error inserting record:", model.lastError().text())

        print( "the database has not yet been updated -- "
                "you may want to update_db, select_all or get_data_from_model next ")

    # -----------------------
    def add_test_record(self):
        """
        what it says
            try to add to every column
            just test data so we can see where it goes

        some set data just disappears and mapping seems wrong
        """
        print_func_header( "add_test_record" )

        msg             = "data is data_0 _1....."
        print( msg )

        model           = self.model
        new_record      = model.record()

        # put in data
        c_names         = []
        for ix in range( 7 ):
            i_name     = new_record.fieldName( ix )
            c_names.append( i_name )
            print( f"{ix = }: {new_record.fieldName( ix ) = } " )
            if i_name:
                new_record.setValue( i_name, f"data_{ix}")

        if model.insertRecord(-1, new_record):
            pass

        else:
            print("Error inserting record:", model.lastError().text())


        print( "the database has not yet been updated -- you may want to update_db, select_all or get_data_from_model next ")


    # -----------------------
    def update_db(self):
        """
        what it says
        """
        print_func_header( "update_db" )

        model           = self.model

        if model.submitAll():
            print("Changes committed no error detected ")
        else:
            print("Error committing changes:", model.lastError().text())

        print( "you may want to select_all or get_data_from_model next ")


    # ------------------------
    def set_heading_by_number( self ):
        """
        what it says
        """
        print_func_header( "set_heading_by_number" )

        msg        = "The lables are in numeric order ."
        print( msg )

        model      = self.model
        model.setHeaderData(0, Qt.Horizontal, "c0")
        model.setHeaderData(1, Qt.Horizontal, "c1")
        model.setHeaderData(2, Qt.Horizontal, "c2")
        model.setHeaderData(3, Qt.Horizontal, "c3")
        model.setHeaderData(4, Qt.Horizontal, "c4")
        model.setHeaderData(5, Qt.Horizontal, "c5")
        model.setHeaderData(6, Qt.Horizontal, "c6")

    # ------------------------
    def set_heading_by_name(self):
        """
        what it says
        """
        print_func_header( "set_heading_by_name" )

        msg        = "I have tried to get the qualified database names in here."
        print( msg )
        msg        = "Note that headers can span lines."
        print( msg )
        model      = self.model
        model.setHeaderData(0, Qt.Horizontal, "people_phone\n.id" )
        model.setHeaderData(1, Qt.Horizontal, "people\n.name")
        model.setHeaderData(2, Qt.Horizontal, "people\n.age")
        model.setHeaderData(3, Qt.Horizontal, "people_phone\n.phone_number")
        model.setHeaderData(4, Qt.Horizontal, "people_phone\n.zone")
        model.setHeaderData(5, Qt.Horizontal, "c5")
        model.setHeaderData(6, Qt.Horizontal, "c6")


    # ------------------------
    def select_all(self):
        """
        select with a sort
        """
        print_func_header( "select_all" )

        model        = self.model

        # this may cause problems elsewhere
        # column_index = model.fieldIndex( "age" )  # Get the column index for "name"
        # print( f"for sorting {column_index = }")
        # model.setSort( column_index , Qt.AscendingOrder)  # seems needs to be index no

        model.setFilter( "" )

        model.select()

    # ------------------------
    def select_some(self):
        """
        select base on some criteria, read the code for details
        """
        print_func_header( "select_some" )

        self.model.setFilter('age >  26 '   )
        self.model.select()

    # -----------------------
    def get_data_from_model(self):
        """
        What it says
            get data
            get rowcount
            can we get column count
            can we get column names
            note we also have a view
        """
        print_func_header( "select_some" )

        model           = self.model

        row_count       = model.rowCount()
        column_count    = model.columnCount()

        for ix_row in range( row_count ):
            for ix_col  in range( column_count ):   # should figure out a column count
                index     = model.index( ix_row,   ix_col   )
                data      = model.data( index )
                msg       = f"for {ix_row = } {ix_col = }  {data = }"
                print( msg )

    # ------------------------
    def do_selections(self):
        """
        not sure ... is dead?
        """
        print_func_header( "do_selections" )


    # ------------------------
    def get_selected_rows(self, index,   ):
        """ """
        print_func_header( "get_selected_rows" )

        # from PyQt5.QtWidgets import QTableView, QAbstractItemView
        # from PyQt5.QtCore import Qt

        view            = self.view
        # Assuming `view` is your QTableView
        selection_model = view.selectionModel()
        if selection_model:
            selected_indexes = selection_model.selectedRows()  # Get the selected rows

            # Iterate over the selected rows
            for index in selected_indexes:
                row = index.row()  # Get the row number
                print( f"Selected row: {row = }" )

    # ------------------------
    def delete_selected_row(self):
        """
        or even rows
        """
        print_func_header( "delete_selected_row" )

        #from PyQt5.QtSql import QSqlRelationalTableModel

        view            = self.view

        msg     = "for now just get first seleectd row if any "

        selection_model = view.selectionModel()
        if selection_model:
            selected_indexes = selection_model.selectedRows()  # Get the selected rows

            # Iterate over the selected rows
            for index in selected_indexes:
                row = index.row()  # Get the row number
                print( f"Selected row: {row = }" )
                break

        if row >= 0:
            # Assuming you already have a configured QSqlRelationalTableModel
            model = self.model

            # Deleting a single row
            #row_to_delete = 2  # Replace with the row number you want to delete
            if model.removeRow( row ):
                print(f"Row {row = } marked for deletion. But may still show in view")
            else:
                print("Failed to mark row for deletion.")

            print( "for things to continue to work you should probably update the db ")

        # # Committing the changes to the database
        # if model.submitAll():
        #     print("Changes committed to the database.")
        # else:
        #     print("Failed to commit changes to the database:", model.lastError().text())

        # # If you want to refresh the view after deletion
        # model.select()


    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection
        my_self                 = self
        parent_window           = self.parent( ).parent( ).parent().parent()
        a_db                    = parent_window.sample_db
        local_self_model        = self.model    # relational model
        local_self_view         = self.view     #  QTableView

        new_record              = self.model.record()  # just to see what we can see

        wat_inspector.go(
             msg            = "inspect for QSqlRelationalTableModel_2 new_record just for inspection ",
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

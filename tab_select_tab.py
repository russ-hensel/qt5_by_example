#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
select tab to open by running key word search
"""
# ---- tof
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #qt_search.main()
# --------------------


import inspect
import subprocess
import sys
import time
from datetime import datetime
from functools import partial
from subprocess import PIPE, STDOUT, Popen, run

import key_words
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
                             QDial,
                             QDoubleSpinBox,
                             QFontComboBox,
                             QGridLayout,
                             QGroupBox,
                             QHBoxLayout,
                             QLabel,
                             QLCDNumber,
                             QLineEdit,
                             QListWidget,
                             QListWidgetItem,
                             QMainWindow,
                             QMenu,
                             QMessageBox,
                             QProgressBar,
                             QPushButton,
                             QRadioButton,
                             QSizePolicy,
                             QSlider,
                             QSpinBox,
                             QTableView,
                             QTableWidget,
                             QTableWidgetItem,
                             QTabWidget,
                             QTextEdit,
                             QTimeEdit,
                             QVBoxLayout,
                             QWidget)

#import app_services
import global_vars
#import parameters
#import qt_search
import qt_sql_query
#import qt_widgets
import utils_for_tabs as uft
import wat_inspector
import parameters

# ---- imports neq qt

# ---- end imports

print_func_header   = uft.print_func_header

#  --------
class Search_Tab( QWidget ) :
    def __init__(self):
        """
        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py
        tab_misc_widgets.py
        """
        super().__init__()
        self._build_gui()
        self.mutate_ix   = 0

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of buttons
        """
        tab_page        = self
        layout          = QVBoxLayout( tab_page )

        widget = QLabel("Enter key words to search for a widget or use"
                        "\n    Box works, list works .... "
                        "\n    Capitilization... is ignored \n      ")

        layout.addWidget( widget  )

        # ---- a row
        row_layout      = QHBoxLayout(   )
        layout.addLayout( row_layout )

        widget          = QLabel("Key Words-> ")
        row_layout.addWidget( widget )

        widget               = QLineEdit()
        self.key_word_widget = widget
        #widget.setText( "")
            #\n does not give second line
        # widget.setDisabled( True )
        # widget.setDisabled( False )
        widget.setPlaceholderText( "Enter your key words here" )  # clear to see
        widget.setText( parameters.PARAMETERS.default_search )
        # widget.textChanged.connect( self.on_text_changed ) # user or pro grammatically
        # widget.textEdited.connect(self.on_text_edited)  # user only
        widget.returnPressed.connect( self.criteria_select )
        # widget.editingFinished.connect(self.on_editing_finished) # done leaves control
        # widget.setReadOnly(True)
        # widget.setReadOnly(False)
        row_layout.addWidget( widget )

        # ---- PB
        widget = QPushButton("Select")
        widget.clicked.connect( self.run_select    )
        row_layout.addWidget( widget,   )

        # ---- a row
        row_layout          = QHBoxLayout(   )
        layout.addLayout( row_layout )

        db                  = global_vars.TAB_DB
        model               = QSqlTableModel( self, db )
        self.list_model     = model

        model.setTable( "tabs" )

        model.setEditStrategy( QSqlTableModel.OnManualSubmit) # = never

        # COMMENT  out to default  Set column headers	model.setHorizontalHeaderLabels([...])

        view                 = QTableView()
        self.list_view       = view
        view.setSelectionBehavior( QTableView.SelectRows )
        view.setModel( model )

        row_layout.addWidget( view )

        view.clicked.connect( self.open_tab_select )

        """
        i have a QTableView how do i control the titles of the columns and their width ?
        """
        model.setHeaderData( 0, Qt.Horizontal, "Seq.")
        model.setHeaderData( 1, Qt.Horizontal, "Obj Name"  )
        view.setColumnWidth( 0, 50   )
        ix   = 1
        view.setColumnWidth( ix, 200  )

        ix   += 1
        model.setHeaderData( ix, Qt.Horizontal, "Widgets")
        view.setColumnWidth( ix, 700  )

        ix   += 1
        model.setHeaderData( ix, Qt.Horizontal, "Module")
        view.setColumnWidth( ix, 150  )

        ix   += 1
        model.setHeaderData( ix, Qt.Horizontal, "Class")
        view.setColumnWidth( ix, 150  )

        # suppress excess columns
        ix   += 1
        view.setColumnHidden( ix, True)

        ix   += 1
        view.setColumnHidden( ix, True)

        ix   += 1
        view.setColumnHidden( ix, True)
        #view.setModel( model )

        #model.setTable( "tabs" )  # suppresse above

        # Set specific column widths	table_view.setColumnWidth(column, width)
        # Auto-size columns	table_view.horizontalHeader().setSectionResizeMode()
        # Stretch columns to fit	QHeaderView.Stretch


        # self.widgets_list   = widgets   # for inspection later

        # for w in widgets:
        #     layout.addWidget(w())

        # # ---- new row, standard buttons
        # button_layout = QHBoxLayout(   )
        # layout.addLayout( button_layout,  )



        # # ---- PB breakpoint
        # widget = QPushButton("breakpoint\n")
        # widget.clicked.connect( self.breakpoint    )
        # button_layout.addWidget( widget,   )

    # ------------------------
    def run_select(self):
        """
        what it says
        """
        self.criteria_select()
        return

        widget = self.key_word_widget

        widget.clear()

        values    =  [ "oneish", "twoish", "threeish"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )
            index_to_select = 2
            widget.setCurrentRow(index_to_select)

    # -------------
    def criteria_select( self,     ):
        """
        do the select
        comment out to remove errors
        """
        model                           = self.list_model

        query                           = QSqlQuery( QSqlDatabase.database( "tab_db" )  ) # ) or use the global ??
        query_builder                   = qt_sql_query.QueryBuilder( query, print_it = False, )

        kw_table_name                   = "tabs_key_word"

        column_list                     = [ "id", "tab_title", "widgets", "module", "class"     ]

        a_key_word_processor            = key_words.KeyWords( kw_table_name, global_vars.TAB_DB )
        query_builder.table_name        = "tabs"
        query_builder.column_list       = column_list

        # ---- add criteria
        #criteria_dict                   = self.get_criteria()

        # ---- key words
        criteria_key_words              = self.key_word_widget.text()

        # criteria_key_words              = criteria_dict[ "key_words" ]
        criteria_key_words              = a_key_word_processor.string_to_key_words( criteria_key_words, caps_split = False )
        key_word_count                  = len(  criteria_key_words )

        criteria_key_words              = ", ".join( [ f'"{i_word}"' for i_word in criteria_key_words ] )
        criteria_key_words              = f'( {criteria_key_words} ) '    # ( "one", "two" )

        if key_word_count > 0:
            query_builder.group_by_c_list   = column_list
            query_builder.sql_inner_join    = " tabs_key_word  ON tabs.id = tabs_key_word.id "
            query_builder.sql_having        = f" count(*) = {key_word_count} "

            query_builder.add_to_where( f" key_word IN {criteria_key_words}" , [] )


        query_builder.prepare_and_bind()

        # msg      = f"{query_builder = }"
        # print( msg )

        self.query_exec_model( query,
                               model,
                               msg = "tab criteria_select" )

        msg      = (  query.executedQuery() )
        #rint( f"{msg  = }" )

    # -------------------------------------------
    def query_exec_model(self, query, model,  msg = None ):
        """
        exec queries with some error checking
        return ok   = True if now error

        is_ok  = AppGlobal.qsql_db_access.query_exec_model( query,
                                                  model,
                                                  msg = None )
        """

        # wat_inspector.go(
        #      msg            = "query_exec_model",
        #      a_locals       = locals(),
        #      a_globals      = globals(), )


        # msg      = f"Executing SQL query:  {query.executedQuery() = }"
        # print( msg )

        if query.exec():
            model.setQuery( query )
            if model.lastError().isValid():
                msg     = f"Query Error: {model.lastError().text() = }"
                print( msg )
                return False

        else:
            print( "Query Execution Error:", query.lastError().text())
            print( msg )
            print( query.executedQuery()   )
            return False

        return True

    # ------------------------
    def open_tab_select(self, index ):
        """
            CREATE TABLE tabs (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_file_name   TEXT,
                name            TEXT,
                tab_title       TEXT,
                module          TEXT,
                class           TEXT,
                widgets         TEXT,
                key_words       TEXT
        """

        row            = index.row()

        model          = self.list_model

        # Get the column index for the column name
        column      = model.fieldIndex( "tab_title" )
        model_index = model.index( row, column)
        tab_title   = model.data( model_index ).strip()  # do strip before add to db

        column      = model.fieldIndex( "module" )     # file name less .py
                    # /mnt/WIN_D/Russ/0000/python00/python3/_projects/stuffdb/tab_custom_widgets
                    # i want the stem so rsplit on /


        model_index       = model.index( row, column)
        module      = model.data( model_index ).strip()
        splits      = module.rsplit( "/", maxsplit = 1 )
        if len( splits )  == 2:
            module   = splits[1]
        else:
            module   = splits[0]

        column      = model.fieldIndex( "class" )
        model_index       = model.index( row, column)
        a_class     = model.data( model_index ).strip()

        ix          = global_vars.CONTROLLER.switch_to_tab_by_class_name( a_class )
        if ix >= 0:
            return

        #rint( f"open_tab_select: {row = },  {tab_title = }    {module = }   {a_class = }   ")
        pass

        global_vars.CONTROLLER.open_tab_select( module, a_class , tab_title  )





# ---- eof
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof


"""
KEY_WORDS:  Fitz chapter 23.  23. Querying SQL databases with Qt models
CLASS_NAME: Fitz_23_A_Tab
WIDGETS:    QTableView() QSqlTableModel
STATUS:     just started
TAB_TITLE:  Fitz SqlModel Chapt 23 A


looked at

"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_filterproxy_widget_mapper_controls.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_querymodel.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_querymodel_parameter.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_querymodel_search.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_relationalmodel.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_relationalmodel_delegate.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_tablemodel.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_tablemodel_filter.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_tablemodel_filter_clean.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_tablemodel_sort.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_tablemodel_sortname.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_tablemodel_titles.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/tableview_tablemodel_titlesname.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/widget_mapper.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/databases/widget_mapper_controls.py"


"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #qt_fitz_book.main()
# --------------------


import inspect
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from functools import partial
from subprocess import PIPE, STDOUT, Popen, run

import wat
from PyQt5 import QtGui
from PyQt5.QtCore import (QAbstractListModel,
                          QAbstractTableModel,
                          QDate,
                          QDateTime,
                          QModelIndex,
                          QSize,
                          Qt,
                          QTime,
                          QTimer)
from PyQt5.QtGui import QColor, QImage, QPalette, QTextCursor, QTextDocument, QIcon
# sql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
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
                             QListView,
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

import parameters
#import qt_widgets
import utils_for_tabs as uft
import wat_inspector
import global_vars
# ---- imports neq qt



# ---- end imports

print_func_header   = uft.print_func_header

basedir = os.path.dirname(__file__)

tick = QImage(os.path.join("tick.png"))



# Color scale, which is taken from colorbrewer2.org.
# Color range -5 to +5; 0 = light gray
COLORS = [
    "#053061",
    "#2166ac",
    "#4393c3",
    "#92c5de",
    "#d1e5f0",
    "#f7f7f7",
    "#fddbc7",
    "#f4a582",
    "#d6604d",
    "#b2182b",
    "#67001f",
]



#  --------
class Fitz_23_A_Tab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()
        self.help_file_name     =  "fitz_23_tab.txt"
        self._build_model()
        self._build_gui()
        self.mutate_ix   = 0
        self.ix_sort     = 0   # for sorting


    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of widgets
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        # ---- new row
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        widget    =  self.view
        row_layout.addWidget( widget,   )

        # ---- new row,
        row_layout = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        # ---- PB
        widget = QPushButton("select_all\n")
        widget.clicked.connect( self.select_all  )
        row_layout.addWidget( widget,   )

        # ----set_headers
        widget = QPushButton("set_headers\n")
        widget.clicked.connect( self.set_headers    )
        row_layout.addWidget( widget,   )

        # ----remove_columns
        widget = QPushButton("remove_columns\n")
        widget.clicked.connect( self.remove_columns    )
        row_layout.addWidget( widget,   )

        # # ---- new row,
        # row_layout = QHBoxLayout(   )
        # layout.addLayout( row_layout,  )

        # ---- "
        widget = QPushButton("select_with_filter\n" )
        widget.clicked.connect( self.select_with_filter   )
        row_layout.addWidget( widget,   )

        # # ---- new row,
        # row_layout = QHBoxLayout(   )
        # layout.addLayout( row_layout,  )

        # # ---- PB self.load
        # widget = QPushButton("load\n")
        # widget.clicked.connect( self.load    )
        # row_layout.addWidget( widget,   )

        # # ---- PB self.save
        # widget = QPushButton("save\n")
        # widget.clicked.connect( self.save    )
        # row_layout.addWidget( widget,   )

        # ---- self.inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        row_layout.addWidget( widget,   )

        # ---- PB self.breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        row_layout.addWidget( widget,   )

    # -------------------------------
    def _build_model(self,   ):
        """
        and the view
        """
        self.view               = QTableView()

        model                   = QSqlTableModel( self, global_vars.EX_DB   )
        self.model              = model
        self.people_model      = model
        model.setTable('people')


        self.view.setModel( self.model )

        # #query       = QSqlQuery( "SELECT Name,   FROM people ", db = global_vars.EX_DB )
        # self.model.setTable( "People" )



    print( "button code from other example may reacivate some ")

    def add(self):
        """
        Add an item to our todo list, getting the text from the QLineEdit .todoEdit
        and then clearing it.
        """
        print_func_header( "add" )

        text = self.todoEdit.text()
        # Remove whitespace from the ends of the string.
        text = text.strip()
        if text:  # Don't add empty strings.
            # Access the list via the model.
            self.model.todos.append((False, text))
            # Trigger refresh.
            self.model.layoutChanged.emit()  # <1>
            # Empty the input
            self.todoEdit.setText("")

    def delete(self):
        """ """
        print_func_header( "delete" )

        indexes = self.todoView.selectedIndexes()
        if indexes:
            # Indexes is a single-item list in single-select mode.
            index = indexes[0]
            # Remove the item and refresh.
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()

    def complete(self):
        """
        mark selected row as complete
        """
        print_func_header( "complete" )

        indexes = self.todoView.selectedIndexes()
        if indexes:
            index           = indexes[0]
            row             = index.row()
            msg             = f"completing {row = }"
            print( msg )
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            # .dataChanged takes top-left and bottom right, which are equal
            # for a single selection.
            self.model.dataChanged.emit(index, index)
            # Clear the selection (as it is no longer valid).
            self.todoView.clearSelection()
        else:
            msg    = "no selection to complete"
            print( msg )

    def set_headers( self ):
        """ """
        print_func_header( "select_with_filter" )

        model    = self.model      # would think in view but no

        model.setHeaderData(1, Qt.Horizontal, "SetCol1")
        model.setHeaderData(2, Qt.Horizontal, "SetCol2")

    def remove_columns( self ):
        """ """
        print_func_header( "remove_columns from what is visible " )
        msg                 = "here remove by column name"
        print( msg )
        model               = self.model
        columns_to_remove   = ['name', 'something']
        for c_name in columns_to_remove:
            idx = model.fieldIndex( c_name )
            model.removeColumns( idx, 1 )  # what is 1

    def select_with_filter( self ):
        """ """
        print_func_header( "select_with_filter" )
        a_name     = "a"
        filter_str = f"Name LIKE %{ a_name }%"
        self.model.setFilter( filter_str )


    def select_all( self ):
        """ """
        print_func_header( "select_all" )

        self.ix_sort    += 1
        if self.ix_sort > 1:
            self.ix_sort = 0

        if self.ix_sort == 0:
            sort_order   = Qt.DescendingOrder
        else:
            sort_order   = Qt.AscendingOrder

        msg      = f"{sort_order = }"
        print( msg )

        self.model.setFilter( "" )
        idx = self.model.fieldIndex( "age" )
        self.model.setSort( idx, sort_order )

        self.model.select()

        #self.model.layoutChanged.emit() # This triggers a refresh of the entirety of the view. I


    def save(self):
        print_func_header( "save" )

        with open("data.json", "w") as f:
            data = json.dump(self.model.todos, f)


    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_model         = self.model
        self_view     = self.view

        wat_inspector.go(
             msg            = "locals for model and view",
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
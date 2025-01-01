#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


self.help_file_name     =  "sql_query_model_tab.txt"

KEY_WORDS:      sql query model select update delete crud
CLASS_NAME:     SqlQueryModelTab
WIDGETS:        QSqlQueryModel  QTableWidget
STATUS:         works
TAB_TITLE:      SqlQueryModel



"""
# ---- tof
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_sql_widgets
    qt_sql_widgets.main()
# --------------------


import inspect
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from functools import partial
from random import randint
from subprocess import PIPE, STDOUT, Popen, run

import pyqtgraph as pg  # import PyQtGraph after PyQt5
import wat
from PyQt5 import QtGui
from PyQt5.QtCore import (QAbstractListModel,
                          QDate,
                          QDateTime,
                          QModelIndex,
                          QSize,
                          Qt,
                          QTime,
                          QTimer)
from PyQt5.QtGui import QColor, QImage, QPalette, QTextCursor, QTextDocument
# sql
# sql
from PyQt5.QtSql import (QSqlDatabase,
                         QSqlQuery,
                         QSqlQueryModel,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlRelationalTableModel,
                         QSqlTableModel)
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

import utils_for_tabs as uft
import wat_inspector

# ---- imports



# ---- end imports

print_func_header   = uft.print_func_header

basedir = os.path.dirname(__file__)

print( "salvaged but not functional is it a dup ??")

#  --------
class SqlQueryModelTab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()

        self.help_file_name     =  "sql_query_model_tab.txt"
        self._build_gui()
        self.mutate_ix          = 0

        # self.timer = QTimer()
        # self.timer.setInterval(50)
        # self.timer.timeout.connect(self.update_plot_data)
        # self.timer.start()

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of widgets
        """
        tab_page            = self
        layout              = QVBoxLayout( tab_page )

        table_widget        = QTableWidget(4, 5)  # row, column ??third arg parent
        self.table_widget   = table_widget
        layout.addWidget( table_widget )

        # ---- new row
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        # # ---- PB "start\n"
        # widget = QPushButton("start\n")
        # widget.clicked.connect( self.start    )
        # row_layout.addWidget( widget,   )

        # # ---- PB breakpoint
        # widget = QPushButton("stop\n")
        # widget.clicked.connect( self.stop    )
        # row_layout.addWidget( widget,   )


        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        row_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        row_layout.addWidget( widget,   )


    def run_it( self, ):
        """
        from chat
        """
        #def loop_through_rows():
        """Loop through rows using QSqlQueryModel."""

        print( "need !! to set in db connect ")
        model = QSqlQueryModel( )

        # Set the query to fetch data from the 'people' table
        model.setQuery("SELECT * FROM people")

        # or
        model.setQuery("SELECT name, age FROM people")

        if model.lastError().isValid():
            print("Error: ", model.lastError().text())
            return

        for row in range(model.rowCount()):
            # Extract data from each column in the current row
            row_data = []
            for col in range(model.columnCount()):
                row_data.append( model.data(model.index(row, col)))

            print(f"Row {row + 1}: {row_data}")

    # ------------------------
    # def start(self):
    #     """ """
    #     print_func_header( "start" )
    #     return
    #     self.timer.start()

    # # ------------------------
    # def stop(self):
    #     """ """
    #     print_func_header( "stop" )
    #     return

    #     self.timer.stop()

    # # ------------------------
    # def update_plot_data(self):

    #     pass
    #     return

    #     self.x = self.x[1:]  # Remove the first y element.
    #     self.x.append(
    #         self.x[-1] + 1
    #     )  # Add a new value 1 higher than the last.

    #     self.y = self.y[1:]  # Remove the first
    #     self.y.append(randint(0, 100))  # Add a new random value.

    #     self.data_line.setData(self.x, self.y)  # Update the data.

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # self_graph_widget   = self.graphWidget
        # self_timer          = self.timer
        wat_inspector.go(
             msg            = "sql query model tab",
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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---- tof
"""
could use a rename to chapter of the book


KEY_WORDS:      some stuff from the m fitz book a graph of static data chapter 35
CLASS_NAME:     Fitz_6_Tab
WIDGETS:        PlotWidget PyQtGraph pg.PlotWidget pg.mkPen  Grid Range
STATUS:         works
TAB_TITLE:      Fitz_Chapter 35 A_Tab



 "/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_1.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_1b.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_2.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_3.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_4.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_5.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/todo_6.py"

largely the last


"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #main.main()
# -------------------


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

#import parameters
#import qt_widgets
import utils_for_tabs as uft
import wat_inspector

# ---- imports neq qt



# ---- end imports

print_func_header   = uft.print_func_header

basedir = os.path.dirname(__file__)


#  --------
class Fitz_6_Tab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()
        self.help_file_name     =  "fitz_6_tab.txt"
        self._build_gui()
        self.mutate_ix   = 0

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of widgets
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        #self.graphWidget = pg.PlotWidget()
        widget              = pg.PlotWidget()
        self.graphWidget    = widget
        layout.addWidget( self.graphWidget )

        self.graphWidget.setBackground("w")

        pen = pg.mkPen(color=(255, 0, 0))

        # Add Background color to white
        self.graphWidget.setBackground("w")  # w = white

        self.graphWidget.setTitle(
            "Your Title Here", color="b", size="30pt"
        )
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hour (H)", **styles)
        # Add legend
        self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)
        # Set Range
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)

        # ---- new row
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        # ---- PB clear
        widget = QPushButton("clear\n")
        widget.clicked.connect( self.graphWidget.clear     )
        row_layout.addWidget( widget,   )

        # ---- PB plot
        widget = QPushButton("plot\n")
        widget.clicked.connect( self.plot    )
        row_layout.addWidget( widget,   )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        row_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        row_layout.addWidget( widget,   )


    def plot(self,  ):
        """ """
        print_func_header( "plot" )

        hour            = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature_1   = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        temperature_2   = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]

        self.plot_data(hour, temperature_1, "Sensor1", "r")
        self.plot_data(hour, temperature_2, "Sensor2", "b")


    def plot_data(self, x, y, plotname, color):
        """ """
        print_func_header( "plot_data" )

        pen = pg.mkPen(color=color)
        self.graphWidget.plot(
            x,
            y,
            name=plotname,
            pen=pen,
            symbol="+",
            symbolSize=30,
            symbolBrush=(color),
        )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_graph_widget   = self.graphWidget

        wat_inspector.go(
             msg            = "locals are graph and timer",
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

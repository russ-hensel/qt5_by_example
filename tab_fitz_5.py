#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----tof
"""
KEY_WORDS:      some stuff from the m fitz book a dynamic graph
CLASS_NAME:     Fitz_5_Tab
WIDGETS:        QTimer pg.PlotWidget pg.mkPen
STATUS:         works ??
TAB_TITLE:      Fitz Dynamic Plot



"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_fitz_book
    qt_fitz_book.main()
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
class Fitz_5_Tab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()
        self._build_gui()

        self.help_file_name     =  "fitz_5_tab.txt"
        self.mutate_ix   = 0

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of widgets
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        widget              = pg.PlotWidget()
        self.graphWidget    = widget
        layout.addWidget( self.graphWidget )

        self.x = list(range(100))  # 100 time points
        self.y = [
            randint(0, 100) for _ in range(100)
        ]  # 100 data points

        self.graphWidget.setBackground("w")

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(
            self.x, self.y, pen=pen
        )  # <1>


        # ---- new row
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        # ---- PB "start\n"
        widget = QPushButton("start\n")
        widget.clicked.connect( self.start    )
        row_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("stop\n")
        widget.clicked.connect( self.stop    )
        row_layout.addWidget( widget,   )


        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        row_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        row_layout.addWidget( widget,   )

    # ------------------------
    def start(self):
        """ """
        print_func_header( "start" )

        self.timer.start()

    # ------------------------
    def stop(self):
        """ """
        print_func_header( "stop" )

        self.timer.stop()


    # ------------------------
    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(
            self.x[-1] + 1
        )  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0, 100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.



    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_graph_widget   = self.graphWidget
        self_timer          = self.timer
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
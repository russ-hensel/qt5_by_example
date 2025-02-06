#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KEY_WORDS:      some stuff from the m fitz book .....
CLASS_NAME:     Fitz_7_Tab
WIDGETS:        QTableView QStyledItemDelegate QAbstractTableModel Qt.ToolTipRole QImage
STATUS:         works
TAB_TITLE:      Fitz7 Book

        self.help_file_name     =  "fitz_7_tab.txt"

 /mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/delegate_1.py

where in the book
tab_fitz_7

"""
# ---- tof
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #qt_fitz_book.main()
# --------------------


import glob
import inspect
import json
import math
import os
import subprocess
import sys
import time
from collections import namedtuple
from datetime import datetime
from functools import partial
from random import randint
from subprocess import PIPE, STDOUT, Popen, run

import pyqtgraph as pg  # import PyQtGraph after PyQt5
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
from PyQt5.QtGui import QColor, QImage, QPalette, QTextCursor, QTextDocument
# sql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
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
                             QStyledItemDelegate,
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

# Create a custom namedtuple class to hold our data.
preview = namedtuple("preview", "id title image")

NUMBER_OF_COLUMNS = 4
CELL_PADDING = 20  # all sides


class PreviewDelegate( QStyledItemDelegate ):
    def paint(self, painter, option, index):
        # data is our preview object
        data = index.model().data(index, Qt.DisplayRole)
        if data is None:
            return

        width = option.rect.width() - CELL_PADDING * 2
        height = option.rect.height() - CELL_PADDING * 2

        # option.rect holds the area we are painting on the widget (our table cell)
        # scale our pixmap to fit
        scaled = data.image.scaled(
            width,
            height,
            aspectRatioMode=Qt.KeepAspectRatio,
        )
        # Position in the middle of the area.
        x = CELL_PADDING + (width - scaled.width()) / 2
        y = CELL_PADDING + (height - scaled.height()) / 2

        painter.drawImage(
            int( option.rect.x() + x ) , int( option.rect.y() + y ), scaled
        )

    def sizeHint(self, option, index):
        # All items the same size.
        return QSize(300, 200)


class PreviewModel(QAbstractTableModel):
    def __init__(self, todos=None):
        super().__init__()
        # .data holds our data for display, as a list of Preview objects.
        self.previews = []

    def data(self, index, role):
        try:
            data = self.previews[index.row() * 4 + index.column()]
        except IndexError:
            # Incomplete last row.
            return

        if role == Qt.DisplayRole:
            return data  # Pass the data to our delegate to draw.

        if role == Qt.ToolTipRole:
            return data.title

    def columnCount(self, index):
        return NUMBER_OF_COLUMNS

    def rowCount(self, index):
        n_items = len(self.previews)
        return math.ceil(n_items / NUMBER_OF_COLUMNS)

#  --------
class Fitz_7_Tab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()
        self.help_file_name     =  "fitz_7_tab.txt"
        self._build_gui()
        self.mutate_ix          = 0

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout      #self.graphWidget = pg.PlotWidget()
        widget              = pg.PlotWidget()
        self.graphWidget    = widget
        layout.addWidget( self.graphWidget )

        self.graphWidget.setBackground("w")

        pen = pg.mkPen(color=(255, 0, 0))


            h_box for or each row of widgets
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        self.view = QTableView()
        self.view.horizontalHeader().hide()
        self.view.verticalHeader().hide()
        self.view.setGridStyle(Qt.NoPen)

        delegate = PreviewDelegate()
        self.view.setItemDelegate(delegate)
        self.model = PreviewModel()
        self.view.setModel(self.model)

        # self.setCentralWidget(self.view)
        layout.addWidget( self.view )

        # Add a bunch of images.
        image_files = glob.glob("*.jpg")
        for n, fn in enumerate(image_files):
            image   = QImage(fn)
            item    = preview(n, fn, image)
            self.model.previews.append(item)
        self.model.layoutChanged.emit()

        self.view.resizeRowsToContents()
        self.view.resizeColumnsToContents()

        # ---- new row
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        # ---- PB plot
        widget = QPushButton("clear\n")
        #widget.clicked.connect( self.graphWidget.clear     )
        row_layout.addWidget( widget,   )

        # ---- PB plot
        widget = QPushButton("plot\n")
        #widget.clicked.connect( self.plot    )
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

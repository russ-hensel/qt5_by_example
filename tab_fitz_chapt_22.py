#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof


"""
KEY_WORDS:  Fitz chapter 22. A Table Model and View  formating  ..zz  zzz
CLASS_NAME: Fitz_22_Tab
WIDGETS:    QAbstractTableModel  QTableView DecorationRole    BackgroundRole QIcon TextAlignmentRole
STATUS:     just started
TAB_TITLE:  Fitz TableModel



looked at
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_demo.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_dictionary.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_format_1.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_format_2.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_format_3.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_format_4.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_format_5.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_format_6.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_format_7.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_format_8.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_format_9.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_numpy.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/model-views/tableview_pandas.py"

largely the last


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

import parameters
#import qt_widgets
import utils_for_tabs as uft
import wat_inspector

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







#basedir = os.path.dirname(__file__)


class TableModel( QAbstractTableModel ):
    def __init__(self, data):
        super().__init__()
        self._data = data

        # Row colors empty by default.
        self._row_colors = {}

    def data(self, index, role):
        """
        returns some sort of data based on index.
        can do formattion here and much more

        """
        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, bool):
                if value:
                    return QIcon(
                        os.path.join(basedir, "tick.png")
                    )

                return QIcon(os.path.join(basedir, "cross.png"))

            if isinstance(value, datetime):
                 return QtGui.QIcon("calendar.png")

        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, int) or isinstance(value, float):
                # Align right, vertical middle.
                return Qt.AlignVCenter | Qt.AlignRight
                # or for ex Qt.AlignHCenter   Qt.AlignBottom + Qt.AlignRight.

        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")

            return value

        if role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]
            if (isinstance(value, int) or isinstance(value, float)) and value < 0:
                return QtGui.QColor("red")


        if role == Qt.BackgroundRole:
            color = self._row_colors.get(
                index.row()
            )  # returns None if not in.
            if color:
                return QColor(color)

        # is reachable print( "alternate background unreachabel form tableview_format_5")
        if role == Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                value = int(value)  # Convert to integer for indexing.

                # Limit to range -5 ... +5, then convert to 0..10
                value = max(-5, value)  # values < -5 become -5
                value = min(5, value)  # valaues > +5 become +5
                value = value + 5  # -5 becomes 0, +5 becomes + 10

                return QColor(COLORS[value])




    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def set_row_color(self, row, color):
        self._row_colors[row] = color


#  --------
class Fitz_22_Tab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()
        self.help_file_name     =  "fitz_22_tab.txt"
        self._build_model()
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

        # ---- new row
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        widget    =  self.view
        row_layout.addWidget( widget,   )

        # ---- new row,
        row_layout = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        # # ---- PB
        # widget = QPushButton("delete\n")
        # widget.clicked.connect( self.delete   )
        # row_layout.addWidget( widget,   )

        # # ---- PB
        # widget = QPushButton("complete\n")
        # widget.clicked.connect( self.complete    )
        # row_layout.addWidget( widget,   )

        # # ---- new row,
        # row_layout = QHBoxLayout(   )
        # layout.addLayout( row_layout,  )

        # # ---- Line Edit
        # widget = QLineEdit("new items here")
        # self.todoEdit  = widget
        # #widget.clicked.connect( self.inspect    )
        # row_layout.addWidget( widget,   )

        # # # ---- new row,
        # # button_layout = QHBoxLayout(   )
        # # layout.addLayout( button_layout,  )

        # # ---- "add\n_todo"
        # widget = QPushButton("add\n_todo")
        # widget.clicked.connect( self.add    )
        # row_layout.addWidget( widget,   )

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
        self.view      = QTableView()

        data = [
            [True, 9, 2],
            [1, 0, -1],
            [3, 5, False],
            [3, 3, 2],
            [datetime(2019, 5, 4), 8, 9],
        ]

        data            = 5 * data
        self.data       = data # just for debug
        self.model      = TableModel(data)
        self.model.set_row_color(1, "#b2182b")
        self.model.set_row_color(3, "#92c5de")

        self.view .setModel(self.model)



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

    # tag::loadsave[]
    def load(self):
        print_func_header( "load" )

        try:
            with open("data.json", "r") as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

        self.model.layoutChanged.emit() # This triggers a refresh of the entirety of the view. I


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
        self_todo_view     = self.view
        self_data          = self.data
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

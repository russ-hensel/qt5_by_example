#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ---- tof

"""
KEY_WORDS:      some stuff from the m fitz book mouse events

CLASS_NAME:     Fitz_3_Tab
WIDGETS:        QMenu Qt.LeftButton
STATUS:         works

TAB_TITLE:      MouseEvents



"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/basic/events_1.py",
.../basic/events_1b.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/basic/events_2.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/basic/events_3.py",
"/mnt/WIN_D/Russ/0000/python00/python3/_examples/python_book_code/book_pyqt5_src/basic/events_4.py"
"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import qt_fitz_book
    qt_fitz_book.main()
# --------------------


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

import parameters
# import qt_widgets
import utils_for_tabs as uft
import wat_inspector

# ---- end imports

print_func_header   = uft.print_func_header

#  --------
class Fitz_3_Tab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()
        self.help_file_name     =   "fitz_3_tab.txt"
        self._build_gui()
        self.mutate_ix   = 0

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box for or each row of buttons
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        # ----
        row_layout    = QHBoxLayout(   )
        layout.addLayout( row_layout,  )

        widget          =  QLabel("Mouse around; Mouse Events ---> ")
        row_layout.addWidget( widget )

        widget         = QLabel( "mouse events come here 1 " )
        self.label_1   = widget
        row_layout.addWidget( widget )

        widget         = QLabel( "mouse events come here 2" )
        self.label_2   = widget
        row_layout.addWidget( widget )

        # mouse tracking on the whole tab page
        self.setMouseTracking(True)

        # ---- new row, standard buttons
        button_layout = QHBoxLayout(   )
        layout.addLayout( button_layout,  )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )


    def contextMenuEvent( self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec_(e.globalPos())


    def mouseMoveEvent(self, e):

        self.label_1.setText("mouseMoveEvent")
        # deeper analysis in lable_2
        pos         = e.pos()
        global_pos  = e.globalPos()
        self.label_2.setText( "mouseMoveEvent: %s %s " % ( pos, global_pos ))


    def mousePressEvent(self, e):
        """ """
        self.label_1.setText("mousePressEvent")
        # deeper analysis in lable_2
        if e.button() == Qt.LeftButton:
            # handle the left-button press in here
            self.label_2.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            # handle the middle-button press in here.
            self.label_2.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            # handle the right-button press in here.
            self.label_2.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        """ """
        self.label_1.setText("mouseReleaseEvent")
        # deeper analysis in lable_2

        if e.button() == Qt.LeftButton:
            self.label_2.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label_2.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label_2.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        """ """
        self.label_1.setText("mouseDoubleClickEvent")
        # deeper analysis in lable_2
        if e.button() == Qt.LeftButton:
            self.label_2.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label_2.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label_2.setText("mouseDoubleClickEvent RIGHT")

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_widgets_list   = self.widgets_list
        wat_inspector.go(
             msg            = "see self_widgets_list",
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

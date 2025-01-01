#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ---- tof
"""
KEY_WORDS:      dialog boxes of various forms modal browse for file or directory path
CLASS_NAME:     DialogEtcTab
WIDGETS:        QMessageBox  QFileDialog
STATUS:         works
TAB_TITLE:      Dialog Boxes
TAB_HELP:       use  self.help_file_name     =  "dialog_boxes_tab.txt"


 /mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example/docs/date_edit_widget_tab.txt

/mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example/docs/date_edit_widget_tab.txtper_tab.txt



"""

# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    # qt_widgets.main( )
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

from PyQt5.QtWidgets import (QAction,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDateEdit,
                             QDateTimeEdit,
                             QDialog,
                             QFileDialog,
                             QGridLayout,
                             QGroupBox,
                             QHBoxLayout,
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

import utils_for_tabs as uft
import wat_inspector

# ---- imports neq qt



# ---- end imports


INDENT          = uft.INDENT
INDENT          = uft.BEGIN_MARK_1
INDENT          = uft.BEGIN_MARK_2
#INDENT          = qt_sql_widgets.

print_func_header =  uft.print_func_header


#  --------
class DialogEtcTab( QWidget ):
    def __init__(self):
        """
        q_dialog_etc_tab.py
        """
        super().__init__()
        self.help_file_name     =  "dialog_boxes_tab.txt"
        self._build_gui()
        self.mutate_ix          = 0

    # -------------------------------
    def _build_gui(self,   ):
        """
        layouts
            a vbox for main layout
            h_box f or each row
        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        # ---- New Row
        row_layout          = QHBoxLayout(   )
        layout.addLayout( row_layout )

        # ---- QPushButton("Open Messagebox")
        widget          = QPushButton("show_message\n_box")
        widget.setCheckable(True)
        widget.clicked.connect( lambda: self.show_message_box( ) )
        row_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("browse_for\nfile")
        widget.clicked.connect( self.browse_for_file    )
        row_layout.addWidget( widget,   )

        # ---- PB inspect
        widget = QPushButton("browse_for\ndirectory")
        widget.clicked.connect( self.browse_for_directory    )
        row_layout.addWidget( widget,   )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        row_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        row_layout.addWidget( widget,   )

    # ------------------------------------
    def show_message_box( self ):
        """
        what is says
        """
        print_func_header( "show_message_box" )

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Make a Choice")
        msg_box.setText("Please choose one:")

        choice_a = msg_box.addButton("Choice A", QMessageBox.ActionRole)
        choice_b = msg_box.addButton("Choice B", QMessageBox.ActionRole)

        # Set the dialog to be modal (blocks interaction with other windows)
        msg_box.setModal(True)

        msg_box.exec_()

        if msg_box.clickedButton() == choice_a:
            print("Choice A selected")
        elif msg_box.clickedButton() == choice_b:
            print("Choice B selected")

        QMessageBox.information( self, "a title",
                                "additional message")

    # ------------------------
    def browse_for_file(self):
        """
        what it says
        """
        print_func_header( "browse_for_file" )
        initial_dir     = "/mnt/WIN_D/Russ/0000/python00/python3/_projects/stuffdb/__pycache__"

        file_dialog     = QFileDialog(self, "Select Files")

        file_dialog.setFileMode(QFileDialog.ExistingFiles) #multiple file selection
        file_dialog.setFileMode(QFileDialog.ExistingFile)  # Single file selection
        #file_dialog.setNameFilter("All Files (*);;Python Files (*.py)")  # File filters
        file_dialog.setNameFilter("All Files (*);;Text Files (*.txt)")
        file_dialog.setDirectory( initial_dir )
        # file_dialog.setWindowTitle(  title      )
        # #file_dialog.setNameFilter(   file_types  )

        if file_dialog.exec_():
            #files = file_dialog.selectedFiles()   # multiple files
            files = file_dialog.getOpenFileName()             # single file
            print("browse Selected files:")
            for file in files:
                print(file)
                row_data     = [ file, "1", "2"]

        # ---- also work this in
        # Configure the QFileDialog for a single file
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            caption="Select a File",            # Window title
            directory=".",                      # Initial directory
            filter="All Files (*);;Python Files (*.py)"  # File type filters
        )

        # Print the selected file path
        if file_path:
            print(f"Selected file: {file_path}")
        else:
            print("No file selected.")

    # ------------------------
    def browse_for_directory(self):
        """
        what it says
        """
        print_func_header( "browse_for_directory" )

        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            print (f"Selected Directory: {directory}")
        else:
            print("No directory selected")

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        wat_inspector.go(
             msg            = "DialogEtcTab",
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
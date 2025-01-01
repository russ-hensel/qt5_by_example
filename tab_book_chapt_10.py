#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ---- tof


"""
KEY_WORDS:  Some book chapter 10 dock widgets zz
CLASS_NAME: Dock_10_Tab
WIDGETS:    QDockWidget
STATUS:     first draft -- runs but needs work
TAB_TITLE:  Dock Widget



looked at



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


#import PyQt5.QtCore

from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QLabel


from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("LeftDockWidgetArea Example")

#         # Central widget
#         central_label = QLabel("Central Widget")
#         self.setCentralWidget(central_label)

#         # Create a dock widget
#         dock = QDockWidget("Dockable", self)
#         dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

#         dock_label = QLabel("This is a dockable widget.")
#         dock.setWidget(dock_label)

#         # Add the dock to the left dock widget area
#         self.addDockWidget(Qt.LeftDockWidgetArea, dock)

# # Run the application
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()

from PyQt5.QtCore import Qt, QTimer, QObject, pyqtSignal, QRect
from PyQt5 import QtCore
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



from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QLabel

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



#basedir = os.path.dirname(__file__)



#  --------
class Dock_10_Tab( QWidget ) :
    def __init__(self):
        """

        """
        super().__init__()
        self.help_file_name     =  "dock_10_tab.txt"
        #self._build_model()

        # Track the number of opened windows
        self.window_counter     = 0
        self.open_windows       = []

        self._build_gui()

        self.mutate_ix          = 0
        self.ix_sort            = 0   # for sorting

        x = """
        suppose i have code for a pushbutton that i would
        like to open a second ( or third... ) mainwindow.
        what would the code be, and how do i close the new
        window so that it is also deleted/destroyed? could you
        give me the full code?
        """

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

        # # ---- new row,
        # row_layout = QHBoxLayout(   )
        # layout.addLayout( row_layout,  )

        # ---- PB
        widget = QLabel( "for dock-able objects you need a new main window --------------------> " )

        row_layout.addWidget( widget,   )

        # ---- PB
        widget = QPushButton("open_new_window\n")
        widget.clicked.connect( self.open_new_window  )
        row_layout.addWidget( widget,   )

        # # self.dockWidget.setGeometry( QtCore.QRect(40, 10, 111, 191) )
        # #dockWidget.setGeometry( QRect(40, 10, 111, 191) )


        # dock_widget.setFloating( False )
        # dock_widget.setFeatures( QDockWidget.AllDockWidgetFeatures )

        # #self.dockWidget.setAllowedAreas( QtCore.Qt.LeftDockWidgetArea )

        # dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        # #self.dockWidget.setObjectName( "dockWidget" )




        """
        could you give me a short example of an application using
        QDockWidget in the widger place a few QPushbuttons, some
        QlineEdits and some QCheckBoxes.  Include a lot of features
        turned on for the qdockwidget
        """




        # ---- new row,
        row_layout = QHBoxLayout(   )
        layout.addLayout( row_layout,  )



        # # ----set_headers
        # widget = QPushButton("set_headers\n")
        # widget.clicked.connect( self.set_headers    )
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


    def open_new_window(self):
        """
        Opens a new secondary window
        """
        self.window_counter += 1
        new_window = SecondaryWindow(self.window_counter)
        new_window.show()

        # Keep track of open windows
        self.open_windows.append(new_window)

        # Connect to the destroyed signal to remove references
        new_window.destroyed.connect(lambda: self.remove_window_reference(new_window))

    def remove_window_reference(self, window):
        """Remove reference to the window when it is closed."""
        if window in self.open_windows:
            self.open_windows.remove(window)
            print("Window reference removed!")


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



    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_window_counter     = self.window_counter
        self_open_windows       = self.open_windows

        wat_inspector.go(
             msg            = "some locals for tab",
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


class SecondaryWindow(QMainWindow):
    def __init__(self, window_number):
        super().__init__()
        self.setWindowTitle(f"Secondary Window {window_number}")
        self.resize(300, 200)


        # Log the window creation
        print(f"Secondary Window {window_number} created!")

        self.setWindowTitle("QDockWidget Example")
        self.resize(800, 600)

        # Central widget
        central_label = QLabel("This is the central widget.")
        central_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(central_label)

        dock_widget     = self.build_dock()
        # Add the dock widget to the main window
        self.addDockWidget( Qt.LeftDockWidgetArea, dock_widget)
        # Add the dock widget to the main window
        #self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

        dock_widget     = self.build_dock()
        # Add the dock widget to the main window
        self.addDockWidget( Qt.RightDockWidgetArea, dock_widget)


    def build_dock( self ):
        """
        """
        # Create a dock widget
        dock_widget         = QDockWidget("Dockable Panel", self)
        self.dock_widget    = dock_widget
        dock_widget.setAllowedAreas( Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea )

        # Enable floating and close features
        dock_widget.setFeatures(
            QDockWidget.DockWidgetMovable |
            QDockWidget.DockWidgetFloatable |
            QDockWidget.DockWidgetClosable
        )


        # Create the dock widget content
        dock_content    = QWidget()
        dock_layout     = QVBoxLayout()

        # Add widgets to the dock
        dock_layout.addWidget(QPushButton("Button 1"))
        dock_layout.addWidget(QPushButton("Button 2"))
        dock_layout.addWidget(QLineEdit("Enter text here"))
        dock_layout.addWidget(QCheckBox("Check Option 1"))
        dock_layout.addWidget(QCheckBox("Check Option 2"))

        # # ---- new row,
        # row_layout = QHBoxLayout(   )
        # layout.addLayout( row_layout,  )

        # ---- PB
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect )
        dock_layout.addWidget( widget,   )

        dock_content.setLayout(dock_layout)
        dock_widget.setWidget(dock_content)

        return dock_widget


    def closeEvent(self, event):
        print(f"Secondary Window destroyed!")
        super().closeEvent(event)

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        self_dock_widget         = self.dock_widget

        wat_inspector.go(
             msg            = "locals for secondary window",
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

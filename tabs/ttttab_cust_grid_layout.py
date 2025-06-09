#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---- tof
"""

tab_groupbox.py

self.help_file_name     =  "group_widget_tab.txt"

KEY_WORDS:      grid layout table new   custom perhaps with cqlineedit
CLASS_NAME:     CGridLayoutTab
WIDGETS:        CGridLayout
STATUS:         new end of feb
TAB_TITLE:      CustGridLayoutTab

"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
    #qt_widgets.main( )
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

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel

from PyQt5.QtWidgets import (QAction,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDateEdit,
                             QDateTimeEdit,
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
import tab_base
import utils_for_tabs as uft
import wat_inspector
import tab_base
import gui_qt_ext


# ---- end imports


# # these must be defined at import time in uft
# INDENT          = uft.INDENT
# INDENT          = uft.BEGIN_MARK_1
# INDENT          = uft.BEGIN_MARK_2
# #INDENT          = qt_sql_widgets.

# print_func_header =  uft.print_func_header

# ----------------------------
class CGridLayoutTab( tab_base.TabBase  ) :
    def __init__(self):
        """
        the usual
            grid_layout_tab.GridLayoutTab
        """
        super().__init__()

        self.help_file_name     =  "grid_layout_tab.txt"

        self.mutate_dict[0]    = self.mutate_0
        self.mutate_dict[1]    = self.mutate_1
        self.mutate_dict[2]    = self.mutate_2
        # self.mutate_dict[3]    = self.mutate_3
        # self.mutate_dict[4]    = self.mutate_4

        self._build_gui()


    def _build_gui_widgets(self, main_layout  ):
        """
        the usual, build the gui with the widgets of interest
        and the buttons for examples
        """
        temp_widget         = QWidget( )  # we will distrooy and rebuild as desired
        self.temp_widget    = temp_widget
        main_layout.addWidget( temp_widget)

        self.main_layout    = main_layout   # or doen in parent

        mutating_layout              = gui_qt_ext.CQGridLayout( col_max = 8  )
        self.mutating_layout         = mutating_layout
        temp_widget.setLayout( mutating_layout )

        button_layout        = QHBoxLayout(   )

    # # ----------------------------
    # def _build_gui(self,   ):
    #     """
    #     the usual
    #     """

    #     tab_page      = self

    #     layout        = QGridLayout( tab_page )

        ix_row        = 1
        ix_col        = 0

        row_span      = 1 # default is 1
        col_span      = 1 # default is 1

        # rowSpan: (Optional) The number of rows the widget should span. Defaults to 1.
        # columnSpan: (Optional) The number of columns the widget should span. Defaults to 1.

        for ix_row  in range( 0, 6 ):
            for ix_col in range( 0,4 ):
                #widget = QPushButton(f"r{ix_row} c{ix_col}")
                widget = QPushButton(f"{0}")
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                mutating_layout.addWidget( widget,  columnspan   = 1,  rowspan = row_span )
                widget.setText(  mutating_layout.get_add_parm_str() )
        # for ix_row  in range( 0, 6, 2 ):
        #     row_span      = 2   # using None seems ok to get default
        #     col_span      = 1   # using None seems ok to get default

        #     for ix_col in range( 4, 6 ):

        #         widget = QPushButton(f"r{ix_row} c{ix_col}")
        #         widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #         layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # ix_row   += 2
        # button_layout  = QHBoxLayout()
        # layout.addLayout( button_layout, ix_row, 0, row_span, 6 )


        ix_row   += 2
        button_layout  = QHBoxLayout()
        mutating_layout.addLayout( button_layout, ix_row, 0, row_span, 6 )

        widget = QPushButton("mutate\n")
        #self.button_ex_1         = widget
        widget.clicked.connect( lambda: self.mutate( ) )
        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )


    # ------------------------------------
    def mutate_0( self ):
        """
        read it -- mutate the widgets
        """
        self.append_function_msg( "mutate_0" )

        # self.temp_widget    = temp_widget
        # main_layout.addWidget( temp_widget)
        # self.main_layout    = main_layout   # or

        msg    = "lets try a remove and rebuild cannot get size right will return so gui not damaged"
        self.append_msg( msg, )
        return

        # self.main_layout.removeWidget( self.temp_widget )

        # self.temp_widget.setParent(None)  # Completely detach from parent
        # self.temp_widget.deleteLater()  # Schedules deletion for when it's safe

        # # done delete rebuild
        # temp_widget         = QWidget( )
        # self.temp_widget    = temp_widget
        # # self.main_layout.insertWidget(1, temp_widget, stretch = 1 )

        # layout              = gui_qt_ext.CQGridLayout( col_max = 6  )
        # temp_widget.setLayout( layout )
        # button_layout        = QHBoxLayout(   )

        # row_span = 3
        # for ix_row  in range( 0, 6 ):
        #     for ix_col in range( 0,4 ):
        #         widget = QPushButton(f"r{ix_row} c{ix_col}")
        #         widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #         layout.addWidget( widget,  columnspan   = 1,  rowspan = row_span )
        #         widget.setText(  mutating_layout.get_add_parm_str() )
        # #grid_layout.setColumnStretch(column_index, stretch_factor)


        # # moved down to see if it would behave better
        # self.main_layout.insertWidget(1, temp_widget, stretch = 1 )

        # self.main_layout.setRowStretch(0, 0 )
        # self.main_layout.setRowStretch(1, 1 )
        # self.main_layout.setRowStretch(2, 1 )


        # self.append_msg( tab_base.DONE_MSG )

    # ------------------------------------
    def mutate_1( self ):
        """
        read it -- mutate the widgets
            clear everything even the buttons


        """
        self.append_function_msg( "mutate_1" )

        msg    = "first clear  "
        self.append_msg( msg, )

        mutating_layout = self.mutating_layout


        self.clear_grid_layout( self.mutating_layout )

        ix_row        = 1
        ix_col        = 0

        row_span      = 1 # default is 1
        col_span      = 1 # default is 1

        # rowSpan: (Optional) The number of rows the widget should span. Defaults to 1.
        # columnSpan: (Optional) The number of columns the widget should span. Defaults to 1.

        for ix_row  in range( 0, 6 ):
            for ix_col in range( 0,4 ):
                widget = QPushButton(f"r{ix_row} c{ix_col}")
                widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                mutating_layout.addWidget( widget,  columnspan   = 1,  rowspan = row_span )
                widget.setText(  mutating_layout.get_add_parm_str() )
        # for ix_row  in range( 0, 6, 2 ):
        #     row_span      = 2   # using None seems ok to get default
        #     col_span      = 1   # using None seems ok to get default

        #     for ix_col in range( 4, 6 ):

        #         widget = QPushButton(f"r{ix_row} c{ix_col}")
        #         widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #         layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # ix_row   += 2
        # button_layout  = QHBoxLayout()
        # layout.addLayout( button_layout, ix_row, 0, row_span, 6 )


        ix_row   += 2
        button_layout  = QHBoxLayout()
        mutating_layout.addLayout( button_layout, ix_row, 0, row_span, 6 )

        widget = QPushButton("mutate\n")
        #self.button_ex_1         = widget
        widget.clicked.connect( lambda: self.mutate( ) )
        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )


        self.append_msg( tab_base.DONE_MSG )


    # ------------------------------------
    def mutate_2( self ):
        """
        read it -- mutate the widgets
            clear everything even the buttons




        """
        self.append_function_msg( "mutate_2" )

        msg    = "first clear  "
        self.append_msg( msg, )

        mutating_layout = self.mutating_layout


        self.clear_grid_layout( self.mutating_layout )
        mutating_layout.reset(  col_max = 8  )



        row_span      = 1 # default is 1
        col_span      = 1 # default is 1

        # rowSpan: (Optional) The number of rows the widget should span. Defaults to 1.
        # columnSpan: (Optional) The number of columns the widget should span. Defaults to 1.

        for ix  in range( 0, 6 ):

            widget = QPushButton(f"???")
            widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            mutating_layout.addWidget( widget,  columnspan   = int( ix ),  rowspan = row_span )
            widget.setText(  mutating_layout.get_add_parm_str() )
        # for ix_row  in range( 0, 6, 2 ):
        #     row_span      = 2   # using None seems ok to get default
        #     col_span      = 1   # using None seems ok to get default

        #     for ix_col in range( 4, 6 ):

        #         widget = QPushButton(f"r{ix_row} c{ix_col}")
        #         widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #         layout.addWidget( widget, ix_row, ix_col, row_span, col_span )

        # ix_row   += 2
        # button_layout  = QHBoxLayout()
        # layout.addLayout( button_layout, ix_row, 0, row_span, 6 )

        ix_row   = mutating_layout.ix_row

        button_layout  = QHBoxLayout()
        mutating_layout.addLayout( button_layout, ix_row, 0, row_span, 6 )

        widget = QPushButton("mutate\n")
        #self.button_ex_1         = widget
        widget.clicked.connect( lambda: self.mutate( ) )
        button_layout.addWidget( widget )

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        clear_button = widget
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        clear_button = widget
        button_layout.addWidget( widget,   )


        self.append_msg( tab_base.DONE_MSG )






    #-----------------------------
    def clear_grid_layout(self, grid_layout):
        # Get all items from the grid layout
        while grid_layout.count():
            # Get the first item
            item = grid_layout.takeAt(0)

            # If the item has a widget
            if item.widget():
                # Remove and destroy the widget
                widget = item.widget()
                widget.setParent(None)
                widget.deleteLater()
            # If the item has a layout (nested layout)
            elif item.layout():
                # Recursively clear the nested layout
                self.clear_grid_layout(item.layout())
                item.layout().setParent(None)

    # Now the grid is empty and you can add new widgets
    # ------------------------
    def inspect(self):
        """
        the usual
        """
        self.append_function_msg( "inspect" )

        # make some locals for inspection
        wat_inspector.go(
             msg            = "gridlayouttab",
             a_locals       = locals(),
             a_globals      = globals(), )

        self.append_msg( tab_base.DONE_MSG )

    # ------------------------
    def breakpoint(self):
        """
        keep this in each object so user breaks into that object
        """
        self.append_function_msg( "breakpoint" )

        breakpoint()

        self.append_msg( tab_base.DONE_MSG )

# ---- eof
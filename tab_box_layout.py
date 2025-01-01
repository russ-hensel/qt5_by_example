#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

KEY_WORDS:      examples of box layouts stretch

CLASS_NAME:     QBoxLayoutTab
WIDGETS:        QHBoxLayout QVBoxLayout
STATUS:         partly works
TAB_TITLE:      Box\nLayouts


"""
# ---- tof

"""

Chat says

n PyQt5, QHBoxLayout is a layout manager that arranges child widgets horizontally in a single row. Using a QHBoxLayout, you can organize widgets within a window or container, setting their alignment, spacing, and more. Here’s a breakdown of how to use it and the available options.
1. Basic Setup

To start, create a QHBoxLayout and add it to your widget:

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

app = QApplication([])

# Create main widget
main_widget = QWidget()

# Create an instance of QHBoxLayout
layout = QHBoxLayout()

# Add widgets to the layout
button1 = QPushButton("Button 1")
button2 = QPushButton("Button 2")
button3 = QPushButton("Button 3")

layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)

# Set the layout on the main widget
main_widget.setLayout(layout)
main_widget.show()

app.exec_()

2. Adding Widgets with addWidget()

The addWidget() method adds a widget to the layout, arranging them horizontally in the order they are added. You can specify alignment within the layout for each widget:

layout.addWidget(button1, alignment=Qt.AlignLeft)
layout.addWidget(button2, alignment=Qt.AlignCenter)
layout.addWidget(button3, alignment=Qt.AlignRight)

3. Adding Spacing with addSpacing()

Use addSpacing() to add a fixed space (in pixels) between widgets:

layout.addSpacing(20)  # Adds 20 pixels of space

4. Adding Stretch with addStretch()

addStretch() inserts flexible space between widgets, expanding as the layout resizes. Multiple stretches will divide space proportionally:

layout.addStretch()      # Adds space that can expand
layout.addWidget(button2)
layout.addStretch()      # Adds expandable space again

5. Setting Margins and Spacing

Margins control the space between the layout and the edges of the widget, while spacing controls the space between widgets within the layout:

layout.setContentsMargins(10, 10, 10, 10)  # left, top, right, bottom
layout.setSpacing(15)                      # Space between widgets

6. Adding Stretch Factors to Widgets

You can control how much space each widget takes up relative to others with addStretch():

layout.addWidget(button1, stretch=1)  # Takes up 1 unit of space
layout.addWidget(button2, stretch=2)  # Takes up 2 units of space
layout.addWidget(button3, stretch=1)  # Takes up 1 unit of space

Summary of Key Methods and Options
Method	Description
addWidget(widget)	Adds a widget to the layout.
addSpacing(px)	Adds fixed spacing in pixels between widgets.
addStretch()	Adds flexible space between widgets.
setContentsMargins(l, t, r, b)	Sets margins around the layout.
setSpacing(px)	Sets spacing between widgets within the layout.
alignment=Qt.AlignX	Aligns widget horizontally or vertically.
stretch=number	Sets stretch factor, allocating relative space to widgets.

By combining these methods, you have fine control over the horizontal arrangement of widgets within a layout.
You said:
could you write this all up as one code example?
ChatGPT said:
ChatGPT

Certainly! Here’s a complete code example that demonstrates using a QHBoxLayout with various options like alignment, spacing, margins, and stretch factors for widgets.

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt

app = QApplication([])

# Create the main widget
main_widget = QWidget()

# Create an instance of QHBoxLayout
layout = QHBoxLayout()

# Set margins around the layout (left, top, right, bottom)
layout.setContentsMargins(10, 20, 10, 20)

# Set spacing between widgets
layout.setSpacing(15)

# Add the first button with left alignment
button1 = QPushButton("Button 1")
layout.addWidget(button1, alignment=Qt.AlignLeft)

# Add some fixed spacing (20 pixels)
layout.addSpacing(20)

# Add the second button in the center with a higher stretch factor
button2 = QPushButton("Button 2")
layout.addWidget(button2, alignment=Qt.AlignCenter, stretch=2)

# Add flexible space that expands as the layout resizes
layout.addStretch()

# Add the third button with right alignment
button3 = QPushButton("Button 3")
layout.addWidget(button3, alignment=Qt.AlignRight, stretch=1)

# Set the layout on the main widget
main_widget.setLayout(layout)

# Show the widget
main_widget.show()

app.exec_()

Explanation of the Code

    Margins: layout.setContentsMargins(10, 20, 10, 20) sets the space around the layout inside the widget.
    Spacing: layout.setSpacing(15) defines the space between widgets within the layout.
    Alignment and Stretch:
        Button 1 is aligned to the left.
        Button 2 is centered and given a higher stretch factor (stretch=2), making it occupy more space relative to other widgets.
        Button 3 is aligned to the right and given a stretch factor of 1.
    Additional Spacing and Stretch: layout.addSpacing(20) adds a fixed 20-pixel space, and layout.addStretch() inserts flexible space that expands to fill the available area.

This example brings together the key features of QHBoxLayout for effective horizontal layout management in PyQt5.


end of chat

tab_box_layout.py

"""
# --------------------
if __name__ == "__main__":
    #----- run the full app
    import main
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
class QBoxLayoutTab( QWidget ) :
    def __init__(self):
        """
        some content from and there may be more
        /mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib/gui_qt_ext.py
        tab_box_layout.QBoxLayoutTab
        """
        super().__init__()
        self.help_file_name     =  "combo_box_widget_tab.txt"
        self._build_gui()

    # ----------------------------------
    def _build_gui(self,   ):
        """
        the usual
        """
        tab_page      = self

        layout        = QVBoxLayout( tab_page )

        row_layout      = QHBoxLayout( )
        self.row_layout_1   = row_layout
        layout.addLayout( row_layout )


        # and some options to look into

        # # Set margins around the layout (left, top, right, bottom)
        # layout.setContentsMargins(10, 20, 10, 20)

        # # Set spacing between widgets
        # layout.setSpacing(15)

        # # Add the left alignment

        # layout.addWidget(button1, alignment=Qt.AlignLeft)


        stretch                     = 0
        widget                      = QPushButton( f"{ stretch = }")
        self.pb_0_0                 = widget
        row_layout.addWidget( widget, stretch = stretch,  )


        stretch                     = 1
        widget                      = QPushButton( f"{ stretch = }")
        self.pb_0_1                 = widget
        row_layout.addWidget( widget, stretch = stretch,  )

        stretch                     = 2
        widget                      = QPushButton( f"{ stretch = }")
        self.pb_0_2                 = widget
        row_layout.addWidget( widget, stretch = stretch,  )

        row_layout      = QHBoxLayout( )
        self.row_layout_1   = row_layout
        layout.addLayout( row_layout )

        stretch                     = 2
        widget                      = QPushButton( f"{ stretch = }")
        row_layout.addWidget( widget, stretch = stretch,  )

        stretch                     = 1
        widget                      = QPushButton( f"{ stretch = }")
        row_layout.addWidget( widget, stretch = stretch,  )

        stretch                     = 0
        widget                      = QPushButton( f"{ stretch = }")
        row_layout.addWidget( widget, stretch = stretch,  )




        layout_b     = QHBoxLayout(    )
        layout.addLayout( layout_b )

        # ---- PB inspect
        widget = QPushButton("show\n_values")
        layout_b.addWidget( widget )
        widget.clicked.connect( self.show_values )

        # widget = QPushButton("remove_add\n_widget")
        # layout_b.addWidget( widget )
        # widget.clicked.connect( lambda: self.remove_add_widget_layout_tab() )

        # widget = QPushButton("replace\n_widget")
        # layout_b.addWidget( widget )
        # widget.clicked.connect( lambda: self.replace_widget_layout_tab() )

        # --------
        widget = QPushButton( "change_size_\npolicy" )  # showminimized iconify
        layout_b.addWidget( widget )
        widget.clicked.connect(  self.change_size_policy )

        button_layout = layout_b

        # ---- PB inspect
        widget = QPushButton("inspect\n")
        widget.clicked.connect( self.inspect    )
        button_layout.addWidget( widget,   )

        # ---- PB breakpoint
        widget = QPushButton("breakpoint\n")
        widget.clicked.connect( self.breakpoint    )
        button_layout.addWidget( widget,   )

    #-----------------------------------------------
    def remove_add_widget_layout_tab( self, ):
        """
        deletes and adds but position may change
        """
        print_func_header( "remove_add_widget_layout_tab" )

        print( "replace widget is better may need delete later ")
        self.widget_ix             += 1
        widget              = QPushButton("Button + str(self.widget_ix)")

        self.layout_tab_layout_a.removeWidget( self.widget_temp  )
        self.widget_temp    = widget
        # button1.deleteLater()  # Optionally delete the old widget
        self.layout_tab_layout_a.addWidget( widget )

    #-----------------------------------------------
    def replace_widget_layout_tab( self, ):
        """
        deletes and adds but position may change
        """
        print_func_header( "replace_widget_layout_tab" )

        widget                      = self.widget_temp
        self.widget_ix             += 1
        widget_new                  = QPushButton( f"Button   {self.widget_ix}")
        #self.keep_me                = widget_new
        # stop from delete

        self.replace_layout_widget( self.layout_tab_layout_a, widget, widget_new )
        self.widget_temp            = widget_new

    # -----------------------------
    def replace_layout_widget( self, layout, widget, widget_new ):
        """
        function should work copy and paste
        will be a problem if widget is not found in layout

        """
        print_func_header( "replace_layout_widget" )

        index               = layout.indexOf( widget )
        print( f"widget at {index}")
        # Remove the old widget
        widget_to_remove    = layout.takeAt(index).widget()

        # see if this is causing a problem
        if widget_to_remove:
            widget_to_remove.deleteLater()

    # -----------------------
    def build_gui_sub(self, layout ):
        """
        = QGroupBox()
        """


    # ------------------------
    def change_size_policy(self):
        """
        what it says
        """
        print_func_header( "change_size_policy" )

        self.pb_0_0.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding ) # x and y direction ?



    # ------------------------
    def show_values(self):
        """
        what it says
        """
        print_func_header( "show_values" )

        print( f"{ self.pb_0_0.width() = } " )
        print( f"{ self.pb_0_1.width() = } " )
        print( f"{ self.pb_0_2.width() = } " )

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection
        my_tab_widget           = self
        #parent_window = self.parent( ).parent( ).parent().parent()
        self_row_layout_1   = self.row_layout_1
        self_pb_0_0         = self.pb_0_0
        self_pb_0_1         = self.pb_0_1
        self_pb_0_2         = self.pb_0_2

        wat_inspector.go(
             msg            = "inspect self_ insead of self. pb for pushbuttons ",
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
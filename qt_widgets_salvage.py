

# ---- tof
""""

Put all work into the tabs of WidgetExample
    except perhaps for placer work in second example
    rest for code extraction and deletion


"""
# ---- search
"""
    Search for the following in the code below:

        border        -- only on some widgets not QWidet
        button
        checkbox
        combobox     is a dropdownlist ddl
        edit          QLineEdit,   QTextEdit,
        action
        menu
        groupbox
        isChecked
        get_text
        grid
        label
        lineEdit
        listbox      QListWidget         in ex_  listbox
        icon
        MessageBox     QMessageBox
        qdate
        self.showMinimized()
        minimized
        show
        iconify
        radiobutton
        radiobutton index
        row
        size
        select
        stylesheet
        style
        text
        textOnLeft           for radiobutton
        widget
        partial

    See Also:

    Links
        Create Python GUIs with PyQt5 — Simple GUIs to full apps
            *>url  https://www.pythonguis.com/pyqt5/
        Qt Widget Gallery | Qt Widgets 5.15.14
            *>url  https://doc.qt.io/qt-5/gallery.html
        Widgets Classes | Qt Widgets 5.15.14
            *>url  https://doc.qt.io/qt-5/widget-classes.html


"""

# ---- imports


import time
from platform import python_version

import wat

import adjust_path
import wat_inspector

print( f"your python version is: {python_version()}"  )   # add to running on

# import PyQt5.QtWidgets as qtw    #  qt widgets avaoid so much import below
# from   PyQt5.QtCore import Qt, QTimer
# from   PyQt5 import QtGui


# ---- imports neq qt

import inspect
import subprocess
import sys
#import datetime
from datetime import datetime
# import PyQt5.QtWidgets as qtw    #  qt widgets avaoid so much import above
from functools import partial
from subprocess import PIPE, STDOUT, Popen, run

#from   ex_qt import ia_qt
import ia_qt
from PyQt5 import QtGui
from PyQt5.QtCore import QDate, QDateTime, QModelIndex, Qt, QTimer
from PyQt5.QtGui import QTextCursor, QTextDocument
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
                             QVBoxLayout,
                             QWidget)

sys.path.append( r"D:\Russ\0000\python00\python3\_examples"  )
sys.path.append( r"D:\Russ\0000\python00\python3\_projects\rshlib"  )
sys.path.append( "../")  # not working today vscode
sys.path.insert( 1, "/mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib" )
import ex_helpers
import gui_qt_ext
#import picture_viewer
import wat

import utils_for_tabs as uft

#wat_inspector    = wat.Wat( "joe")

# ---- end imports


INDENT        = uft.INDENT
BEGIN_MARK_1  = uft.BEGIN_MARK_2
BEGIN_MARK_2  = uft.BEGIN_MARK_2



what   = Qt.AlignCenter   # valid aligment perhaps to addWidget   layout.addWidget
#	addWidget(QWidget *widget, int stretch = 0, Qt::Alignment alignment = Qt::Alignment())
note   = """
main work example it WidgetExamplesInTabs

Widget example with placer should be same with placer -- may have good salvage code
same for the rest of the examples

"""
print( note )

function_nl     = "\n\n"   #   msg   = f"{function_nl}function_name"   print( msg )


# --------------------------------
def set_groupbox_style( groupbox ):
        """
        used to modify the appearance of a groupbox
        see the groupbox tab
        """
        groupbox.setStyleSheet("""
            QGroupBox {
                border: 2px solid blue;
                border-radius: 10px;
                margin-top: 15px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px;
                background-color: white;
            }
        """)


# ----------------------------
class CustomDateEdit( QDateEdit ):
    """
    move a version to stuffdb
    custom_widget.pb   as CQDateEdit
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCalendarPopup(True)

        # Set an initial date (optional)
        self.setDate(QDate.currentDate())

    def contextMenuEvent(self, event):
        # Create the context menu
        context_menu = QMenu(self)

        # Add custom actions
        clear_action = QAction("Clear Date", self)
        today_action = QAction("Set to Today", self)

        # Connect actions to methods
        clear_action.triggered.connect(self.clear_date)
        today_action.triggered.connect(self.set_to_today)

        # Add actions to the menu
        context_menu.addAction(clear_action)
        context_menu.addAction(today_action)

        # Show the context menu
        context_menu.exec_(event.globalPos())

    def clear_date(self):
        self.clear()  # Clears the QDateEdit

    def set_to_today(self):
        self.setDate(QDate.currentDate())  # Sets date to today



# ---- eof
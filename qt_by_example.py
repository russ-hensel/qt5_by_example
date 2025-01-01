"""

an app that searches for a tab with
example, running, code for qt in python


"""
# ---- top/search
""""
    Search for the following in the code below:

    See Also:

    Links

"""

# ---- imports
import psutil
import inspect
import os
import sqlite3 as lite
import functools
import subprocess
import sys
from functools import partial
from platform import python_version
from subprocess import PIPE, STDOUT, Popen, run

#from app_global import AppGlobal
from PyQt5 import QtGui
from PyQt5.QtCore import (QDate,
                          QModelIndex,
                          QSize,
                          QSortFilterProxyModel,
                          Qt,
                          QTimer)
# sql
from PyQt5.QtSql import (QSqlDatabase,
                         QSqlField,
                         QSqlQuery,
                         QSqlQueryModel,
                         QSqlRecord,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlRelationalTableModel,
                         QSqlTableModel)
from PyQt5.QtWidgets import (QAbstractItemView,
                             QAction,
                             QApplication,
                             QButtonGroup,
                             QCheckBox,
                             QComboBox,
                             QDataWidgetMapper,
                             QDateEdit,
                             QDialog,
                             QDoubleSpinBox,
                             QFormLayout,
                             QGridLayout,
                             QGroupBox,
                             QHBoxLayout,
                             QHeaderView,
                             QLabel,
                             QLineEdit,
                             QListWidget,
                             QListWidgetItem,
                             QMainWindow,
                             QMenu,
                             QMessageBox,
                             QPushButton,
                             QRadioButton,
                             QSpinBox,
                             QStyledItemDelegate,
                             QTableView,
                             QTableWidget,
                             QTableWidgetItem,
                             QTabWidget,
                             QTextEdit,
                             QVBoxLayout,
                             QWidget)

import adjust_path
import app_services
import global_vars
import index_and_search
import parameters
import qt_table_model

import tab_qsql_database
import tab_select_tab

import utils_for_tabs as uft
import wat_inspector
import show_parameters

# ---- end imports



INDENT          = uft.INDENT
BEGIN_MARK_1    = uft.BEGIN_MARK_2
BEGIN_MARK_2    = uft.BEGIN_MARK_2

print_func_header  = uft.print_func_header

__VERSION__  = "ver_07"

# ---- main window ===================================================================
class QtByExample( QMainWindow ):
    def __init__(self):
        """
        the usual
        """
        super().__init__()

        global_vars.set_controller( self )  # import global_vars

        my_parameters       = parameters.Parameters()
        self.parameters     = my_parameters
        uft.parameters      = my_parameters
        uft.main_window     = self
        #app_services_obj    = app_services

        qt_xpos             = my_parameters.qt_xpos
        qt_ypos             = my_parameters.qt_ypos
        qt_width            = my_parameters.qt_width
        qt_height           = my_parameters.qt_height

        uft.TEXT_EDITOR     = my_parameters.text_editor

        global DB_FILE

        DB_FILE             = my_parameters.db_file_name
        #uft.DB_FILE         = DB_FILE
        #uft.TEXT_EDITOR     = my_parameters.text_editor

        # next builds and populates the db, or may depending on refactor
        self.index_search    =  index_and_search.IndexSearch()
        #self.test_init()

        self.tab_dict        = {}    # key class name, contents for now just index
        self.tab_help_dict   = { }
        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )
        self.doc_dir             = "./docs/"
        #self.create_db()

        self.build_gui()
        self.current_tab_index   = 0   # I need to track in changed
        self.tab_widget.setCurrentIndex( 0 )

        if parameters.PARAMETERS.do_search_on_init:
            self.search_tab.criteria_select()

    # ------------------
    def build_gui( self ):
        """
        main gui build method -- for some sub layout use other methods
        """
        self.setWindowTitle( f"QtExampleByKeyWord {__VERSION__}" )
        self.build_menu( )

        #self.setWindowIcon( QtGui.QIcon('clipboard_b_red_gimp.ico') )
        #self.setWindowIcon( QtGui.QIcon( './designer.png' ) )  # cannot get this to work

        icon    = QtGui.QIcon(  "/mnt/WIN_D/Russ/0000/python00/python3/_projects/qt_by_example/icons/icons/abacus.png"  )
        self.setWindowIcon(icon)

        central_widget          = QWidget()
        self.setCentralWidget(central_widget)

        central_widget_layout   =  QVBoxLayout( central_widget )

        # --- out main layout
        layout      = QVBoxLayout(   )
        central_widget_layout.addLayout( layout )

        # ---- Create tabs
        self.tab_widget = QTabWidget()   # really the folder for the tabs
                                         # tabs themselves are just Widgets

        # Set custom height for the tabs
        self.tab_widget.setStyleSheet("QTabBar::tab { height: 60px; }")

        self.tab_widget.currentChanged.connect(self.on_tab_changed)
        self.tab_widget.tabBarClicked.connect( self.on_tab_clicked)

        self.tab_widget.tabCloseRequested.connect( self.on_tab_close_requested)
        self.tab_widget.setTabsClosable( False )
            # Allows you to enable or disable the close button on tabs.
        self.tab_widget.setMovable( True )
            # what it says

        layout.addWidget( self.tab_widget   )

        title    = "Select\nTab"
        tab      = tab_select_tab.Search_Tab()
        self.search_tab            = tab
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "select_tab.txt"

        self.open_tab_select( "tab_qsql_database", "QSqlDatabaseTab", "QSqlDatabase QSqlQuery"  )

        button_layout = QHBoxLayout(   )
        central_widget_layout.addLayout( button_layout )

    # ------------------------
    def switch_to_tab_by_class_name( self, class_name,   ):
        """
        do action
        return tab index or -1
        """
        tab_index      =  self.tab_dict.get( class_name, -1 )

        if tab_index >= 0:
            self.tab_widget.setCurrentIndex( tab_index )

        return tab_index

    # ------------------------
    def open_tab_select( self, module_name, class_name, title  ):
        """
        open_tab_select( self, module_name, class_name, title  ):
        widget          = self.selected_widget
        row             = widget.row( item )

        text            = item.text()
        """
        # title           = eval( "'" + title + "'" )

        # something like this ??
        # tab_title                   = doc_data[ "tab_title" ].strip()
        # tab_title.replace( "/", "\n")

        #print(f"open_tab_select: {row}, text: {text}")
        tab             = app_services.create_instance( module_name, class_name, )

        tab_index      = self.tab_widget.indexOf( tab  )

        self.tab_widget.addTab( tab, title  )
        tab_index      = self.tab_widget.indexOf( tab  )
        self.tab_widget.setCurrentIndex( tab_index )
        self.tab_dict[  class_name  ]  = tab_index

    # ------------------------------------
    def build_menu( self,  ):
        """
        what it says:
        """
        menubar         = self.menuBar()
        self.menubar    = menubar
        # ---- Configuration
        a_menu          = menubar.addMenu("Configuration")

        open_action     = QAction( "Open Log", self )
        connect_to      = functools.partial( self.open_txt_file,
                                              parameters.PARAMETERS.pylogging_fn  )
        open_action.triggered.connect( connect_to )
        a_menu.addAction( open_action )

        #---------------
        open_action     = QAction( "Show Parameters", self )
        connect_to      = self.show_parameters
        open_action.triggered.connect( connect_to )
        a_menu.addAction( open_action )

        # #---------------
        # open_action     = QAction( "Open Parameters", self )
        # connect_to      = AppGlobal.controller.os_open_parmfile
        # open_action.triggered.connect( connect_to )
        # a_menu.addAction( open_action )

        a_menu.addSeparator()
        # a_menu.addSeparator()

        # ---- Help
        menu_help       = menubar.addMenu( "Help" )

        action          = QAction( "README.md...", self )
        connect_to      = partial( self.open_txt_file, "README.md" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "General Help...", self )
        connect_to      = partial( self.open_txt_file, "./docs/general_help.txt" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        # action          = QAction( "Guide to QT Book Examples...", self )
        # connect_to      = partial( self.open_txt_file, "./docs/guide_to_qt_book_examples.txt" )
        # action.triggered.connect( connect_to )
        # menu_help.addAction( action )

        action          = QAction( "Current Tab Help...", self )
        connect_to      = self.open_tab_help
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "Developer Notes...", self )
        connect_to      = partial( self.open_txt_file, "readme_rsh.txt" )
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        about_action1 = QAction( "About...", self )
        about_action1.triggered.connect( self.show_about_box )
        menu_help.addAction( about_action1 )   # action is added directly to menu

    #----------------------------
    def test_initxxxx( self,   ):
        """
        what it says read:
        """
        db      = self.index_search.build_stuff()
        global   DB
        DB      = db

    #----------------------------
    def not_implemented( self,   ):
        """
        what it says read:
        """
        QMessageBox.information(self, "Not Implemented", "Working on this...")

    #----------------------------
    def inspect_mutate_not_conndected ( self,   ):
        """
        what it says read:
        """
        uft.print_func_header( "inspect......" )
        index = self.tab_widget.currentIndex()
        self.tab_widget.setCurrentIndex(2)  # Set the active tab by index

        text = self.tab_widget.tabText(0)  # Get the label of the first tab
        self.tab_widget.setTabText(0, "New Label")  # Set a new label

    #-------
    def open_general_help( self,   ):
        """
        what it says read:
        """
        doc_name            = f"{self.doc_dir}qt_widgets_help.txt"
        ex_editor           = r"xed"
        proc                = subprocess.Popen( [ ex_editor, doc_name ] )

    # ---- events ------------------------------------------
    #----------------------------
    def on_tab_changed(self, index):
        """
        what it says, read it
        """
        #print(f"on_tab_changed from { self.current_tab_index = } to {index = }")
        # !! THINK the widge does this itself
        self.current_tab_index   = index
        self.tab_page_info()

    #----------------------------
    def on_tab_close_requested( self, index):
        self.tab_widget.removeTab(index)

    #----------------------------
    def on_tab_clicked(self, index):

        return    # return to silence
        print(f"Tab {index} clicked.")

    #----------------------------
    def tab_page_info( self ):
        """
        what it says, read it
        """
        return    # return to silence
        nb    = self.tab_widget
        print(f"nb.select()  >>{nb.currentIndex() = }<<")
        print(f'>>{nb.tabText(nb.currentIndex()) = }<<')
        # print(f'{ nb.index("current" ) = }' )

    # ----
    def iconify( self ):
        """
        what it says
        """
        self.showMinimized()   # for minimizing your window

    #-------
    def open_tab_help( self,   ):
        """
        what it says read:
        """
        current_tab     = self.tab_widget.currentWidget()
        doc_name        = current_tab.help_file_name

        # tab_index           = self.tab_widget.currentIndex()
        # tab_title           = self.tab_widget.tabText( self.tab_widget.currentIndex())
        # doc_name            = self.tab_help_dict.get( tab_title, "no_specific_help.txt")
        doc_name            = f"{self.doc_dir}{doc_name}"
        #rint( f"open_tab_help {doc_name = }")

        self.open_txt_file( doc_name )

    #-------
    def open_txt_file( self, file_name  ):
        """
        what it says read
        """
        proc               = subprocess.Popen( [ uft.TEXT_EDITOR, file_name ] )

    # -----------------------
    def show_about_box(self):
        """
        what it says, but !! more inf
        """
        mode        = parameters.PARAMETERS.mode
        version     = "Version = {stuffdb.__version__}"
        process_pid = psutil.Process(os.getpid())
        #print( f"process.memory_info().rss >>{process.memory_info().rss}<<")  # in bytes

        msg      =  "get the size this process thru its pid "
        memory   = process_pid.memory_info().rss/1_000_000
        memory   = f"Memory = {memory} Mbytes"
        repo     = " coming soom          "
        msg      = ( f"Stuff DB {version} {mode}"
                     f"\n{memory}"
                     f"\n{repo}"
                     )

        QMessageBox.about(self, "About", msg )

    # -----------------------
    def show_parameters(self):
        """
        what it says,
        """
        dialog     = show_parameters.DisplayParameters( parent = self )
        if dialog.exec_() == QDialog.Accepted:
            #self.model.submitAll()
            # ok     = stuffdb_tabbed_sub_window.model_submit_all(
            #            model,  f"StuffEventsSubTab.add_record " )
            # model.select()
            pass

    #-------
    def create_db( self,   ):
        """
        what it says read:
            this is for the examples not the tab database
        """
        print( "moved to create tab")
        1/0
        self.sample_db          =  tab_qsql_database.SampleDB()

    # ------------------------
    def inspect(self):
        """
        the usual
        """
        print_func_header( "inspect" )

        # make some locals for inspection

        self_parameters    = self.parameters
        self_menubar       = self.menubar

        self_tab_dict      = self.tab_dict

        self_tab_widget     = self.tab_widget

        wat_inspector.go(
             msg            = "inspect !! more locals would be nice ",
             # inspect_me     = self.people_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def breakpoint(self):
        """
        keep this in each object so user breaks into that object
        """
        print_func_header( "breakpoint" )
        breakpoint()

# -----------------------------------
def main():
    """
    yes this is the main app
    """
    app                 = QApplication( [] )
    #dialog          = wat_inspector.DisplayWat( app )  # Create an instance of your custom QDialog
    a_wat_inspector     = wat_inspector.WatInspector( app )
    window              = QtByExample()
    window.show()

    app.exec()

    #sys.exit( 0 )

# --------------------
if __name__ == "__main__":
    main()


# ---- eof

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
import logging
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

#  ---- local imports
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
import tab_base
import logging
import app_logging

#logger   = logging.getLogger()

# ---- end imports

INDENT          = uft.INDENT
BEGIN_MARK_1    = uft.BEGIN_MARK_2
BEGIN_MARK_2    = uft.BEGIN_MARK_2

print_func_header  = uft.print_func_header

__VERSION__  = "ver_12 - 2025 02 06.0"

# ---- main window ===================================================================
class Qt5ByExample( QMainWindow ):
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

        app_logging.init()

        #self.config_logger()

        # next builds and populates the db, or may depending on refactor
        self.index_search    =  index_and_search.IndexSearch()

        #self.test_init()

        self.tab_dict        = {}    # key class name, contents for now just index
                                     # {'QSqlDatabaseTab': 1, 'Dock_10_Tab': 2, 'Fitz_22_Tab': 2}
                                     # but index is unstable
        self.tab_help_dict   = {}
        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )

        self.doc_dir             = my_parameters.help_path
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
        self.setWindowTitle( f"Qt5Example  {__VERSION__}" )
        self.build_menu( )

        icon    = QtGui.QIcon(  "./other/broom_edit_2.png"  )
        #/mnt/WIN_D/russ/0000/python00/python3/_projects/qt5_by_example/other/broom_edit_2.png
        self.setWindowIcon(icon)

        central_widget          = QWidget()
        self.setCentralWidget(central_widget)

        central_widget_layout   =  QVBoxLayout( central_widget )

        # --- out main layout
        layout          = QVBoxLayout(   )
        central_widget_layout.addLayout( layout )

        # ---- Create tabs
        self.tab_widget = QTabWidget()   # really the folder for the tabs
                                         # tabs themselves are just Widgets
        # there is another approach using a style sheet acording to chat
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect( self.close_tab )
        # Set custom height for the tabs
        self.tab_widget.setStyleSheet("QTabBar::tab { height: 60px; }")

        self.tab_widget.currentChanged.connect( self.on_tab_changed )
        self.tab_widget.tabBarClicked.connect(  self.on_tab_clicked )

        # self.tab_widget.tabCloseRequested.connect( self.on_tab_close_requested )
        # self.tab_widget.setTabsClosable( False )
            # Allows you to enable or disable the close button on tabs.
        self.tab_widget.setMovable( True )
            # what it says

        layout.addWidget( self.tab_widget   )

        title                   = "Select\nTab"
        tab                     = tab_select_tab.Search_Tab()
        self.search_tab         = tab
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "select_tab.txt"

        #self.open_tab_select( "tab_base", "TabBase", "TabBase the base tab", widgets = "" )
        self.open_tab_select( "tab_qsql_database", "QSqlDatabaseTab", "QSqlDatabase QSqlQuery", widgets = ""  )
        #open_tab_select( self, module_name, class_name, title  ):

        button_layout = QHBoxLayout(   )
        central_widget_layout.addLayout( button_layout )

    # ------------------------
    def switch_to_tab_by_class_name( self, class_name,   ):
        """
        do action
        return tab index or -1
        tab_dict will not work as index is not stable
        """
        tab_index   = -1
        #print( f"looking for {class_name} = " )
        tab            =  self.tab_widget
        for ix_tab in range( tab.count() ):
             tab_page       = tab.widget( ix_tab )
             full_type      = type( tab_page )
             i_class_name   = full_type.__name__

             #rint( f"found for {class_name =}   " )
             if class_name == i_class_name:
                 tab_index   = ix_tab
                 break

        if tab_index >= 0:
            self.tab_widget.setCurrentIndex( tab_index )

        return tab_index

    # ------------------------
    def switch_to_tab_by_class_name_old( self, class_name,   ):
        """
        do action
        return tab index or -1
        tab_dict will not work as index is not stable
        """
        tab_index      =  self.tab_dict.get( class_name, -1 )

        if tab_index >= 0:
            self.tab_widget.setCurrentIndex( tab_index )

        return tab_index

    # ------------------------
    def open_tab_select( self, module_name, class_name, title,  widgets  ):
        """
        open_tab_select( self, module_name, class_name, title  widgets = widgets  ) ):
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

        tab_index       = self.tab_widget.indexOf( tab  )

        self.tab_widget.addTab( tab, title  )
        tab_index       = self.tab_widget.indexOf( tab  )
        self.tab_widget.setCurrentIndex( tab_index )
        self.tab_dict[  class_name  ]  = tab_index    # depricate i think

        if   isinstance( tab, tab_base.TabBase ):
            #rint( f"yes widgets ==================={widgets}" )
            msg       = f"Widgest of interest >> {widgets}"
            tab.class_widget.setText( msg )


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

        #---------------
        open_action     = QAction( "Open Parameters", self )
        connect_to      = partial( self.open_txt_file, "./parameters.py" )
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
    def close_tab( self, index  ):
        """
        what it says read:
        but moving around causes index change

        """
        #rint( "close tab ")
        tab         = self.tab_widget
        widget      = tab.widget(index)
        text        = tab.tabText(index)
        tooltip     = tab.tabToolTip(index)
        icon        = tab.tabIcon(index)

        #rint( f"{type( widget )=}")

        if ( isinstance( widget,  tab_select_tab.Search_Tab ) or
             isinstance( widget,  tab_qsql_database.QSqlDatabaseTab )
            ):
            print(f"Tab {index} {type( widget )=} cannot be closed because it is key to the operation of this app")
            return

        # if index in [0, 1]:  # Allow closing the first tab
        #     print(f"Tab {index} cannot be closed.")
        else:
            #rint(f"Tab {index} will be closed.")
            self.tab_widget.removeTab(index)

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

    # # ------------------------------------------
    # def config_logger( self, ):
    #     """
    #     configure the python logger
    #     return change of state
    #     !! consider putting in app global, include close
    #     new with print from chat
    #     import logging
    #     logger  = logging.get_
    #     """

    #     # Configure logging
    #     log_filename = self.parameters.pylogging_fn  # File to log messages
    #     logging.basicConfig(
    #         level=self.parameters.logging_level,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    #         format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    #         handlers=[
    #             logging.FileHandler(log_filename),  # Log to a file
    #             # had to restart spyder for this to work may be wanky
    #             logging.StreamHandler( sys.stdout )  # Log to the console (stdout)
    #         ]
    #     )

    #     # for old setup
    #     logger          = logging.getLogger( )
    #     self.logger     = logger

    #     # # Example usage
    #     # logging.debug("This is a DEBUG message")
    #     # logging.info("This is an INFO message")
    #     # logging.warning("This is a WARNING message")
    #     # logging.error("This is an ERROR message")
    #     # logging.critical("This is a CRITICAL message")


    #     # # Explicitly log with a specific level
    #     # logging.log(logging.DEBUG, "This is a DEBUG message.")
    #     # logging.log(logging.INFO, "This is an INFO message.")
    #     # logging.log(logging.WARNING, "This is a WARNING message.")
    #     # logging.log(logging.ERROR, "This is an ERROR message.")
    #     # logging.log(logging.CRITICAL, "This is a CRITICAL message.")



    #     # # Explicitly log messages at specific levels
    #     # logger.log(logging.DEBUG, "This is a DEBUG message from my_logger.")
    #     # logger.log(logging.INFO, "This is an INFO message from my_logger.")
    #     # logger.log(logging.WARNING, "This is a WARNING message from my_logger.")
    #     # logger.log(logging.ERROR, "This is an ERROR message from my_logger.")
    #     # logger.log(logging.CRITICAL, "This is a CRITICAL message from my_logger.")
    #     # logger.log(22, "This is a 22 message from my_logger.")


    #     # AppGlobal.logger.log(22, "This is a 22 message from my_AppGlobal.")

    #     # use these
    #     logger.log( logging.CRITICAL, "call was logger.log( logging.CRITICAL,")
    #     logger.log(22, "This is a 22 message from my_logger.")
    #     logging.debug( "call was: logging.debug" )
    #     logging.info( "call was: logging.info"  )

    #     # AppGlobal.logger.log(22, "AppGlobal.logger.log(22 This is a 22 message from my_AppGlobal.")
    #     # AppGlobal.logger.debug(" AppGlobal.logger.debug This is a DEBUG message my_AppGlobal ")


    #     # import inspect  # for debug i
    #     # import logging
    #     loc        = f"{self.__class__.__name__}.{inspect.currentframe().f_code.co_name} "
    #     debug_msg  = f"{loc} >>> this might be our standard {self = }"
    #     logging.debug( debug_msg )



    #     # AppGlobal.logger_id     = "App"
    #     # logger                  = logging.getLogger( AppGlobal.logger_id )
    #     # logger.handlers         = []  # get stuff to close from here

    #     # logger.setLevel( self.parameters.logging_level )

    #     # # create the logging file handler
    #     # file_handler = logging.FileHandler( self.parameters.pylogging_fn )

    #     # formatter    = logging.Formatter( '%(asctime)s - %(name)s - %(levelname)s - %(message)s' )
    #     # file_handler.setFormatter( formatter )

    #     # # add handler to logger object -- want only one add may be a problem
    #     # logger.addHandler( file_handler )
    #     # msg  = "pre logger debug -- did it work"
    #     # AppGlobal.logger.debug( msg )

    #     # logger.info( "Done config_logger .. next AppGlobal msg" )
    #     # #rint( "configured logger", flush = True )
    #     # self.logger      = logger   # for access in rest of class?
    #     # AppGlobal.set_logger( logger )

    #     # msg  = ( f"Message from AppGlobal.print_debug >> logger level in App = "
    #     #          f"{self.logger.level} will show at level 10"
    #     #         )
    #     # AppGlobal.print_debug( msg )


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
        #rint(f"on_tab_changed from { self.current_tab_index = } to {index = }")
        # !! THINK the widge does this itself
        self.current_tab_index   = index
        self.tab_page_info()

    # #----------------------------
    # def on_tab_close_requested( self, index):
    #     self.tab_widget.removeTab(index)

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
        self.showMinimized()



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
        version     = f"Version = {__VERSION__}"
        process_pid = psutil.Process(os.getpid())
        #rint( f"process.memory_info().rss >>{process.memory_info().rss}<<")  # in bytes

        msg      =  "get the size this process thru its pid "
        memory   = process_pid.memory_info().rss/1_000_000
        memory   = f"Memory = {memory} Mbytes"
        repo     = " coming soon... more stuff          "
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

        print( __file__ )

        breakpoint()

# -----------------------------------
def main():
    """
    yes this is the main app
    """
    app                 = QApplication( [] )
    #dialog          = wat_inspector.DisplayWat( app )  # Create an instance of your custom QDialog
    a_wat_inspector     = wat_inspector.WatInspector( app )
    window              = Qt5ByExample()
    window.show()

    app.exec()

    #sys.exit( 0 )

# --------------------
if __name__ == "__main__":
    main()


# ---- eof

""""

Examples of the qtsql widgets in use

    this is a redoo, with time all will run on the same sample
    database and use inspection as part of there operation

    QSqlTableModel Tab


"""
# ---- top/search
"""
    Search for the following in the code below:



        crud            build_rr_w_crud_tab
        edit            EditStrat
        delegate
        groupbox
        isChecked
        get_text
        hide            hide a row
                        hide a column
        label
        lineEdit
        listbox      QListWidget         in ex_  listbox
        icon
        indexer       not yet need add_indexer  see stuffdb
        menu
        messagebox    see qt_widgets.py
        self.showMinimized()
        minimized
        select
        selectrows         table_view.setSelectionBehavior( QTableView.SelectRows )
        show
        iconify
        radiobutton
        radiobutton index
        size
        table_model                use a lot in stuffdb
                  set value at index
                  set_row_of_data
        tab tabpage
        text
        textOnLeft           for radiobutton
        widget


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


from platform import python_version

import adjust_path

print( f"your python version is: {python_version()}"  )   # add to running on

# import PyQt5.QtWidgets as qtw    #  qt widgets avaoid so much import below
# from   PyQt5.QtCore import Qt, QTimer
# from   PyQt5 import QtGui



import inspect
import os
import subprocess
import sys
from subprocess import PIPE, STDOUT, Popen, run

from app_global import AppGlobal
from PyQt5 import QtGui
from PyQt5.QtCore import (QDate,
                          QModelIndex,
                          QSize,
                          QSortFilterProxyModel,
                          Qt,
                          QTimer)
# sql
from PyQt5.QtSql import (QSqlDatabase,
                         QSqlQuery,
                         QSqlQueryModel,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlRelationalTableModel,
                         QSqlTableModel)
# widgets biger
# widgets -- small
# layouts
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

#import ia_qt

what   = Qt.AlignCenter   # valid aligment perhaps to addWidget   layout.addWidget
import sys
#	addWidget(QWidget *widget, int stretch = 0, Qt::Alignment alignment = Qt::Alignment())
# import PyQt5.QtWidgets as qtw    #  qt widgets avaoid so much import above
from functools import partial

# sys.path.append( r"D:\Russ\0000\python00\python3\_examples"  )
# sys.path.append( r"D:\Russ\0000\python00\python3\_projects\rshlib"  )
# sys.path.append( "../")  # not working today vscode
# sys.path.insert( 1, "/mnt/WIN_D/Russ/0000/python00/python3/_projects/rshlib" )
import ex_helpers
import gui_qt_ext
import rr_w_crud
import table_model

import wat_inspector

#import table_widget



# ---- end imports
# ---- a few parameters
rr_w_crud_app_title   = "russ_qsqlrelationalmodel_with_crud.py"
rr_w_crud_db_file     = "texs_x.db"
rr_w_crud_db_file     = ':memory:'
note   = """
main work example it WidgetExample
Widget example with placer should be same with placer -- may have good salbage code
same for the rest of the examples


"""
print( note )
basedir = os.path.dirname(__file__)


DB_FILE       = "sample.db"
DB_FILE       =  ':memory:'

EXAMPLE_DB    = None  # populated later anyone can connect to this it is open
DB_OBJECT     = None  # for its onwn functions
INDENT        = "    "   # {INDENT}
BEGIN_MARK_1  = "\n------------ "
BEGIN_MARK_2  =  " ------------ "
# ---------------------------------------
def rr_w_crud_create_connection_and_dbxxx():
    """
    uses key gen later but this is jus static

    """
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName( rr_w_crud_db_file )
    if not db.open():
        print("Unable to establish a database connection. {rr_w_crud_db_file}")
        return None

    query = QSqlDatabase.database().exec()

    # Create tables
    query.exec_("""CREATE TABLE department (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(20) NOT NULL)""")

    query.exec_("""CREATE TABLE employee (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    department_id INTEGER,
                    phone VARCHAR(50),
                    FOREIGN KEY (department_id) REFERENCES department(id))""")

    # Insert sample data
    query.exec_("INSERT INTO department (id, name) VALUES (100, 'HR')")
    query.exec_("INSERT INTO department (id, name) VALUES (101, 'Finance')")


    query.exec_("INSERT INTO employee (id, name, department_id, phone ) VALUES (200, 'Alice', 100,  '800 555-1212' )")
    query.exec_("INSERT INTO employee (id, name, department_id, phone ) VALUES (201, 'Bob',   101,  '800 555-1212' )")
    query.exec_("INSERT INTO employee (id, name, department_id, phone ) VALUES (202, 'Bobie',   101,  '800 555-0202' )")
    query.exec_("INSERT INTO employee (id, name, department_id, phone ) VALUES (203, 'Booby',   101,  '800 555-1212' )")
    query.exec_("INSERT INTO employee (id, name, department_id, phone ) VALUES (204, 'Robert',   101,  '800 555-2040')")


    return db

# -------------------------------------
class SampleDB():
    """
    this will create an instance of SampleDB and set up two module Globals
        global EXAMPLE_DB   used to connect widgets to the db
        global DB_OBJECT    this object



    From Chat code now modified :
        Here’s a complete example of how to create a SQLite database with
        two tables: people and people_phones, which have a one-to-many relationship.
        The people table contains personal information, and the people_phones
        table contains multiple phone numbers for each person.
        The primary keys for both tables are integers.

        access as .db
    """
    #-------------------
    def __init__( self ):
        """
        """
        self.db     = None
        self.create_connection()
        self.create_tables()
        self.populate_data()
        #self.query_data()

    #------------
    def create_connection( self, ):
        """Create a SQLite database connection."""
        global EXAMPLE_DB
        global DB_OBJECT


        db           = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName( DB_FILE ) # ':memory:')  # In-memory database for this example
        self.db      = db
        EXAMPLE_DB   = db   # for simple module access
        DB_OBJECT    = self
        if not db.open():
            print("SampleDB Error: Unable to establish a database connection.")
            return False
        return True

    def create_tables( self, ):
        """Create people and people_phones tables."""
        query = QSqlQuery( self.db )

        # Create the 'people' table
        query.exec_("""
            CREATE TABLE people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                family_relation TEXT
            )
        """)

        # Create the 'people_phones' table with a foreign key to the 'people' table
        query.exec_("""
            CREATE TABLE people_phones (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id       INTEGER,
                phone_number    TEXT,
                FOREIGN KEY(person_id) REFERENCES people(id) ON DELETE CASCADE
            )
        """)

    #------------
    def populate_data( self, ):
        """Populate the people and people_phones tables with sample data."""
        query = QSqlQuery( self.db )

        # Insert 5 people into the 'people' table
        people_data = [
            ("Alice",   25,   "Aunt"     ),
            ("Bob",     30,   "Uncke"    ),
            ("Charlie", 35,   "Daughte"  ),
            ("David",   40,   "Daughte2" ),
            ("James",   28,   "Aunt"     ),
            ("Jim",     28,   "Son"      ),
            ("Judy",    28,   "Sun"      ),
            ("Jo",      29,   "God"      ),
        ]

        for name, age, family_relation in people_data:
            # this only one way to bind
            query.prepare("INSERT INTO people (name, age, family_relation) VALUES (?,?, ?)")
            query.addBindValue(name)
            query.addBindValue(age)
            query.addBindValue(family_relation)
            query.exec_()

        # Insert 20 phone numbers into the 'people_phones' table
        phones_data = [
            (1, "555-1234"), (1, "555-5678"), (1, "555-8765"),
            (2, "555-4321"), (2, "555-8765"), (2, "555-3456"),
            (3, "555-9876"), (3, "555-1111"), (3, "555-2222"),
            (4, "555-3333"), (4, "555-4444"), (4, "555-5555"),
            (5, "555-6666"), (5, "555-7777"), (5, "555-8888"),
            (5, "555-9999"), (5, "555-0000"), (5, "555-1235"),
            (2, "555-2345"), (1, "555-3456")
        ]

        for person_id, phone_number in phones_data:
            query.prepare("INSERT INTO people_phones (person_id, phone_number) VALUES (?, ?)")
            query.addBindValue(person_id)
            query.addBindValue(phone_number)
            query.exec_()

    #------------
    def query_data( self, ):
        """SampleDB.query_dataQuery and print data from the tables."""
        query           = QSqlQuery( self.db )

        # Query all people
        print("People:")
        query.exec_("SELECT id, name, age FROM people")
        while query.next():
            person_id   = query.value(0)
            name        = query.value(1)
            age         = query.value(2)
            print(f"ID: {person_id}, Name: {name}, Age: {age}")

        # Query all phone numbers associated with people
        print("\nPeople and their phone numbers:")
        query.exec_("""
            SELECT people.name, people_phones.phone_number
            FROM people
            JOIN people_phones ON people.id = people_phones.person_id
            ORDER BY people.name ASC
        """)
        while query.next():
            name            = query.value(0)
            phone_number    = query.value(1)
            print(f"Name: {name}, Phone: {phone_number}")

# -------------------------------------
class KeyGen():
    """
    """
    #-------------------
    def __init__( self ):
        """
        """
        self.keys     = list( range( 2000, 5000 ))
        self.ix_keys  = -1

    #-------------------
    def get_next_key( self, ):
        """
        """
        self.ix_keys  += 1
        return self.keys[ self.ix_keys ]


#-----------------------------------------------
class FilterProxyModelContent( QSortFilterProxyModel ):
    """
    from chat seems to filter based on content
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Custom filtering method to hide specific rows
    def filterAcceptsRow(self, source_row, source_parent):
        # Example condition: hide rows where column 0 value is "HideMe"
        source_model    = self.sourceModel()
        index           = source_model.index(source_row, 0, source_parent)
        value           = source_model.data(index, Qt.DisplayRole)

        # Return True to keep the row, False to hide it
        return value != "HideMe"






class DateDelegate( QStyledItemDelegate ):
    """
    most of code in tab_data_mapper.py
    example from chat of a delegate
    for DelegateTab

    """

    def createEditor(self, parent, option, index):
        editor = QDateEdit(parent)
        editor.setDisplayFormat('yyyy-MM-dd')
        editor.setCalendarPopup(True)
        return editor

    def setEditorData(self, editor, index):
        # Get the current data from the model and set it into the editor
        date_str = index.model().data(index, Qt.EditRole)
        date = QDate.fromString(date_str, 'yyyy-MM-dd')
        editor.setDate(date)

    def setModelData(self, editor, model, index):
        # When the editor is done, save the data back to the model
        date = editor.date().toString('yyyy-MM-dd')
        model.setData(index, date, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        # Position the editor correctly within the cell
        editor.setGeometry(option.rect)


#-----------------------------------------------
class DelegateToLineEditsTab( QWidget ):
    """
    here build a tab in its own class to hide its variables
    and have its own namespace
    this delegate interacts with a line edits
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        if not self.create_tab_connection():
            sys.exit(-1)

        self.build_tab()
        # Create a QSqlTableModel and set it to the people table
        self.row_index  = 0   # row we will edit

        model           = QSqlTableModel( self, self.db )
        self.model      = model
        model.setTable('people')
        model.select()  # Load the data into the model
        self.load_data()

        # Create a form widget that works with the first row (index 0)
        #form = FormWidget(model, 0)
        #form.setWindowTitle('Edit Person Record')
        #form.show()
# ----------

#     class FormWidget(QWidget):
#         def __init__(self, model, row_index):
#             super().__init__()
#             self.model = model
#             self.row_index = row_index

#             self.init_ui()
#             self.load_data()


# ---------------


    #-----------------------------------------------
    def build_tab(self,   ):
        """

        """
        self.init_ui()

    #-----------------------------------------------
    def create_tab_connection( self ):
        db = QSqlDatabase.addDatabase('QSQLITE')
        self.db    = db
        db.setDatabaseName(':memory:')  # Use an in-memory database for testing purposes
        if not db.open():
            print("Unable to open database")
            return False

        # Create a test table and populate it with some data
        query = db.exec_("""
            CREATE TABLE people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                dob TEXT,
                occupation TEXT
            );
        """)

        query = db.exec_("""
            INSERT INTO people (name, dob, occupation) VALUES
            ('Alice', '1990-04-20', 'Engineer'),
            ('Bob', '1985-11-30', 'Designer'),
            ('Charlie', '1992-06-15', 'Developer');
        """)

        return True

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Create QLineEdit widgets
        self.name_edit = QLineEdit(self)
        self.dob_edit  = QLineEdit(self)
        self.occupation_edit = QLineEdit(self)

        # Add labels and line edits to the layout
        self.layout.addWidget(QLabel("Name"))
        self.layout.addWidget(self.name_edit)
        self.layout.addWidget(QLabel("Date of Birth"))
        self.layout.addWidget(self.dob_edit)
        self.layout.addWidget(QLabel("Occupation"))
        self.layout.addWidget(self.occupation_edit)

        # Button to submit changes
        self.submit_button = QPushButton('Submit Changes')
        self.submit_button.clicked.connect(self.submit_changes)

        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def load_data(self):
        """Load data from the model into the QLineEdits."""
        self.name_edit.setText(self.model.index(self.row_index, 1).data())
        self.dob_edit.setText(self.model.index(self.row_index, 2).data())
        self.occupation_edit.setText(self.model.index(self.row_index, 3).data())

    def submit_changes(self):
        """Submit changes back to the model and database."""
        self.model.setData(self.model.index(self.row_index, 1), self.name_edit.text())
        self.model.setData(self.model.index(self.row_index, 2), self.dob_edit.text())
        self.model.setData(self.model.index(self.row_index, 3), self.occupation_edit.text())

        # Submit the changes to the database
        if self.model.submitAll():
            print("Changes submitted successfully!")
        else:
                print(f"Error submitting changes: {self.model.lastError().text()}")

#-----------------------------------------------
class TableModelTab( QWidget ):
    """
    and table view
    from  QAbstractTableModel
    see ez_qt table_widget and table_model table_widget
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self.build_tab()

    #-----------------------------------------------
    def build_tab( self, ):
        """

        """
        self.table_model_is_hidden  = False

        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        button_layout =  QHBoxLayout(   )

        headers = ["Name", "Age", "Occupation" ]
        #self.view           = QTableView()
        self.table_model          = table_model.TableModel( headers )  # QAbstractTableModel
        #self.model.set_data( data )

        table_view                  = QTableView()
        self.table_model_table_view = table_view
        # Connect the clicked signal to a slot
        table_view.doubleClicked.connect( self.double_clicked )
        table_view.doubleClicked.connect( self.clicked )
        table_view.setModel( self.table_model )

        print( "some selection options" )
        table_view.setSelectionBehavior( QTableView.SelectRows )       # For row selection
        # table_view.setSelectionBehavior( QTableView.SelectColumns )  # For column selection
        # table_view.setSelectionBehavior(QTableView.SelectItems)      # For item selection

        layout.addWidget( table_view )

        # ---- QPushButtons
        layout.addLayout( button_layout )
        widget        = QLabel( 'table_model\n TableModel()/QTableView()' )
        button_layout.addWidget( widget )

        widget = QPushButton("QPushButton")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("populate")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.table_model_tab_populate() )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("get_data")
        widget.clicked.connect(lambda: self.table_model_tab_get_data( ) )
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("hide/unhide")
        widget.clicked.connect(lambda: self.table_model_hide_unhide( ) )
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        #-------------
        widget = QPushButton("hide/unhide column")
        widget.clicked.connect(lambda: self.table_model_toggle_hide_column( ) )
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        layout.addLayout( button_layout )
        widget        = QPushButton('Inspect')
        widget.clicked.connect(self.table_model_inspect )
        button_layout.addWidget( widget )

        widget        = QPushButton('Info/Help')
        connect_to      = partial( AppGlobal.os_open_txt_file,  txt_file = "table_model.txt" )
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        return tab_page

    # -------------------------------------
    def table_model_tab_populate(self,   ):
        """
        what it says
            seems ok
        populates a row at a time
        """
        model      = self.table_model
        #print( f" add_to_model_all_subjects {photo_id = } , {table = }, {table_id = },  {info =} "  )
        #key           = ( table, table_id )
        #key_row       = model_display.indexer.find( key )
        # set_row_of_data
        for ix in range( 3 ):
            # self.view_all_subjects.setModel(  self.model_all_subjects )
            # model        = self.model_display
            row_data     = [  f"a{ix}", f"b{ix}",   f"c{ix}", f"d{ix}"   ]
            #rint( f"{row_data = }")
            model.addRow( row_data)
            #model_display.indexer.set_is_valid( False )
        # set value at index
        an_index       = model.index( 2,2 )
        value          = 9999
        model.set_data_at_index(  an_index, value,  )

    #---------------------------------------
    def table_model_hide_unhide( self ):
        """
        onece filter applide not sure how to remove
        this is messed up might want to start over with chat
        """
        if self.table_model_filter:
            self.table_model_filter   = FilterProxyModelHideRows( )


    #-----------------------------------------------
    def double_clicked( self, index: QModelIndex):
        """
        what it says,
        index coms from table view
        """
        model    = self.table_model
        row      = index.row()
        print( f"on_row_other_clicked {row = }")
        #self.add_ix_other( row )

    #-----------------------------------------------
    def clicked( self, index: QModelIndex):
        """
        what it says,
        index coms from table view
        """
        print( "clicked" )
        model    = self.table_model
        row      = index.row()
        print( f"on_row_other_clicked {row = }")

        self.select_row( row )
        #self.add_ix_other( row )

    #-----------------------------------------------
    def select_row(self, row_index ):
         """Select a specific row."""

         print( "select_row" )
         # Get the selection model from the view
         selection_model = self.table_view.selectionModel()

         # Create an index for the row
         row_start      = self.model.index(row_index, 0)
         row_end        = self.model.index(row_index, self.model.columnCount() - 1)

         # Select the row
         selection_model.select(row_start, selection_model.Select | selection_model.Rows)

    def select_column(self, col_index):
            """
            Select a specific column.
            may want to test and hook up
            """
            # Get the selection model from the view
            selection_model = self.table_view.selectionModel()

            # Create an index for the column
            col_start       = self.model.index(0, col_index)
            col_end         = self.model.index(self.model.rowCount() - 1, col_index)

            # Select the column
            selection_model.select(col_start, selection_model.Select | selection_model.Columns)

    #-----------------------------------------------
    def table_model_toggle_hide_column(self,   ):
        """
        we actually use the view
        """
        print( "table_model_toggle_hide_column")
        self.table_model_is_hidden  = not self.table_model_is_hidden
        if self.table_model_is_hidden:
            self.table_model_table_view.hideColumn( 1 )
        else:
            self.table_model_table_view.showColumn( 1 )

        self.table_model_table_view.show()


    #-----------------------------------------------
    def table_model_tab_get_data(self,   ):
        """
        what it says
        seem ok
        """
        model           = self.table_model

        table_model.model_dump( model )

        data_list       = [  ]
        ix_row          = 0
        for ix_col in range( 3 ):
            index     = model.index( ix_row, ix_col )
            data      = model.data( index, ) #role=Qt.DisplayRole)
            data_list.append( data )
        print( f"table_model_tab_get_data   {data_list = }" )

    # ------------------------------------------
    def table_model_inspect(self):
        """
        what it says, read
        """
        # ia_qt.ia_obj( self.table_model,             msg = "table_model_inspect" )
        # ia_qt.ia_obj( self.table_model_table_view,  msg = "table_view_inspect" )
        ia_qt.q_abstract_table_model( self.table_model,   msg = "table_model_inspect" )

        view     = self.table_model_table_view
        # def get_selected_row_and_column():
        selected_indexes = view.selectionModel().selectedIndexes()
        if selected_indexes:
            for index in selected_indexes:
                row     = index.row()
                column  = index.column()
                print(f"Selected Cell - Row: {row}, Column: {column}")
        else:
            print("No selection")

    # ------------------------------------------
    def add_row_at_end(self):
        """
        may work needs to be hooked up
        """
        row_position = self.table_widget_1.rowCount()
        self.table_widget_1.insertRow( row_position )
    # ------------------------------------------
    def remove_row_currrent(self):
        """
        may work needs to be hooked up
        """
        row_position = self.table_widget_1.currentRow()
        self.table_widget_1.removeRow(row_position)

    # ------------------------------
    def set_size(self):
        """
        read it
        may work needs to be hooked up
        """

        self.table_widget_1.horizontalHeader().setStretchLastSection(True)
        self.table_widget_1.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    # ------------------------------
    def sort(self):
        """
        read it
        """
        """
        may work needs to be hooked up
        """
        msg   = "click headers to sort   "
        print( msg )
        # !! more research on args
        self.table_widget_1.sortItems (  1 , Qt.AscendingOrder  )

    # ------------------------------
    # def on_list_clicked( self  index: QModelIndex ): ) :
    #     """
    #     read it
    #     """
    #     msg   = "click headers to sort   "
    #     print( msg )
    # ------------------------------
    def on_cell_clicked( self, row, col  ):
        """
        read it

        """
        """
        may work needs to be hooked up
        """
        table      = self.table_widget_1

        item       = table.item( row, col )
        if item:
            print(f"Cell clicked: Row {row}, Column {col}, Data: {item.text()}")
        else:
            print(f"Cell clicked: Row {row}, Column {col}, Data: None")

    # ------------------------------
    def search(self, search_for   = "1," ):
        """
        read it
        passing of argument unclear ????
        """
        """
        may work needs to be hooked up
        """
        search_for   = "1,"
        msg          = f"search {search_for = }"
        print( msg )
        a_widget    =    self.table_widget_1
        # Clear current selection.
        a_widget.setCurrentItem( None )

        if not search_for:
            msg      =  "Empty string, don't search."
            print( msg )
            return

        matching_items = a_widget.findItems(search_for,  Qt.MatchContains )
        if matching_items:
            # We have found something.
            item       = matching_items[0]  # Take the first.
            msg        = f"found {item = }"
            print( msg )
            a_widget.setCurrentItem(item)
        else:
            msg        = f"nothing found {search_for = }"
            print( msg )

    def find_row_with_text( self  ):
        """
        read it

        """
        table               = self.table_widget_1
        ix_col_searched     = 2
        ix_found            = None
        target_text   = "Cell (2, 2)"
        for row in range( table.rowCount() ):
            item = table.item( row, ix_col_searched )  # Column 5
            if item and item.text() == target_text:
                ix_found = row

        print( f"find_row_with_text {ix_found = }")

        return ix_found

    def find_row_with_text_in_column(self, ):
        """
        might be faster
        might be wrong depending on how matching works
        from chat
        may be ok not yet tested
        """
        table               = self.table_widget_1

        ix_col_searched     = 2
        ix_found            = None
        target_text     = "xyz"

        matching_items = table_widget.findItems(target_text, QtCore.Qt.MatchExactly)
        for item in matching_items:
            if item.column() == column:
                ix_found            =  item.row()

        print( f"find_row_with_text {ix_found = }")

        return ix_found


print( "!! next not completed")
#-----------------------------------------------


#-----------------------------------------------
class QSqlQueryModelTab( QWidget ):
    """
    Yes, you can use a QSqlQueryModel to loop through all the rows of a
    database table. While QSqlQueryModel is primarily a model class for
    displaying read-only data in views like QTableView, you can
    still access the data programmatically by iterating through the rows and columns.

    Here’s an example of how to use QSqlQueryModel to loop through each row in the table.
    """
    def __init__(self, ):
        """
        """
        super().__init__( )
        self.build_tab()

    #-----------------------------------------------
    def build_tab(self,   ):
        """

        """
        tab_page            = self
        layout              = QVBoxLayout( tab_page )

        table_widget        = QTableWidget(4, 5)  # row, column ??third arg parent
        self.table_widget   = table_widget
        layout.addWidget( table_widget )

    def run_it( self, ):
        """
        from chat
        """
        #def loop_through_rows():
        """Loop through rows using QSqlQueryModel."""

        print( "need !! to set in db connect ")
        model = QSqlQueryModel()

        # Set the query to fetch data from the 'people' table
        model.setQuery("SELECT * FROM people")

        # or

        model.setQuery("SELECT name, age FROM people")

        # Check if the query executed successfully
        if model.lastError().isValid():
            print("Error: ", model.lastError().text())
            return

        # Loop through the rows of the model
        for row in range(model.rowCount()):
            # Extract data from each column in the current row
            row_data = []
            for col in range(model.columnCount()):
                row_data.append(model.data(model.index(row, col)))

            print(f"Row {row + 1}: {row_data}")

        # or


#-----------------------------------------------
class QTableWidgetTab( QWidget ):
    """
    here build a tab in its own class to hide its variables
    and have its own namespace
    this delegate interacts with a view
    """
    def __init__(self, ):
        """
        """
        super().__init__( )
        self.build_tab()

    #-----------------------------------------------
    def build_tab(self,   ):
        """

        """
        tab_page            = self
        layout              = QVBoxLayout( tab_page )

#-----------------------------------------------
class QTableWidgetTab2( QWidget ):
    """
    here build a tab in its own class to hide its variables
    and have its own namespace
    this delegate interacts with a view
    """
    def __init__(self, ):
        """
        """
        super().__init__( )
        self.build_tab()

    #-----------------------------------------------
    def build_tab(self,   ):
        """

        """
        tab_page            = self
        layout              = QVBoxLayout( tab_page )

        table_widget        = QTableWidget(4, 5)  # row, column ??third arg parent
        self.table_widget   = table_widget
        layout.addWidget( table_widget )

        # ---- insert data --- now a mess, parameterize this
        print( "this adds cell 'upside down' and cell cords are ng ")
        for i in range( 4, 0,   -1 ):  # better match table
            for j in range( 5,  0, -1 ):  # col
                # these items arguments must be strings
                item     = QTableWidgetItem("Cell ({}, {})".format( i, j))
                table_widget.setItem(i, j, item)

        ix_col   = 1
        table_widget.setColumnWidth( ix_col, 22 )
        # Set selection behavior and mode

        print( "how select_row works may depend on these ")
        table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)  # Can be SelectRows, SelectColumns, or SelectItems
        # table_widget.setSelectionMode(QAbstractItemView.MultiSelection)  # Can be SingleSelection or MultiSelection

        # set row count works but messes up model
        # row_count   = 2
        # a_widget.setRowCount( row_count )  # increase or decrease rows

        print( "also setColumnCount()  ")

        #self.table.setHorizontalHeaderLabels(employees[0].keys())

        labels  = [ "label0" ]   #ok
        labels  = [ "label0", "label1",
                    "label2", "label3", "label4" ] # too many also ok

        table_widget.setHorizontalHeaderLabels( labels  )
        table_widget.setSortingEnabled( True )

        table_widget.setSortingEnabled( True )

        table_widget.cellClicked.connect( self.on_cell_clicked )

        #layout.addWidget(self.table)  # Add the table to the layout

        # getting an error !!
        print( f"{table_widget.currentRow()}")
            # method returns the currently selected row. It returns -1 i

        # ---- buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # --- begin a_widget method
        a_widget           = QPushButton("add_row_at_end")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.add_row_at_end)

        button_layout.addWidget(a_widget)


        # delete or remove a row
        a_widget           = QPushButton("remove_row_currrent")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.remove_row_currrent)
        button_layout.addWidget(a_widget)

        # delete or remove a row
        a_widget           = QPushButton("set_size")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.set_size)
        button_layout.addWidget(a_widget)

        #
        a_widget           = QPushButton("sort")
        self.add_button    = a_widget
        a_widget.clicked.connect(self.sort)
        button_layout.addWidget(a_widget)

        # ---- search
        a_widget           = QPushButton( "search" )
        self.add_button    = a_widget
        a_widget.clicked.connect( self.search )
        button_layout.addWidget(a_widget)

        # ---- search
        a_widget           = QPushButton( "find_row_with_text" )
        self.add_button    = a_widget
        a_widget.clicked.connect( self.find_row_with_text )
        button_layout.addWidget(a_widget)




        # # ---- QLineEdit  can it hold some data, the date?
        # widget          = QLineEdit()
        # widget.setText( "QLineEdit use set text to set value")
        # layout.addWidget( widget )


        # # ---- QPushButton
        # widget              = QPushButton("QPushButton x")
        # self.button_ex_1    = widget
        # # widget.clicked.connect(lambda: self.print_message(widget.text()))
        # a_widget        = widget
        # widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        # layout.addWidget( widget )


        # Create the table widget with 3 rows and 3 columns
        self.table_widget = QTableWidget(3, 3)

        # Set up column headers
        self.table_widget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        # Add some sample data to the table
        self.populate_table()

        # Set selection behavior and mode
        self.table_widget.setSelectionBehavior( QAbstractItemView.SelectRows)  # Can be SelectRows, SelectColumns, or SelectItems
        self.table_widget.setSelectionMode(QAbstractItemView.MultiSelection)   # Can be SingleSelection or MultiSelection

        # Programmatically select a row and a column
        self.select_row(1)  # Select the second row (index 1)
        self.select_column(2)  # Select the third column (index 2)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    # -------------------------------------
    def populate_table(self):
        """Populate the table with some sample data."""
        for row in range(3):
            for col in range(3):
                item = QTableWidgetItem(f"Item {row + 1}, {col + 1}")
                self.table_widget.setItem(row, col, item)

    # -------------------------------------
    def select_row(self, row_index):
        """Select a specific row.
        may depend on selection mode
        """
        print( f"select_row {row_index = }")
        self.table_widget.selectRow( row_index )

    # -------------------------------------
    def select_column(self, col_index):
        """Select a specific column."""
        self.table_widget.selectColumn(col_index)

    # #-----------------------------------------------
    # def clicked( self, index: QModelIndex):
    #     """
    #     see on_cell_clicked
    #     what it says,
    #     index coms from table view
    #     """
    #     print( "clicked" )
    #     model    = self.table_model
    #     row      = index.row()
    #     print( f"on_row_other_clicked {row = }")

    #     self.select_row( row )
    #     #self.add_ix_other( row )

    # ------------------------------
    def on_cell_clicked( self, row, col  ):
        """
        read it

        """
        print( "on_cell_clicked ")
        table      = self.table_widget

        item       = table.item( row, col )
        if item:
            print(f"Cell clicked: Row {row}, Column {col}, Data: {item.text()}")
        else:
            print(f"Cell clicked: Row {row}, Column {col}, Data: None")

        print( "enable some select if you wish ")
        self.select_row( row )


    # some of next may be mixed up with tableModel, beware
    # -------------------------------------
    def add_row_at_end(self):
        row_position = self.table_widget_1.rowCount()
        self.table_widget_1.insertRow( row_position )

    # -------------------------------------
    def remove_row_currrent(self):
        row_position = self.table_widget_1.currentRow()
        self.table_widget_1.removeRow(row_position)

    # ------------------------------
    def set_size(self):
        """
        read it
        """
        self.table_widget_1.horizontalHeader().setStretchLastSection(True)
        self.table_widget_1.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

    # ------------------------------
    def sort(self):
        """
        read it
        """
        msg   = "click headers to sort   "
        print( msg )
        # !! more research on args
        self.table_widget.sortItems (  1 , Qt.AscendingOrder  )

    # ------------------------------
    # def on_list_clicked( self  index: QModelIndex ): ) :
    #     """
    #     read it
    #     """
    #     msg   = "click headers to sort   "
    #     print( msg )

    # ------------------------------
    def search(self, search_for   = "1," ):
        """
        read it
        passing of argument unclear ????
        """
        search_for   = "1,"
        msg          = f"search {search_for = }"
        print( msg )
        a_widget    =    self.table_widget_1
        # Clear current selection.
        a_widget.setCurrentItem( None )

        if not search_for:
            msg      =  "Empty string, don't search."
            print( msg )
            return

        matching_items = a_widget.findItems(search_for,  Qt.MatchContains )
        if matching_items:
            # We have found something.
            item       = matching_items[0]  # Take the first.
            msg        = f"found {item = }"
            print( msg )
            a_widget.setCurrentItem(item)
        else:
            msg        = f"nothing found {search_for = }"
            print( msg )

    def find_row_with_text( self  ):
        """
        read it
        getText get text
        """
        table               = self.table_widget_1
        ix_col_searched     = 2
        ix_found            = None
        target_text   = "Cell (2, 2)"
        for row in range( table.rowCount() ):
            item = table.item( row, ix_col_searched )  # Column 5
            if item and item.text() == target_text:
                ix_found = row

        print( f"find_row_with_text {ix_found = }")

        return ix_found

    def find_row_with_text_in_column(self, ):
        """
        might be faster
        might be wrong depending on how matching works
        from chat
        may be ok not yet tested
        """
        table               = self.table_widget_1

        ix_col_searched     = 2
        ix_found            = None
        target_text     = "xyz"

        matching_items = table_widget.findItems(target_text, QtCore.Qt.MatchExactly)
        for item in matching_items:
            if item.column() == column:
                ix_found            =  item.row()

        print( f"find_row_with_text {ix_found = }")

        return ix_found


#-----------------------------------------------
class DelegateTab( QWidget ):
    """
    most of code in tab_data_mapper.py
    here build a tab in its own class to hide its variables
    and have its own namespace
    this delegate interacts with a view
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self.create_tab_connection()
        self.build_tab()
        self.model.select()

    #-----------------------------------------------
    def build_tab(self,   ):
        """

        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        # # ---- QLabel
        # widget  = QLabel("Qlabel 1")
        # layout.addWidget( widget )

        # self.qlabel_ex_1  = widget

        # # ---- QLineEdit
        # widget          = QLineEdit()
        # widget.setText( "QLineEdit use set text to set value")
        # layout.addWidget( widget )

        # self.line_edit_ex_1        = widget

        # # ---- QPushButton
        # widget = QPushButton("QPushButton x")
        # # widget.clicked.connect(lambda: self.print_message(widget.text()))
        # a_widget        = widget
        # widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        # layout.addWidget( widget )

        # self.button_ex_1         = widget

        # # ---- QCheckBox
        # widget      =  QCheckBox("I have a Cat")

        # widget.animal = "Cat"   # monkey patch ??
        # widget.setChecked(True)
        # #widget.toggled.connect( self.cbox_clicked )

        # layout.addWidget( widget )

        #self.cbox_ex_1   = widget

        # # ----  QRadioButton
        # widget        = QRadioButton("AUSTRALIA")
        # #radiobutton   = QRadioButton("AUSTRALIA")
        # widget = QRadioButton('Left-Text Radio Button')
        # widget.setChecked(True)  # Set as default selected
        # widget.setLayoutDirection(Qt.RightToLeft)  # Set text layout direction to right-to-left textOnLeft
        # layout.addWidget( widget )

        # #def setup_model_and_view(): # ---- QLabel
        # widget  = QLabel("Qlabel 1")
        # layout.addWidget( widget )

        # self.qlabel_ex_1  = widget

        # # ---- QLineEdit
        # widget          = QLineEdit()
        # widget.setText( "QLineEdit use set text to set value")
        # layout.addWidget( widget )

        # self.line_edit_ex_1        = widget


        # # ---- QCheckBox
        # widget      =  QCheckBox("I have a Cat")

        # widget.animal = "Cat"   # monkey patch ??
        # widget.setChecked(True)
        #widget.toggled.connect( self.cbox_clicked )


        model           = QSqlTableModel(  self, self.db )
        self.model      = model
        model.setTable('people')
        model.select()  # Load data into the model

        table_view = QTableView()
        table_view.setModel(model)

        # Apply the date delegate to the 'dob' column (column index 1)
        date_delegate = DateDelegate()
        table_view.setItemDelegateForColumn( 1, date_delegate )

        table_view.show()

        layout.addWidget( table_view )

        # ---- QLineEdit  can it hold some data, the date?
        widget          = QLineEdit()
        widget.setText( "QLineEdit use set text to set value")
        layout.addWidget( widget )



        # ---- QPushButton
        widget              = QPushButton("QPushButton x")
        self.button_ex_1    = widget
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        layout.addWidget( widget )



        #return table_view

    def create_tab_connection( self ):
        # Setup a connection to an SQLite database (for example)
        db = QSqlDatabase.addDatabase('QSQLITE')
        self.db    = db
        db.setDatabaseName(':memory:')  # In-memory database, for demo purposes
        if not db.open():
            print("Unable to open database")
            return False

        # Create a sample table and insert data
        query = db.exec_("""
            CREATE TABLE people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                dob TEXT,
                occupation TEXT
            );
        """)

        query = db.exec_("""
            INSERT INTO people (name, dob, occupation) VALUES
            ('Alice', '1990-04-20', 'Engineer'),
            ('Bob', '1985-11-30', 'Designer'),
            ('Charlie', '1992-06-15', 'Developer');
        """)

        return True


#-----------------------------------------------
class DataMapperTab( QWidget ):
    """
    most of code in tab_data_mapper.py
    here build a tab in its own class to hide its variables

    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self. create_tab_connection()

        # Create a QSqlTableModel and set it to the people table
        model       = QSqlTableModel( self, self.db )
        self.model  = model
        model.setTable('people')
        model.select()  # Load the data into the model

        self.row_index = 1

        self.build_tab()

    #-----------------------------------------------
    def build_tab(self,   ):
        """

        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

        button_layout = QHBoxLayout( tab_page )


        # Create QLineEdit widgets
        self.name_edit          = QLineEdit(self)
        self.dob_edit           = QLineEdit(self)
        self.occupation_edit    = QLineEdit(self)

        # Add labels and line edits to the layout
        layout.addWidget(QLabel("Name"))
        layout.addWidget(self.name_edit)
        self.layout.addWidget(QLabel("Date of Birth"))
        self.layout.addWidget(self.dob_edit)
        self.layout.addWidget(QLabel("Occupation"))
        self.layout.addWidget(self.occupation_edit)

        layout.addLayout( button_layout )
        # Button to submit changes
        self.submit_button = QPushButton('Submit Changes')
        self.submit_button.clicked.connect(self.submit_changes)
        button_layout.addWidget(self.submit_button)

        # ---- QPushButton
        widget = QPushButton(">Next")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.goto_next( ) )
        button_layout.addWidget( widget )


        # ---- QPushButton
        widget = QPushButton("<Prior")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        widget.clicked.connect( lambda: self.goto_prior( ) )
        button_layout.addWidget( widget )


        # ---- data mapper
        # Set up QDataWidgetMapper
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)

        # Map the fields to the respective columns
        self.mapper.addMapping(self.name_edit,       1)  # Column 1: "name"
        self.mapper.addMapping(self.dob_edit,        2)   # Column 2: "dob"
        self.mapper.addMapping(self.occupation_edit, 3)  # Column 3: "occupation"

        # Set the row to display and map data to the widgets
        self.mapper.setCurrentIndex( self.row_index )

    # -----------------------------
    def submit_changes(self):
        """
        Submit changes back to the database.
        """
        # Submit the changes to the model and the database
        self.mapper.submit()
        if self.model.submitAll():
            print("Changes submitted successfully!")
        else:
            print(f"Error submitting changes: {self.model.lastError().text()}")

    # -----------------------------
    def goto_next(self):
        """
        readme
        """
        self.row_index += 1
        self.mapper.setCurrentIndex( self.row_index )
        print( f"{self.row_index = }")

    # -----------------------------
    def goto_prior(self):
        """
        readme
        """
        self.row_index -= 1
        self.mapper.setCurrentIndex( self.row_index )
        print( f"{self.row_index = }")


    #-----------------------------------------------
    def create_tab_connection( self ):
        # Setup a connection to an SQLite database (for example)
        pass

    #def create_connection():
        db = QSqlDatabase.addDatabase('QSQLITE')
        self.db     = db
        db.setDatabaseName(':memory:')  # Use an in-memory database for testing purposes
        if not db.open():
            print("Unable to open database")
            return False

        # Create a test table and populate it with some data
        query = db.exec_("""
            CREATE TABLE people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                dob TEXT,
                occupation TEXT
            );
        """)

        query = db.exec_("""
            INSERT INTO people (name, dob, occupation) VALUES
            ('Alice', '1990-04-20', 'Engineer'),
            ('Bob', '1985-11-30', 'Designer'),
            ('Charlie', '1992-06-15', 'Developer');
        """)

        return True





# Custom Delegate for Occupation
class OccupationDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        # Assuming the third column (occupation) needs a combo box
        if index.column() == 3:
            combo = QComboBox(parent)
            combo.addItems(['Engineer', 'Designer', 'Developer', 'Manager', 'Other'])
            return combo
        return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        if isinstance(editor, QComboBox) and index.column() == 3:
            value = index.model().data(index, Qt.DisplayRole)
            editor.setCurrentText(value)
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        if isinstance(editor, QComboBox) and index.column() == 3:
            model.setData(index, editor.currentText())
        else:
            super().setModelData(editor, model, index)


#-----------------------------------------------
class DataMapperDelegateTab( QWidget ):
    """
    here build a tab in its own class to hide its variables

    """
    def __init__(self, ):
        """
        """
        super().__init__( )
        self.row_index = 0
        self.create_tab_connection()

        # Create a QSqlTableModel and set it to the people table
        model           = QSqlTableModel( self, self.db )
        self.model      = model
        model.setTable('people')
        model.select()  # Load the data into the model


        self.build_tab()


    #-----------------------------------------------
    def build_tab(self,   ):
        """

        """
        tab_page      = self
        layout        = QVBoxLayout( tab_page )
        self.layout   = layout
        #move here self.init_ui()

        # def init_ui(self):
        #self.setWindowTitle("Edit Person Record")

        # self.layout = QVBoxLayout()

        # Create QLineEdit widgets
        self.name_edit = QLineEdit(self)
        self.dob_edit = QLineEdit(self)
        self.occupation_combo = QComboBox(self)

        # Add labels and line edits to the layout
        self.layout.addWidget(QLabel("Name"))
        self.layout.addWidget(self.name_edit)
        self.layout.addWidget(QLabel("Date of Birth"))
        self.layout.addWidget(self.dob_edit)
        self.layout.addWidget(QLabel("Occupation"))
        self.layout.addWidget(self.occupation_combo)

        # Button to submit changes
        self.submit_button = QPushButton('Submit Changes')
        self.submit_button.clicked.connect(self.submit_changes)
        self.layout.addWidget(self.submit_button)

        # # Central widget setup
        # central_widget = QWidget()
        # central_widget.setLayout(self.layout)
        # self.setCentralWidget(central_widget)

        # Set up QDataWidgetMapper
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel( self.model )

        # Map the fields to the respective widgets
        self.mapper.addMapping(self.name_edit, 1)  # Column 1: "name"
        self.mapper.addMapping(self.dob_edit, 2)   # Column 2: "dob"
        self.mapper.addMapping(self.occupation_combo, 3)  # Column 3: "occupation"

        # Set up custom delegate for the entire mapper
        delegate = OccupationDelegate(self)
        self.mapper.setItemDelegate(delegate)

        # Set the row to display and map data to the widgets
        self.mapper.setCurrentIndex(self.row_index)

    def two_way_to_remove_mapper(self):
        """
        from chat not tested
        """
        # Disconnect the mapper from the model
        self.mapper.setModel( None )

        # Clear the mappings
        self.mapper.clearMapping()

        # Optionally, clear any custom delegate
        self.mapper.setItemDelegate( None )

    def create_tab_connection( self ):
        # Setup a connection to an SQLite database (for example)

        db = QSqlDatabase.addDatabase('QSQLITE')
        self.db     = db
        db.setDatabaseName(':memory:')  # In-memory database for testing
        if not db.open():
            print("Unable to open database")
            return False

        # Create a test table and insert data
        query = db.exec_("""
            CREATE TABLE people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                dob TEXT,
                occupation TEXT
            );
        """)
        query = db.exec_("""
            INSERT INTO people (name, dob, occupation) VALUES
            ('Alice', '1990-04-20', 'Engineer'),
            ('Bob', '1985-11-30', 'Designer'),
            ('Charlie', '1992-06-15', 'Developer');
        """)
        return True


    def submit_changes(self):
        """Submit changes back to the database."""
        # Submit the changes to the model and the database
        self.mapper.submit()
        if self.model.submitAll():
            print("Changes submitted successfully!")
        else:
            print(f"Error submitting changes: {self.model.lastError().text()}")


# def main():
#     app = QApplication(sys.argv)

#     # Create database connection
#     if not create_connection():
#         sys.exit(-1)




#-----------------------------------------------
class FilterProxyModelHideRows(QSortFilterProxyModel):
    def __init__(self, rows_to_hide=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store the list of row indices to hide
        self.rows_to_hide = rows_to_hide if rows_to_hide is not None else []

    # Custom filtering method to hide specific rows
    def filterAcceptsRow(self, source_row, source_parent):
        # Hide the row if its index is in the rows_to_hide list
        return source_row not in self.rows_to_hide

    # Method to update the list of rows to hide
    def setRowsToHide(self, rows):
        self.rows_to_hide = rows
        self.invalidateFilter()  # Reapply the filter to update the view

# ---- new redo ** ------------------------------------------------
#-----------------------------------------------
class QSqlDatabaseTab( QWidget ):
    """
    and table view
    from  QAbstractTableModel
    see ez_qt table_widget and table_model table_widget
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self.build_tab()

    #-----------------------------------------------
    def build_tab( self, ):
        """

        """
        self.table_model_is_hidden  = False

        tab_page      = self
        layout        = QVBoxLayout( tab_page )

        button_layout =  QHBoxLayout(   )
        layout.addLayout( button_layout )


        # ---- PBrebuild_db
        widget              = QPushButton("rebuild_db\n ")
        self.button_ex_1    = widget
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        # ---- PB print_db
        widget              = QPushButton("print_db\n ")
        connect_to          = self.print_db
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )


        # ---- PB inspect
        widget              = QPushButton("inspect\n")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        connect_to        = self.inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # widget              = QPushButton("Inspect\nia")
        # # widget.clicked.connect(lambda: self.print_message(widget.text()))
        # connect_to        = self.inspect_ia
        # widget.clicked.connect( connect_to )
        # button_layout.addWidget( widget )


        widget              = QPushButton("breakpoint\n ")
        connect_to          = self.breakpoint
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

    # ------------------------
    def breakpoint(self):
        """ """
        what    = "breakpoint"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")
        breakpoint()


    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        the_global_db  = DB_OBJECT
        # parent_window = self.parent( ).parent( ).parent().parent()
        # a_db          = parent_window.sample_db
        # model         = self.people_model
        # view          = self.people_view
        wat_inspector.go(
             msg            = "see the_global_db",
             inspect_me     = the_global_db,
             a_locals       = locals(),
             a_globals      = globals(), )

    # ------------------------
    def print_db(self):
        """ """
        what    = "print_db"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        DB_OBJECT.query_data()

    # ------------------------
    def rebuild_db(self):
        """ """
        what    = "rebuild_db"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        DB_OBJECT.query_data()

#-----------------------------------------------
class QSqlRelationalTableModelTab( QWidget ):
    """

    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        # if not self.create_tab_connection():
        #     sys.exit(-1)

        #self.build_tab()

        self._build_model()
        self._build_gui()


        # Create a QSqlTableModel and set it to the people table
        #self.row_index  = 0   # row we will edit

        self.people_model.select()  # Load the data into the model
        self.phone_model.select()  # Load the data into the model
        #self.load_data()

        # Create a form widget that works with the first row (index 0)
        #form = FormWidget(model, 0)
        #form.setWindowTitle('Edit Person Record')
        #form.show()

    # ------------------------------
    def _build_gui( self,   ):
        """

        """
        tab_page       = self

        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

        layout.addWidget( self.people_view   )

        layout.addWidget( self.phone_view    )


        # --- buttons
        button_layout      = QHBoxLayout(   )
        layout.addLayout( button_layout )

        # ---- QPushButton
        widget              = QPushButton("QPushButton\n x")
        self.button_ex_1    = widget
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        # ---- QPushButton
        widget              = QPushButton("Inspect\n")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        connect_to        = self.inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # widget              = QPushButton("Inspect\nia")
        # # widget.clicked.connect(lambda: self.print_message(widget.text()))
        # connect_to        = self.inspect_ia
        # widget.clicked.connect( connect_to )
        # button_layout.addWidget( widget )

        widget              = QPushButton("Print\nData")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        connect_to        = self.print_data
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )


    # ------------------------------
    def _build_model( self,   ):
        """
        build model and views if used here

        """
        # ---- people
        model                  = QSqlTableModel( self, EXAMPLE_DB  )
        self.people_model      = model
        model.setTable('people')

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
        model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.people_view        = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        view.setSelectionBehavior( QTableView.SelectRows )
        view.clicked.connect( self._people_view_clicked  )


        # ---- people_phones
        model                  = QSqlTableModel( self, EXAMPLE_DB  )
        self.phone_model       = model
        model.setTable( 'people_phones' )

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
        #model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.phone_view         = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        #view.setSelectionBehavior( QTableView.SelectRows )
        #view.clicked.connect( self._view_clicked  )


            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
       #  model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));


    # ------------------------
    def _people_view_clicked(self, index,   ):
        """ """
        what    = "_people_view_clicked"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        view    = self.people_view
        msg     = f"_view_clicked  "
        print( msg )
        msg     = f"{INDENT}{view = } there is much to explore here, row, column, values"
        print( msg )

        msg     = f"{INDENT}{index} {index.row() = } {index.column() = } "
        print( msg )

        model      = self.people_model
        people_model = model
        no_rows    = model.rowCount()

        msg     = f"{INDENT}{model.rowCount() = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        age_ix       = 2
        age          = model.data( model.index( row_ix, age_ix ) )

        msg     = f"{INDENT}xtracted data {age = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        key_ix       = 0 # may have been hidden
        key          = model.data( model.index( row_ix, key_ix ) )

        msg     = f"{INDENT}xtracted data {key = }   "
        print( msg )

        # ---- sync up second model
        phone_model     = self.phone_model
        phone_model.setFilter( f"person_id = {key}" )
        phone_model.select()

    # -----------------------
    def add_record(self):
        """ """
        what    = "add_record -- tbd"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    # ------------------------
    def print_data(self):
        """ """
        what    = "print_data"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        DB_OBJECT.query_data()

    # ------------------------
    def do_selections(self):
        """ """
        what    = "print_data"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        parent_window = self.parent( ).parent( ).parent().parent()
        a_db          = parent_window.sample_db
        model         = self.people_model
        view          = self.people_view
        wat_inspector.go(
             msg            = "self.model from inspect method",
             inspect_me     = self.people_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # # ------------------------
    # def inspect_ia(self):
    #     """ """
    #     ia_qt. ia_obj(      self,
    #                         msg             = "self, just a test ",
    #                         max_len         = None,

    #                         print_it        = True,
    #                         sty             = "",
    #                         include_dir     = False,
    #                         )


#-----------------------------------------------
class SeperatorTab( QWidget ):
    """
    Table model
        some of this works as well for a query model
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        self._build_gui()
    # ------------------------------
    def _build_gui( self,   ):
        """

        """
        tab_page       = self

        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

#-----------------------------------------------
class QSqlTableModelTab( QWidget ):
    """
    Table model
        some of this works as well for a query model
    """
    def __init__(self, ):
        """
        """
        super().__init__( )

        # if not self.create_tab_connection():
        #     sys.exit(-1)

        #self.build_tab()

        self._build_model()
        self._build_gui()


        # Create a QSqlTableModel and set it to the people table
        #self.row_index  = 0   # row we will edit

        self.people_model.select()  # Load the data into the model
        self.phone_model.select()  # Load the data into the model
        #self.load_data()

        # Create a form widget that works with the first row (index 0)
        #form = FormWidget(model, 0)
        #form.setWindowTitle('Edit Person Record')
        #form.show()

    # ------------------------------
    def _build_gui( self,   ):
        """

        """
        tab_page       = self

        layout        = QVBoxLayout( tab_page )
        self.layout   = layout

        layout.addWidget( self.people_view   )

        layout.addWidget( self.phone_view    )


        # --- buttons
        button_layout      = QHBoxLayout(   )
        layout.addLayout( button_layout )

        # ---- QPushButton
        widget              = QPushButton("QPushButton\n x")
        self.button_ex_1    = widget
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        # ---- QPushButton
        widget              = QPushButton("Inspect\n")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        connect_to        = self.inspect
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # widget              = QPushButton("Inspect\nia")
        # # widget.clicked.connect(lambda: self.print_message(widget.text()))
        # connect_to        = self.inspect_ia
        # widget.clicked.connect( connect_to )
        # button_layout.addWidget( widget )

        widget              = QPushButton("Print\nData")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        connect_to        = self.print_data
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )


    # ------------------------------
    def _build_model( self,   ):
        """
        build model and views if used here

        """
        # ---- people
        model                  = QSqlTableModel( self, EXAMPLE_DB  )
        self.people_model      = model
        model.setTable('people')

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
        model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.people_view        = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        view.setSelectionBehavior( QTableView.SelectRows )
        view.clicked.connect( self._people_view_clicked  )


        # ---- people_phones
        model                  = QSqlTableModel( self, EXAMPLE_DB  )
        self.phone_model       = model
        model.setTable( 'people_phones' )

        model.setEditStrategy( QSqlTableModel.OnManualSubmit )
            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
        #model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));

        view                    = QTableView( )
        self.phone_view         = view
        view.setModel( model  )
        view.hideColumn( 0 )       # hide is hear but header on model
        #view.setSelectionBehavior( QTableView.SelectRows )
        #view.clicked.connect( self._view_clicked  )


            #  OnFieldChange , OnRowChange , and OnManualSubmit .
        # model->select();
       #  model.setHeaderData(2, Qt.Horizontal, "Age*" ) # QtHorizontal in c
        #model->setHeaderData(1, Qt::Horizontal, tr("Salary"));


    # ------------------------
    def _people_view_clicked(self, index,   ):
        """ """
        what    = "_people_view_clicked"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        view    = self.people_view
        msg     = f"_view_clicked  "
        print( msg )
        msg     = f"{INDENT}{view = } there is much to explore here, row, column, values"
        print( msg )

        msg     = f"{INDENT}{index} {index.row() = } {index.column() = } "
        print( msg )

        model      = self.people_model
        people_model = model
        no_rows    = model.rowCount()

        msg     = f"{INDENT}{model.rowCount() = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        age_ix       = 2
        age          = model.data( model.index( row_ix, age_ix ) )

        msg     = f"{INDENT}xtracted data {age = }   "
        print( msg )

        # extract some data
        row_ix       = index.row()
        key_ix       = 0 # may have been hidden
        key          = model.data( model.index( row_ix, key_ix ) )

        msg     = f"{INDENT}xtracted data {key = }   "
        print( msg )

        # ---- sync up second model
        phone_model     = self.phone_model
        phone_model.setFilter( f"person_id = {key}" )
        phone_model.select()

    # -----------------------
    def add_record(self):
        """ """
        what    = "add_record -- tbd"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    # ------------------------
    def print_data(self):
        """ """
        what    = "print_data"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        DB_OBJECT.query_data()

    # ------------------------
    def do_selections(self):
        """ """
        what    = "print_data"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

    # ------------------------
    def inspect(self):
        """ """
        what    = "inspect"
        print( f"{BEGIN_MARK_1}{what}{BEGIN_MARK_2}")

        # make some locals for inspection
        my_tab_widget = self
        parent_window = self.parent( ).parent( ).parent().parent()
        a_db          = parent_window.sample_db
        model         = self.people_model
        view          = self.people_view
        wat_inspector.go(
             msg            = "self.model from inspect method",
             inspect_me     = self.people_model,
             a_locals       = locals(),
             a_globals      = globals(), )

    # # ------------------------
    # def inspect_ia(self):
    #     """ """
    #     ia_qt. ia_obj(      self,
    #                         msg             = "self, just a test ",
    #                         max_len         = None,

    #                         print_it        = True,
    #                         sty             = "",
    #                         include_dir     = False,
    #                         )

#---- Master Window ===========================================================
class QtSqlWidgetExamplesInTabs( QMainWindow ):
    def __init__(self):
        """
        Lots of widget to run and examine each in own tab
        eventually all against the same db
        """
        super().__init__()

        qt_xpos     = 10
        qt_ypos     = 10
        qt_width    = 1400
        qt_height   = 800

        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )

        self._build_menu()
        self.create_db()


        self._build_gui()

        self.table_model_filter = None   # will be used to hide unhide

        return

    #------------------------------
    def _build_gui( self ):
        """
        main gui build method -- for some sub layout use other methods
        """
        self.setWindowTitle( "QtSqlWidgetExamplesInTabs" )

        self.setWindowIcon( QtGui.QIcon( './designer.png' ) )  # cannot get this to work

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        central_widget_layout  =  QVBoxLayout( central_widget )

        # --- out main layout
        layout      = QVBoxLayout(   )
        central_widget_layout.addLayout( layout )

        # ---- Create tabs
        self.tab_help_dict   = {}
        self.tab_widget     = QTabWidget()   # really the folder for the tabs
                                             # tabs themselves are just QWidgets

        # Set custom height for the tabs
        self.tab_widget.setStyleSheet("QTabBar::tab { height: 40px; }") # 40 enough for 2 lines ??
        layout.addWidget( self.tab_widget   )

        # ---- Done
        tab      = SeperatorTab()
        title    = "Done\n>>"
        self.tab_widget.addTab( tab, title  )

        # ---- QSqlDatabaseTab
        tab      = QSqlDatabaseTab()
        title    = "QSqlDatabaseTab\nTab"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_database_tab.txt"

        # ----
        tab      = SeperatorTab()
        title    = "Draft\n>>"
        self.tab_widget.addTab( tab, title  )

        # ---- QSqlTableModelTab
        tab      = QSqlTableModelTab()
        title    = "QSqlTableModel\nTab"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_table_model_tab.txt"

        tab      = SeperatorTab()
        title    = "TBD\n>>"
        self.tab_widget.addTab( tab, title  )


        tab      = QSqlRelationalTableModelTab()
        title    = "QSqlRelationalTableModel\nTab"
        self.tab_widget.addTab( tab, title  )
        self.tab_help_dict[ title ] = "qsql_relational_table_model_tab.txt"

        tab      = SeperatorTab()
        title    = "Planned\n>>"
        self.tab_widget.addTab( tab, title  )
        #self.tab_help_dict[ title ] = "qsql_relational_table_model_tab.txt"




        print( "later tabs are messing up the db beware")

        # tab      = TableModelTab()
        # title    = "TableModelTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "table_model_tab.txt"

        # tab      = QTableWidgetTab()
        # title    = "QTableWidgetTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "table_widget_tab.txt"

        # tab      = DataMapperTab()
        # title    = "DataMapperTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "data_mapper_tab.txt"

        # tab      = DataMapperDelegateTab()
        # title    = "DataMapper\nDelegateTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "data_mapper_delegate_tab.txt"



        # tab      = QSqlQueryTab()
        # title    = "QSqlQueryTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "q_sql_Query_tab.txt"

        # tab      = DelegateTab()
        # title    = "DelegateTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "delegate_tab.txt"

        # tab      = DelegateToLineEditsTab()
        # title    = "DelegateToLineEditsTab"
        # self.tab_widget.addTab( tab, title  )
        # self.tab_help_dict[ title ] = "delegate_line_edit_tab.txt"

        # tab      = self.build_db_tab()
        # self.tab_widget.addTab( tab, "BasicDB"  )

        # tab      = self.build_tvrmd_tab()
        # self.tab_widget.addTab( tab, "build_tvrmd_tab"  )

        # tab      = self.build_tvtmt_tab()
        # self.tab_widget.addTab( tab, "build_tvtmt_tab"  )
        # # tableview_tablemodel_titles.py  tvtmt

        # tab      = self.build_wmc_tab()
        # self.tab_widget.addTab( tab, "build_wmc_tab"  )

        # # look at later
        # # tab      = self.build_rr_w_crud_tab()
        # # self.tab_widget.addTab( tab, "build_rr_w_crud_tab"  )

        # # self.tab_widget.addTab( self.build_layout_tab( ), "Layouts" )

        # # tab      = self.create_tab_with_buttons( ["Button 1", "Button 2", "Button 3"])
        # # self.tab_widget.addTab( tab, "Tab 1"  )

    # ------------------------------------
    def _build_menu( self,  ):
        """
        what it says read:

        """
        menubar         = self.menuBar()
        self.menubar    = menubar

        # a_menu.addSeparator()

        # ---- Help
        menu_help       = menubar.addMenu( "Help" )

        action          = QAction( "General Help...", self )
        connect_to      = self.open_general_help
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

        action          = QAction( "Current Tab Help...", self )
        connect_to      = self.open_tab_help
        action.triggered.connect( connect_to )
        menu_help.addAction( action )

    #----------------------------
    def not_implemented( self,   ):
        """
        what it says read:
        """
        QMessageBox.information(self, "Not Implemented", "Working on this...")

    #-------
    def create_db( self,   ):
        """
        what it says read:

        """
        self.sample_db          =  SampleDB()



    #-------
    def open_general_help( self,   ):
        """
        what it says read:

        """
        doc_name        = "qsql_widgets_help.txt"
        ex_editor       = r"xed"
        proc            = subprocess.Popen( [ ex_editor, doc_name ] )

    #-------
    def open_tab_help( self,   ):
        """
        what it says read:
            still needs work
        """
        tab_title    = self.tab_widget.tabText( self.tab_widget.currentIndex())
        print( f"{tab_title = }")


        doc_name  = self.tab_help_dict.get( tab_title, "no_specific_help.txt")
        print( f"{doc_name = }")
        ex_editor          = r"xed"

        proc               = subprocess.Popen( [ ex_editor, doc_name ] )
        #AppGlobal.os_open_txt_file( doc_name  )

    # ---- mostly junk from here down ----------------------------------
    #-----------------------------------------------
    def build_list_widget_tab(self,   ):
        """
        should be in qt_widgets not here
        """
        tab_page      = QWidget()
        layout        = QVBoxLayout( tab_page )

        widget        = QListWidget(    )
        widget.setGeometry( 50, 50, 200, 200 )
        layout.addWidget( widget )

        #widget.itemClicked.connect( self.activate_clicked_command )

        values    =  [ "one", "two"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )

        widget.clear()

        values    =  [ "oneish", "twoish"]
        for value in values:
            item = QListWidgetItem( value )
            widget.addItem( item )
            index_to_select = 2

            widget.setCurrentRow(index_to_select)

        ia_qt.q_list( widget )

        return tab_page

    #-----------------------------------------------
    def build_db_tab( self, ):
        """

        """
        tab_page      = QWidget()
        layout        = QVBoxLayout( tab_page )

        button_layout =  QHBoxLayout(   )
        layout.addLayout( button_layout )

        # self.line_edit_ex_1        = widget

        # ---- QPushButton
        widget = QPushButton("QPushButton x")
        # widget.clicked.connect(lambda: self.print_message(widget.text()))
        a_widget        = widget
        #widget.clicked.connect( lambda: self.widget_clicked( a_widget ) )
        button_layout.addWidget( widget )

        # ---- QPushButton
        widget = QPushButton("button 2")

    #-----------------------------------------------
    def build_group_tab(self,   ):
        """
        should not be here should be in qt_widgets
        """
        tab_page      = QWidget()
        layout        = QVBoxLayout( tab_page )
        # ---- QGroupBox
        #groupbox   = QGroupBox()
        groupbox   = QGroupBox( "QGroupBox 1" )   # version with title
        layout.addWidget( groupbox )
        layout_b     = QHBoxLayout( groupbox  )
        self.build_gui_in_groupbox( layout_b )
        return tab_page


    #-----------------------------------------------
    def build_tvrmd_tab(self,   ):
        """
        from book examplse adapted for tab
        tableview_relationalmodel_delegate.py   tvrmd
        an refactored to be less selfish

        """
        tab_page        = QWidget()
        layout          = QVBoxLayout( tab_page )

        button_layout   = QHBoxLayout(   )


        self.tvrmd_table = QTableView()
        table            = self.tvrmd_table

        self.tvrmd_db = QSqlDatabase("QSQLITE")
        db            = self.tvrmd_db

        db.setDatabaseName( os.path.join(basedir, "Chinook_Sqlite.sqlite"))
        db.open()

        self.tvrmd_model = QSqlRelationalTableModel(db=self.tvrmd_db)
        model            = self.tvrmd_model

        table.setModel( model)

        # tag::setRelation[]
        model.setTable("Track")
        model.setRelation(2, QSqlRelation("Album", "AlbumId", "Title"))
        model.setRelation(3, QSqlRelation("MediaType", "MediaTypeId", "Name"))
        model.setRelation(4, QSqlRelation("Genre", "GenreId", "Name"))

        delegate = QSqlRelationalDelegate( table )
        table.setItemDelegate( delegate )

        model.select()
        # end::setRelation[]self.tvrmd_

        # self.setMinimumSize(QSize(1024, 600))
        # self.setCentralWidget(self.table)
        layout.addWidget( table )

        layout.addLayout( button_layout )
        widget        = QPushButton('Inspect')
        widget.clicked.connect(self.tvmd_inspect )
        button_layout.addWidget( widget )

        widget        = QPushButton('Info/Help')
        connect_to      = partial( AppGlobal.os_open_txt_file,  txt_file = "tvmd.txt" )
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        return tab_page

    # ------------------------------------------
    def tvmd_inspect(self):
        """
        what it says, read?
        """
        print( "rr_w_crud_inspect" )
        ia_qt.ia_obj( self.rr_w_crud_view, msg = "rr_w_crud_inspect" )     # self.rr_w_crud_view = QTableView(   )




    # ---- tableview_tablemodle_titles.py --------------------------------
    def build_tvtmt_tab(self,   ):
        """
         # tableview_tablemodle_titles.py  tvtmt
         update
             ??
        """
        tab_page      = QWidget()
        layout        = QVBoxLayout( tab_page )

        self.tvtmt_table = QTableView()
        table            = self.tvtmt_table

        self.tvtmt_db = QSqlDatabase("QSQLITE")
        db             = self.tvtmt_db
        db.setDatabaseName(os.path.join(basedir, "Chinook_Sqlite.sqlite"))
        db.open()

        self.tvtmt_model = QSqlTableModel(db= db)
        model            = self.tvtmt_model
        table.setModel(model)

        # tag::titles[]
        model.setTable("Track")
        model.setHeaderData(1, Qt.Horizontal, "Name")
        model.setHeaderData(2, Qt.Horizontal, "Album (ID)")
        model.setHeaderData(3, Qt.Horizontal, "Media Type (ID)")
        model.setHeaderData(4, Qt.Horizontal, "Genre (ID)")
        model.setHeaderData(5, Qt.Horizontal, "Composer")
        # end::titles[]

        model.select()

        layout.addWidget( table )

        return tab_page


    # ---- widget_maper_controls.py  wmc --------------------------------
    def build_wmc_tab(self,   ):
        """
        need to fix self. that are too broad
        widget_maper_controls.py  wmc
        could mak less selfish and refoamat
        """
        tab_page      = QWidget()
        layout        = QVBoxLayout( tab_page )
        #------

        form            = QFormLayout()

        self.wmc_track_id = QSpinBox()
        self.wmc_track_id.setRange(0, 2147483647)
        self.wmc_track_id.setDisabled(True)
        self.wmc_name       = QLineEdit()
        self.wmc_album      = QComboBox()
        self.wmc_media_type = QComboBox()
        self.wmc_genre      = QComboBox()
        self.wmc_composer   = QLineEdit()

        self.wmc_milliseconds = QSpinBox()
        self.wmc_milliseconds.setRange(0, 2147483647)
        self.wmc_milliseconds.setSingleStep(1)

        self.wmc_bytes = QSpinBox()
        self.wmc_bytes.setRange(0, 2147483647)
        self.wmc_bytes.setSingleStep(1)

        self.wmc_unit_price = QDoubleSpinBox()
        self.wmc_unit_price.setRange(0, 999)
        self.wmc_unit_price.setSingleStep(0.01)
        self.wmc_unit_price.setPrefix("$")

        form.addRow(QLabel("Track ID"), self.wmc_track_id)
        form.addRow(QLabel("Track name"), self.wmc_name)
        form.addRow(QLabel("Composer"), self.wmc_composer)
        form.addRow(QLabel("Milliseconds"), self.wmc_milliseconds)
        form.addRow(QLabel("Bytes"), self.wmc_bytes)
        form.addRow(QLabel("Unit Price"), self.wmc_unit_price)

        self.wmc_db = QSqlDatabase("QSQLITE")
        self.wmc_db.setDatabaseName(os.path.join("Chinook_Sqlite.sqlite"))
        self.wmc_db.open()

        self.wmc_model = QSqlTableModel(db=self.wmc_db)

        self.wmc_mapper = QDataWidgetMapper()
        mapper          = self.wmc_mapper
        mapper.setModel( self.wmc_model )

        mapper.addMapping(self.wmc_track_id, 0)
        mapper.addMapping(self.wmc_name, 1)
        mapper.addMapping(self.wmc_composer, 5)
        mapper.addMapping(self.wmc_milliseconds, 6)
        mapper.addMapping(self.wmc_bytes, 7)
        mapper.addMapping(self.wmc_unit_price, 8)

        self.wmc_model.setTable("Track")
        self.wmc_model.select()

        mapper.toFirst()

        # tag::controls[]
        #self.setMinimumSize(QSize(400, 400))

        controls = QHBoxLayout()

        prev_rec = QPushButton("Previous")
        prev_rec.clicked.connect(mapper.toPrevious)

        next_rec = QPushButton("Next")
        next_rec.clicked.connect(mapper.toNext)

        save_rec = QPushButton("Save Changes")
        save_rec.clicked.connect(mapper.submit)


        controls.addWidget(prev_rec)
        controls.addWidget(next_rec)
        controls.addWidget(save_rec)

        widget        = QLabel( 'wmc QSqlTableModel\nQDataWidgetMapper' )
        controls.addWidget( widget )

        widget        = QPushButton('Inspect')
        widget.clicked.connect(self.wmc_inspect )
        controls.addWidget( widget )

        widget          = QPushButton('Info/Help')
        connect_to      = partial( AppGlobal.os_open_txt_file,  txt_file = "wmc.txt" )
        widget.clicked.connect( connect_to )
        controls.addWidget( widget )

        layout.addLayout(form)
        layout.addLayout(controls)

        return tab_page

    # ------------------------------------------
    def wmc_inspect(self):
        """
        what it says, read?
        """
        print( "rr_w_crud_inspect" )
        ia_qt.ia_obj( self.rr_w_crud_view, msg = "rr_w_crud_inspect" )



    # ---- build_rr_w_crud_tab  -----------------------------------------------
    def build_rr_w_crud_tab(self,   ):
        """
        russ_qsqlrelationalmodel_with_crud.py  rr_w_crud
        import
        """
        return None
        print( "first my db")
        db     = rr_w_crud_create_connection_and_db()
        self.rr_w_crud_db   = db
        self.keygen         = KeyGen()

        tab_page            = QWidget()
        layout              = QVBoxLayout( tab_page )

        button_layout       = QHBoxLayout(   )

        main_layout         = layout

        # Create a table view
        self.rr_w_crud_view = QTableView(   )
        self.rr_w_crud_view.setSelectionBehavior( QTableView.SelectRows )
        main_layout.addWidget(self.rr_w_crud_view)

        layout.addLayout( button_layout )

        widget        = QPushButton('Add')
        #add_button    = widget
        widget.clicked.connect(self.rr_w_crud_add_record)
        button_layout.addWidget( widget )

        widget        = QPushButton('Edit')
        widget.clicked.connect(self.rr_w_crud_edit_record)
        button_layout.addWidget( widget )

        widget        = QPushButton('Delete')
        widget.clicked.connect(self.rr_w_crud_delete_record)
        button_layout.addWidget( widget )

        widget        = QPushButton('Clear/Select')
        widget.clicked.connect(self.rr_w_crud_clear_select)
        button_layout.addWidget( widget )

        widget        = QPushButton('Inspect')
        widget.clicked.connect(self.rr_w_crud_inspect )
        button_layout.addWidget( widget )

        widget        = QPushButton('Info/Help')
        from functools import partial
        connect_to      = partial( AppGlobal.os_open_txt_file,  txt_file = "rr_w_crud.txt" )
        widget.clicked.connect( connect_to )
        button_layout.addWidget( widget )

        # ---- model probrbly should be in _build_model
        # Set up the model
        self.rr_w_crud_model = QSqlRelationalTableModel( self, db  )   # self is parent controls deletion change self to db ?
        self.rr_w_crud_model.setTable('employee')
        self.rr_w_crud_model.setEditStrategy(QSqlTableModel.OnManualSubmit) #  OnFieldChange
        self.rr_w_crud_model.setRelation(2, QSqlRelation( 'department', 'id', 'name') )
        self.rr_w_crud_model.select()

        # Set the model to the view
        self.rr_w_crud_view.setModel(self.rr_w_crud_model)
        self.rr_w_crud_view.setItemDelegate(QSqlRelationalDelegate(self.rr_w_crud_view))


        return tab_page
    # ------------------------------------------
    def rr_w_crud_add_record(self):
        """
        what it says, read?
        """
        dialog = rr_w_crud.EditDialog(self.rr_w_crud_model, self.keygen)
        if dialog.exec_() == QDialog.Accepted:
            self.model.select()

    # ------------------------------------------
    def rr_w_crud_clear_select(self):
        """
        what it says, read?
        """
        # dialog = rr_w_crud.EditDialog(self.rr_w_crud_model, self.keygen)
        # if dialog.exec_() == QDialog.Accepted:
        #     self.model.select()
        self.rr_w_crud_model.select()

    # ------------------------------------------
    def rr_w_crud_delete_record(self):
        """
        what it says, read?
        can we let this pend, need to experiment
        """
        index = self.view.currentIndex()
        if index.isValid():
            self.model.removeRow(index.row())
            self.model.submitAll() # Submit changes to the database
            self.model.select()

    # ------------------------------------------
    def rr_w_crud_edit_record(self):
        """
        what it says, read?
        """
        index = self.rr_w_crud_view.currentIndex()
        if index.isValid():
            dialog = rr_w_crud.EditDialog( self.rr_w_crud_model, self.keygen, index )
            if dialog.exec_() == QDialog.Accepted:
                self.rr_w_crud_model.select()

    # ------------------------------------------
    def rr_w_crud_inspect(self):
        """
        what it says, read?
        """
        print( "rr_w_crud_inspect" )
        ia_qt.ia_obj( self.rr_w_crud_view, msg = "rr_w_crud_inspect" )     # self.rr_w_crud_view = QTableView(   )

    # -----------------------
    def build_gui_sub(self, layout ):
        """
        = QGroupBox()
        """

    # --------
    def current_text_changed(self, s):
        """

        """
        print("Current text: ", s)

    # --------
    def show_values(self):
        """
        show all the values from widgets
        """
        print( "get and show values of widgets")

        line_edit_value  = self.line_edit_ex_1.text()
        cbox_value       = str( self.cbox_ex_1.isChecked())
        # need to save  list and loop thru    radioButton.isChecked() --- or ask the group
        cb1_text         = self.combobox_ex_1.currentText()

        msg   = ( f"\nline_edit_value    = {line_edit_value}"
                  f"\ncbox_value         = {cbox_value}"
                  f"\ncb1_text           = {cb1_text}"
        )
        print( msg )
        # self.message_widget.display_string( msg, )

    # --------
    def print_message(self, text):
        print("Button clicked:", text)

     # --------
    def make_partial_widget_clicked( self, widget):
        """
        """
        from functools import partial
        a_partial_foo       = partial( self.widget_clicked,  widget = widget )

        return a_partial_foo

    # --------
    def widget_clicked( self, widget):
        """
        alterternative button clicked function
        seems like will not work with labmda instead use make_partial_widget_clicked
        """
        print( "widget_clicked" )
        print( f"widget >{widget}<")
        print( f"widget.text() >{widget.text()}<")

    # ----
    def iconify( self ):
        """

        """
        self.showMinimized()   # for minimizing your window

    # --------
    def close_event(self, event):
        """
        Args:
            event (TYPE): DESCRIPTION.

        Returns:
            None.

        """
        if self.popup_question():
            print("The program was shut down.")
            event.accept()
        else:
            print("not exiting")
            event.ignore()


    # --------
    def gen_db(self):
        """
        Chat:
            could you build me a sample data base ( sqllite )for people with a thable
            people and another people_phones with a one to many relationship.
            make all the primary keys integers.
            Have about 5 peopel in the people table, about 20 phone numbers in the people_phones table
        """



    # --------
    def popup_question(self):
        """
        Generate a popup that requests if you want to do something or not.
        here exit the application --- see close_event
        """
        msgbox =  QMessageBox()
        msgbox.setWindowTitle("Whatever title you want to add.")
        msgbox.setIcon( QMessageBox.Warning)
        msgbox.setText("Do you want to quit WidgetExample?")
        botonyes =  QPushButton("Yes")
        msgbox.addButton(botonyes, QMessageBox.YesRole)
        botonno =  QPushButton("No")
        msgbox.addButton(botonno, QMessageBox.NoRole)
        msgbox.exec_()
        if msgbox.clickedButton() == botonno:
            return False
        else:
            return True

# --------
# --------------------
if __name__ == "__main__":


    app         = QApplication(sys.argv)
    a_wat_inspector     = wat_inspector.WatInspector( app )

    window      = QtSqlWidgetExamplesInTabs()
    window.show()
    app.exec()

    sys.exit( 0 )  # cleanup do we need


# ---- eof


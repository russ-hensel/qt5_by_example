#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 08:28:36 2024

stuff_document_edit.EditStuffEvents( model, keygen, index = None, parent = None)



"""

# ---- tof

# --------------------
if __name__ == "__main__":
    import main
    main.main()
# --------------------




import sys

from app_global import AppGlobal
from PyQt5.QtCore import Qt
from PyQt5.QtSql import (QSqlDatabase,
                         QSqlDriver,
                         QSqlQuery,
                         QSqlRecord,
                         QSqlRelation,
                         QSqlRelationalDelegate,
                         QSqlRelationalTableModel,
                         QSqlTableModel)
# ----QtWidgets layouts
from PyQt5.QtWidgets import (QApplication,
                             QComboBox,
                             QDialog,
                             QFormLayout,
                             QGridLayout,
                             QHBoxLayout,
                             QLabel,
                             QLineEdit,
                             QMainWindow,
                             QMessageBox,
                             QPushButton,
                             QTableView,
                             QTextEdit,
                             QVBoxLayout,
                             QWidget)

# ---- local imports
# import  tracked_qsql_relational_table_model

import parameters

# ---- end imports



class DisplayParameters( QDialog ):
    """


    """
    # ------------------------------------------
    def __init__(self,  parent ):
        """
        Args:


        Returns:
            None.

        """
        super().__init__( parent )
        self.parent         = parent  # parent may be a function use parent_window
        self.parent_window  = parent
        msg   = "Display Parameters "

        self.setWindowTitle( msg  )

        qt_xpos     = 10
        qt_ypos     = 10
        qt_width    = 1000
        qt_height   = 500
        self.tab_help_dict   = { }
        self.setGeometry(  qt_xpos,
                           qt_ypos ,
                           qt_width,
                           qt_height  )

        self._build_gui()

    # ------------------------------------------
    def _build_gui( self, ):
        """
        what it says, read?
        """
        layout              = QVBoxLayout( self )
        self.layout         = layout


        # ---- code_gen: edit_fields_for_form  -- end table entries

        # Create QTextEdit widget
        text_edit           = QTextEdit()
        # layout.addWidget(text_edit, 4, 0, 1, 3)  # Row 4, Column 0, RowSpan 1, ColumnSpan 3
        self.text_edit  = text_edit
        layout.addWidget( text_edit )



        # ex_text   = (

        # """
        # widget = QPushButton( "Delete Text" )
        # widget.clicked.connect(lambda: self.delete_text(text_edit))
        # widget.setMaximumWidth(150)
        # button_layout.addWidget( widget,   )

        # widget = QPushButton( "inspect_widget" )
        # widget.clicked.connect(lambda: self.inspect_widget(text_edit))
        # widget.setMaximumWidth(150)
        # button_layout.addWidget( widget,   )
        # """ )

        parm_text      = str( parameters.PARAMETERS )

        cursor = text_edit.textCursor()
        cursor.insertText( parm_text )



        # # ---- buttons
        # self.setLayout( self.layout )
        #self.button_layout      = QVBoxLayout()
        button_layout           = layout


        a_widget                = QPushButton("OK")
        self.save_button        = a_widget
        a_widget.clicked.connect(         self.accept )
        button_layout.addWidget( a_widget )

        # # ----
        # self.buttons.setLayout( self.button_layout )

        # self.layout.addRow(self.buttons)



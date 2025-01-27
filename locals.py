#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:33:15 2025

@author: russ
"""


# ---- tof

# ---- imports

# ---- end imports


#-------------------------------






# ---- eof

        self.line_edit     = QLineEdit()


        # ---- see if these are legal
        #widget.setHeight( )

        # widget.maximumHeight(…) # maximumHeight(self) -> int
        # widget.maximumSize(…) # maximumSize(self) -> QSize
        # widget.maximumViewportSize(…) # maximumViewportSize(self) -> QSize
        # widget.maximumWidth(…) # maximumWidth(self) -> int

        widget.setPlaceholderText("Enter search text")
        layout.addWidget( widget  )




        widget             = QLineEdit()
        self.line_edit     = widget

        # ---- see if these are legal
        #widget.setHeight( )

        # widget.maximumHeight(…) # maximumHeight(self) -> int
        # widget.maximumSize(…) # maximumSize(self) -> QSize
        # widget.maximumViewportSize(…) # maximumViewportSize(self) -> QSize
        # widget.maximumWidth(…) # maximumWidth(self) -> int

        widget.setPlaceholderText("Enter search text")
        layout.addWidget( widget, ix_row, ix_col, row_span,  col_span )


---------------------


        widget = QLineEdit()
        self.line_edit_widget = widget
        widget.setText( "Some initial text" )
        widget.setEnabled( False )
        widget.setPlaceholderText( "Your Text Here " )
        widget.setToolTip( "This is your ToolTip" )
        layout.addWidget( widget, )

------------------------------

        self.line_edit_widget = QLineEdit()
        self.line_edit_widget.setText( "Some initial text" )
        self.line_edit_widget.setEnabled( False )
        self.line_edit_widget.setPlaceholderText( "Your Text Here " )
        self.line_edit_widget.setToolTip( "This is your ToolTip" )
        layout.addWidget( self.line_edit_widget )


----------------------------------

        # the model 1
        self.model_1 = QSqlTableModel( ... )
        self.model_1.setTable( 'table_1')

        # the view 1
        self.view_1 = QTableView( )
        self.view_1.setModel( self.model_1  )
        self.view_1.hideColumn( 0 )
        self.view_1.setSelectionBehavior( QTableView.SelectRows )
        self.view_1.view.setSortingEnabled( True )

        # the model 2
        self.model_2 = QSqlTableModel( ... )
        self.model_2.setTable( 'table_2')

        # the view 2 -- with a mistake
        self.view_2 = QTableView( )
        self.view_2.setModel( self.model_1  )
        self.view_2.hideColumn( 3 )
        self.view_2.setSelectionBehavior( QTableView.SelectRows )
        self.view_2.setSortingEnabled( False )

--------------

        # the model 1
        self.model_1 = QSqlTableModel( ... )
        self.model_1 = model

        model.setTable( 'table_1')

        # the view 1
        view = QTableView( )
        self.view_1  = view
        view.setModel( self.model_1  )
        view.hideColumn( 0 )
        view.setSelectionBehavior( QTableView.SelectRows )
        view.setSortingEnabled( True )

        # the model 2
        model = QSqlTableModel( ... )
        self.model_2 = model
        model.setTable( 'table_2')

        # the view 2 -- with a mistake corrected
        view = QTableView( )
        self.view_2 = view
        view.setModel( model  )
        view.hideColumn( 3 )
        view.setSelectionBehavior( QTableView.SelectRows )
        view.setSortingEnabled( False )
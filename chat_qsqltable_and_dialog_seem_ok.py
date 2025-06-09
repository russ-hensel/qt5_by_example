#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 13:07:09 2025

@author: russ
"""


# ---- tof

# ---- imports

# ---- end imports


#-------------------------------

import sys
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout,
                           QHBoxLayout, QDialog, QFormLayout, QLineEdit, QDateTimeEdit,
                           QSpinBox, QComboBox, QDialogButtonBox, QMessageBox, QWidget)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt, QDateTime


class StuffEventDialog(QDialog):
    """Dialog for adding or editing a record in the stuff_event table."""

    def __init__(self, parent=None, edit_data=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Event" if edit_data is None else "Edit Event")

        # Create form layout and fields
        form_layout = QFormLayout()

        # ID field
        self.id_edit = QLineEdit()
        self.id_edit.setMaxLength(15)
        form_layout.addRow("ID:", self.id_edit)

        # Stuff ID field
        self.stuff_id_edit = QLineEdit()
        self.stuff_id_edit.setMaxLength(15)
        form_layout.addRow("Stuff ID:", self.stuff_id_edit)

        # Event date/time field (stored as integer timestamp)
        self.event_date_edit = QDateTimeEdit(QDateTime.currentDateTime())
        form_layout.addRow("Event Date:", self.event_date_edit)

        # DLR field (integer)
        self.dlr_spinbox = QSpinBox()
        self.dlr_spinbox.setRange(0, 9999)
        form_layout.addRow("DLR:", self.dlr_spinbox)

        # Comment field
        self.comment_edit = QLineEdit()
        self.comment_edit.setMaxLength(150)
        form_layout.addRow("Comment:", self.comment_edit)

        # Type field
        self.type_combobox = QComboBox()
        # Add your event types here
        self.type_combobox.addItems(["Type1", "Type2", "Type3"])
        form_layout.addRow("Type:", self.type_combobox)

        # If we're editing, populate the fields with the existing data
        if edit_data is not None:
            self.id_edit.setText(edit_data["id"])
            self.stuff_id_edit.setText(edit_data["stuff_id"])

            # Convert timestamp to QDateTime
            dt = QDateTime()
            dt.setSecsSinceEpoch(edit_data["event_dt"])
            self.event_date_edit.setDateTime(dt)

            self.dlr_spinbox.setValue(edit_data["dlr"])
            self.comment_edit.setText(edit_data["cmnt"])

            # Find and set the index for the type
            index = self.type_combobox.findText(edit_data["type"])
            if index >= 0:
                self.type_combobox.setCurrentIndex(index)

        # Button box
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)

    def get_form_data(self):
        """Get the data from the form fields as a dictionary."""
        data = {
            "id": self.id_edit.text(),
            "stuff_id": self.stuff_id_edit.text(),
            "event_dt": int(self.event_date_edit.dateTime().toSecsSinceEpoch()),
            "dlr": self.dlr_spinbox.value(),
            "cmnt": self.comment_edit.text(),
            "type": self.type_combobox.currentText()
        }
        return data


class MainWindow(QMainWindow):
    """Main application window displaying the stuff_event table."""

    def __init__(self, database):
        super().__init__()
        self.database = database

        self.setWindowTitle("Stuff Events Manager")
        self.resize(800, 600)

        # Create the SQL table model
        self.model = QSqlTableModel(self, self.database)
        self.model.setTable("stuff_event")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()

        # Set up headers for better display
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Stuff ID")
        self.model.setHeaderData(2, Qt.Horizontal, "Event Date")
        self.model.setHeaderData(3, Qt.Horizontal, "DLR")
        self.model.setHeaderData(4, Qt.Horizontal, "Comment")
        self.model.setHeaderData(5, Qt.Horizontal, "Type")

        # Create table view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSortingEnabled(True)
        self.view.setSelectionBehavior(QTableView.SelectRows)  # Select entire rows
        self.view.setSelectionMode(QTableView.SingleSelection)  # Allow only single selection
        self.view.resizeColumnsToContents()

        # Add button for new records
        add_button = QPushButton("Add New Event")
        add_button.clicked.connect(self.add_new_event)

        # Edit button for selected record
        edit_button = QPushButton("Edit Selected")
        edit_button.clicked.connect(self.edit_selected_event)

        # Delete button for selected record
        delete_button = QPushButton("Delete Selected")
        delete_button.clicked.connect(self.delete_selected_event)

        # Submit changes button
        submit_button = QPushButton("Save Changes")
        submit_button.clicked.connect(self.submit_changes)

        # Revert changes button
        revert_button = QPushButton("Revert Changes")
        revert_button.clicked.connect(self.model.revertAll)

        # Layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(submit_button)
        button_layout.addWidget(revert_button)
        button_layout.addStretch()

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.view)
        main_layout.addLayout(button_layout)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def add_new_event(self):
        """Open dialog to add a new event and insert it into the model."""
        dialog      = StuffEventDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            form_data = dialog.get_form_data()

            # Create a new record
            row = self.model.rowCount()
            self.model.insertRow(row)

            # Set data for each field
            self.model.setData(self.model.index(row, 0), form_data["id"])
            self.model.setData(self.model.index(row, 1), form_data["stuff_id"])
            self.model.setData(self.model.index(row, 2), form_data["event_dt"])
            self.model.setData(self.model.index(row, 3), form_data["dlr"])
            self.model.setData(self.model.index(row, 4), form_data["cmnt"])
            self.model.setData(self.model.index(row, 5), form_data["type"])

    def get_selected_row_data(self):
        """Get the data from the currently selected row."""
        # Get the currently selected row
        indexes = self.view.selectedIndexes()
        if not indexes:
            QMessageBox.warning(self, "Warning", "No record selected.")
            return None

        # Get the model row index
        model_row = indexes[0].row()

        # Extract data from the row
        data = {
            "id": self.model.data(self.model.index(model_row, 0)),
            "stuff_id": self.model.data(self.model.index(model_row, 1)),
            "event_dt": self.model.data(self.model.index(model_row, 2)),
            "dlr": self.model.data(self.model.index(model_row, 3)),
            "cmnt": self.model.data(self.model.index(model_row, 4)),
            "type": self.model.data(self.model.index(model_row, 5))
        }

        return (model_row, data)

    def edit_selected_event(self):
        """Open dialog to edit the currently selected event."""
        selected_data = self.get_selected_row_data()
        if selected_data is None:
            return

        row, data = selected_data

        # Open dialog with the current data
        dialog = StuffEventDialog(self, edit_data=data)
        if dialog.exec_() == QDialog.Accepted:
            form_data = dialog.get_form_data()

            # Update the row with the new data
            self.model.setData(self.model.index(row, 0), form_data["id"])
            self.model.setData(self.model.index(row, 1), form_data["stuff_id"])
            self.model.setData(self.model.index(row, 2), form_data["event_dt"])
            self.model.setData(self.model.index(row, 3), form_data["dlr"])
            self.model.setData(self.model.index(row, 4), form_data["cmnt"])
            self.model.setData(self.model.index(row, 5), form_data["type"])

    def delete_selected_event(self):
        """Delete the currently selected event."""
        selected_data = self.get_selected_row_data()
        if selected_data is None:
            return

        row, data = selected_data

        # Confirm deletion with the user
        reply = QMessageBox.question(self, "Confirm Deletion",
                                    f"Are you sure you want to delete the selected event (ID: {data['id']})?",
                                    QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Remove the row from the model
            self.model.removeRow(row)

    def submit_changes(self):
        """Submit all changes to the database."""
        if self.model.submitAll():
            QMessageBox.information(self, "Success", "Changes saved to database successfully.")
        else:
            QMessageBox.warning(self, "Error",
                               f"Database error: {self.model.lastError().text()}")


def main():
    app = QApplication(sys.argv)

    # Set up the database connection
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("stuff_events.db")

    if not db.open():
        QMessageBox.critical(None, "Database Error",
                           f"Could not open database: {db.lastError().text()}")
        return -1

    # Create table if it doesn't exist
    query = QSqlQuery()
    query.exec_("""
    CREATE TABLE IF NOT EXISTS stuff_event (
        id VARCHAR(15),
        stuff_id VARCHAR(15),
        event_dt INTEGER,
        dlr INTEGER,
        cmnt VARCHAR(150),
        type VARCHAR(15)
    )
    """)

    window = MainWindow(db)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()






# ---- eof
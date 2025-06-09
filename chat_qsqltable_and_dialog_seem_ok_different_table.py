#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 13:40:18 2025

@author: russ
"""


# ---- tof

# ---- imports

# ---- end imports


#-------------------------------

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout,
                           QHBoxLayout, QDialog, QFormLayout, QLineEdit, QSpinBox,
                           QTextEdit, QDialogButtonBox, QMessageBox, QWidget)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt


class PersonDialog(QDialog):
    """Dialog for adding or editing a person record."""

    def __init__(self, parent=None, edit_data=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Person" if edit_data is None else "Edit Person")

        # Create form layout and fields
        form_layout = QFormLayout()

        # ID field (Only shown when editing)
        self.id_spinbox = QSpinBox()
        self.id_spinbox.setRange(1, 999999)
        if edit_data is not None:
            form_layout.addRow("ID:", self.id_spinbox)
            self.id_spinbox.setValue(edit_data["id"])
            self.id_spinbox.setReadOnly(True)  # ID shouldn't be changed

        # Name field
        self.name_edit = QLineEdit()
        self.name_edit.setMaxLength(150)
        form_layout.addRow("Name:", self.name_edit)

        # Age field
        self.age_edit = QLineEdit()
        self.age_edit.setMaxLength(150)
        form_layout.addRow("Age:", self.age_edit)

        # Family relation field
        self.family_relation_edit = QTextEdit()
        self.family_relation_edit.setAcceptRichText(False)
        form_layout.addRow("Family Relation:", self.family_relation_edit)

        # Additional Keywords field
        self.add_kw_edit = QLineEdit()
        self.add_kw_edit.setMaxLength(150)
        form_layout.addRow("Additional Keywords:", self.add_kw_edit)

        # If we're editing, populate the fields with the existing data
        if edit_data is not None:
            self.name_edit.setText(edit_data["name"])
            self.age_edit.setText(edit_data["age"])
            self.family_relation_edit.setPlainText(edit_data["family_relation"])
            self.add_kw_edit.setText(edit_data["add_kw"])

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
        self.setMinimumWidth(400)

    def get_form_data(self):
        """Get the data from the form fields as a dictionary."""
        data = {
            "name": self.name_edit.text(),
            "age": self.age_edit.text(),
            "family_relation": self.family_relation_edit.toPlainText(),
            "add_kw": self.add_kw_edit.text()
        }

        # Include ID if it exists (edit mode)
        if hasattr(self, 'id_spinbox') and self.id_spinbox.isVisible():
            data["id"] = self.id_spinbox.value()

        return data


class MainWindow(QMainWindow):
    """Main application window displaying the persons table."""

    def __init__(self, database):
        super().__init__()
        self.database = database

        self.setWindowTitle("Persons Manager")
        self.resize(900, 600)

        # Create the SQL table model
        self.model = QSqlTableModel(self, self.database)
        self.model.setTable("persons")
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        # Set up headers for better display
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Age")
        self.model.setHeaderData(3, Qt.Horizontal, "Family Relation")
        self.model.setHeaderData(4, Qt.Horizontal, "Additional Keywords")

        # Load data
        self.model.select()

        # Create table view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setSortingEnabled(True)
        self.view.setSelectionBehavior(QTableView.SelectRows)  # Select entire rows
        self.view.setSelectionMode(QTableView.SingleSelection)  # Allow only single selection
        self.view.resizeColumnsToContents()

        # Add button for new records
        add_button = QPushButton("Add Person")
        add_button.clicked.connect(self.add_new_person)

        # Edit button for selected record
        edit_button = QPushButton("Edit Selected")
        edit_button.clicked.connect(self.edit_selected_person)

        # Delete button for selected record
        delete_button = QPushButton("Delete Selected")
        delete_button.clicked.connect(self.delete_selected_person)

        # Submit changes button
        submit_button = QPushButton("Save All Changes")
        submit_button.clicked.connect(self.submit_changes)

        # Revert changes button
        revert_button = QPushButton("Revert All Changes")
        revert_button.clicked.connect(self.model.revertAll)

        # Refresh button
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.refresh_data)

        # Layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(submit_button)
        button_layout.addWidget(revert_button)
        button_layout.addWidget(refresh_button)
        button_layout.addStretch()

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.view)
        main_layout.addLayout(button_layout)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def add_new_person(self):
        """Open dialog to add a new person and insert it into the model."""
        dialog = PersonDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            form_data = dialog.get_form_data()

            # Create a new record
            row = self.model.rowCount()
            self.model.insertRow(row)

            # Set data for each field (except ID which is auto-incremented)
            self.model.setData(self.model.index(row, 1), form_data["name"])
            self.model.setData(self.model.index(row, 2), form_data["age"])
            self.model.setData(self.model.index(row, 3), form_data["family_relation"])
            self.model.setData(self.model.index(row, 4), form_data["add_kw"])

            # Submit the new record immediately to get the ID
            if self.model.submitAll():
                QMessageBox.information(self, "Success", "New person added successfully.")
                self.model.select()  # Refresh to show the new ID
            else:
                QMessageBox.warning(self, "Error",
                                   f"Database error: {self.model.lastError().text()}")

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
            "name": self.model.data(self.model.index(model_row, 1)),
            "age": self.model.data(self.model.index(model_row, 2)),
            "family_relation": self.model.data(self.model.index(model_row, 3)),
            "add_kw": self.model.data(self.model.index(model_row, 4))
        }

        return (model_row, data)

    def edit_selected_person(self):
        """Open dialog to edit the currently selected person."""
        selected_data = self.get_selected_row_data()
        if selected_data is None:
            return

        row, data = selected_data

        # Open dialog with the current data
        dialog = PersonDialog(self, edit_data=data)
        if dialog.exec_() == QDialog.Accepted:
            form_data = dialog.get_form_data()

            # Update the row with the new data
            self.model.setData(self.model.index(row, 1), form_data["name"])
            self.model.setData(self.model.index(row, 2), form_data["age"])
            self.model.setData(self.model.index(row, 3), form_data["family_relation"])
            self.model.setData(self.model.index(row, 4), form_data["add_kw"])

    def delete_selected_person(self):
        """Delete the currently selected person."""
        selected_data = self.get_selected_row_data()
        if selected_data is None:
            return

        row, data = selected_data

        # Confirm deletion with the user
        reply = QMessageBox.question(self, "Confirm Deletion",
                                    f"Are you sure you want to delete the selected person (ID: {data['id']}, Name: {data['name']})?",
                                    QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Remove the row from the model
            self.model.removeRow(row)

            # Apply the deletion immediately
            if self.model.submitAll():
                QMessageBox.information(self, "Success", "Person deleted successfully.")
            else:
                QMessageBox.warning(self, "Error",
                                   f"Database error: {self.model.lastError().text()}")
                self.model.select()  # Refresh the view

    def submit_changes(self):
        """Submit all changes to the database."""
        if self.model.submitAll():
            QMessageBox.information(self, "Success", "All changes saved to database successfully.")
        else:
            QMessageBox.warning(self, "Error",
                               f"Database error: {self.model.lastError().text()}")

    def refresh_data(self):
        """Refresh the data from the database."""
        self.model.select()


def main():
    app = QApplication(sys.argv)

    # Set up the database connection
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("persons.db")

    if not db.open():
        QMessageBox.critical(None, "Database Error",
                           f"Could not open database: {db.lastError().text()}")
        return -1

    # Create table if it doesn't exist
    query = QSqlQuery()
    query.exec_("""
    CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(150),
        age VARCHAR(150),
        family_relation TEXT,
        add_kw VARCHAR(150)
    )
    """)

    window = MainWindow(db)
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()




# ---- eof
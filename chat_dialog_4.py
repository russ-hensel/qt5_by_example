#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 16:41:44 2025

@author: chat
"""

import sys
import time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout,
    QWidget, QDialog, QTextEdit, QHBoxLayout
)
from PyQt5.QtCore import QThread, pyqtSignal


class CounterThread(QThread):
    update_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._running = True

    def run(self):
        self._running = True
        for ix in range(10):
            if not self._running:
                break
            self.update_signal.emit(str(ix))
            time.sleep(0.5)
        self.finished_signal.emit()

    def stop(self):
        self._running = False


class CounterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Counter Dialog")
        self.resize(300, 200)

        # Layout
        layout = QVBoxLayout(self)
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        button_layout = QHBoxLayout()
        self.stop_button = QPushButton("Stop", self)
        button_layout.addWidget(self.stop_button)
        layout.addLayout(button_layout)

        # Thread setup
        self.thread = CounterThread()
        self.thread.update_signal.connect(self.update_text)
        self.thread.finished_signal.connect(self.close)

        # Connect stop button
        self.stop_button.clicked.connect(self.stop_counter)

    def start_counter(self):
        self.text_area.clear()
        if not self.thread.isRunning():
            self.thread.start()

    def stop_counter(self):
        if self.thread.isRunning():
            self.thread.stop()

    def update_text(self, text):
        self.text_area.append(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(400, 200)

        # Central widget
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.open_dialog_button = QPushButton("Open Counter Dialog", self)
        layout.addWidget(self.open_dialog_button)

        self.setCentralWidget(central_widget)

        # Connect button
        self.open_dialog_button.clicked.connect(self.open_counter_dialog)

    def open_counter_dialog(self):
        dlg = CounterDialog(self)
        dlg.show()
        dlg.start_counter()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

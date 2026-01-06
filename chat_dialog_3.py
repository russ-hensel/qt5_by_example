#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 16:39:07 2025

@author: russ
"""

import sys
import time
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal


class CounterThread(QThread):
    update_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._running = True

    def run(self):
        self._running = True
        for ix in range(10):
            if not self._running:
                break
            self.update_signal.emit(str(ix))
            time.sleep(0.5)  # simulate work

    def stop(self):
        self._running = False


class CounterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Counter Dialog")
        self.resize(300, 200)

        layout = QVBoxLayout(self)
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        self.start_button = QPushButton("Start Counter", self)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Counter", self)
        layout.addWidget(self.stop_button)

        # Thread setup
        self.thread = CounterThread()
        self.thread.update_signal.connect(self.update_text)

        # Connect buttons
        self.start_button.clicked.connect(self.start_counter)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = CounterDialog()
    dlg.show()
    sys.exit(app.exec_())

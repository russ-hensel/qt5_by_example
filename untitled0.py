#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 13:47:03 2025

@author: russ
"""


# ---- tof

# ---- imports

# ---- end imports


#-------------------------------






# ---- eof


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        # Create a Figure and Canvas
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)

        # Create the navigation toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_example(self):
        # Clear the axes
        self.axes.clear()

        # Create a simple plot
        x = [0, 1, 2, 3, 4, 5]
        y = [0, 1, 4, 9, 16, 25]
        self.axes.plot(x, y, 'r-')
        self.axes.set_title('y = x²')
        self.axes.grid(True)

        # Refresh the canvas
        self.canvas.draw()

    def update_plot(self, new_x, new_y):
        self.axes.clear()
        self.axes.plot(new_x, new_y)
        self.canvas.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Matplotlib in PyQt5")
        self.setGeometry(100, 100, 800, 600)

        # Create the Matplotlib widget
        self.plot_widget = MatplotlibWidget()

        # Set as central widget
        self.setCentralWidget(self.plot_widget)

        # Plot an example
        self.plot_widget.plot_example()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

class MovingVerticalLineWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Create a pyqtgraph PlotWidget
        self.plot_widget = pg.PlotWidget(self)
        layout.addWidget(self.plot_widget)

        # Create a vertical line item
        self.vertical_line = pg.InfiniteLine(angle=90, movable=False, pen='r')
        self.plot_widget.addItem(self.vertical_line)

        self.setLayout(layout)

        # Set up a QTimer to update the line position
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_line_position)
        self.timer.start(50)  # Update every 50 milliseconds

        # Initialize line position
        self.line_position = 0

    def update_line_position(self):
        # Update the line position (you can replace this with your own logic)
        self.line_position += 0.1

        # Set the new position of the vertical line
        self.vertical_line.setValue(self.line_position)

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    moving_line_widget = MovingVerticalLineWidget()
    window.setCentralWidget(moving_line_widget)
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle('Moving Vertical Line Example')
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

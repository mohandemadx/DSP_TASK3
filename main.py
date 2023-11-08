# File: main.py
import sys
from os import path
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QFileDialog, QListWidgetItem, QVBoxLayout, QWidget


FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "design.ui"))

class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle("Signal Equalizer")

        
def main():
    app = QApplication(sys.argv)
    
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
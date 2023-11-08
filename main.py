# File: main.py
import sys
from os import path
from PyQt5.uic import loadUiType
import functions as f
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import wave
import classes as c

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "design.ui"))

class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)

        self.setupUi(self)
        self.setWindowTitle("Signal Equalizer")
        
        # Variables
        
        self.audio_data = None
        self.sliders_list = []
        self.indicators_list = []
        self.mapping_mode = { 
            0 : c.default,
            1 : c.ecg,
            2 : c.animals,
            3 : c.musical,
            }
        
        # Setting the Ui
        self.SliderFrame.setMaximumHeight(200)
        self.change_mode(self.mode_comboBox.currentIndex())
        
        # Signals
        self.importButton.clicked.connect(lambda: self.upload(self.musicfileName))
        self.mode_comboBox.currentIndexChanged.connect(lambda: self.change_mode(self.mode_comboBox.currentIndex()))
        
        
    # FUNCTIONS
    
    def upload(self, label):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        filters = "WAV Files (*.wav)"
        file_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileNames()", "", filters, options=options)

        if file_path:
            # Store file name
            file_name = file_path.split('/')[-1]
            label.setText(file_name)
            
            # Open the .wav file for reading
            with wave.open(file_path, 'rb') as audio_file:
                # Get the audio file's parameters
                num_frames = audio_file.getnframes()
                
                # Read audio data as bytes
                self.audio_data = audio_file.readframes(num_frames)
            
    def change_mode(self, index):
        mode = self.mapping_mode[index]
        
        if index == 0:
            self.sliders_list, self.indicators_list = f.create_sliders(mode.num_sliders, mode.labels, self.SliderFrame)
            
        elif index == 1:
            self.sliders_list, self.indicators_list = f.create_sliders(mode.num_sliders, mode.labels, self.SliderFrame)
            
        elif index == 2:
            self.sliders_list, self.indicators_list = f.create_sliders(mode.num_sliders, mode.labels, self.SliderFrame)
            
        elif index == 3:
            self.sliders_list, self.indicators_list = f.create_sliders(mode.num_sliders, mode.labels, self.SliderFrame)
        
        # Refresh Sliders
        self.sliders_refresh()
        
    def sliders_refresh(self):
        for i, slider in enumerate(self.sliders_list):
            slider = self.sliders_list[i]
            slider.valueChanged.connect(self.update_indicators)    

    def update_indicators(self):
        if self.sliders_list:
            print('lol')
            for i, slider in enumerate(self.sliders_list):
                self.indicators_list[i].setText(f"{slider.value()*2-10}")  
        
   
def main():
    app = QApplication(sys.argv)
    
    # with open("style.qss", "r") as f:
    #     _style = f.read()
    #     app.setStyleSheet(_style)

    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
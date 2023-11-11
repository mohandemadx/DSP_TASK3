# File: main.py
import sys
from os import path
from PyQt5.uic import loadUiType
import functions as f
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import wave
import classes as c
from PyQt5 import QtCore


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
        self.window_sliders = []
        self.window_indicators = []
        self.mapping_mode = { 
            0 : c.default,
            1 : c.ecg,
            2 : c.animals,
            3 : c.musical,
            }
        self.window_map = { 
            0 : c.hamming,
            1 : c.hanning,
            2 : c.gaussian,
            }
        
        # Timers
        self.timer = QtCore.QTimer()
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        
        # Setting the Ui        
        self.SliderFrame.setMaximumHeight(200)
        self.change_mode(self.mode_comboBox.currentIndex())
        self.smoothing_window_type(self.window_comboBox.currentIndex())
        
        # Signals
        self.importButton.clicked.connect(lambda: self.upload(self.musicfileName))
        self.mode_comboBox.currentIndexChanged.connect(lambda: self.change_mode(self.mode_comboBox.currentIndex()))
        self.window_comboBox.currentIndexChanged.connect(lambda: self.smoothing_window_type(self.window_comboBox.currentIndex()))
        self.playallButton.clicked.connect(lambda: f.play_n_pause(self.playallButton, self.timer))
        self.playButton1.clicked.connect(lambda: f.play_n_pause(self.playButton1, self.timer1))
        self.playButton2.clicked.connect(lambda: f.play_n_pause(self.playButton2, self.timer2))
        self.speedSlider.valueChanged.connect(lambda: f.speed(self.speedSlider.value(), self.speedLabel))
    
    
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
        sliders_list, indicators_list = f.create_sliders(mode.num_sliders, mode.labels, self.SliderFrame, 2)
        if index==0:
            f.synthesize_signal(self.InputGraph)
        else:
            self.InputGraph.clear()
        # Refresh Sliders
        self.sliders_refresh(sliders_list, indicators_list)
        
    def sliders_refresh(self, sliders, indicators):
        if sliders:
            for slider in sliders:
                slider.valueChanged.connect(lambda: self.update_indicators(sliders, indicators))    

    def update_indicators(self, sliders, indicators):
        if sliders:
            for i, slider in enumerate(sliders):
                indicators[i].setText(f"{slider.value()*2-10}")
    
    def smoothing_window_type(self, index):
        window = self.window_map[index]
        
        self.window_sliders, self.window_indicators = f.create_sliders(window.num_sliders, window.labels, self.WindowFrame, 1)
        
        # Refresh Sliders
        self.sliders_refresh(self.window_sliders, self.window_indicators)
            
        
        
   
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
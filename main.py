# File: main.py
from collections import namedtuple
import sys
from os import path
from PyQt5.uic import loadUiType
import functions as f
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import wave
import classes as c
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "design.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)


        self.setupUi(self)
        self.setWindowTitle("Signal Equalizer")
        
        # Objects
        self.hamming = c.WindowType(['N'], 1)
        self.hanning = c.WindowType(['N'], 1)
        self.gaussian = c.WindowType(['Std'], 1)
        self.rectangle = c.WindowType(['constant'], 1)

        r = namedtuple('Range', ['min', 'max'])
        self.default = c.Mode([f'{i} to {i + 1} KHz' for i in range(10)],
                              [r(i * 1000 + 1, (i + 1) * 1000) for i in range(10)], 10)
        self.ecg = c.Mode(['A1', 'A2', 'A3'], [1 for _ in range(3)], 3)
        self.animals = c.Mode(['Duck', 'Dog', 'Monkey', 'Owl'], [1 for _ in range(4)], 4)
        self.musical = c.Mode(['Drums', 'Trumpet', 'Flute', 'Piano'], [1 for _ in range(4)], 4)

        # Variables
        
        self.index = 0
        self.audio_data = []
        self.sample_rate=44100
        self.sliders_list = []
        self.indicators_list = []
        self.window_sliders = []
        self.window_indicators = []
        self.mapping_mode = {
            0: self.default,
            1: self.ecg,
            2: self.animals,
            3: self.musical,
        }
        self.window_map = {
            0: self.hamming,
            1: self.hanning,
            2: self.gaussian,
            3: self.rectangle,
        }

        # Timers
        self.timer = QtCore.QTimer()
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer.timeout.connect(self.update_waveform)
        # self.timer1.timeout.connect(self.timer_timeout)
        # self.timer2.timeout.connect(self.timer_timeout)

        # Audio Players
        self.media_playerIN = QMediaPlayer()
        self.media_playerOUT = QMediaPlayer()

        # Setting the Ui
        self.SliderFrame.setMaximumHeight(200)
        self.change_mode(self.mode_comboBox.currentIndex())
        self.smoothing_window_type(self.window_comboBox.currentIndex())
        self.InputGraph.setBackground('w')
        self.OutputGraph.setBackground('w')
        self.freqGraph.setBackground('w')


        # Signals
        self.importButton.clicked.connect(lambda: self.upload(self.musicfileName))
        self.mode_comboBox.currentIndexChanged.connect(lambda: self.change_mode(self.mode_comboBox.currentIndex()))
        self.window_comboBox.currentIndexChanged.connect(
            lambda: self.smoothing_window_type(self.window_comboBox.currentIndex()))
        self.playallButton.clicked.connect(lambda: f.play_n_pause(self.playallButton, self.timer, False, _))
        self.playButton1.clicked.connect(lambda: f.play_n_pause(self.playButton1, self.timer1, True, self.media_playerIN))
        self.playButton2.clicked.connect(lambda: f.play_n_pause(self.playButton2, self.timer2, True, self.media_playerOUT))
        self.speedSlider.valueChanged.connect(lambda: f.speed(self.speedSlider.value(), self.speedLabel, self.timer))
        self.resetButton.clicked.connect(self.reset)
        self.showCheckBox.stateChanged.connect(lambda: f.plot_specto(self.audio_data, self.sample_rate, self.spectoframe1, self.showCheckBox))
        self.window_comboBox.currentIndexChanged.connect(lambda:f.get_smoothing_window(self.window_comboBox.currentIndex(),self.freqGraph,self.output_amplitudes,self.frequency_comp,1))
        
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
            if self.media_playerIN.state() == QMediaPlayer.StoppedState:
                    self.media_playerIN.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))

            # Open the .wav file for reading
            with wave.open(file_path, 'rb') as audio_file:
                # Get the audio file's parameters
                num_frames = audio_file.getnframes()
                
                # Read audio data as bytes
                raw_audio_data = audio_file.readframes(num_frames)

                # Convert raw bytes to numerical values (assuming 16-bit PCM)
                self.audio_data = np.frombuffer(raw_audio_data, dtype=np.int16)

                sample_width = audio_file.getsampwidth()
                self.sample_rate = audio_file.getframerate()
                self.time = np.arange(0, len(self.audio_data)) / self.sample_rate

                # Enabling the UI
                self.playallButton.setEnabled(True)
                self.resetButton.setEnabled(True)
                self.zoomOutButton.setEnabled(True)
                self.zoomInButton.setEnabled(True)
                self.speedSlider.setEnabled(True)
                self.showCheckBox.setEnabled(True)
                
                if self.showCheckBox.isChecked():
                    f.plot_specto(self.audio_data, self.sample_rate, self.spectoframe1)


                # Update the signal
                self.update_signal(self.mode_comboBox.currentIndex())
                f.update_plotting(self.frequency_comp, self.output_amplitudes, self.freqGraph)
    
    
    def reset(self):
        if self.timer.isActive():
            f.play_n_pause(self.playallButton, self.timer)
            self.InputGraph.clear()
            self.index = 0
        else:
            self.InputGraph.clear()
            self.index = 0
        
    def update_waveform(self):
        x_min = self.index
        x_max = min(len(self.time), self.index + 10)
        
        # self.InputGraph.setXRange(x_min, x_max)
        
        plot_item = self.InputGraph.plot(pen='b')
        plot_item.setData(self.time[x_min:x_max], self.audio_data[x_min:x_max])

        if self.index >= len(self.time):
            self.index = 0    
        self.index += 1
        
           


                

    def change_mode(self, index):
        mode = self.mapping_mode[index]
        self.sliders_list, indicators_list = f.create_sliders(mode.num_sliders, mode.labels, self.SliderFrame, 2)
        self.sliders_refresh(self.sliders_list, indicators_list)
        self.update_signal(index)
        self.connect_slider_signals()

    def update_signal(self, index):
        if index == 0:
            self.signal = f.synthesize_signal()
            Ts = 1/1000

        else:
            self.signal = self.audio_data
            Ts=1/self.sample_rate


        if len(self.signal):
            self.amplitudes, self.frequency_comp, self.phases = f.compute_fourier_transform(self.signal, Ts)
            self.output_amplitudes = self.amplitudes.copy()

    def sliders_refresh(self, sliders, indicators):
        if sliders:
            for slider in sliders:
               slider.valueChanged.connect(lambda: self.update_indicators(sliders, indicators))
               # slider.valueChanged.connect(lambda: self.modifying_amplitudes(self.sliders_list.index(slider), slider.value() * 2 - 10, self.amplitudes, self.output_amplitudes))

    def update_indicators(self, sliders, indicators):
        if sliders:
            for i, slider in enumerate(sliders):
                indicators[i].setText(f"{slider.value() * 2 - 10}")

    def smoothing_window_type(self, index):
        window = self.window_map[index]

        self.window_sliders, self.window_indicators = f.create_sliders(window.num_sliders, window.labels,
                                                                       self.WindowFrame, 1)

        # Refresh Sliders
        self.sliders_refresh(self.window_sliders, self.window_indicators)
        for slider in self.window_sliders: slider.valueChanged.connect(lambda:f.get_smoothing_window_parameters(slider.value(),self.window_comboBox.currentIndex(),self.freqGraph,self.output_amplitudes,self.frequency_comp))

    def connect_slider_signals(self):
        for slider in self.sliders_list:slider.valueChanged.connect(lambda value, slider=slider: self.modifying_amplitudes(self.sliders_list.index(slider),slider.value() * 2 - 10, self.amplitudes,self.output_amplitudes))

    def modifying_amplitudes(self, freq_component_index, gain, input_amplitudes, output_amplitudes):
        # Frequency Ranges Mapping
        animals_mode = {0: [1000, 7000], 1: [7000,20000], 2: [500, 2000], 3: [2000, 5000]}
        music_mode = {0: [30, 150], 1: [349, 1400], 2: [262, 2500], 3: [27.5, 4180]}
        ecg_mode = {0: [1, 5], 1: [2, 10], 2: [10, 20]}
        default_mode = {key: key + 1 for key in range(10)}

        mode_index = self.mode_comboBox.currentIndex()

        if mode_index == 0:
            output_amplitudes[default_mode[freq_component_index]] = gain * input_amplitudes[
                default_mode[freq_component_index]]
        elif mode_index == 1:
            start, end = ecg_mode[freq_component_index]
            output_amplitudes[start:end] = gain * input_amplitudes[start:end]
        elif mode_index == 2:
            start, end = animals_mode[freq_component_index]
            output_amplitudes[start:end] = gain * input_amplitudes[start:end]
        elif mode_index == 3:
            start, end = music_mode[freq_component_index]
            output_amplitudes[start:end] = gain * input_amplitudes[start:end]
       # f.apply_smoothing_window(output_amplitudes,f.get_smoothing_window_parameters,f.get_smoothing_window)
       #  f.update_plotting(self.frequency_comp,output_amplitudes,self.freqGraph)
        f.plot_smoothing_window(0,self.freqGraph,output_amplitudes,self.frequency_comp,1)


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
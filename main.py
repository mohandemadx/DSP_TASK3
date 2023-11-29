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
import pyqtgraph as pg

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "design.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)


        self.setupUi(self)
        self.setWindowTitle("Signal Equalizer")

        # Objects
        self.hamming = c.WindowType(['α'], 1)
        self.hanning = c.WindowType(['α'], 1)
        self.gaussian = c.WindowType(['Mean', 'Std'], 2)
        self.rectangle = c.WindowType(['constant'], 1)

        r = namedtuple('Range', ['min', 'max'])
        self.default = c.Mode([f'{i} to {i + 1} KHz' for i in range(10)],
                              [r(i * 1000 + 1, (i + 1) * 1000) for i in range(10)], 10)
        self.ecg = c.Mode(['A1', 'A2', 'A3'], [1 for _ in range(3)], 3)
        self.animals = c.Mode(['Duck', 'Dog', 'Monkey', 'Owl'], [1 for _ in range(4)], 4)
        self.musical = c.Mode(['Drums', 'Trumpet', 'Flute', 'Piano'], [1 for _ in range(4)], 4)

        # Variables
        self.line_position = 0
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
        self.timer.timeout.connect(lambda: f.time_tracker(self.vertical_line1, self.line_position))
        self.timer.timeout.connect(lambda: f.time_tracker(self.vertical_line2, self.line_position))
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
        self.SpectoGraph1.setBackground('w')
        self.SpectoGraph2.setBackground('w')
        self.freqGraph.setBackground('w')

        self.vertical_line1 = pg.PlotCurveItem(pen='r')
        self.vertical_line2 = pg.PlotCurveItem(pen='r')
        self.InputGraph.addItem(self.vertical_line1)
        self.OutputGraph.addItem(self.vertical_line2)

        x_data = [0, 0]
        y_data = [-20000, 20000]  # You can adjust the y values based on your plot's range

        self.vertical_line1.setData(x=x_data, y=y_data)
        self.vertical_line2.setData(x=x_data, y=y_data)

        # Signals
        self.importButton.clicked.connect(lambda: self.upload(self.musicfileName))
        self.mode_comboBox.currentIndexChanged.connect(lambda: self.change_mode(self.mode_comboBox.currentIndex()))
        self.window_comboBox.currentIndexChanged.connect(
            lambda: self.smoothing_window_type(self.window_comboBox.currentIndex()))
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
                raw_audio_data = audio_file.readframes(num_frames)

                # Convert raw bytes to numerical values (assuming 16-bit PCM)
                self.audio_data = np.frombuffer(raw_audio_data, dtype=np.int16)

                sample_width = audio_file.getsampwidth()
                sample_rate = audio_file.getframerate()
                self.sample_rate = audio_file.getframerate()


                f.plot_waveform(self.audio_data, self.sample_rate, self.InputGraph)
                f.plot_specto(self.audio_data, self.sample_rate, self.spectoframe1)
                f.plot_waveform(self.audio_data, self.sample_rate, self.OutputGraph)
                f.plot_specto(self.audio_data, self.sample_rate, self.spectoframe2)


                # Update the signal
                self.update_signal()
                f.update_plotting(self.frequency_comp, self.output_amplitudes, self.freqGraph)

    def change_mode(self, index):
        mode = self.mapping_mode[index]
        self.sliders_list, indicators_list = f.create_sliders(mode.num_sliders, mode.labels, self.SliderFrame, 2)
        self.sliders_refresh(self.sliders_list, indicators_list)
        self.update_signal()
        self.connect_slider_signals()

    def update_signal(self):
        if self.mode_comboBox.currentIndex() == 0:
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

    def connect_slider_signals(self):
        for slider in self.sliders_list:
            slider.valueChanged.connect(
                lambda value, slider=slider: self.modifying_amplitudes(self.sliders_list.index(slider),
                                                                       slider.value() * 2 - 10, self.amplitudes,
                                                                       self.output_amplitudes))

    def modifying_amplitudes(self, freq_component_index, gain, input_amplitudes, output_amplitudes):
        # Frequency Ranges Mapping
        animals_mode = {0: [1000, 7000], 1: [7000,44100], 2: [500, 2000], 3: [2000, 5000]}
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
        #f.apply_smoothing_window(output_amplitudes,f.get_smoothing_window_parameters)
        f.update_plotting(self.frequency_comp,output_amplitudes,self.freqGraph)


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
import sys
import numpy as np
import wave
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
import pyqtgraph as pg
import sounddevice as sd

class WaveformPlot(QWidget):
    def __init__(self, parent=None):
        super(WaveformPlot, self).__init__(parent)

        self.plot_widget = pg.PlotWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.plot_widget)

        self.setLayout(self.layout)

    def plot_waveform(self, data, sample_rate):
        time = np.arange(0, len(data)) / sample_rate
        self.plot_widget.plot(time, data, pen='b')
        self.plot_widget.setLabel('left', 'Amplitude')
        self.plot_widget.setLabel('bottom', 'Time (s)')
        self.plot_widget.showGrid(x=True, y=True)

class SoundPlayer(QThread):
    finished = pyqtSignal()

    def __init__(self, data, sample_rate, parent=None):
        super(SoundPlayer, self).__init__(parent)
        self.data = data
        self.sample_rate = sample_rate

    def run(self):
        import sounddevice as sd  # Make sure to install sounddevice using `pip install sounddevice`
        sd.play(self.data, self.sample_rate)
        sd.wait()
        self.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Waveform Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = WaveformPlot(self)
        self.setCentralWidget(self.central_widget)

        self.open_button = QPushButton('Open .wav file', self)
        self.play_button = QPushButton('Play', self)
        self.play_button.setEnabled(False)

        self.open_button.clicked.connect(self.load_wav_file)
        self.play_button.clicked.connect(self.play_sound)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.open_button)
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.central_widget)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        self.sound_data = None
        self.sample_rate = None
        self.player_thread = None

    def load_wav_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open .wav file", "", "Waveform Audio File (*.wav);;All Files (*)", options=options)

        if file_name:
            self.sound_data, self.sample_rate = self.read_wav_file(file_name)
            self.display_waveform()

    def read_wav_file(self, file_name):
        with wave.open(file_name, 'rb') as wav_file:
            sample_width = wav_file.getsampwidth()
            sample_rate = wav_file.getframerate()
            num_frames = wav_file.getnframes()

            raw_data = wav_file.readframes(num_frames)
            audio_data = np.frombuffer(raw_data, dtype=np.int16)

            return audio_data, sample_rate

    def display_waveform(self):
        self.central_widget.plot_widget.clear()
        self.central_widget.plot_waveform(self.sound_data, self.sample_rate)
        self.play_button.setEnabled(True)

    def play_sound(self):
        if self.sound_data is not None and self.sample_rate is not None:
            self.player_thread = SoundPlayer(self.sound_data, self.sample_rate)
            self.player_thread.finished.connect(self.playback_finished)
            self.play_button.setEnabled(False)
            self.player_thread.start()

    def playback_finished(self):
        self.play_button.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QPushButton, QFileDialog, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from scipy.io import wavfile

class SpectrogramWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        # Create a QFrame to hold the matplotlib plot
        self.frame = QFrame(self.central_widget)
        layout.addWidget(self.frame)

        # Create a matplotlib FigureCanvas
        self.canvas = FigureCanvas(plt.Figure())
        self.frame_layout = QVBoxLayout(self.frame)
        self.frame_layout.addWidget(self.canvas)

        # Create a button to load a .wav file
        self.load_button = QPushButton('Load .wav File', self.central_widget)
        self.load_button.clicked.connect(self.load_wav_file)
        layout.addWidget(self.load_button)

        self.central_widget.setLayout(layout)

    def load_wav_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("WAV files (*.wav)")
        file_dialog.setDefaultSuffix("wav")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.plot_spectrogram(file_path)

    def plot_spectrogram(self, file_path):
        # Read the .wav file
        sample_rate, data = wavfile.read(file_path)

        # Plot the spectrogram
        plt.figure()
        plt.specgram(data, Fs=sample_rate, cmap='viridis', aspect='auto')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.title('Spectrogram')
        self.canvas.figure.clear()
        self.canvas.figure = plt.gcf()
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = SpectrogramWidget()
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle('Spectrogram Viewer')
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

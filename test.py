import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create a media player instance
        self.media_player = QMediaPlayer()

        # Set up the UI
        play_button = QPushButton('Play', self)
        play_button.clicked.connect(self.play_audio)

        pause_button = QPushButton('Pause', self)
        pause_button.clicked.connect(self.pause_audio)

        file_button = QPushButton('Select File', self)
        file_button.clicked.connect(self.select_file)

        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Audio Player')

        play_button.move(50, 50)
        pause_button.move(150, 50)
        file_button.move(250, 50)

    def play_audio(self):
        # Load a sound file
        if hasattr(self, 'file_path'):
            media_content = QMediaContent(QMediaContent, self.file_path)
            self.media_player.setMedia(media_content)
            self.media_player.play()

    def pause_audio(self):
        # Pause the audio
        self.media_player.pause()

    def select_file(self):
        # Open a file dialog to select a .wav file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select .wav file", "", "WAV Files (*.wav);;All Files (*)", options=options)
        
        if file_name:
            self.file_path = file_name

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = AudioPlayer()
    player.show()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from scipy.signal import *



# FUNCTIONS
def create_sliders(sliders_number, labels_list, frame, alignment):
    clear(frame)
    sliders_list = []
    indicators = []

    layout = frame.layout()
    for i in range(sliders_number):

        # create sliders and store them
        slider = QSlider()

        # Vertical Sliders
        if alignment == 1:
            slider.setRange(0, 10)
            slider.setValue(5)

            # creating labels
            label = QLabel(labels_list[i])
            label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

            # creating value indicators
            indicator = QLabel('0')
            indicator.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # Horizontal Sliders
        else:
            slider.setRange(0, 10)
            slider.setValue(5)

            # creating labels
            label = QLabel(labels_list[i])
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            # creating value indicators
            indicator = QLabel('0')
            indicator.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

        slider.setOrientation(alignment)

        layout.addWidget(label)
        layout.addWidget(slider)
        layout.addWidget(indicator)

        sliders_list.append(slider)
        indicators.append(indicator)

    frame.setLayout(layout)
    return sliders_list, indicators


def clear(frame):
    layout = frame.layout()
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


def play_n_pause(button, timer, sound, player):
    if (timer.isActive()):
        icon = QIcon("icons/play.png")  # Use the resource path
        button.setIcon(icon)
        timer.stop()
        if sound:
            pause_audio(player)
    else:
        icon = QIcon("icons/pause.png")  # Use the resource path
        button.setIcon(icon)
        timer.start(100)
        if sound:
            play_audio(player)

def speed(slider_value, speed_label, timer):
    map_speed_factor = {
        1: 0.2,
        2: 0.5,
        3: 1.0,
        4: 1.5,
        5: 2.0,
    }
    speed_factor = map_speed_factor[slider_value]
    speed_label.setText(f'x {speed_factor}')
    time_interval = int(100 / speed_factor ) # ms
    
    update_speed(timer, time_interval)
    
def update_speed(timer, time_interval):
    timer.stop()
    timer.start(time_interval)
    
def synthesize_signal():
    fs = 1000
    T = 1 / fs
    t = np.arange(0, 1, T)

    num_components = 10

    # Frequencies of the components in the range 1 to 10 Hz
    frequencies = np.linspace(1, 10, num_components)

    # Amplitudes of the components (set to 1 for each component)
    amplitudes = np.ones(num_components)

    # Synthesize the signal in the time domain
    signal_time_domain = np.zeros_like(t)
    for i in range(num_components):
        signal_time_domain += amplitudes[i] * np.sin(2 * np.pi * frequencies[i] * t)

    return signal_time_domain


def compute_fourier_transform(signal, Ts):
    fourier_transform = np.fft.rfft(signal)
    frequencies_fft = np.fft.rfftfreq(len(signal), Ts)
    amplitudes = np.abs(fourier_transform)/(len(signal) /2)
    phases = np.angle(fourier_transform)
    return amplitudes, frequencies_fft, phases

def apply_smoothing_window(output_amplitudes, index, parameter):
        window_length = parameter*len(output_amplitudes)
        if index == 0:  # Hamming
            alpha = 0.54
            n = np.arange(window_length)
            smoothing_window = alpha - (1 - alpha) * np.cos(2 * np.pi * n / (window_length - 1))
            return output_amplitudes[0:int(window_length)+1]* smoothing_window
        elif index == 1:  # Hanning
            n = np.arange(window_length)
            smoothing_window = 0.5 * (1 - np.cos(2 * np.pi * n / (window_length - 1)))
            return output_amplitudes[0:int(window_length)+1]* smoothing_window
        elif index == 2:  # gaussian
            # sigma = ?
            x = np.linspace(-1, 1, int(window_length))
            smoothing_window = np.exp(-(x ** 2) / (2 * parameter ** 2))
            return output_amplitudes[0:int(window_length)]* smoothing_window

        elif index == 3:  # rectangle
            smoothing_window = np.ones(int(window_length))
            # smoothing_window = np.ones(window_length) * scaling_factor  # (scaling factor law msh ayzaha 1)
            return output_amplitudes[0:int(window_length)] * smoothing_window



def update_plotting(freq_comp,output_amplitudes,plot_widget):
    plot_widget.clear()
    plot_widget.plot(freq_comp, output_amplitudes,pen="b")
    plot_widget.setLabel('left', 'Amplitude')
    plot_widget.setLabel('bottom', 'Frequency (Hz)')


def get_smoothing_window(window_index,plot_widget,output_amp,freq_comp,parameter):
    plot_smoothing_window(window_index,plot_widget,output_amp,freq_comp,parameter)



def plot_smoothing_window(window_index,plot_widget,output_amp,freq_comp,parameter):
    N = len(output_amp)
    window_length=parameter*N
    std=parameter
    scale=max(output_amp)
    n = np.arange(0, window_length)

    # Hamming
    if window_index==0:
       window =scale*( 0.54 - 0.46 * np.cos(2 * np.pi * n / (window_length- 1)))

    # Hanning
    elif window_index==1:
        window =scale*( 0.5 * (1 - np.cos(2 * np.pi * n / (window_length - 1))))

    #Gaussian
    elif window_index==2:
        x = np.linspace(-1, 1, N)
        window=scale*( np.exp(-(x ** 2) / (2 * parameter ** 2)))


    #Rectangular
    elif window_index==3:
         window=scale*np.ones(int(window_length))
    plot_widget.clear()
    update_plotting(freq_comp,output_amp,plot_widget)
    apply_smoothing_window(output_amp,window_index,parameter)
    plot_widget.plot(window,pen='r',fillLevel=0, fillBrush=(255, 0, 0, 100) )

def get_smoothing_window_parameters(value,window_index,plot_widget,output_amp,freq_comp):
    new_value = (value / 10) * 0.9 + 0.1
    plot_smoothing_window(window_index,plot_widget,output_amp,freq_comp,new_value)

def compute_inverse_fourier_transform():
    new_fft_result = new_amplitudes * np.exp(1j * phases)
    inverse_fft = np.fft.irfft(new_fft_result)
    return inverse_fft


def play_audio(player):
    player.play()
    
def pause_audio(player):
    player.pause()
    
def plot_specto(data, sample_rate, frame, checkbox):
    clear(frame)
    if checkbox.isChecked():
        canvas = FigureCanvas(plt.Figure())
        layout = frame.layout()
        layout.addWidget(canvas)

        # Plot the spectrogram
        plt.figure()
        plt.specgram(data, Fs=sample_rate, cmap='viridis', aspect='auto')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.title('Spectrogram')
        canvas.figure.clear()
        canvas.figure = plt.gcf()
        canvas.draw()
    else:
        return


        
    
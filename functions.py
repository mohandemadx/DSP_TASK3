from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.signal
from scipy.signal import windows,gaussian,hann

# FUNCTIONS
def create_sliders(sliders_number, labels_list, frame, alignment):
    clear(frame)
    sliders_list = []
    indicators = []

    layout = frame.layout()
    for i in range(sliders_number):

        # create sliders and store them
        slider = QSlider()
        slider.setRange(0, 10)
        slider.setValue(1)

        # Vertical Sliders
        if alignment == 1:
            # creating labels
            label = QLabel(labels_list[i])
            label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

            # creating value indicators
            indicator = QLabel('1')
            indicator.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # Horizontal Sliders
        else:
            # creating labels
            label = QLabel(labels_list[i])
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            # creating value indicators
            indicator = QLabel('1')
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


def play_n_pause(button, timer_input, sound, player):
    if timer_input.isActive():
        icon = QIcon("icons/play.png")  # Use the resource path
        button.setIcon(icon)
        timer_input.stop()

        if sound:
            pause_audio(player)
    else:
        icon = QIcon("icons/pause.png")  # Use the resource path
        button.setIcon(icon)
        timer_input.start(100)

        if sound:
            play_audio(player)


def speed(slider_value, speed_label, timer, button):
    map_speed_factor = {
        1: 0.2,
        2: 0.5,
        3: 1.0,
        4: 1.5,
        5: 2.0,
    }
    icon = QIcon("icons/pause.png")  # Use the resource path
    button.setIcon(icon)
    speed_factor = map_speed_factor[slider_value]
    speed_label.setText(f'x {speed_factor}')
    time_interval = int(100 / speed_factor) # ms
    
    update_speed(timer, time_interval)
    
def update_speed(timer, time_interval):
    timer.stop()
    timer.start(time_interval)


def compute_fourier_transform(signal, Ts):
    fourier_transform = np.fft.rfft(signal)
    frequencies_fft = np.fft.rfftfreq(len(signal), Ts)
    amplitudes = np.abs(fourier_transform)
    phases = np.angle(fourier_transform)
    return amplitudes, frequencies_fft, phases

# def apply_smoothing_window(output_amplitudes, index, parameter):
#
#         window_length = parameter*len(output_amplitudes)
#
#         if index == 0:  # Hamming
#             alpha = 0.54
#             n = np.arange(window_length)
#             smoothing_window = alpha - (1 - alpha) * np.cos(2 * np.pi * n / (window_length - 1))
#             smoothed_signal= output_amplitudes[0:int(window_length)+1]* smoothing_window
#             return smoothed_signal
#         elif index == 1:  # Hanning
#             n = np.arange(window_length)
#             smoothing_window = 0.5 * (1 - np.cos(2 * np.pi * n / (window_length - 1)))
#             smoothed_signal = output_amplitudes[0:int(window_length)+1]* smoothing_window
#             return smoothed_signal
#         elif index == 2:  # gaussian
#
#             x = np.linspace(-1, 1, int(window_length))
#             smoothing_window = np.exp(-(x ** 2) / (2 * parameter ** 2))
#             smoothed_signal = output_amplitudes[0:int(window_length)]* smoothing_window
#             return smoothed_signal
#
#         elif index == 3:  # rectangle
#             smoothing_window = np.ones(int(window_length))
#             smoothed_signal = output_amplitudes[0:int(window_length)] * smoothing_window
#             return smoothed_signal


def apply_smoothing_window(output_amplitudes, index,parameter):

        window_length = len(output_amplitudes)
        std=parameter
        if index == 0:  # Hamming
            window = scipy.signal.windows.hamming(window_length)
            smoothed_signal = window*output_amplitudes
            return smoothed_signal
        elif index == 1:  # Hanning
            window = scipy.signal.windows.hann(window_length)
            smoothed_signal = window * output_amplitudes
            return smoothed_signal
        elif index == 2:# gaussian
            window = scipy.signal.windows.gaussian(window_length, std*window_length)
            smoothed_signal = window * output_amplitudes
            return smoothed_signal
        elif index == 3:  # rectangle
            window = scipy.signal.windows.boxcar(window_length)
            smoothed_signal = window * output_amplitudes
            return smoothed_signal

# def apply_windowing(self, range, index, parameter):
#         # window = scipy.signal.windows.boxcar(len(signal))
#         # windowed_signal = signal * window
#         # return windowed_signal
#         if index == 3:
#             window = scipy.signal.windows.boxcar(range)
#         elif index == 0:
#             window = scipy.signal.windows.hamming(range)
#         elif index == 1:
#             window = scipy.signal.windows.hann(range)
#         elif index == 2:
#             window = scipy.signal.windows.gaussian(range, std=0.1)
#
#         windowed_signal = window * slider_value
#
#         return windowed_signal


def freq_domain_plotting(freq_comp,output_amplitudes,plot_widget):
    plot_widget.clear()
    plot_widget.plot(freq_comp, output_amplitudes,pen="b")
    plot_widget.setLabel('left', 'Amplitude')
    plot_widget.setLabel('bottom', 'Frequency (Hz)')





def plot_smoothing_window(window_index,plot_widget,output_amp,freq_comp,start,end,parameter):

    N = len(output_amp[start:end])
    window_length=N
    std=parameter
    scale=max(output_amp)


    # Hamming
    if window_index==0:
        window_type='hamming'
        hamming_window = windows.get_window(window_type, window_length)
        frequency_domain_window = np.zeros_like(freq_comp)
        frequency_domain_window[start:end] = hamming_window
       # window =scale*( 0.54 - 0.46 * np.cos(2 * np.pi * n / (window_length- 1)))


    # Hanning
    elif window_index==1:
        hanning_window = hann(window_length)
        frequency_domain_window = np.zeros_like(freq_comp)
        frequency_domain_window[start:end] = hanning_window

    #Gaussian
    elif window_index==2:
        gaussian_window = scipy.signal.windows.gaussian(window_length, std*window_length)
        frequency_domain_window = np.zeros_like(freq_comp)
        frequency_domain_window[start:end] = gaussian_window


    #Rectangular
    elif window_index==3:
        frequency_domain_window = np.zeros_like(freq_comp)
        frequency_domain_window[start:end] = 1

    plot_widget.clear()
    freq_domain_plotting(freq_comp,output_amp,plot_widget)
    #apply_smoothing_window(output_amp,window_index,parameter)
    plot_widget.plot(freq_comp,scale*frequency_domain_window,pen='r',fillLevel=0, fillBrush=(255, 0, 0, 100) )



def compute_inverse_fourier_transform(new_amplitude,freq_comp,phases):
    # new_amplitudes=new_amplitude*len(new_amplitude)/2
    new_amplitudes = new_amplitude
    new_fft_result = new_amplitudes * np.exp(1j * phases)
    inverse_fft = np.fft.irfft(new_fft_result)
    return inverse_fft


def play_audio(player):
    player.play()


def pause_audio(player):
    player.pause()


def plot_specto(data, sample_rate, frame, checkbox):
    clear(frame)
    if len(data) == 0:
        return
    else:
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
def zoomIN(Input_plot_widget,output_plot_widget):
    zoom_factor = 0.8
    Input_plot_widget.getViewBox().scaleBy((zoom_factor, zoom_factor))
    output_plot_widget.getViewBox().scaleBy((zoom_factor, zoom_factor))


def zoomOUT(Input_plot_widget,output_plot_widget):
    zoom_factor = 1.2
    Input_plot_widget.getViewBox().scaleBy((zoom_factor, zoom_factor))
    output_plot_widget.getViewBox().scaleBy((zoom_factor, zoom_factor))

def plot_waveform(data, sample_rate, plot_widget):
    time = np.arange(0, len(data)) / sample_rate
    plot_widget.plot(time, data)
    plot_widget.setLabel('left', 'Amplitude')
    plot_widget.setLabel('bottom', 'Time (s)')
    plot_widget.showGrid(x=True, y=True)

    
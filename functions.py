from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import numpy as np


# VARIABLES
time_interval = 1000 #ms
Ts=1/44100

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
             
def play_n_pause(button, timer):

    if (timer.isActive()):
        icon = QIcon("icons/play.png")  # Use the resource path
        button.setIcon(icon)
        timer.stop()
    else:
        icon = QIcon("icons/pause.png")  # Use the resource path
        button.setIcon(icon)
        timer.start(time_interval)     

def speed(slider_value, speed_label): 
    map_speed_factor = {
        1 : 0.2,
        2 : 0.5,
        3 : 1.0,
        4 : 1.5,
        5 : 2.0,
    }
    speed_factor = map_speed_factor[slider_value]
    speed_label.setText(f'x {speed_factor}')
    time_interval = 1000*speed_factor #ms
    return time_interval
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

def compute_fourier_transform(signal):
    fourier_transform = np.fft.rfft(signal)
    frequencies_fft = np.fft.rfftfreq(len(signal), 1/1000)
    amplitudes = np.abs(fourier_transform)/(len(signal)/2)
    return amplitudes, frequencies_fft









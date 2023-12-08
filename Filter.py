import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def limit_to_band(input_file, output_file, lowcut, highcut):
    # Read the WAV file
    fs, y = wavfile.read(input_file)

    # Ensure mono by taking the first channel if stereo
    if len(y.shape) > 1:
        y = y[:, 0]

    # Apply the bandpass filter
    y_filtered = butter_bandpass_filter(y, lowcut, highcut, fs)

    # Write the output to a new WAV file
    wavfile.write(output_file, fs, y_filtered.astype(np.int16))

# input_file = "audio/singleCat.wav"
# input_file = "audio/singlepuppy.wav"

# input_file = "output3.wav"
# output_file = "catmod2.wav"
# lowcut = 3200  # Lower cutoff frequency in Hz
# highcut = 4150  # Upper cutoff frequency in Hz


input_file = "BeforeEditSounds\Animals\Eagle.wav"
output_file = "eagle_out2.wav"
lowcut = 3000 # Lower cutoff frequency in Hz
highcut = 10000  # Upper cutoff frequency in Hz

limit_to_band(input_file, output_file, lowcut, highcut)

# Wolf ==> 400, 800
# Cow ==> 800, 1300
# Eagle ==> 3000, 10000
# Monkey ==> 1400, 3000

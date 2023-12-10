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


input_file = "BeforeEditSounds\Musical\drums.wav"
output_file = "drums_out.wav"
lowcut = 3000 # Lower cutoff frequency in Hz
highcut = 5000  # Upper cutoff frequency in Hz

limit_to_band(input_file, output_file, lowcut, highcut)

# Wolf ==> 500, 720 ++++> 200, 1000 ?? 300Hz Thres
# Cow ==> 1300, 1650 ++++> 1050, 1900
# Eagle ==> 1800, 2300 +++> 1800, 2800
# Monkey ==> 3000, 6000 +++> 2800, 10000

# Drums ==> 1800, 3200 ++++> 1300,4000
# Guitar ==> 600, 900 ++++> 200, 1200
# Saxs ==> 500, 900 +++> 200, 1200
# Triangle ==> 6500,14000
# Piano ==> 1500, 4500
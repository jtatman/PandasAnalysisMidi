from scipy.io.wavfile import write
from scipy.signal import buttord, butter, filtfilt
from scipy.stats import norm
from numpy import int16
from scipy.fftpack import fft 
import matplotlib.pyplot as plt



def turn_green(signal, samp_rate):
    # start and stop of green noise range
    left = 1612 # Hz
    right = 2919 # Hz

    nyquist = (samp_rate/2)
    left_pass  = 1.1*left/nyquist
    left_stop  = 0.9*left/nyquist
    right_pass = 0.9*right/nyquist
    right_stop = 1.1*right/nyquist

    (N, Wn) = buttord(wp=[left_pass, right_pass],
                      ws=[left_stop, right_stop],
                      gpass=2, gstop=30, analog=0)
    (b, a) = butter(N, Wn, btype='band', analog=0, output='ba')
    return filtfilt(b, a, signal)

def to_integer(signal):
    # Take samples in [-1, 1] and scale to 16-bit integers,
    # values between -2^15 and 2^15 - 1.
    signal /= max(signal)
    return int16(signal*(2**15 - 1))


def write_gn():
    N = 48000 # samples per second
    white_noise= norm.rvs(0, 1, 300*N) # five minutes of audio
    green = turn_green(white_noise, N)
    write("green_noise.wav", N, to_integer(green))
    # plot using pyplot 
    #plt.rcParams["figure.figsize"] = (1,1)
    one_sec = green[0:N]
    plt.plot(abs(fft(one_sec)))
    plt.xlim((300,150))
    plt.show()

    

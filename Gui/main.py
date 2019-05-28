from Gui import Form
import matplotlib.pyplot as plt
import scipy.integrate as integ
from Logic import Signal
import numpy as np
import Logic.Window as Window
import Logic.Operations as Operations


# Form.start_Gui()

# signal1 = Signal.Signal(time0=0, time=10, freq=1, alt=1, sample=100)
# signal1.setAsRectangle()
# signal2 = Signal.Signal(time0=0, time=10, freq=1, alt=1, sample=100)
# signal2.setAsRectangle()
# # RYSOWANIE SYGNAŁU
# plt.subplot(1, 1, 1)
# x = signal1.getTime()
# y = np.convolve(signal1.signal, signal2.signal)
# z = np.correlate(signal1.getSignal(x), signal2.getSignal(x), mode="full")
# duration1 = len() * signal1.sample
# duration2 = len(z) * signal1.sample
# temp1 = np.linspace(signal1.time0, signal1.time0 + duration1, len(y))
# temp2 = np.linspace(signal1.time0, signal1.time0 + duration2, len(z))
# plt.plot(temp1, y, '-', markersize=0.9)
# plt.show()
# plt.plot(temp2, z, '-', markersize=0.9)
# plt.show()

# def low_filter():
#
#
# def high_filter():
#
#
# def both_sides_filter():


def low_filter(length, f0, sampling_rate, window="blackman"):
    time = np.linspace(0, length / sampling_rate, num=length)
    time = time - time[-1] / 2
    ideal_filter = f0 * np.sinc(2 * f0 * time)
    window_signal = np.ones(ideal_filter.shape)
    if window is "blackman":
        timeline, window_signal = Window.getBlackmanWindow(length)
    if window is "hamming":
        timeline, window_signal = Window.getHammingWindow(length)
    if window is "hanning":
        timeline, window_signal = Window.getHanningWindow(length)
    filter = ideal_filter * window_signal
    filter /= np.max(np.abs(filter), axis=0)

    return Signal.Signal(signal=filter, time=np.linspace(0, length / sampling_rate, num=length),
                         sampling_rate=sampling_rate,
                         duration=length / sampling_rate)


def high_filter(length: int, f0: int, sampling_rate, window="blackman"):
    _filter = low_filter(length, sampling_rate // 2 - f0, sampling_rate, window)

    _filter.signal[::2] *= -1

    return _filter


def low_high_filter(length: int, f1: int, f2: int, sampling_rate, window: str = "blackman"):
    _low_filter = low_filter(length=length // 2 + 1, f0=f2, sampling_rate=sampling_rate)
    _high_filter = high_filter(length=length // 2 + 1, f0=f1, sampling_rate=sampling_rate)
    band_filter = np.convolve(_low_filter.signal, _high_filter.signal)
    window_signal = np.ones(band_filter.shape)
    if window is "blackman":
        timeline, window_signal = Window.getBlackmanWindow(len(band_filter))
    if window is "hamming":
        timeline, window_signal = Window.getHammingWindow(len(band_filter))
    if window is "hanning":
        timeline, window_signal = Window.getHanningWindow(len(band_filter))

    return Signal.Signal(signal=band_filter * window_signal,
                         time=np.linspace(0, length / sampling_rate, num=length),
                         sampling_rate=sampling_rate,
                         duration=length / sampling_rate)


def convolve(signal1, signal2):
    array = np.convolve(signal1.signal, signal2.signal)
    duration = len(array) / signal1.sampling_rate
    time = np.linspace(signal1.time[0], signal1.time[0] + duration, num=len(array))
    return Signal.Signal(signal=array, time=time, sampling_rate=signal1.sampling_rate, duration=duration)


def correlate(signal1, signal2):
    array = np.correlate(signal1.signal, signal2.signal, mode='full')
    duration = len(array) / signal1.sampling_rate
    time = np.linspace(signal1.time[0], signal1.time[0] + duration, num=len(array))
    return Signal.Signal(signal=array, time=time, sampling_rate=signal1.sampling_rate, duration=duration)


def get_spectrum(signal: Signal.Signal):
    fft = np.fft.rfft(signal.signal)
    amplitudes = np.abs(fft)
    plt.plot(np.arange(len(amplitudes)) * signal.sampling_rate / (2 * len(amplitudes)), amplitudes)
    plt.xlabel("[Hz]")
    plt.ylabel("amp")
    plt.show()


def get_signal(signal):
    plt.plot(signal.time, signal.signal, markersize=0.9)
    plt.show()

samplingRate = 100
sig0 = Signal.createAsChirp(time0=0.0, duration=5.0, sampling_rate=300, freq0=1.0, time1=3.0, freq1=5.0)
plt.plot(sig0.time, sig0.signal)
plt.show()

# sig1 = Signal.createAsSin(time0=0.0, duration=1.0, sampling_rate=10, amp=1, freq=100)
# # sig2 = Signal.createAsSin(time0=0.0, duration=1.0, sampling_rate=2000, amp=1, freq=800)
# # # x, y = Window.getHammingWindow(5000)
# #
filter4 = low_filter(length=100, f0=10, sampling_rate=10)
# # # tempsig = Signal.Signal(y, 5.0, 100, 5.0)
# # # sig3 = convolve(sig1, tempsig)
# # # sig3 = convolve(sig3, tempsig)
# # # sig3 = convolve(sig3, sig1)
# # sig3 = convolve(sig1, sig2)
# # get_spectrum(sig3)
sig3 = convolve(sig0, filter4)
plt.plot(sig3.time, sig3.signal, '-', markersize=0.9)
plt.show()
# # get_spectrum(sig3)
# # get_spectrum(filter4)
# get_signal(sig3)
#
# dist = 1000
# speed = 20
# emited = Signal.createAsSin(time0=0.0, duration=1.0, sampling_rate=2000, amp=1, freq=1)
# delayed = emited.delay(2 * dist / speed)
# correlated = correlate(emited, delayed)
# t_max = correlated.time[np.argmax(correlated.signal)]
# print("Dystans obliczony  ", (correlated.time[-1] - t_max) / 2 * speed)
# print("Dystans rzeczywisty", dist)
#
# # sig3 = correlate(sig1, filter)
# # plt.plot(sig3.time, sig3.signal, '-', markersize=0.9)
# # plt.show()
# # x, y = Window.getBlackmanWindow(10)
# # plt.plot(x, y, '-')
# # plt.show()
# # x, y = Window.getHammingWindow(10)
# # plt.plot(x, y, '-')
# # plt.show()
# # x, y = Window.getHanningWindow(10)
# # time = np.linspace(0, 100, num=101)
# # time = time - time[-1] / 2
# # plt.plot(time, np.sinc(2 * 1 * time), '-')
# # plt.show()

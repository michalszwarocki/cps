from Gui import Form
from Logic import Signal
from Logic import Operations
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integ
from scipy import signal
import time as timer

Form.start_Gui()


# Hdb6 = [0.47046721, 1.14111692, 0.650365, -0.19093442, -0.12083221, 0.0498175]
# Gdb6 = [0.47046721, -1.14111692, 0.650365, 0.19093442, -0.12083221, -0.0498175]
# #
# #
# start = timer.time()
# samplefreq = 1024                               # sampling rate
# samplinginterval = 1.0/samplefreq               # sampling interval
# time = np.arange(0, 1, samplinginterval)        # time vector
# frequency = 10                                  # frequency of the signal
# signal = lambda t: 2 * np.sin(np.pi * t) + np.sin(2 * np.pi * t) + 5 * np.sin(4 * np.pi * t)
# # yarray = np.sin(2 * np.pi * frequency * time)   # 10 hz sine wave signal
# yarray = signal(time)
# start = timer.time()
# a, b = Operations.compute_dft(yarray, np.zeros(len(yarray)))
# print("PIERWSZE", timer.time() - start)
# start = timer.time()
# c, d = Operations.compute_fft(yarray, np.zeros(len(yarray)))
# print("DRUGIE", timer.time() - start)
# plt.subplot(2, 1, 1)
# plt.plot(a)
# plt.subplot(2, 1, 2)
# plt.plot(c)
# plt.show()
#
# plt.subplot(2, 1, 1)
# plt.plot(b)
# plt.subplot(2, 1, 2)
# plt.plot(d)
# plt.show()
#

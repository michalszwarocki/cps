from Gui import Form
from Logic import Signal
from Logic import Operations
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integ
from scipy import signal

Form.start_Gui()

# signal = Signal.Signal(0, 64, 2, 5, 300).setChirp(10, 5)
# sig1 = Signal.Signal(0, 2000, 0.005, 2, 1).setAsSin()
# sig2 = Signal.Signal(0, 2000, 0.005, 4, 1).setAsRectangle()
# sig3 = Operations.low_high_filter(50, 5, 40, "hamming")
# sig4 = Signal.Signal(0, 10, 1, 5, 40).setChirp(2, 5)
# print(sig4.time)
# filteredSignal = Operations.filtering(sig4, 'srodkowoprzepustowy', 'hamming', 50, 5)
# plt.subplot(3,1,1)
# plt.plot(sig4.timeline, sig4.getSignalForOperation())
# plt.subplot(3,1,2)
# plt.plot(sig3.timeline, sig3.getSignalForOperation())
# plt.subplot(3,1,3)
# plt.plot(filteredSignal[0], filteredSignal[1])
# plt.show()


# # RYSOWANIE SYGNAŁU
# plt.subplot(4, 1, 1)
# x = signal.getTime()
# y = signal.getSignal(x)
# plt.plot(x, y, '-', markersize=0.9)
#
# # RYSOWANIE PRÓBKOWANIA
# plt.subplot(4, 1, 2)
# x1 = signal.samplingTime(0.05)
# y1 = signal.sampling(0.05)
# plt.plot(x1, y1, 'o', markersize=0.9)
#
# #RYSOWANIE KWANTYZACJI Z OBCIĘCIEM
# plt.subplot(4, 1, 3)
# x2 = x1
# y2 = Operations.Operations().quantizate(signal, 5, y1)
# plt.plot(x,y)
# plt.step(x1, y2, where='post')
#
# #RYSOWANIE KWANTYZACJI Z ZAOKRĄGLENIEM
# plt.subplot(4, 1, 4)
# x3 = x1
# y3 = Operations.Operations().quantizate(signal, 2, y1)
# plt.plot(x,y)
# plt.plot(x3,y3,'o')
# plt.step(x3, y3, where='mid')
# print(y3)
#
# plt.show()
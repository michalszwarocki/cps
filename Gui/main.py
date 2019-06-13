from Gui import Form
from Logic import Signal
from Logic import Operations
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integ
from scipy import signal
import time as timer

# Form.start_Gui()

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

Hdb6 = [0.47046721, 1.14111692, 0.650365, -0.19093442, -0.12083221, 0.0498175]

def bracewell_buneman(xarray, length, log2length):
    '''
    bracewell-buneman bit reversal function
    inputs: xarray is array; length is array length; log2length=log2(length).
    output: bit reversed array xarray.
    '''
    muplus = int((log2length+1)/2)
    mvar = 1
    reverse = np.zeros(length, dtype = int)
    upper_range = muplus+1
    for _ in np.arange(1, upper_range):
        for kvar in np.arange(0, mvar):
            tvar = 2*reverse[kvar]
            reverse[kvar] = tvar
            reverse[kvar+mvar] = tvar+1
        mvar = mvar+mvar
    if (log2length & 0x01):
        mvar = mvar/2
    for qvar in np.arange(1, mvar):
        nprime = qvar-mvar
        rprimeprime = reverse[int(qvar)]*mvar
        for pvar in np.arange(0, reverse[int(qvar)]):
            nprime = nprime+mvar
            rprime = rprimeprime+reverse[int(pvar)]
            temp = xarray[int(nprime)]
            xarray[int(nprime)] = xarray[int(rprime)]
            xarray[int(rprime)] = temp
    return xarray



def dif_fft0 (xarray, twiddle, log2length):
    '''
    radix-2 dif fft
    '''
    xarray = xarray.astype(np.complex_)
    b_p = 1
    nvar_p = xarray.size
    twiddle_step_size = 1
    for _ in range(0,  log2length):           # pass loop
        nvar_pp =  nvar_p/2
        base_e = 0
        for _ in range(0,  b_p):       # block loop
            base_o = base_e+nvar_pp
            for nvar in range(0,  int(nvar_pp)):   # butterfly loop
                evar = xarray[int(base_e+nvar)]+xarray[int(base_o+nvar)]
                if nvar == 0:
                    ovar = xarray[int(base_e+nvar)]-xarray[int(base_o+nvar)]
                else:
                    twiddle_factor =  nvar*twiddle_step_size
                    ovar = (xarray[int(base_e+nvar)] \
                        -xarray[int(base_o+nvar)])*twiddle[int(twiddle_factor)]
                xarray[int(base_e+nvar)] = evar
                xarray[int(base_o+nvar)] = ovar
            base_e = base_e+nvar_p
        b_p = b_p*2
        nvar_p = nvar_p/2
        twiddle_step_size = 2*twiddle_step_size
    xarray = bracewell_buneman(xarray, xarray.size, log2length)
    return xarray


def test(time, yarray, samplefreq):
    '''
    Set up plot, call FFT function, plot result.
    Called  from testbench function.
    Inputs time:time vector, yarray: array, samplefreq: sampling rate.
    Outputs: none.
    '''
    plt.subplot(2, 1, 1)
    plt.title('Test of DIF FFT with 10 Hz Sine Input')
    plt.plot(time, yarray ,'k-')
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.subplot(2, 1, 2)
    ylength = len(yarray)                       # length of the signal
    kvar = np.arange(ylength)
    tvar = ylength/samplefreq
    frq = kvar/tvar                        # two-sided frequency range
    freq = frq[range(int(ylength/2))]           # one-sided frequency range
    twiddle = np.exp(-2j*np.pi*np.arange(0, 0.5, 1./ylength, dtype=np.complex_))
    y2array = abs(dif_fft0(yarray, twiddle, \
              int(np.log2(ylength)))/ylength)   # fft normalized magnitude
    y3array = y2array[range(int(ylength/2))]
    markerline, stemlines, baseline = plt.stem(freq, y3array, '--')
    plt.xlabel('freq (Hz)')
    plt.ylabel('|Y(freq)|')
    # plt.ylim((0.0, 0.55))
    plt.setp(markerline, 'markerfacecolor', 'b')
    plt.setp(baseline, 'color', 'b', 'linewidth', 2)
    plt.show()
    return None


def compute_dft_real_pair(inreal, inimag):
    assert len(inreal) == len(inimag)
    n = len(inreal)
    outreal = []
    outimag = []
    for k in range(n):  # For each output element
        sumreal = 0.0
        sumimag = 0.0
        for t in range(n):  # For each input element
            angle = 2 * np.pi * t * k / n
            sumreal +=  inreal[t] * np.cos(angle) + inimag[t] * np.sin(angle)
            sumimag += -inreal[t] * np.sin(angle) + inimag[t] * np.cos(angle)
        outreal.append(sumreal)
        outimag.append(sumimag)
    return (outreal, outimag)


start = timer.time()
samplefreq = 200                                # sampling rate
samplinginterval = 1.0/samplefreq               # sampling interval
time = np.arange(0, 20, samplinginterval)        # time vector
frequency = 10                                  # frequency of the signal
signal = lambda t: 2 * np.sin(np.pi * t) + np.sin(2 * np.pi * t) + 5 * np.sin(4 * np.pi * t)
# yarray = np.sin(2 * np.pi * frequency * time)   # 10 hz sine wave signal
yarray = signal(time)
a, b = compute_dft_real_pair(yarray, np.zeros(len(yarray)))
plt.plot(a)
plt.show()
plt.plot(b)
plt.show()
print("PIERWSZE", timer.time() - start)
start = timer.time()
test(time, yarray, samplefreq)                 # send sine to test
print("drugie", timer.time() - start)


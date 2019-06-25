import numpy as np
import matplotlib.pyplot as plt
from Logic import Window
from Logic import Signal


def addTwoSignals(firstSignal, secondSignal):
    return firstSignal.getSignalForOperation() + secondSignal.getSignalForOperation()


def substractTwoSignals(firstSignal, secondSignal):
    return firstSignal.getSignalForOperation() - secondSignal.getSignalForOperation()


def multiplyTwoSignals(firstSignal, secondSignal):
    return firstSignal.getSignalForOperation() * secondSignal.getSignalForOperation()


def divideTwoSignals(firstSignal, secondSignal):
    t = []

    for x, y in zip(firstSignal.getSignalForOperation(), secondSignal.getSignalForOperation()):
        if y == 0:
            t.append(x/0.00001)
        else:
            t.append(x/y)
    return t


def sampling(signal, period):
    timeSamples = np.linspace(signal.time0, signal.time0 + signal.time, signal.time * 1.0/period)
    amplitudeSamples = signal.signalFunction(timeSamples)
    samples = [timeSamples, amplitudeSamples]
    return samples


def quantizate(bits, samples):
    numberOfLevels = 2 ** bits - 1
    minAmplitudeValue = min(samples)
    maxAmplitudeValue = max(samples)
    Q = (maxAmplitudeValue - minAmplitudeValue)/numberOfLevels
    return Q * (np.floor(samples / Q) + 0.5)


def findTwoNearestElements(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    sortedArray = sorted(array, key=lambda x: np.abs(x-value))[:2]
    return sortedArray


def sincInterpolate(t, samplesTimeline, samplesAmplitudes, howMany):
    if np.size(samplesTimeline) > 2:
        samplingPeriod = samplesTimeline[1] - samplesTimeline[0]
    else:
        print("Array has to have minimum 2 elements")
        return

    value = 0
    if t in samplesTimeline[:]:
        index = int(np.where(t == samplesTimeline)[0])
        pointsIndexes = np.arange(index - howMany, index + howMany + 1)
    else:
        twoNearest = findTwoNearestElements(samplesTimeline, t)
        smallerIndex = int(np.where(min(twoNearest) == samplesTimeline)[0])
        biggerIndex = int(np.where(max(twoNearest) == samplesTimeline)[0])
        pointsIndexes = np.arange(smallerIndex - howMany + 1, biggerIndex + howMany)

    pointsIndexes = np.array([num for num in pointsIndexes if num >= 0])
    pointsIndexes = np.array([num for num in pointsIndexes if num <= np.size(samplesAmplitudes)-1])
    for i in pointsIndexes:
        value += np.take(samplesAmplitudes, i)*np.sinc(t/samplingPeriod - i)

    return value


def sincInterpolateArray(array, samplesTimeline, samplesAmplitudes, howMany):
    values = None
    for element in array:
        values = np.append(values, sincInterpolate(element, samplesTimeline, samplesAmplitudes, howMany))
    values = np.delete(values, 0)
    return values


def tri(t):
    if np.abs(t) < 1:
        return 1 - np.abs(t)
    else:
        return 0


def fohInterpolate(t, samplesTimeline, samplesAmplitudes, howMany):
    if np.size(samplesTimeline) > 2:
        samplingPeriod = samplesTimeline[1] - samplesTimeline[0]
    else:
        print("Array has to have minimum 2 elements")
        return

    value = 0
    if t in samplesTimeline[:]:
        index = int(np.where(t == samplesTimeline)[0])
        pointsIndexes = np.arange(index - howMany, index + howMany + 1)
    else:
        twoNearest = findTwoNearestElements(samplesTimeline, t)
        smallerIndex = int(np.where(min(twoNearest) == samplesTimeline)[0])
        biggerIndex = int(np.where(max(twoNearest) == samplesTimeline)[0])
        pointsIndexes = np.arange(smallerIndex - howMany + 1, biggerIndex + howMany)

    pointsIndexes = np.array([num for num in pointsIndexes if num >= 0])
    pointsIndexes = np.array([num for num in pointsIndexes if num <= np.size(samplesAmplitudes)-1])

    for i in pointsIndexes:
        value += np.take(samplesAmplitudes, i)*tri(t/samplingPeriod - i)

    return value


def fohInterpolateArray(array, samplesTimeline, samplesAmplitudes, howMany):
    values = None
    for element in array:
        values = np.append(values, fohInterpolate(element, samplesTimeline, samplesAmplitudes, howMany))
    values = np.delete(values, 0)
    return values


def convolve(signal1, signal2):
    firstValues = signal1.getSignalForOperation()
    if(type(signal2) == type(Signal)):
        secondValues = signal2.getSignalForOperation()
    else:
        secondValues = signal2

    length = len(firstValues) + len(secondValues) - 1
    values = []
    for n in range(length):
        firstTime = 0
        for k in range(len(firstValues)):
            if 0 <= n-k < len(secondValues):
                if firstTime == 0:
                    values.append(firstValues[k] * secondValues[n-k])
                    firstTime += 1
                else:
                    values[n] += firstValues[k] * secondValues[n - k]
    if (type(signal2) == type(Signal)):
        timeline = np.linspace(0, signal1.time + signal2.time, len(values))
    else:
        timeline = np.linspace(0, signal1.time + len(signal2), len(values))
    return [timeline, values]


def correlate(signal1, signal2):
    firstValues = signal1.getSignalForOperation()
    secondValues = signal2.getSignalForOperation()
    sec = list(reversed(secondValues))

    length = len(firstValues) + len(sec) - 1
    values = []
    for n in range(length):
        firstTime = 0
        for k in range(len(firstValues)):
            if 0 <= n-k < len(sec):
                if firstTime == 0:
                    values.append(firstValues[k] * sec[n-k])
                    firstTime += 1
                else:
                    values[n] += firstValues[k] * sec[n - k]
    timeline = np.linspace(0, signal1.time + signal2.time, len(values))
    return [timeline, values]


def low_filter(M, fo, fs, window):
    impulseResponseValues = []
    for n in range(M):
        if n == (M - 1) / 2:
            impulseResponseValues.append(2.0 *fo / fs)
        else:
            impulseResponseValues.append(np.sin(2.0 * np.pi * (n - (M - 1.0) / 2.0) *fo/ fs) / (np.pi * (n - (M - 1.0) / 2.0)))

    if window == 'Blackman':
        impulseResponseValues = Window.getBlackmanWindow(impulseResponseValues, M)
    if window == 'Hamming':
        impulseResponseValues = Window.getHammingWindow(impulseResponseValues, M)
    if window == 'Hanning':
        impulseResponseValues = Window.getHanningWindow(impulseResponseValues, M)

    signal = Signal.Signal(0, len(impulseResponseValues)-1, 1, 1, 1)
    signal.setAsOperation(np.array(impulseResponseValues))
    return signal


def high_filter(M, fo, fs, window):
    impulseResponseValues = []
    signal = low_filter(M, fo, fs, window)

    for n in range(len(signal.getSignalForOperation())):
        impulseResponseValues.append(signal.getSignalForOperation()[n]*((-1)**n))

    signal.setAsOperation(np.array(impulseResponseValues))
    return signal


def low_high_filter(M, fo, fs, window):
    impulseResponseValues = []
    signal = low_filter(M, fo, fs, window)

    for n in range(len(signal.getSignalForOperation())):
        impulseResponseValues.append(signal.getSignalForOperation()[n]*2*np.sin(np.pi*n/2))

    signal.setAsOperation(np.array(impulseResponseValues))
    return signal


def filtering(signal, filterType, window, M, fo):
    if filterType == 'dolnoprzepustowy':
        fil = low_filter(M, fo, signal.sample, window)
    elif filterType == 'gornoprzepustowy':
        print(window)
        fil = high_filter(M, fo, signal.sample, window)
    elif filterType == 'srodkowoprzepustowy':
        fil = low_high_filter(M, fo, signal.sample, window)

    filteredSignal = convolve(signal, fil)

    return filteredSignal, fil


def radar(signal, speed, distance):
    time = distance/speed
    delayed_signal = signal
    signal.singalPoints = signal.getSignalForOperation()
    delayed_signal.singalPoints = delayed_signal.getSignalForOperation()
    delayed_signal.delay(time * 2)
    time2, signal2 = correlate(signal, delayed_signal)
    t_max = time2[np.argmax(signal2)]
    calc_dist = ((time2[int(len(time2)/2)] - t_max) * speed)
    return calc_dist


def radar2(signal, delayed_signal, speed, distance):
    time = 2 * distance / speed
    signal.singalPoints = signal.getSignalForOperation()
    # delayed_signal.singalPoints = delayed_signal.getSignalForOperation()
    # delayed_signal.delay(time * 2)
    time2, signal2 = correlate(signal, delayed_signal)
    t_max = time2[np.argmax(signal2)]
    print(time2[int(len(time2)/2)])
    print(t_max)
    temp = signal.timeline[int(len(signal.timeline)/2)]
    print(temp)
    calc_dist = np.abs(((temp - t_max) * speed/2))


def compute_dft(inreal, inimag):
    assert len(inreal) == len(inimag)
    n = len(inreal)
    outreal = []
    outimag = []
    for k in range(n):  # For each output element
        sumreal = 0.0
        sumimag = 0.0
        for t in range(n):  # For each input element
            angle = 2 * np.pi * t * k / n
            sumreal += inreal[t] * np.cos(angle) + inimag[t] * np.sin(angle)
            sumimag += -inreal[t] * np.sin(angle) + inimag[t] * np.cos(angle)
        outreal.append(sumreal)
        outimag.append(sumimag)
    return outreal, outimag


def compute_fft(inreal, inimag):
    N = len(inreal)
    if N == 1:
        return [inreal[0]], [inimag[0]]

    if N % 2 != 0:
        return None, None

    evenReal = []
    evenImag = []
    for k in range(int(N/2)):
        evenReal.append(inreal[2 * k])
        evenImag.append(inimag[2 * k])

    qReal, qImag = compute_fft(evenReal, evenImag)

    oddReal = []
    oddImag = []
    for k in range(int(N / 2)):
        oddReal.append(inreal[2 * k +1])
        oddImag.append(inimag[2 * k +1])

    rReal, rImag = compute_fft(oddReal, oddImag)

    yReal = [None] * N
    yImag = [None] * N
    for k in range(int(N / 2)):
        kth = -2 * k * np.pi / N
        wkReal = np.cos(kth)
        wkImag = np.sin(kth)

        yReal[k] = (wkReal * rReal[k] - wkImag * rImag[k]) + qReal[k]
        yImag[k] = (wkReal * rImag[k] + wkImag * rReal[k]) + qImag[k]
        yReal[k+ int(N/2)] = qReal[k] - (wkReal * rReal[k] - wkImag * rImag[k])
        yImag[k+ int(N/2)] = qImag[k] - (wkReal * rImag[k] + wkImag * rReal[k])
    return yReal, yImag


Hdb6 = [0.47046721, 1.14111692, 0.650365, -0.19093442, -0.12083221, 0.0498175]
Gdb6 = [0.47046721, -1.14111692, 0.650365, 0.19093442, -0.12083221, -0.0498175]


def computeWaveletTransform(signal):
    hSamples = convolve(signal, Hdb6)
    gSamples = convolve(signal, Gdb6)
    hHalf = []
    gHalf = []
    for i in range(len(hSamples)):
        if(i % 2 == 0):
            hHalf.append(hSamples[i])
        else:
            gHalf.append(gSamples[i])
    return hHalf, gHalf


def computeWaveletBackwardTransform(real, imag):
    return



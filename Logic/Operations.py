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
    timeSamples = np.linspace(signal.time0, signal.time0 + signal.time, signal.time * 1.0/period + 1)
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
    secondValues = signal2.getSignalForOperation()

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
    timeline = np.linspace(0, signal1.time + signal2.time, len(values))
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
    time = distance / speed
    signal.singalPoints = signal.getSignalForOperation()
    # delayed_signal.singalPoints = delayed_signal.getSignalForOperation()
    # delayed_signal.delay(time * 2)
    time2, signal2 = correlate(signal, delayed_signal)
    t_max = time2[np.argmax(signal2)]
    calc_dist = ((time2[int(len(time2)/2)] - t_max) * speed)
    return calc_dist
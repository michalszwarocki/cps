import numpy as np
import matplotlib.pyplot as plt


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


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def sincInterpolate(t, samples, howMany):
    if np.size(samples) > 2:
        samplingPeriod = samples[0][1] - samples[0][0]
    else:
        print("Array has to have minimum 2 elements")
        return

    value = 0
    if t in samples[0][:]:
        index = int(np.where(t == samples[0])[0])
    else:
        nearest = find_nearest(samples[0], t)
        index = int(np.where(nearest == samples[0])[0])

    pointsIndexes = np.arange(index-howMany, index+howMany+1)
    pointsIndexes = np.array([num for num in pointsIndexes if num >= 0])
    pointsIndexes = np.array([num for num in pointsIndexes if num <= np.size(samples[1])-1])

    for i in pointsIndexes:
        value += np.take(samples[1], i)*np.sinc(t/samplingPeriod - i)

    return value


def sincInterpolateArray(array, samples, howMany):
    values = None
    for element in array:
        values = np.append(values, sincInterpolate(element, samples, howMany))
    values = np.delete(values, 0)
    return values


def tri(t):
    if np.abs(t) < 1:
        return 1 - np.abs(t)
    else:
        return 0

def fohExtrapolate(t, samples, howMany):
    if np.size(samples) > 2:
        samplingPeriod = samples[0][1] - samples[0][0]
    else:
        print("Array has to have minimum 2 elements")
        return

    value = 0
    if t in samples[0][:]:
        index = int(np.where(t == samples[0])[0])
    else:
        nearest = find_nearest(samples[0], t)
        index = int(np.where(nearest == samples[0])[0])

    pointsIndexes = np.arange(index-howMany, index+howMany+1)
    pointsIndexes = np.array([num for num in pointsIndexes if num >= 0])
    pointsIndexes = np.array([num for num in pointsIndexes if num <= np.size(samples[1])-1])

    for i in pointsIndexes:
        value += np.take(samples[1], i)*tri(t/samplingPeriod - i)

    return value


def fohExtrapolateArray(array, samples, howMany):
    values = None
    for element in array:
        values = np.append(values, fohExtrapolate(element, samples, howMany))
    values = np.delete(values, 0)
    return values



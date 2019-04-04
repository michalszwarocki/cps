import numpy as np


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
    timeSamples = np.linspace(signal.time0, signal.time0 + signal.time, signal.time * period)
    amplitudeSamples = signal.signalFunction(timeSamples)
    samples = [timeSamples, amplitudeSamples]
    return samples


def quantizate(signal, bits, samples):
    numberOfLevels = 2 ** bits - 1
    minAmplitudeValue = min(samples)
    maxAmplitudeValue = max(samples)
    Q = (maxAmplitudeValue - minAmplitudeValue)/numberOfLevels
    return Q * (np.floor(samples / Q) + 0.5)

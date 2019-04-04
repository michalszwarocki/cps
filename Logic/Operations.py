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


def quantizate(signal, bits, samples):
    Q = signal.alt * 2.0 / pow(2, bits)
    return Q * (np.floor(samples / Q) + 0.5)

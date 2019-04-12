import numpy as np


def meanSquaredError(originalSignal, receivedSignal):
    result = 0
    for i in range(len(originalSignal)):
        result += (originalSignal[i]-receivedSignal[i])**2
    result /= np.size(originalSignal)

    return result


def signalToNoiseRatio(originalSignal, receivedSignal):
    originalSquared = 0
    differenceSquared = 0
    for i in range(len(originalSignal)):
        originalSquared += originalSignal[i]**2
        differenceSquared += (originalSignal[i]-receivedSignal[i])**2
    if differenceSquared == 0:
        differenceSquared = 0.001
    if originalSquared/differenceSquared != 0:
        result = 10*np.log10(originalSquared/differenceSquared)
    else:
        result = 10 * np.log10(0.001)

    return result


def peakSignalToNoiseRatio(originalSignal, receivedSignal):
    maxSignalValue = np.amax(originalSignal)
    mse = meanSquaredError(originalSignal, receivedSignal)
    if mse == 0:
        mse = 0.001
    if maxSignalValue/mse != 0:
        result = 10*np.log10(maxSignalValue/mse)
    else:
        result = 10*np.log10(0.001)

    return result


def maximumDifference(originalSignal, receivedSignal):
    differences = np.subtract(originalSignal, receivedSignal)
    result = np.amax(differences)

    return result

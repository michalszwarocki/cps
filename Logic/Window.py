import numpy as np


def getBlackmanWindow(impulseResponseValues, M):
    newImpulseresponseValues = []
    for n in range(len(impulseResponseValues)):
        windowValue = 0.42 - 0.5 * np.cos(2 * np.pi * n/M) + 0.08 * np.cos(4 * np.pi * n/M)
        newImpulseresponseValues.append(impulseResponseValues[n]*windowValue)
    return newImpulseresponseValues


def getHammingWindow(impulseResponseValues, M):
    newImpulseresponseValues = []
    for n in range(len(impulseResponseValues)):
        windowValue = 0.53836 - 0.46164 * np.cos(2 * np.pi * n / M)
        newImpulseresponseValues.append(impulseResponseValues[n] * windowValue)
    return newImpulseresponseValues


def getHanningWindow(impulseResponseValues, M):
    newImpulseresponseValues = []
    for n in range(len(impulseResponseValues)):
        windowValue = 0.5 - 0.5 * np.cos(2 * np.pi * n / M)
        newImpulseresponseValues.append(impulseResponseValues[n] * windowValue)
    return newImpulseresponseValues
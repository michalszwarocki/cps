import numpy as np


def getBlackmanWindow(length):
    signal = np.linspace(0, 1, length)
    return signal, 0.42 - 0.5 * np.cos(2 * np.pi * signal) + 0.08 * np.cos(4 * np.pi * signal)


def getHammingWindow(length):
    signal = np.linspace(0, 1, length)
    return signal, 0.53836 - 0.46164 * np.cos(2 * np.pi * signal)


def getHanningWindow(length):
    signal = np.linspace(0, 1, length)
    return signal, 0.5 - 0.5 * np.cos(2 * np.pi * signal)

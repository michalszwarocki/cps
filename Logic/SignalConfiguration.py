import numpy as np


class Configuration:
    time0: float
    time: float
    frequency: float
    amplitude: float
    numberOfSamples: float
    infiltrator: float
    jumpMoment: float
    possibility: float
    jumpSample : int
    signalType: str
    noise: str
    points: np.array

    def __init__(self, t0, time, freq, ampl, samples, infil, jumpMom, possib, jumpSamp, type, noise):
        self.time0 = t0
        self.time = time
        self.frequency = freq
        self.amplitude = ampl
        self.numberOfSamples = samples
        self.infiltrator = infil
        self.jumpMoment = jumpMom
        self.possibility = possib
        self.jumpSample = jumpSamp
        self.signalType = type
        self.noise = noise

    def setPoints(self, signal):
        self.points = np.array(signal)



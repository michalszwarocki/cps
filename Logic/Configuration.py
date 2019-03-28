
class Configuration:
    time0: float
    time: float
    frequency: float
    amplitude: float
    numberOfSamples: float
    signalType: str
    infiltrator: float
    noise: str
    jumpMoment: float

    def __init__(self, t0, time, freq, ampl, samples, type, infil, noise, jumpMom):
        self.time0 = t0
        self.time = time
        self.frequency = freq
        self.amplitude = ampl
        self.numberOfSamples = samples
        self.signalType = type
        self.infiltrator = infil
        self.noise = noise
        self.jumpMoment = jumpMom



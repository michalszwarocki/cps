import numpy as np


class Signal:
    timeline: np.array
    time0: float
    freq: float
    amp: float
    sample: int

    def __init__(self, time0, time, freq, alt, sample):
        self.time0 = time0
        self.time = time
        self.freq = freq
        self.amp = alt
        self.timeline = np.linspace(time0, time0 + time, time * sample)
        self.signal = lambda t: t * 0

    def getSignal(self, time):
        return self.signal(time)

    def getTime(self):
        return self.timeline

    def samplingTime(self, period):
        return np.linspace(self.time0, self.time0 + self.time, self.time / period)

    def sampling(self, period):
        return self.signal(self.samplingTime(period))

    def setAsSin(self):
        self.signal = lambda t: self.amp * np.sin(2 * np.pi * self.freq * t)
        return self

    def setHalfStraight(self):
        self.signal = lambda t: 0.5 * self.amp * (
                    np.sin(2 * np.pi * self.freq * t) + np.abs(np.sin(2 * np.pi * self.freq * t)))
        return self

    def setFullStraight(self):
        self.signal = lambda t: self.amp * np.abs(np.sin(2 * np.pi * self.freq * t))
        return self

    def setGaussNoise(self, noise_amp=1):
        self.signal = lambda t: np.random.normal(0, noise_amp, t.shape)
        return self

    def setUniformNoise(self):
        '''not working so far :('''
        self.signal = lambda t: np.random.uniform(-self.amp, self.amp, t.shape)
        return self

    def setAsRectangle(self, infil=0.5):
        self.signal = lambda t: (t % self.freq < self.freq * infil) * np.ones(t.shape) * self.amp
        # x = np.where(self.timeline % self.freq > self.freq * infil)
        # self.signal[x] = 0
        return self

    def setAsSyncRectangle(self, infil=0.5):
        self.signal = lambda t: (t % self.freq < self.freq * infil) * np.ones(t.shape) * self.amp
        # self.signal = np.ones(self.signal.shape) * self.amp * 2
        # x = np.where(self.timeline % self.freq > self.freq * infil)
        # self.signal[x] = 0
        # self.signal -= self.amp
        return self


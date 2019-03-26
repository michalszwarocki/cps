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
        self.timeline = np.linspace(time0, time0 + time, time * sample + 1)
        self.signal = lambda t: t * 0

    def getSignal(self, time=None):
        if time is None:
            time = self.timeline
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
        self.signal = lambda t: np.random.uniform(-self.amp, self.amp, t.shape)
        return self

    def setAsRectangle(self, infil=0.5):
        print(self.freq, 1 / self.freq)
        self.signal = lambda t: (t % (1 / self.freq) < (1 / self.freq) * infil) * np.ones(t.shape) * self.amp
        # x = np.where(self.timeline % self.freq > self.freq * infil)
        # self.signal[x] = 0
        return self

    def setAsSyncRectangle(self, infil=0.5):
        self.signal = lambda t: (t % self.freq < self.freq * infil) * np.ones(t.shape) * self.amp * 2 - self.amp
        return self

    def setSingleJump(self, ts=0):
        self.signal = lambda t: (t > ts) * np.ones(t.shape) * self.amp
        return self

    def setImpulse(self, possibility=0.5):
        self.signal = lambda t: np.random.choice([0, 1], size=t.shape, p=[1 - possibility, possibility])
        return self

    def setTriangle(self, infil=0.5):
        okres = 1 / self.freq
        self.signal = lambda t: (t % okres <= (okres * infil)) * (
                ((t % okres) / (okres * infil)) * self.amp) + (
                                        t % okres > (okres * infil)) * (
                                        self.amp - (((t % okres) - infil * okres) / (okres * (1 - infil))) * self.amp)
        return self

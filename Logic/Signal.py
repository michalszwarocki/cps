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
        self.one_period = np.linspace(time0, time0 + 1 / freq, 1 / freq * sample)
        self.signal = lambda t: t * 0
        self.points = np.array([])

    def getSignal(self, time=None, one_period=False):
        if time is None:
            if one_period:
                time = self.one_period
            else:
                time = self.timeline
        return self.signal(time)

    def getTime(self, one_period=False):
        if one_period:
            return self.one_period
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
        self.signal = lambda t: np.random.normal(0, size=t.shape)
        return self

    def setUniformNoise(self):
        self.signal = lambda t: np.random.uniform(-self.amp, self.amp, t.shape)
        return self

    def setAsRectangle(self, infil=0.5):
        okres = 1 / self.freq
        self.signal = lambda t: (t % okres < okres * infil) * np.ones(t.shape) * self.amp
        # x = np.where(self.timeline % self.freq > self.freq * infil)
        # self.signal[x] = 0
        return self

    def setAsSyncRectangle(self, infil=0.5):
        okres = 1 / self.freq
        self.signal = lambda t: (t % okres < okres * infil) * np.ones(t.shape) * self.amp * 2 - self.amp
        return self

    def setSingleJump(self, ts=0):
        self.signal = lambda t: (t > ts) * np.ones(t.shape) * self.amp
        return self

    def setImpulseNoice(self, possibility=0.5):
        self.signal = lambda t: np.random.choice([0, 1], size=t.shape, p=[1 - possibility, possibility])
        return self

    def setTriangle(self, infil=0.5):
        okres = 1 / self.freq
        self.signal = lambda t: (t % okres <= (okres * infil)) * (
                ((t % okres) / (okres * infil)) * self.amp) + (
                                        t % okres > (okres * infil)) * (
                                        self.amp - (((t % okres) - infil * okres) / (okres * (1 - infil))) * self.amp)
        return self

    def setImpulse(self, n = 0):
        temp = self.timeline * False
        temp[n] = True
        self.signal = lambda t: self.amp * np.ones(t.shape) * temp
        # print(temp)
        return self

    def setAsOperation(self, points):
        self.points = points

    def add(self, signal):
        if signal.points.size == 0:
            if self.points.size == 0:
                return self.getSignal() + signal.getSignal()
            else:
                return self.points + signal.getSignal()
        else:
            if self.points.size == 0:
                return self.getSignal() + signal.points
            else:
                return self.points + signal.points

    def sub(self, signal):
        if signal.points.size == 0:
            if self.points.size == 0:
                return self.getSignal() - signal.getSignal()
            else:
                return self.points - signal.getSignal()
        else:
            if self.points.size == 0:
                return self.getSignal() - signal.points
            else:
                return self.points - signal.points

    def mul(self, signal):
        if signal.points.size == 0:
            if self.points.size == 0:
                return self.getSignal() * signal.getSignal()
            else:
                return self.points * signal.getSignal()
        else:
            if self.points.size == 0:
                return self.getSignal() * signal.points
            else:
                return self.points * signal.points

    def div(self, signal):
        t = []

        if self.points.size == 0:
            first = self.getSignal()
        else:
            first = self.points

        if signal.points.size == 0:
            second = signal.getSignal()
        else:
            second = signal.points

        for x, y in zip(first, second):
            if y == 0:
                t.append(x/0.00001)
            else:
                t.append(x/y)
        return t
        # return self.getSignal() / signal.getSignal()

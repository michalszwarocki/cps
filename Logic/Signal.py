import numpy as np


class Signal:

    timeline = np.array
    time0 = 0
    freq = 0
    alt = 0
    sample = 0

    def __init__(self, time0, time, freq, alt, sample):
        self.time0 = time0
        self.time = time
        self.freq = freq
        self.alt = alt
        self.timeline = np.linspace(time0, time0+time, time*sample)
        self.signal = lambda t: t*0

    def getSignal(self, time):
        return self.signal(time)

    def getTime(self):
        return self.timeline

    def samplingTime(self, period):
        return np.linspace(self.time0, self.time0+self.time, self.time/period)

    def sampling(self, period):
        return self.signal(self.samplingTime(period))

    def setAsSin(self):
        self.signal = lambda t: self.alt*np.sin(2 * np.pi * self.freq * t)
        return self

    def setHalfStraight(self):
        self.signal = lambda t: 0.5*self.alt*(np.sin(2 * np.pi * self.freq * t) + np.abs(np.sin(2 * np.pi * self.freq * t)))
        return self

    def setFullStraight(self):
        self.signal = lambda t: self.alt*np.abs(np.sin(2 * np.pi * self.freq * t))
        return self

    def setGaussNoise(self, noiseAmp = 1):
        self.signal = self.signal + np.random.normal(0, noiseAmp, self.signal.shape)
        return self

    def setUniformNoise(self):
        '''not working so far :('''
        self.signal = self.signal + np.random.uniform(-1, 1, self.signal.shape)
        return self

    def setAsRectangle(self, infil = 0.5):
        self.signal = np.ones(self.signal.shape) * self.alt
        x = np.where(self.timeline % self.freq > self.freq*infil)
        self.signal[x] = 0
        return self

    def setAsSyncRectangle(self, infil = 0.5):
        self.signal = np.ones(self.signal.shape) * self.alt * 2
        x = np.where(self.timeline % self.freq > self.freq*infil)
        self.signal[x] = 0
        self.signal -= self.alt
        return self


class dupa:
    x = 2
    def pomnoz(self):
        self.x *= 2
        return self

    def odejmij(self):
        self.x -= 2
        return self

    def zwroc(self):
        return self.x

import numpy as np
import scipy.integrate as integ

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
        self.sample = sample
        self.timeline = np.linspace(time0, time0 + time, time * sample + 1)
        self.one_period = np.linspace(time0, time0 + 1 / freq, 1 / freq * sample)
        self.signalFunction = lambda t: t * 0
        self.singalPoints = np.array([])
        self.imagPoints = np.array([])

    def getSignal(self, time=None, one_period=False):
        if time is None:
            if one_period:
                time = self.one_period
            else:
                time = self.timeline
        return self.signalFunction(time)

    def getTime(self, one_period=False):
        if one_period:
            return self.one_period
        return self.timeline

    def setAsSin(self):
        self.signalFunction = lambda t: self.amp * np.sin(2 * np.pi * self.freq * t)
        return self

    def setHalfStraight(self):
        self.signalFunction = lambda t: 0.5 * self.amp * (
                np.sin(2 * np.pi * self.freq * t) + np.abs(np.sin(2 * np.pi * self.freq * t)))
        return self

    def setFullStraight(self):
        self.signalFunction = lambda t: self.amp * np.abs(np.sin(2 * np.pi * self.freq * t))
        return self

    def setGaussNoise(self, noise_amp=1):
        self.signalFunction = lambda t: np.random.normal(0, size=t.shape)
        return self

    def setUniformNoise(self):
        self.signalFunction = lambda t: np.random.uniform(-self.amp, self.amp, t.shape)
        return self

    def setAsRectangle(self, infil=0.5):
        okres = 1 / self.freq
        self.signalFunction = lambda t: (t % okres < okres * infil) * np.ones(t.shape) * self.amp
        return self

    def setAsSyncRectangle(self, infil=0.5):
        okres = 1 / self.freq
        self.signalFunction = lambda t: (t % okres < okres * infil) * np.ones(t.shape) * self.amp * 2 - self.amp
        return self

    def setSingleJump(self, ts=0):
        self.signalFunction = lambda t: (t > ts) * np.ones(t.shape) * self.amp
        return self

    def setImpulseNoice(self, possibility=0.5):
        self.signalFunction = lambda t: np.random.choice([0, 1], size=t.shape, p=[1 - possibility, possibility])
        return self

    def setTriangle(self, infil=0.5):
        okres = 1 / self.freq
        self.signalFunction = lambda t: (t % okres <= (okres * infil)) * (
                ((t % okres) / (okres * infil)) * self.amp) + (
                                        t % okres > (okres * infil)) * (
                                        self.amp - (((t % okres) - infil * okres) / (okres * (1 - infil))) * self.amp)
        return self

    def setCustomSignal(self):
        self.signalFunction = lambda t: 2 * np.sin(np.pi*t) + np.sin(2*np.pi*t) + 5 * np.sin(4*np.pi*t)
        return self

    def setImpulse(self, n = 0):
        temp = self.timeline * False
        temp[n] = True
        self.signalFunction = lambda t: self.amp * np.ones(t.shape) * temp
        # print(temp)
        return self

    def setChirp(self, time1, freq1):
        ans = lambda t: integ.quad(lambda t: 2.0 * np.pi * (self.freq + (freq1 - self.freq) * t / time1), 0, t)[0]
        self.signalFunction = lambda t: chirpSignal(t, ans)
        return self

    def setAsOperation(self, points):
        self.singalPoints = points

    def getSignalForOperation(self):
        if self.imagPoints.size != 0:
            return self.singalPoints, self.imagPoints
        if self.singalPoints.size != 0:
            return self.singalPoints
        return self.getSignal()


    def delay(self, time):
        self.timeline = np.linspace(self.time0, self.time0 + self.time + time, (self.time0 + self.time + time) * self.sample + 1)
        new_signal = np.zeros((len(self.timeline),))
        new_signal[-len(self.singalPoints):] = self.singalPoints
        self.singalPoints = new_signal

def chirpSignal(a, ans):
    if type(a) is np.ndarray:
        return [chirpSignal(element, ans) for element in a]
    else:
        return np.cos(ans(a))



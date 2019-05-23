import numpy as np


# class Signal:
#     timeline: np.array
#     time0: float
#     freq: float
#     amp: float
#     sample: int
#
#     def __init__(self, array: np.array, time: np.array, sampling_rate, duration: float, freq=None):
#         self.time0 = time0
#         self.time = time
#         self.freq = freq
#         self.amp = alt
#         self.timeline = np.linspace(time0, time0 + time, time * sample + 1)
#         self.one_period = np.linspace(time0, time0 + 1 / freq, 1 / freq * sample)
#         self.signalFunction = lambda t: t * 0
#         self.singalPoints = np.array([])
#         self.sample = sample

class Signal:
    signal: np.array
    time: np.array
    sampling_rate: int
    length: int
    freq: float

    def __init__(self, signal: np.array, time: np.array, sampling_rate: int, duration: float, freq=None):
        self.signal = signal
        self.length = signal.size
        self.sampling_rate = sampling_rate
        self.freq = freq
        self.time = time
        self.duration = duration

    def getSignal(self):
        return self.signalFunction(self.time)

    def getTime(self, one_period=False):
        return self.time


def createAsSin(time0, duration, sampling_rate, amp, freq):
    signalFunction = lambda t: amp * np.sin(2 * np.pi * freq * t)
    timeline = np.linspace(time0, time0 + duration, num=duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsHalfStraight(time0, duration, sampling_rate, amp, freq):
    signalFunction = lambda t: 0.5 * amp * (
            np.sin(2 * np.pi * freq * t) + np.abs(np.sin(2 * np.pi * freq * t)))
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsFullStraight(time0, duration, sampling_rate, amp, freq):
    signalFunction = lambda t: amp * np.abs(np.sin(2 * np.pi * freq * t))
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsGaussNoise(time0, duration, sampling_rate, noise_amp=1):
    signalFunction = lambda t: np.random.normal(0, size=t.shape)
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsUniformNoise(time0, duration, sampling_rate, low, high):
    signalFunction = lambda t: np.random.uniform(low, high, t.shape)
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsRectangle(time0, duration, sampling_rate, amp, freq, infil=0.5):
    okres = 1 / freq
    signalFunction = lambda t: (t % okres < okres * infil) * np.ones(t.shape) * amp
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsSyncRectangle(time0, duration, sampling_rate, amp, freq, infil=0.5):
    okres = 1 / freq
    signalFunction = lambda t: (t % okres < okres * infil) * np.ones(t.shape) * amp * 2 - amp
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsSingleJump(time0, duration, sampling_rate, amp, ts=0):
    signalFunction = lambda t: (t > ts) * np.ones(t.shape) * amp
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsImpulseNoice(time0, duration, sampling_rate, possibility=0.5):
    signalFunction = lambda t: np.random.choice([0, 1], size=t.shape, p=[1 - possibility, possibility])
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsTriangle(time0, duration, sampling_rate, amp, freq, infil=0.5):
    okres = 1 / freq
    signalFunction = lambda t: (t % okres <= (okres * infil)) * (
            ((t % okres) / (okres * infil)) * amp) + (
                                    t % okres > (okres * infil)) * (
                                    amp - (((t % okres) - infil * okres) / (okres * (1 - infil))) * amp)
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)


def createAsImpulse(time0, duration, sampling_rate, n = 0):
    temp = timeline * False
    temp[n] = True
    signalFunction = lambda t: amp * np.ones(t.shape) * temp
    # print(temp)
    timeline = np.linspace(time0, time0 + duration, duration * sampling_rate)
    return Signal(signalFunction(timeline), timeline, sampling_rate=sampling_rate, duration=timeline)

    def setAsOperation(self, points):
        self.singalPoints = points

    def getSignalForOperation(self):
        if self.singalPoints.size != 0:
            return self.singalPoints
        return self.getSignal()

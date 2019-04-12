import Logic.Operations as opr


class ActionTypeSelector:
    receivedSingal = None
    originalTimeline = None
    originalSignal = None
    samplingX = None
    samplingY = None
    receivedTimeline = None
    originalSignalToMetrics = None

    def __init__(self, signal, samplingConfiguration, signalConfig):
        self.setType(signal, samplingConfiguration, signalConfig)

    def setType(self, signal, samplingConfiguration, signalConfig):
        if signalConfig.signalType != 'wynik operacji':
            self.setTypeIfNotRead(signal, samplingConfiguration)
        else:
            self.setTypeIfRead(signal, samplingConfiguration)

    def getReceivedSingnal(self):
        return self.receivedSingal

    def getOriginalTimeline(self):
        return self.originalTimeline

    def getOriginalSignal(self):
        return self.originalSignal

    def getSamplingX(self):
        return self.samplingX

    def getSamplingY(self):
        return self.samplingY

    def getReceivedTimeline(self):
        return self.receivedTimeline

    def getOriginalSignalToMetrics(self):
        return self.originalSignalToMetrics

    def setTypeIfNotRead(self, signal, samplingConfiguration):
        samples = opr.sampling(signal, samplingConfiguration.samplingPeriod)
        self.originalTimeline = signal.getTime()
        self.originalSignal = signal.getSignalForOperation()
        self.samplingX = samples[0]
        self.samplingY = samples[1]

        if samplingConfiguration.action == 'próbkowanie':
            self.receivedSingal = samples[1]
            self.originalSignalToMetrics = samples[1]
            self.receivedTimeline = samples[0]
        elif samplingConfiguration.action == 'kwantyzacja z zaokrągleniem':
            self.receivedSingal = opr.quantizate(samplingConfiguration.quantizationBits, samples[1])
            self.originalSignalToMetrics = samples[1]
            self.receivedTimeline = samples[0]
        elif samplingConfiguration.action == 'interpolacja pierwszego rzędu':
            self.receivedSingal = opr.fohInterpolateArray(signal.timeline, samples[0], samples[1],
                                                          samplingConfiguration.numberOfSamples)
            print(self.receivedSingal)
            self.originalSignalToMetrics = signal.getSignalForOperation()
            self.receivedTimeline = signal.getTime()
        elif samplingConfiguration.action == 'rekonstrukcja sinc':
            self.receivedSingal = opr.sincInterpolateArray(signal.timeline, samples[0], samples[1],
                                                           samplingConfiguration.numberOfSamples)
            self.originalSignalToMetrics = signal.getSignalForOperation()
            self.receivedTimeline = signal.getTime()

    def setTypeIfRead(self, signal, samplingConfiguration):
        samples = signal.singalPoints
        self.originalTimeline = signal.getTime()
        self.originalSignal = signal.getSignalForOperation()
        self.samplingX = signal.getTime()
        self.samplingY = signal.getSignalForOperation()
        self.receivedTimeline = signal.getTime()
        self.originalSignalToMetrics = signal.getSignalForOperation()

        if samplingConfiguration.action == 'próbkowanie':
            self.receivedSingal = samples
        elif samplingConfiguration.action == 'kwantyzacja z zaokrągleniem':
            self.receivedSingal = opr.quantizate(samplingConfiguration.quantizationBits, samples)
        elif samplingConfiguration.action == 'interpolacja pierwszego rzędu':
            self.receivedSingal = opr.fohInterpolateArray(signal.timeline, signal.getTime(), samples,
                                                          samplingConfiguration.numberOfSamples)
        elif samplingConfiguration.action == 'rekonstrukcja sinc':
            self.receivedSingal = opr.sincInterpolateArray(signal.timeline, signal.getTime(), samples,
                                                           samplingConfiguration.numberOfSamples)

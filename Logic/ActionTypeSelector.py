import Logic.Operations as opr


class ActionTypeSelector:

    def __init__(self, signal, samplingConfiguration):
        self.sampling = opr.sampling(signal, samplingConfiguration.samplingPeriod)
        self.actionResult = self.setType(signal, samplingConfiguration)

    def setType(self, signal, samplingConfiguration):
        if samplingConfiguration.action == 'próbkowanie':
            return self.sampling[1]
        elif samplingConfiguration.action == 'kwantyzacja z zaokrągleniem':
            samples = opr.sampling(signal, samplingConfiguration.samplingPeriod)
            return opr.quantizate(samplingConfiguration.quantizationBits, samples[1])
        elif samplingConfiguration.action == 'ekstrapolacja pierwszego rzędu':
            samples = opr.sampling(signal, samplingConfiguration.samplingPeriod)
            return opr.fohExtrapolateArray(signal.timeline, samples[0], samples[1], samplingConfiguration.numberOfSamples)
        elif samplingConfiguration.action == 'rekonstrukcja sinc':
            samples = opr.sampling(signal, samplingConfiguration.samplingPeriod)
            return opr.sincInterpolateArray(signal.timeline, samples[0], samples[1], samplingConfiguration.numberOfSamples)

    def getActionResult(self):
        return self.actionResult

    def getSamplingResult(self):
        return self.sampling

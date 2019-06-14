import Logic.Operations as opr
import numpy as np

from Logic import Signal


class TransformationTypeSelector:
    realOutput = None
    imagOutput = None
    newSignal = None

    def __init__(self, signal, transformationConfiguration, signalConfig):
        self.setType(signal, transformationConfiguration, signalConfig)

    def setType(self, signal, transformationConfiguration, signalConfig):
        values = opr.sampling(signal, 0.066666)

        if transformationConfiguration.transformationType == 'dft':
            self.realOutput, self.imagOutput = opr.compute_dft(values[1],
                                                               np.zeros(len(values[1])))

        if transformationConfiguration.transformationType == 'fft':
            self.realOutput, self.imagOutput = opr.compute_fft(values[1],
                                                               np.zeros(len(values[1])))

        self.newSignal = Signal.Signal(signalConfig.time0, signalConfig.time, signalConfig.frequency,
                                    signalConfig.amplitude, signalConfig.numberOfSamples)

        self.newSignal.singalPoints = self.realOutput
        self.newSignal.imagPoints = self.imagOutput

    def getResultSignal(self):
        return self.newSignal


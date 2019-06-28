import Logic.Operations as opr
import numpy as np
import time as timer

from Logic import Signal


class TransformationTypeSelector:
    realOutput = None
    imagOutput = None
    newSignal = None
    duration = None

    def __init__(self, signal, transformationConfiguration, signalConfig):
        self.setType(signal, transformationConfiguration, signalConfig)

    def setType(self, signal, transformationConfiguration, signalConfig):
        values = opr.sampling(signal, 1/(transformationConfiguration.samplingFrequency))

        if transformationConfiguration.transformationType == 'dft':
            start = timer.time()
            self.realOutput, self.imagOutput = opr.compute_dft(values[1],
                                                               np.zeros(len(values[1])))
            end = timer.time()
            self.duration = end - start

        if transformationConfiguration.transformationType == 'fft':
            start = timer.time()
            self.realOutput, self.imagOutput = opr.compute_fft(values[1],
                                                               np.zeros(len(values[1])))
            end = timer.time()
            self.duration = end - start

        if transformationConfiguration.transformationType == 'dwtDb6':
            start = timer.time()
            self.realOutput, self.imagOutput = opr.computeWaveletTransform(values[1])
            end = timer.time()
            self.duration = end - start

        if transformationConfiguration.transformationType == 'inverseDft':
            start = timer.time()
            self.realOutput, self.imagOutput = opr.compute_inversedft(signal.singalPoints,
                                                              signal.imagPoints)
            end = timer.time()
            self.duration = end - start

        if transformationConfiguration.transformationType == 'inverseFft':
            start = timer.time()
            self.realOutput, self.imagOutput = opr.compute_inversefft(signal.singalPoints,
                                                              signal.imagPoints)
            end = timer.time()
            self.duration = end - start

        if transformationConfiguration.transformationType == 'inverseDwtDb6':
            start = timer.time()
            self.realOutput, self.imagOutput = opr.computeWaveletInverseTransform(signal.singalPoints,
                                                              signal.imagPoints)
            end = timer.time()
            self.duration = end - start

        self.newSignal = Signal.Signal(signalConfig.time0, signalConfig.time, signalConfig.frequency,
                                    signalConfig.amplitude, signalConfig.numberOfSamples)

        self.newSignal.singalPoints = self.realOutput
        self.newSignal.imagPoints = self.imagOutput

    def getResultSignal(self):
        return self.newSignal

    def getDuration(self):
        return self.duration


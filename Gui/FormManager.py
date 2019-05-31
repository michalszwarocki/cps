import Gui.FormSupport as fs
import Logic.SignalTypeSelector as sts
import Logic.OperationTypeSelector as ots
import matplotlib.pyplot as plt
import Logic.SignalConfiguration as configuration
import Logic.SamplingConfiguration as sampConfig
import Logic.OperationConfiguration as operConfig
import Logic.ActionTypeSelector as ats
import Logic.Metrics as met
import numpy as np
import Gui.SignalSerializator as serial
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

class FormManager:

    def readSignalConfiguration(self, which):
        t0 = float(getattr(fs, which + 'Time0Entry').get())
        time = float(getattr(fs, which + 'TimeEntry').get())
        freq = float(getattr(fs, which + 'FrequencyEntry').get())
        ampli = float(getattr(fs, which + 'AmplitudeEntry').get())
        samples = int(getattr(fs, which + 'NOSamplesEntry').get())
        infil = float(getattr(fs, which + 'InfiltratorEntry').get())
        jumpMoment = float(getattr(fs, which + 'JumpMomentEntry').get())
        poss = float(getattr(fs, which + 'PossibilityEntry').get())
        jumpSampl = int(getattr(fs, which + 'JumpSampleEntry').get())
        type = getattr(fs, which + 'TypeCombobox').get()
        noise = getattr(fs, which + 'NoiseCombobox').get()
        time1 = float(getattr(fs, which + 'Time1Entry').get())
        freq1 = float(getattr(fs, which + 'Freq1Entry').get())
        points = np.array
        if which == 'first':
            points = fs.firstPoints
        elif which == 'second':
            points = fs.secondPoints

        config = configuration.Configuration(t0, time, freq, ampli, samples, infil, jumpMoment, poss, jumpSampl, type, noise, time1, freq1)
        config.setPoints(points)
        return config

    def readSamplingConfiguration(self):
        samplingPeriod = float(fs.samplingPeriodEntry.get())
        quantizationBits = int(fs.quantizationBitsEntry.get())
        numberOfSamples = int(fs.nOSamplesEntry.get())
        action = fs.actionCombobox.get()
        config = sampConfig.SamplingConfiguration(samplingPeriod, quantizationBits, numberOfSamples, action)
        return config

    def readOperationConfiguration(self):
        operation = fs.operationCombobox.get()
        filterType = fs.filterTypeCombobox.get()
        windowType = fs.windowCombobox.get()
        mValue = int(fs.mValueEntry.get())
        foValue = float(fs.foEntry.get())
        speed = float(fs.speedEntry.get())
        distance = float(fs.distanceValueEntry.get())
        config = operConfig.OperationConfiguration(operation, filterType, windowType, mValue, foValue, speed, distance)
        return config

    def readFilterOperationConfiguration(self):
        operation = fs.filterOperationCombobox.get()
        filterType = fs.filterTypeCombobox.get()
        windowType = fs.windowCombobox.get()
        mValue = int(fs.mValueEntry.get())
        foValue = float(fs.foEntry.get())
        speed = float(fs.speedEntry.get())
        distance = float(fs.distanceValueEntry.get())
        config = operConfig.OperationConfiguration(operation, filterType, windowType, mValue, foValue, speed, distance)
        return config

    def onSignalDrawClicked(self, which):
        config = self.readSignalConfiguration(which)
        signal = sts.SignalTypeSelector(config).getSignal()
        self.setSignalAvarageValues(signal.getSignalForOperation())
        self.drawPlot(config, signal.getTime(), signal.getSignalForOperation())

    def onActionDrawClicked(self):
        signalConfig = self.readSignalConfiguration('first')
        samplingConfig = self.readSamplingConfiguration()
        signal = sts.SignalTypeSelector(signalConfig).getSignal()
        selectedAction = ats.ActionTypeSelector(signal, samplingConfig, signalConfig)

        receivedTimeline = selectedAction.getReceivedTimeline()
        receivedSignal = selectedAction.getReceivedSingnal()
        originalTimeline = selectedAction.getOriginalTimeline()
        originalSignal = selectedAction.getOriginalSignal()
        samplingX = selectedAction.getSamplingX()
        samplingY = selectedAction.getSamplingY()
        originalSignalToMetrics = selectedAction.getOriginalSignalToMetrics()

        self.setSignalAvarageValues(signal.getSignalForOperation())
        self.setMetricsValues(originalSignalToMetrics, receivedSignal, samplingConfig)
        self.drawPlotForSampling(signalConfig, originalTimeline, originalSignal, receivedTimeline, receivedSignal,
                      samplingX,  samplingY)

    def onSignalSaveClicked(self, which):
        config = self.readSignalConfiguration(which)
        signal = sts.SignalTypeSelector(config).getSignal()

        try:
            fileName = asksaveasfilename()
            serial.save(fileName, config, signal.getSignal())
        except FileNotFoundError:
            print("Nie zapisano pliku!!")

    def onSignalReadClicked(self, which):
        try:
            fileName = askopenfilename()
            configuration = serial.read(fileName)

            getattr(fs, which + 'Time0Entry').set(configuration.time0)
            getattr(fs, which + 'TimeEntry').set(configuration.time)
            getattr(fs, which + 'FrequencyEntry').set(configuration.frequency)
            getattr(fs, which + 'AmplitudeEntry').set(configuration.amplitude)
            getattr(fs, which + 'NOSamplesEntry').set(configuration.numberOfSamples)
            getattr(fs, which + 'InfiltratorEntry').set(configuration.infiltrator)
            getattr(fs, which + 'JumpMomentEntry').set(configuration.jumpMoment)
            getattr(fs, which + 'PossibilityEntry').set(configuration.possibility)
            getattr(fs, which + 'JumpSampleEntry').set(configuration.jumpSample)
            getattr(fs, which + 'TypeCombobox').set(configuration.signalType)
            getattr(fs, which + 'NoiseCombobox').set(configuration.noise)
            getattr(fs, which + 'Time1Entry').set(configuration.time1)
            getattr(fs, which + 'Freq1Entry').set(configuration.freq1)
            if which == 'first':
                fs.firstPoints = configuration.points
            elif which == 'second':
                fs.secondPoints = configuration.points

        except FileNotFoundError:
            print("Nie wybrano pliku!!")

    def onOperationDrawClicked(self):
        configFirstSignal = self.readSignalConfiguration('first')
        configSecondSignal = self.readSignalConfiguration('second')
        config = self.readOperationConfiguration()
        firstSignal = sts.SignalTypeSelector(configFirstSignal).getSignal()
        secondSignal = sts.SignalTypeSelector(configSecondSignal).getSignal()

        signal = ots.OperationTypeSelector(firstSignal, secondSignal, config).getOperationResult()
        self.setSignalAvarageValues(signal)
        self.drawPlot(None, firstSignal.getTime(), signal)

    def onOperationSaveClicked(self):
        configFirstSignal = self.readSignalConfiguration('first')
        configSecondSignal = self.readSignalConfiguration('second')
        config = self.readOperationConfiguration()
        firstSignal = sts.SignalTypeSelector(configFirstSignal).getSignal()
        secondSignal = sts.SignalTypeSelector(configSecondSignal).getSignal()
        signal = ots.OperationTypeSelector(firstSignal, secondSignal, config).getOperationResult()
        configFirstSignal.signalType = 'wynik operacji'
        configFirstSignal.noise = 'wynik operacji'

        try:
            fileName = asksaveasfilename()
            serial.save(fileName, configFirstSignal, signal)
        except FileNotFoundError:
            print("Nie zapisano pliku!!")

    def onFilterOperationDrawClicked(self):
        configFirstSignal = self.readSignalConfiguration('first')
        configSecondSignal = self.readSignalConfiguration('second')
        config = self.readFilterOperationConfiguration()
        firstSignal = sts.SignalTypeSelector(configFirstSignal).getSignal()
        secondSignal = sts.SignalTypeSelector(configSecondSignal).getSignal()

        operationSelector = ots.OperationTypeSelector(firstSignal, secondSignal, config)
        result = operationSelector.getOperationResult()

        if config.operation != 'radar':
            self.drawPlotForOperation(None, operationSelector.getFirstSignal(), operationSelector.getSecondSignal(),
                                      result[0], result[1])

        if config.operation == 'radar':
            self.setRadarValues(config.distance, result)

    def setSignalAvarageValues(self, sig):
        fs.text1Label.set(round(np.mean(sig), 3))
        fs.text2Label.set(round(np.mean(np.abs(sig)), 3))
        fs.text3Label.set(round(np.average(np.square(sig)), 3))
        fs.text4Label.set(round(np.var(sig), 3))
        fs.text5Label.set(round(np.sqrt(np.mean(np.square(sig))), 3))

    def setRadarValues(self, real, result):
        fs.realDistance.set(round(real, 3))
        fs.achievedDistance.set(round(result, 3))

    def setMetricsValues(self, originalSignal, receivedSignal, samplingConfig):
        fs.mseLabel.set(round(met.meanSquaredError(originalSignal, receivedSignal), 3))
        fs.snrLabel.set(round(met.signalToNoiseRatio(originalSignal, receivedSignal), 3))
        fs.psnrLabel.set(round(met.peakSignalToNoiseRatio(originalSignal, receivedSignal), 3))
        fs.mdLabel.set(round(met.maximumDifference(originalSignal, receivedSignal), 3))
        if samplingConfig.action == 'kwantyzacja z zaokrągleniem':
            fs.enobLabel.set(round(met.effectiveNumberOfBits(originalSignal, receivedSignal), 3))
        else:
            fs.enobLabel.set('')

    def drawPlot(self, config, x, y):
        plt.subplot(2, 1, 1)
        if config is not None and (config.signalType == 'impuls jednostkowy' or config.noise == 'impulsowy'):
            plt.plot(x, y, 'o', markersize=0.9)
        else:
            plt.plot(x, y, '-', markersize=0.9)
        plt.subplot(2, 1, 2)
        plt.hist(y, bins=10)
        plt.show()

    def drawPlotForOperation(self, config, signal1, signal2, resultX, resultY):
        plt.subplot(4, 1, 1)
        if config is not None and (config.signalType == 'impuls jednostkowy' or config.noise == 'impulsowy'):
            plt.plot(signal1.getTime(), signal1.getSignalForOperation(), 'o', markersize=0.9)
        else:
            plt.plot(signal1.getTime(), signal1.getSignalForOperation(), '-', markersize=0.9)

        plt.subplot(4, 1, 2)
        if config is not None and (config.signalType == 'impuls jednostkowy' or config.noise == 'impulsowy'):
            plt.plot(signal2.getTime(), signal2.getSignalForOperation(), 'o', markersize=0.9)
        else:
            plt.plot(signal2.getTime(), signal2.getSignalForOperation(), '-', markersize=0.9)

        plt.subplot(4, 1, 3)
        if config is not None and (config.signalType == 'impuls jednostkowy' or config.noise == 'impulsowy'):
            plt.plot(resultX, resultY, 'o', markersize=0.9)
        else:
            plt.plot(resultX, resultY, '-', markersize=0.9)

        plt.subplot(4, 1, 4)
        plt.hist(resultY, bins=10)
        plt.show()

    def drawPlotForSampling(self, config, originalX, originalY, receivedX, receivedY, samplesX, samplesY):
        plt.subplot(4, 1, 1)
        if config is not None and (config.signalType == 'impuls jednostkowy' or config.noise == 'impulsowy'):
            plt.plot(originalX, originalY, 'o', markersize=0.9)
        else:
            plt.plot(originalX, originalY, '-', markersize=0.9)

        plt.subplot(4, 1, 2)
        plt.hist(originalY, bins=10)

        plt.subplot(4, 1, 3)
        if config is not None and (config.signalType == 'impuls jednostkowy' or config.noise == 'impulsowy'):
            plt.plot(originalX, originalY, 'o', markersize=0.9)
        else:
            plt.plot(originalX, originalY, '-', markersize=0.9)
        plt.plot(samplesX, samplesY, 'o', markersize=5)

        plt.subplot(4, 1, 4)
        if config is not None and (config.signalType == 'impuls jednostkowy' or config.noise == 'impulsowy'):
            plt.plot(originalX, originalY, 'o', markersize=0.9)
        else:
            plt.plot(originalX, originalY, '-', markersize=0.9)
        plt.plot(receivedX, receivedY, '-', markersize=0.9)
        plt.show()

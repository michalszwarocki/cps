import Gui.FormSupport as fs
import Logic.SignalTypeSelector as sts
import Logic.OperationTypeSelector as ots
import matplotlib.pyplot as plt
import Logic.Configuration as configuration
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
        points = fs.points
        config = configuration.Configuration(t0, time, freq, ampli, samples, infil, jumpMoment, poss, jumpSampl, type, noise)
        config.setPoints(points)
        return config

    def onSignalDrawClicked(self, which):
        config = self.readSignalConfiguration(which)
        signal = sts.SignalTypeSelector(config).getSignal()

        self.setSignalAvarageValues(signal.getSignalForOperation())
        self.drawPlot(config, signal.getTime(), signal.getSignalForOperation())

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
            fs.points = configuration.points

        except FileNotFoundError:
            print("Nie wybrano pliku!!")

    def onOperationDrawClicked(self):
        configFirstSignal = self.readSignalConfiguration('first')
        configSecondSignal = self.readSignalConfiguration('second')
        operation = fs.operationCombobox.get()
        firstSignal = sts.SignalTypeSelector(configFirstSignal).getSignal()
        secondSignal = sts.SignalTypeSelector(configSecondSignal).getSignal()

        signal = ots.OperationTypeSelector(firstSignal, secondSignal, operation).getOperationResult()

        self.setSignalAvarageValues(signal)
        self.drawPlot(None, firstSignal.getTime(), signal)

    def onOperationSaveClicked(self):
        configFirstSignal = self.readSignalConfiguration('first')
        configSecondSignal = self.readSignalConfiguration('second')
        operation = fs.operationCombobox.get()
        firstSignal = sts.SignalTypeSelector(configFirstSignal).getSignal()
        secondSignal = sts.SignalTypeSelector(configSecondSignal).getSignal()

        signal = ots.OperationTypeSelector(firstSignal, secondSignal, operation).getOperationResult()
        configFirstSignal.signalType = 'wynik operacji'
        configFirstSignal.noise = 'wynik operacji'

        try:
            fileName = asksaveasfilename()
            serial.save(fileName, configFirstSignal, signal)
        except FileNotFoundError:
            print("Nie zapisano pliku!!")

    def setSignalAvarageValues(self, signal):
        fs.text1Label.set(round(np.mean(signal), 3))
        fs.text2Label.set(round(np.mean(np.abs(signal)), 3))
        fs.text3Label.set(round(np.average(np.square(signal)), 3))
        fs.text4Label.set(round(np.var(signal), 3))
        fs.text5Label.set(round(np.sqrt(np.mean(np.square(signal))), 3))

    def drawPlot(self, config, x, y):
        plt.subplot(2, 1, 1)
        if config is not None and (config.signalType == 'impuls jednostkowy' or config.noise == 'impulsowy'):
            plt.plot(x, y, 'o', markersize=0.9)
        else:
            plt.plot(x, y, '-', markersize=0.9)
        plt.subplot(2, 1, 2)
        plt.hist(y, bins=10)
        plt.show()

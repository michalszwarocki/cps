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

    def readFirstSignalConfiguration(self):
        t0 = float(fs.firstTime0Entry.get())
        time = float(fs.firstTimeEntry.get())
        freq = float(fs.firstFrequencyEntry.get())
        ampli = float(fs.firstAmplitudeEntry.get())
        samples = int(fs.firstNOSamplesEntry.get())
        infil = float(fs.firstInfiltratorEntry.get())
        jumpMoment = float(fs.firstJumpMomentEntry.get())
        poss = float(fs.firstPossibilityEntry.get())
        jumpSampl = int(fs.firstJumpSampleEntry.get())
        type = fs.firstTypeCombobox.get()
        noise = fs.firstNoiseCombobox.get()
        points = fs.points
        config = configuration.Configuration(t0, time, freq, ampli, samples, infil, jumpMoment, poss, jumpSampl, type, noise)
        config.setPoints(points)
        return config

    def readSecondSignalConfiguration(self):
        t0 = float(fs.secondTime0Entry.get())
        time = float(fs.secondTimeEntry.get())
        freq = float(fs.secondFrequencyEntry.get())
        ampli = float(fs.secondAmplitudeEntry.get())
        samples = int(fs.secondNOSamplesEntry.get())
        infil = float(fs.secondInfiltratorEntry.get())
        jumpMoment = float(fs.secondJumpMomentEntry.get())
        poss = float(fs.secondPossibilityEntry.get())
        jumpSampl = int(fs.secondJumpSampleEntry.get())
        type = fs.secondTypeCombobox.get()
        noise = fs.secondNoiseCombobox.get()
        points = fs.points
        config = configuration.Configuration(t0, time, freq, ampli, samples, infil, jumpMoment, poss, jumpSampl, type, noise)
        config.setPoints(points)
        return config

    def onFirstSignalDrawClicked(self):
        config = self.readFirstSignalConfiguration()
        signal = sts.SignalTypeSelector(config).getSignal()

        if signal.points.size != 0:
            fs.text1Label.set(np.mean(signal.points))
            fs.text2Label.set(np.mean(np.abs(signal.points)))
            fs.text3Label.set(np.average(np.square(signal.points)))
            fs.text4Label.set(np.var(signal.points))
            fs.text5Label.set(np.sqrt(np.mean(np.square(signal.points))))
            x = signal.getTime()
            y = signal.points

        else:
            fs.text1Label.set(np.mean(signal.getSignal()))
            fs.text2Label.set(np.mean(np.abs(signal.getSignal())))
            fs.text3Label.set(np.average(np.square(signal.getSignal())))
            fs.text4Label.set(np.var(signal.getSignal()))
            fs.text5Label.set(np.sqrt(np.mean(np.square(signal.getSignal()))))
            x = signal.getTime()
            y = signal.getSignal()

        plt.subplot(2, 1, 1)
        plt.plot(x, y, '-', markersize=0.9)
        plt.subplot(2, 1, 2)
        plt.hist(y, bins=10)
        plt.show()

    def onFirstSignalSaveClicked(self):
        config = self.readFirstSignalConfiguration()
        signal = sts.SignalTypeSelector(config).getSignal()

        fileName = asksaveasfilename()
        serial.save(fileName, config, signal.getSignal())

    def onFirstSignalReadClicked(self):
        fileName = askopenfilename()
        configuration = serial.read(fileName)
        fs.firstTime0Entry.set(configuration.time0)
        fs.firstTimeEntry.set(configuration.time)
        fs.firstFrequencyEntry.set(configuration.frequency)
        fs.firstAmplitudeEntry.set(configuration.amplitude)
        fs.firstNOSamplesEntry.set(configuration.numberOfSamples)
        fs.firstInfiltratorEntry.set(configuration.infiltrator)
        fs.firstJumpMomentEntry.set(configuration.jumpMoment)
        fs.firstPossibilityEntry.set(configuration.possibility)
        fs.firstJumpSampleEntry.set(configuration.jumpSample)
        fs.firstTypeCombobox.set(configuration.signalType)
        fs.firstNoiseCombobox.set(configuration.noise)
        fs.points = configuration.points


    def onSecondSignalSaveClicked(self):
        config = self.readSecondSignalConfiguration()
        signal = sts.SignalTypeSelector(config).getSignal()

        fileName = asksaveasfilename()
        serial.save(fileName, config, signal.getSignal())

    def onSecondSignalReadClicked(self):
        fileName = askopenfilename()
        configuration = serial.read(fileName)
        fs.secondTime0Entry.set(configuration.time0)
        fs.secondTimeEntry.set(configuration.time)
        fs.secondFrequencyEntry.set(configuration.frequency)
        fs.secondAmplitudeEntry.set(configuration.amplitude)
        fs.secondNOSamplesEntry.set(configuration.numberOfSamples)
        fs.secondInfiltratorEntry.set(configuration.infiltrator)
        fs.secondJumpMomentEntry.set(configuration.jumpMoment)
        fs.secondPossibilityEntry.set(configuration.possibility)
        fs.secondJumpSampleEntry.set(configuration.jumpSample)
        fs.secondTypeCombobox.set(configuration.signalType)
        fs.secondNoiseCombobox.set(configuration.noise)
        fs.points = configuration.points

    def onSecondSignalDrawClicked(self):
        config = self.readSecondSignalConfiguration()
        signal = sts.SignalTypeSelector(config).getSignal()

        if signal.points.size != 0:
            fs.text1Label.set(np.mean(signal.points))
            fs.text2Label.set(np.mean(np.abs(signal.points)))
            fs.text3Label.set(np.average(np.square(signal.points)))
            fs.text4Label.set(np.var(signal.points))
            fs.text5Label.set(np.sqrt(np.mean(np.square(signal.points))))
            x = signal.getTime()
            y = signal.points

        else:
            fs.text1Label.set(np.mean(signal.getSignal()))
            fs.text2Label.set(np.mean(np.abs(signal.getSignal())))
            fs.text3Label.set(np.average(np.square(signal.getSignal())))
            fs.text4Label.set(np.var(signal.getSignal()))
            fs.text5Label.set(np.sqrt(np.mean(np.square(signal.getSignal()))))
            x = signal.getTime()
            y = signal.getSignal()

        plt.subplot(2, 1, 1)
        plt.plot(x, y, '-', markersize=0.9)
        plt.subplot(2, 1, 2)
        plt.hist(y, bins=10)
        plt.show()

    def onOperationDrawClicked(self):
        configFirstSignal = self.readFirstSignalConfiguration()
        configSecondSignal = self.readSecondSignalConfiguration()
        operation = fs.operationCombobox.get()
        firstSignal = sts.SignalTypeSelector(configFirstSignal).getSignal()
        secondSignal = sts.SignalTypeSelector(configSecondSignal).getSignal()

        signal = ots.OperationTypeSelector(firstSignal, secondSignal, operation).getSignal()

        fs.text1Label.set(np.mean(signal))
        fs.text2Label.set(np.mean(np.abs(signal)))
        fs.text3Label.set(np.average(np.square(signal)))
        fs.text4Label.set(np.var(signal))
        fs.text5Label.set(np.sqrt(np.mean(np.square(signal))))

        x = firstSignal.getTime()
        y = signal

        plt.subplot(2, 1, 1)
        plt.plot(x, y, '-', markersize=0.9)
        plt.subplot(2, 1, 2)
        plt.hist(y, bins=10)
        plt.show()

    def onOperationSaveClicked(self):
        configFirstSignal = self.readFirstSignalConfiguration()
        configSecondSignal = self.readSecondSignalConfiguration()
        operation = fs.operationCombobox.get()
        firstSignal = sts.SignalTypeSelector(configFirstSignal).getSignal()
        secondSignal = sts.SignalTypeSelector(configSecondSignal).getSignal()

        signal = ots.OperationTypeSelector(firstSignal, secondSignal, operation).getSignal()
        configFirstSignal.signalType = 'wynik operacji'
        configFirstSignal.noise = 'wynik operacji'

        fileName = asksaveasfilename()
        serial.save(fileName, configFirstSignal, signal)


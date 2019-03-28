import Gui.FormSupport as fs
import Logic.SignalTypeSelector as sts
import Logic.OperationTypeSelector as ots
import matplotlib.pyplot as plt
import Logic.Configuration as configuration
import numpy as np

class FormManager:

    def readFirstSignalConfiguration(self):
        t0 = float(fs.firstTime0Entry.get())
        time = float(fs.firstTimeEntry.get())
        freq = float(fs.firstFrequencyEntry.get())
        ampli = float(fs.firstAmplitudeEntry.get())
        samples = float(fs.firstNOSamplesEntry.get())
        infil = float(fs.firstInfiltratorEntry.get())
        jumpMoment = float(fs.firstJumpMomentEntry.get())
        poss = float(fs.firstPossibilityEntry.get())
        jumpSampl = float(fs.firstJumpSampleEntry.get())
        type = fs.firstTypeCombobox.get()
        noise = fs.firstNoiseCombobox.get()
        return configuration.Configuration(t0, time, freq, ampli, samples, infil, jumpMoment, poss, jumpSampl, type, noise)

    def readSecondSignalConfiguration(self):
        t0 = float(fs.secondTime0Entry.get())
        time = float(fs.secondTimeEntry.get())
        freq = float(fs.secondFrequencyEntry.get())
        ampli = float(fs.secondAmplitudeEntry.get())
        samples = float(fs.secondNOSamplesEntry.get())
        infil = float(fs.secondInfiltratorEntry.get())
        jumpMoment = float(fs.secondJumpMomentEntry.get())
        poss = float(fs.secondPossibilityEntry.get())
        jumpSampl = float(fs.secondJumpSampleEntry.get())
        type = fs.secondTypeCombobox.get()
        noise = fs.secondNoiseCombobox.get()
        return configuration.Configuration(t0, time, freq, ampli, samples, infil, jumpMoment, poss, jumpSampl, type, noise)

    def onFirstSignalDrawClicked(self):
        config = self.readFirstSignalConfiguration()
        signal = sts.SignalTypeSelector(config).getSignal()
        plt.subplot(2, 1, 1)
        x = signal.getTime()
        y = signal.getSignal()
        print(len(y))
        plt.plot(x, y, '-', markersize=0.9)
        plt.subplot(2, 1, 2)
        plt.hist(y, bins=100)
        plt.show()
        oneperiod = signal.getSignal(one_period=True)
        print('srednia:', np.mean(oneperiod))
        print('srednia bezwzg:', np.mean(np.abs(oneperiod)))
        print('skuteczna:', np.sqrt(np.mean(np.square(oneperiod))))
        print('wariancja', np.var(oneperiod))
        print('moc srednia:', np.average(np.square(oneperiod)))

    def onSecondSignalDrawClicked(self):
        config = self.readSecondSignalConfiguration()
        signal = sts.SignalTypeSelector(config).getSignal()
        plt.subplot(2, 1, 1)
        x = signal.getTime()
        y = signal.getSignal(x)
        plt.plot(x, y, '-', markersize=0.9)
        plt.subplot(2, 1, 2)
        plt.hist(y, bins=100)
        plt.show()
        oneperiod = signal.getSignal(one_period=True)
        print('srednia:', np.mean(oneperiod))
        print('srednia bezwzg:', np.mean(np.abs(oneperiod)))
        print('skuteczna:', np.sqrt(np.mean(np.square(oneperiod))))
        print('wariancja', np.var(oneperiod))
        print('moc srednia:', np.average(np.square(oneperiod)))

    def onOperationClicked(self):
        configFirstSignal = self.readFirstSignalConfiguration()
        configSecondSignal = self.readSecondSignalConfiguration()
        operation = fs.operationCombobox.get()
        firstSignal = sts.SignalTypeSelector(configFirstSignal).getSignal()
        secondSignal = sts.SignalTypeSelector(configSecondSignal).getSignal()

        signal = ots.OperationTypeSelector(firstSignal, secondSignal, operation).getSignal()
        x = firstSignal.getTime()
        y = signal

        plt.subplot(2, 1, 1)
        plt.plot(x, y, '-', markersize=0.9)
        plt.subplot(2, 1, 2)
        plt.hist(y, bins=100)
        plt.show()

import Gui.FormSupport as fs
import Logic.SignalTypeSelector as sts
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
        type = fs.firstTypeCombobox.get()
        infil = float(fs.firstInfiltratorEntry.get())
        noise = fs.firstNoiseCombobox.get()
        jumpMoment = float(fs.firstJumpMomentEntry.get())
        return configuration.Configuration(t0, time, freq, ampli, samples, type, infil, noise, jumpMoment)

    def readSecondSignalConfiguration(self):
        t0 = float(fs.secondTime0Entry.get())
        time = float(fs.secondTimeEntry.get())
        freq = float(fs.secondFrequencyEntry.get())
        ampli = float(fs.secondAmplitudeEntry.get())
        samples = float(fs.secondNOSamplesEntry.get())
        type = fs.secondTypeCombobox.get()
        infil = float(fs.secondInfiltratorEntry.get())
        noise = fs.secondNoiseCombobox.get()
        jumpMoment = float(fs.secondJumpMomentEntry.get())
        return configuration.Configuration(t0, time, freq, ampli, samples, type, infil, noise, jumpMoment)

    def onFirstSignalDrawClicked(self):
        config = self.readFirstSignalConfiguration()
        signal = sts.SignalTypeSelector(config).getSignal()
        plt.subplot(2, 1, 1)
        x = signal.getTime()
        y = signal.getSignal()
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
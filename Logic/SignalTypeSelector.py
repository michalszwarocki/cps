import Logic.Signal as Signal


class SignalTypeSelector:
    def __init__(self, configuration):
        self.signal = Signal.Signal(configuration[0], configuration[1], configuration[2], configuration[3], configuration[4])
        self.setType(configuration[5], configuration[6])
        self.setNoise(configuration[7])

    def setType(self, config, infil):
        if (config == 'sinus'):
            self.signal.setAsSin()
        elif (config == 'sinus wyprostowany jednopołówkowo'):
            self.signal.setHalfStraight()
        elif (config == 'sinus wyprostowany dwupołówkowo'):
            self.signal.setFullStraight()
        elif config == 'prostokątny':
            self.signal.setAsRectangle(infil)
        elif config == 'prostokątny symetryczny':
            self.signal.setAsSyncRectangle(infil)

    def setNoise(self, noise):
        if(noise == 'gaussowski'):
            self.signal.setGaussNoise(self.signal.amp)
        elif(noise == 'o rozkładzie jednostajnym'):
            self.signal.setUniformNoise()
        elif(noise == 'impulsowy'):
            self.signal
    def getSignal(self):
        return self.signal

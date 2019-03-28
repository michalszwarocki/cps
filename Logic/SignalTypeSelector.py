import Logic.Signal as Signal


class SignalTypeSelector:

    def __init__(self, configuration):
        self.signal = Signal.Signal(configuration.time0, configuration.time, configuration.frequency,
                                    configuration.amplitude, configuration.numberOfSamples)
        self.setType(configuration)
        self.setNoise(configuration)

    def setType(self, config):
        if config.signalType == 'sinus':
            self.signal.setAsSin()
        elif config.signalType == 'sinus wyprostowany jednopołówkowo':
            self.signal.setHalfStraight()
        elif config.signalType == 'sinus wyprostowany dwupołówkowo':
            self.signal.setFullStraight()
        elif config.signalType == 'prostokątny':
            self.signal.setAsRectangle(config.infiltrator)
        elif config.signalType == 'prostokatny symetryczny':
            self.signal.setAsSyncRectangle(config.infiltrator)
        elif config.signalType == 'skok jednostkowy':
            self.signal.setSingleJump(config.jumpMoment)
        elif config.signalType == 'impuls jednostkowy':
            self.signal.setImpulse(config.jumpSample)

    def setNoise(self, config):
        if config.noise == 'gaussowski':
            self.signal.setGaussNoise(self.signal.amp)
        elif config.noise == 'o rozkładzie jednostajnym':
            self.signal.setUniformNoise()
        elif config.noise == 'impulsowy':
            self.signal.setImpulseNoice(config.possibility)

    def getSignal(self):
        return self.signal

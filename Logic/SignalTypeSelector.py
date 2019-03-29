import Logic.Signal as Signal


class SignalTypeSelector:

    def __init__(self, configuration):
        self.signal = Signal.Signal(configuration.time0, configuration.time, configuration.frequency,
                                    configuration.amplitude, configuration.numberOfSamples)
        self.setType(configuration)
        self.setNoise(configuration)

    def setType(self, config):
        print(config.signalType)
        if config.signalType == 'sinus':
            self.signal.setAsSin()
        elif config.signalType == 'sinus wyprostowany jednopolowkowo':
            self.signal.setHalfStraight()
        elif config.signalType == 'sinus wyprostowany dwupolowkowo':
            self.signal.setFullStraight()
        elif config.signalType == 'prostokatny':
            self.signal.setAsRectangle(config.infiltrator)
        elif config.signalType == 'prostokatny symetryczny':
            self.signal.setAsSyncRectangle(config.infiltrator)
        elif config.signalType == 'trojkatny':
            self.signal.setTriangle(config.infiltrator)
        elif config.signalType == 'skok jednostkowy':
            self.signal.setSingleJump(config.jumpMoment)
        elif config.signalType == 'impuls jednostkowy':
            self.signal.setImpulse(config.jumpSample)
        elif config.signalType == 'wynik operacji':
            self.signal.setAsOperation(config.points)

    def setNoise(self, config):
        if config.noise == 'gaussowski':
            self.signal.setGaussNoise(self.signal.amp)
        elif config.noise == 'o rozkladzie jednostajnym':
            self.signal.setUniformNoise()
        elif config.noise == 'impulsowy':
            self.signal.setImpulseNoice(config.possibility)

    def getSignal(self):
        return self.signal

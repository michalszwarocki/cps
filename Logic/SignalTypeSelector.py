import Logic.Signal as Signal


class SignalTypeSelector:
    def __init__(self, configuration):
        self.signal = Signal.Signal(configuration[0], configuration[1], configuration[2], configuration[3], configuration[4])
        self.setType(configuration[5])

    def setType(self, config):
        if (config == 'sinus'):
            self.signal.setAsSin()
        elif (config == 'sinus wyprostowany jednopołówkowo'):
            self.signal.setHalfStraight()
        elif (config == 'sinus wyprostowany dwupołówkowo'):
            self.signal.setFullStraight()

    def getSignal(self):
        return self.signal

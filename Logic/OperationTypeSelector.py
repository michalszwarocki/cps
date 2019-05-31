import Logic.Operations as opr


class OperationTypeSelector:

    def __init__(self, firstSignal, secondSignal, configuration):
        self.firstSignal = firstSignal
        self.secondSignal = secondSignal
        self.configuration = configuration
        self.operationResult = self.setType(firstSignal, secondSignal, configuration)

    def setType(self, firstSignal, secondSignal, config):
        if config.operation == 'dodawanie':
            return opr.addTwoSignals(firstSignal, secondSignal)
        elif config.operation == 'odejmowanie':
            return opr.substractTwoSignals(firstSignal, secondSignal)
        elif config.operation == 'mnożenie':
            return opr.multiplyTwoSignals(firstSignal, secondSignal)
        elif config.operation == 'dzielenie':
            return opr.divideTwoSignals(firstSignal, secondSignal)
        elif config.operation == 'splot':
            return opr.convolve(firstSignal, secondSignal)
        elif config.operation == 'korelacja':
            return opr.correlate(firstSignal, secondSignal)
        elif config.operation == 'filtrowanie':
            result, filter = opr.filtering(firstSignal, config.filterType, config.windowType, config.mValue, config.foValue)
            self.secondSignal = filter
            return result
        elif config.operation == 'radar':
            result = opr.radar2(firstSignal, secondSignal, config.speed, config.distance)
            return result

    def getOperationResult(self):
        return self.operationResult

    def getFirstSignal(self):
        return self.firstSignal

    def getSecondSignal(self):
        return self.secondSignal

    def getConfiguration(self):
        return self.configuration

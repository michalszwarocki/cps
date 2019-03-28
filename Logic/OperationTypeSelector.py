import Logic.Signal as Signal


class OperationTypeSelector:

    def __init__(self, firstSignal, secondSignal, operation):
        self.signal = self.setType(firstSignal, secondSignal, operation)

    def setType(self, firstSignal, secondSignal, operation):
        if operation == 'dodawanie':
            return firstSignal.add(secondSignal)
        elif operation == 'odejmowanie':
            return firstSignal.sub(secondSignal)
        elif operation == 'mnożenie':
            return firstSignal.mul(secondSignal)
        elif operation == 'dzielenie':
            return firstSignal.div(secondSignal)

    def getSignal(self):
        return self.signal

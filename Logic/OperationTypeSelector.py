import Logic.Operations as opr


class OperationTypeSelector:

    def __init__(self, firstSignal, secondSignal, operation):
        self.operationResult = self.setType(firstSignal, secondSignal, operation)

    def setType(self, firstSignal, secondSignal, operation):
        if operation == 'dodawanie':
            return opr.addTwoSignals(firstSignal, secondSignal)
        elif operation == 'odejmowanie':
            return opr.substractTwoSignals(firstSignal, secondSignal)
        elif operation == 'mnożenie':
            return opr.multiplyTwoSignals(firstSignal, secondSignal)
        elif operation == 'dzielenie':
            return opr.divideTwoSignals(firstSignal, secondSignal)

    def getOperationResult(self):
        return self.operationResult

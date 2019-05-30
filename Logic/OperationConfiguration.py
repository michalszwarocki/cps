import numpy as np


class OperationConfiguration:
    operation: str
    filterType: str
    windowType: str
    mValue: int
    foValue: float

    def __init__(self, operation, filterType, windowType, mValue, foValue):
        self.operation = operation
        self.filterType = filterType
        self.windowType = windowType
        self.mValue = mValue
        self.foValue = foValue




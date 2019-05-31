import numpy as np


class OperationConfiguration:
    operation: str
    filterType: str
    windowType: str
    mValue: int
    foValue: float
    speed: float
    distance: float

    def __init__(self, operation, filterType, windowType, mValue, foValue, speed, distance):
        self.operation = operation
        self.filterType = filterType
        self.windowType = windowType
        self.mValue = mValue
        self.foValue = foValue
        self.speed = speed
        self.distance = distance




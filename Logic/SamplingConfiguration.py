class SamplingConfiguration:
    samplingPeriod: float
    quantizationBits: int
    numberOfSamples: int
    action: str

    def __init__(self, sampPeriod, quantBits, numOfSamples, action):
        self.samplingPeriod = sampPeriod
        self.quantizationBits = quantBits
        self.numberOfSamples = numOfSamples
        self.action = action

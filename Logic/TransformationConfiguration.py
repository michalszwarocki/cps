class TransformationConfiguration:
    transformationType: str
    plotType: str
    samplingFrequency: float

    def __init__(self, transformationType, plotType, samplingFrequency):
        self.transformationType = transformationType
        self.plotType = plotType
        self.samplingFrequency = samplingFrequency
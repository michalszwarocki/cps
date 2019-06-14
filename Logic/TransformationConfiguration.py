class TransformationConfiguration:
    transformationType: str
    plotType: str

    def __init__(self, transformationType, plotType):
        self.transformationType = transformationType
        self.plotType = plotType
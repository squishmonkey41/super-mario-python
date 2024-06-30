class LeftRightConstrainedTrait:
    def __init__(self, min, max):
        self.xMin = min
        self.xMax = max

    def reset(self):
        self.xMin = None
        self.xMax = None
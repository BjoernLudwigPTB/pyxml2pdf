from reportlab.platypus import Flowable


class FlowableRect(Flowable):
    def __init__(self, width, height, filled):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.filled = filled

    def draw(self):
        self.canv.rect(0, 0, self.width, self.height, fill=self.filled)

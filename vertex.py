class Vertex:
    def __init__(self, label):
        self.inDegree = 0
        self.outDegree = 0
        self.label = label

    def getDegree(self):
        return self.inDegree + self.outDegree
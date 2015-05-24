class Edge:
    def __init__(self, orig, dest, **kwargs):
        self.directed = False
        self.origin = None
        self.destination = None
        self.label = ""
        self.weight = 0
        if kwargs["directed"]:
            self.directed = True
        # expecting vertices as arguments
        self.setOrigin(orig)
        self.setDestination(dest)

    def setOrigin(self, vertex):
        self.origin = vertex
        if self.directed:
            vertex.outDegree += 1

    def setDestination(self, vertex):
        self.destination = vertex
        if self.directed:
            vertex.inDegree += 1

    def getIncidentVertexPair(self):
        if self.origin is not None and self.destination is not None:
            return (self.origin.label , self.destination.label)
        return None
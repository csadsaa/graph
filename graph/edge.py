class Edge:
    def __init__(self, orig, dest, **kwargs):
        self.directed = False
        self.origin = None
        self.destination = None
        self.label = ""
        self.weight = 0
        if "directed" in kwargs:
            self.directed = kwargs["directed"]
        if "label" in kwargs:
            self.label = kwargs["label"]
        if "weight" in kwargs:
            self.weight = kwargs["weight"]
        # expecting vertices as arguments
        self.setOrigin(orig)
        self.setDestination(dest)

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return '{}: {} --{}--> {}'.format(self.__class__.__name__,
                                          self.origin.label,
                                          self.weight,
                                          self.destination.label)

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

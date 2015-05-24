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
            vertex.incOut()

    def setDestination(self, vertex):
        self.destination = vertex
        if self.directed:
            vertex.incIn()
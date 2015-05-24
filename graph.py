from edge import Edge
from vertex import Vertex


class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = {}

    # assuming only 2 vertex labels are given
    def addEdge(self, orig, dest, **kwargs):
        # can only add an edge if the vertices already exist in the graph
        if orig not in self.vertices or dest not in self.vertices:
            return
        self.edges.append(Edge(
            Vertex(orig),
            Vertex(dest),
            **kwargs
        ))

    # assume several vertex labels are given
    # will overwrite vertex if already in dictionary
    def addVertex(self, *args):
        for label in args:
            self.vertices[label] = Vertex(label)

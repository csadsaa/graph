from edge import Edge
from vertex import Vertex
import graphviz


class Graph:
    def __init__(self, directed, label):
        self.directed = directed
        self.label = label
        self.edges = []
        self.vertices = {}

    # assuming only 2 vertex labels are given
    def addEdge(self, orig, dest):
        # can only add an edge if the vertices already exist in the graph
        if orig not in self.vertices or dest not in self.vertices:
            return
        self.edges.append(Edge(
            Vertex(orig),
            Vertex(dest),
            directed=self.directed
        ))

    # assume several vertex labels are given
    # will overwrite vertex if already in dictionary
    def addVertex(self, *args):
        for label in args:
            self.vertices[label] = Vertex(label)

    def render(self):
        if not self.directed:
            dot = graphviz.Graph(name=self.label, engine='neato', format='png')
        else:
            dot = graphviz.Digraph(name=self.label, engine='neato', format='png')
        for e in self.edges:
            if e.weight == 0:
                dot.edge(e.origin.label, e.destination.label, label=e.label)
            else:
                dot.edge(e.origin.label, e.destination.label, label=e.weight)
        # in the case of there being no edges but some vertices, render the vertices
        if len(self.edges) == 0 and len(self.vertices) > 0:
            for key, value in self.vertices.items():
                dot.node(key, label=value.label)
        dot.render('../test-output/' + self.label + '.gv', view=True)
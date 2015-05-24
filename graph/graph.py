from graph.edge import Edge
from graph.vertex import Vertex
import graphviz


class Graph:
    # expect vertices to simply be an enurable of vertex labels
    def __init__(self, vertices=None, label="", directed=False):
        self.directed = directed
        self.label = label
        self.edges = []
        if vertices:
            self.vertices = dict([(label, Vertex(label)) for label in vertices])
        else:
            self.vertices = {}

    # size of a graph is the number of vertices it has
    def __len__(self):
        return len(self.vertices)

    # either one edge is specified
    # or 2 vertex labels are specified
    def addEdge(self, orig, dest=None, **kwargs):
        if dest is not None:
            # if either of the vertices are not already in the graph, add them
            if orig not in self.vertices:
                self.addVertices(orig)
            if dest not in self.vertices:
                self.addVertices(dest)
            kwargs["directed"] = self.directed
            self.edges.append(Edge(
                self.vertices[orig],
                self.vertices[dest],
                **kwargs
            ))
        else:
            if orig.origin not in self.vertices:
                self.addVertices(orig.origin)
            if orig.destination not in self.vertices:
                self.addVertices(orig.destination)
            self.edges.append(orig)

    # assume several vertex labels are given will overwrite vertex if already in dictionary
    def addVertices(self, *args):
        for label in args:
            self.vertices[label] = Vertex(label)

    # return a graph that is the union of this graph and another one
    def getUnion(self, other):
        newOne = Graph(self.vertices.copy(), self.label) # copy self vertices
        newOne.vertices.update(other) # add other vertices
        newOne.edges = list(set(self.edges + other.edges)) # get the unique edges
        return newOne

    def render(self, filename=None):
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
        if not filename:
            filename = self.label
        dot.render('../test-output/' + filename + '.gv', view=True)

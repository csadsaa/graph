from graph.graph import Graph

def KruskalMST(g):
    c = []  # empty set of clusters
    for v in g.vertices:
        c.append(Graph(v))
    q = sorted(g.edges, reverse=True) # use the edge weights as keys
    T = Graph() # empty tree
    counter = 0
    while len(T) < len(g) - 1:
        counter += 1
        e = q.pop()
        origGraph = graphWithVertex(c, e.origin)
        destGraph = graphWithVertex(c, e.destination)
        if origGraph is not None and destGraph is not None:
            if origGraph is not destGraph:
                T.addEdge(e)
                # remove the graphs for union
                c.remove(origGraph)
                c.remove(destGraph)
                c.append(origGraph.getUnion(destGraph))
        T.render(counter)
    return T

# takes an enumerable of graphs and a vertex
def graphWithVertex(graphs, vertex):
    for graph in graphs:
        if vertex.label in graph.vertices:
            return graph
    return None
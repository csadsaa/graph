# this is a tutorial script to show you how you can use the tools to generate graphs, process them with algorithms
# and output the rendered results to a folder of your choice

# give the interpreter the path to the modules
import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))

# first import the definitions and classes you'll be using
from algorithms.kruskal import *

# create a new graph
g = Graph()

# add some edges
g.addEdge('SFO','ORD',weight=1846)
g.addEdge('SFO','BOS',weight=2704)
g.addEdge('SFO','LAX',weight=337)
g.addEdge('SFO','DFW',weight=1464)
g.addEdge('LAX','DFW',weight=1235)
g.addEdge('LAX','MIA',weight=2342)
g.addEdge('DFW','MIA',weight=1121)
g.addEdge('DFW','JFK',weight=1391)
g.addEdge('DFW','ORD',weight=802)
g.addEdge('MIA','BWI',weight=946)
g.addEdge('MIA','JFK',weight=1090)
g.addEdge('MIA','BOS',weight=1258)
g.addEdge('ORD','BWI',weight=621)
g.addEdge('ORD','JFK',weight=740)
g.addEdge('ORD','PVD',weight=849)
g.addEdge('ORD','BOS',weight=867)

g.render('full')

# run the kruskal minimum spanning tree algorithm
KruskalMST(g)
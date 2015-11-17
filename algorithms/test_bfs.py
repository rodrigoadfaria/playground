from graph import graph
from graph.search import bfs

g = graph.Graph()
g.read_graph("graph/in/bfs-test.grp")

(d,p) = bfs(g, 2)

print d
print p

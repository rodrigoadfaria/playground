from graph import graph
from graph.mst import kruskal_mst

g = graph.Graph()
g.read_graph("graph/in/kruskal-test.grp")

mst = kruskal_mst(g)

for e in mst:
	print "(" + str(e.v.index) + ", " + str(e.u.index) + ") = " + str(e.weight) 

from graph.mst import prim_mst
from graph import graph

g = graph.Graph()
g.read_graph("graph/in/kruskal-test.grp")

p = prim_mst(g, 0)

for i in range(0, len(p)):
    if p[i] is not None:
        print "(", i, ",", p[i], ")"

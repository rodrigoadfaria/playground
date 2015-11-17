from graph import graph
from graph.search import dfs

g = graph.Graph()
g.read_graph("graph/in/dfs-test.grp")

(d,f,p) = dfs(g)

g.print_graph()

print d
print f
print p

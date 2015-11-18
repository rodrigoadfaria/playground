from algorithms import sort_edges
from datastructure import DisjointSets

def kruskal_mst(graph):
	A = []
	dsets = DisjointSets(len(graph.vertices))
	edges = graph.get_edges_list()
	sort_edges(edges)
	
	for v in graph.vertices:
		dsets.make_set(v.index)
	
	for e in edges:
		if dsets.find_set(e.v.index) != dsets.find_set(e.u.index):
			A.append(e)
			dsets.union(e.v.index, e.u.index)

	return A
		
	

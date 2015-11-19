from algorithms import sort_edges
from datastructure import DisjointSets
import sys

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

def prim_mst(graph, s):
	Q = Heap(len(graph.vertices))
	p = [int] * len(graph.vertices)

	for v in graph.vertices:
		Q.v[v.index] = sys.maxint

	Q.v[s] = 0
	Q.build_heap()

	while not Q.is_empty():
		v = Q.extract_min()
		for edge in v.edges:
			u = edge.u
			if

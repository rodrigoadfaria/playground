from datastructure import Queue
import sys

class Color:
	White = 0
	Grey = 1
	Black = 2

def bfs(graph, s):
	color = [Color] * len(graph.vertices)
	d = [int] * len(graph.vertices)
	p = [int] * len(graph.vertices)
	Q = Queue()

	for v in graph.vertices:
		color[v.index] = Color.White
		d[v.index] = sys.maxint
		p[v.index] = None

	color[s] = Color.Grey
	d[s] = 0
	Q.enqueue(s)

	while not Q.is_empty():
		v = graph.vertices[Q.front()]
		for edge in v.edges:
			u = edge.u
			if color[u.index] == Color.White:				
				color[u.index] = Color.Grey
				p[u.index] = v.index
				d[u.index] = d[v.index] + 1
				Q.enqueue(u.index)

		Q.dequeue()
		color[v.index] = Color.Black

	return (d, p)

def dfs(graph):
	color = [Color] * len(graph.vertices)
	d = [int] * len(graph.vertices)
	f = [int] * len(graph.vertices)
	p = [int] * len(graph.vertices)
	time = [0]
	
	def dfs_visit(v):
		color[v.index] = Color.Grey
		time[0] = time[0] + 1
		d[v.index] = time[0]
		for edge in v.edges:
			u = edge.u
			if color[u.index] == Color.White:
				p[u.index] = v.index
				dfs_visit(u)
		
		color[v.index] = Color.Black
		time[0] += 1
		f[v.index] = time[0]
	
	for v in graph.vertices:
		color[v.index] = Color.White
		p[v.index] = None

	for v in graph.vertices:
		if color[v.index] == Color.White:
			dfs_visit(v)
		
	return d, f, p
		




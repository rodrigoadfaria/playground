class Queue:
	def	__init__(self):
		self.q = []

	def enqueue(self, element):
		self.q.append(element)

	def dequeue(self):		
		return self.q.pop(0)
	
	def is_empty(self):
		return len(self.q) == 0

	def front(self):
		return self.q[0]


class DisjointSets:
	def __init__(self, size):
		self.parent = [int] * size
		self.rank = [int] * size

	def make_set(self, x):
		self.parent[x] = x
		self.rank[x] = 0

	def find_set(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find_set(self.parent[x])

		return self.parent[x]

	def union(self, x, y):
		xRoot = self.find_set(x)
		yRoot = self.find_set(y)
		
		if xRoot != yRoot:
			if self.rank[xRoot] < self.rank[yRoot]:
				self.parent[xRoot] = yRoot
			elif self.rank[xRoot] > self.rank[yRoot]:
				self.parent[yRoot] = xRoot
			else:
				self.parent[yRoot] = xRoot
				self.rank[xRoot] += 1

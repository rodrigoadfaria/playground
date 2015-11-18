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


class Heap:
	def __init__(self, size):
		self.v = [int] * size
		self.size = size

	def down_heap(self, i, m):
		l = 2*i
		r = 2*i+1
		minimum = -1
		if l <= m  and self.v[l] < self.v[i]:
			minimum = l
		else:
			minimum = i

		if r <= m and self.v[r] < self.v[maximum]:
			minimum = r

		if minimum != i:
			self.v[i], self.v[minimum] = self.v[minimum], self.v[i]
			down_heap(minimum, m)
	
	def build_heap(self):
		m = self.size 
		for i in range(size/2, 0, -1):
			down_heap(i, m)	

	def extract_min(self):
		element = self.v[0]
		self.v[0] = self.v[size-1]
		self.size -= 1
		self.down_heap(0, self.size-1)

	def is_empty():
		return self.size == 0


from heapq import heappush, heappop, heapify
import itertools

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
	REMOVED = -1
	def __init__(self, size):
		self.heap = []
		self.finder = {}
		self.counter = itertools.count()

	def add_or_update_item(self, elementIndex, priority=0):
		if elementIndex in self.finder:
			self.__remove_item(elementIndex)

		count = next(self.counter)
		entry = [priority, count, elementIndex]
		self.finder[elementIndex] = entry
		heappush(self.heap, entry)

	def extract_min(self):
		while self.heap:
			(priority, count, elementIndex) = heappop(self.heap)
			if elementIndex is not self.REMOVED:
				del self.finder[elementIndex]
				return elementIndex
		raise KeyError("pop from an empty priority queue")

	def __remove_item(self, elementIndex):
		entry = self.finder.pop(elementIndex)
		entry[-1] = self.REMOVED

	def key(self, elementIndex):
		entry = self.finder[elementIndex]
		return self.heap[entry[-1]]

	def contains(self, elementIndex):
		return elementIndex in self.finder

	def is_empty(self):
		return len(self.finder) == 0

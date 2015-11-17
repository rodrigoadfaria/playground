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

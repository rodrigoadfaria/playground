from Queue import Queue

class TreeNode:
	def __init__(self, name, conviviality):
		self.conviviality = conviviality
		self.name = name
		self.left_child = None
		self.right_sibling = None
		self.parent = None
		
	def children(self):
		vChildren = []		
		currentNode = self.left_child	
		
		while currentNode is not None:			
			vChildren.append(currentNode)
			currentNode = currentNode.right_sibling
									
		return vChildren
	
	def grandChildren(self):
		vGrandChildren = []
		children = self.children()
		for child in children:
			gChildren = child.children()
			vGrandChildren.extend(gChildren)
		return vGrandChildren
		
def init_solution_table(root):
	q = Queue()
	table = {}
	q.put(root)
	
	while not q.empty():
		currentNode = q.get()
		table[currentNode.name] = None
		children = currentNode.children()
		
		for child in children:
			q.put(child)		
	
	return table

def plan_company_party(root):
	c = init_solution_table(root)
	return plan_company_party_memoized(root, c)	

def plan_company_party_memoized(root, c):
	if root is None:
		return 0
	if c[root.name] is not None:
		return c[root.name]
	else:
		children_sum = 0
		grandChildren_sum = root.conviviality
		children = root.children()
		grandChildren = root.grandChildren()		
		
		for grandChild in grandChildren:
			grandChildren_sum += plan_company_party_memoized(grandChild, c)
		
		for child in children:
			children_sum += plan_company_party_memoized(child, c)
			
		if grandChildren_sum > children_sum:
			c[root.name] = grandChildren_sum
		else:
			c[root.name] = children_sum
			
		return c[root.name]
		
# tree format, one node by line on the following format:
# node name, node conviviality, left child, right sibling, parent
input_tree = """1 2 2 None None
2 5 4 3 1
3 3 6 None 1
4 3 8 5 2
5 2 None None 2
6 1 None 7 3
7 1 None None 3
8 1 None None 4"""
	
def convert_string_into_tree(text):
	lines = text.split("\n")
	vertices = {}
	
	for line in lines:
		itens = line.split(" ")
		vertices[itens[0]] = TreeNode(itens[0], float(itens[1]))
		
	for line in lines:
		itens = line.split(" ")
		node = vertices[itens[0]]
		if itens[2] != "None":
			node.left_child = vertices[itens[2]]
		if itens[3] != "None":
			node.right_sibling = vertices[itens[3]]
		if itens[4] != "None":
			node.parent = vertices[itens[4]]
	
	return vertices[lines[0].split(" ")[0]]
		
		
def main():
	tree_root = convert_string_into_tree(input_tree)	
	solution = plan_company_party(tree_root)
	print solution
		

if __name__ == "__main__":
	main()

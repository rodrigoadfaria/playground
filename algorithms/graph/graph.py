class Vertex:
   def __init__(self, index, weight):
      self.index = index
      self.weight = weight
      self.edges = []
   
   def add_edge(self, v, weight):
      self.edges.append(Edge(self, v, weight))
   
class Edge:
   def __init__(self, v, u, weight):
      self.v = v
      self.u = u
      self.weight = weight
      
class Graph:
   def __init__(self):            
      self.vertices = []
      
   def add_vertex(self, v):
      self.vertices.append(v)
   
   def add_edge(self, v, u, weight):
      v.add_edge(u, weight)
         
   def add_undirected_edge(self, v, u, weight):
      v.add_edge(u, weight)
      u.add_edge(v, weight)
   
   def get_edges_list(self):
		edges = []		
		for v in self.vertices:
			edges += v.edges

		return edges
			        
   def read_graph(self, filename):
      grp_file = open(filename, "r")      
      first_line = grp_file.readline()
      
      is_vertex_weighted = "v" in first_line
      is_edge_weighted = "e" in first_line
      num_vertices = int(first_line.split()[0])
      
      for i in range(0, num_vertices):
         self.add_vertex(Vertex(i, 0))         
         
      for i in range(0, num_vertices):
         current_line = grp_file.readline()
         edges = current_line.split()
         
         for e in edges:
            self.add_edge(self.vertices[i], self.vertices[int(e)], 0)
      
      if is_vertex_weighted:
         self.__read_vertex_weight(grp_file, num_vertices)
      
      if is_edge_weighted:
         self.__read_edge_weight(grp_file, num_vertices)
         
      grp_file.close()
         
   def __read_vertex_weight(self, grp_file, num_vertices):
      grp_file.readline()
      line = grp_file.readline()
      weights = line.split()
      
      for i in range(0, num_vertices):
         self.vertices[i].weight = float(weights[i])
      
   def __read_edge_weight(self, grp_file, num_vertices):
      grp_file.readline()
            
      for i in range(0, num_vertices):
         current_line = grp_file.readline()
         weights = current_line.split()
         j = 0
         
         for w in weights:
            self.vertices[i].edges[j].weight = int(w)
            j += 1
   
   def print_graph(self):
      for v in self.vertices:
         print("w(" + str(v.index) + "):" + str(v.weight))
         for e in v.edges:
            print("\tw(" + str(e.v.index) + ", " + str(e.u.index) + ") = " + str(e.weight))
   
         

def sort_edges(edges):
	quicksort(edges, 0, len(edges)-1)

def quicksort(edges, p, r):
	if p < r:
		q = partition(edges, p, r)
		quicksort(edges, p, q-1)
		quicksort(edges, q+1, r)

def partition(edges, p, r):
	x = edges[r].weight
	i = p-1
	for j in range(p, r):
		if edges[j].weight <= x:
			i += 1
			edges[i], edges[j] = edges[j], edges[i]
	
	edges[i+1], edges[r] = edges[r], edges[i+1]

	return i+1


def partition(A, p, r):
	'''
	Do the partitioning of the given array according a selected pivot.
	'''
	x = A[r] # pivot
	i = p - 1
	# the original pseudocode goes until r - 1 due indexing
	for j in range (p, r):
		if A[j] <= x:
			i = i + 1
			aux = A[i]
			A[i] = A[j]
			A[j] = aux
	aux = A[i + 1]
	A[i + 1] = A[r]
	A[r] = aux

	return i + 1

def quicksort(A, p, r):
	'''
	Original implementation of quicksort.
	'''
	if p < r:
		q = partition(A, p, r)
		quicksort(A, p, q - 1)
		quicksort(A, q + 1, r)

def tail_quicksort(A, p, r):
	'''
	Original implementation of quicksort replacing the tail recursion by a loop.
	'''
	while p < r:
		q = partition(A, p, r)
		tail_quicksort(A, p, q - 1)
		p = q + 1

def half_tail_quicksort(A, p, r):
	'''
	Original implementation of quicksort replacing the tail recursion by a loop
	and checking the partitions to do recursion with the smallest one.
	'''
	while p < r:
		q = partition(A, p, r)
		if (q - p) < (r - q):
			half_tail_quicksort(A, p, q - 1)
			p = q + 1
		else:
			half_tail_quicksort(A, q + 1, r)
			r = q - 1

def main():
	A = [2,4,5,7,1,3,8,6,-2]
	print (A)
	quicksort(A, 0, len(A)-1)
	print ('quicksort sort', A)

	A = [2,4,5,7,1,3,8,6,-2]
	print (A)
	tail_quicksort(A, 0, len(A)-1)
	print ('tail_quicksort sort', A)

	A = [2,4,5,7,1,3,8,6,-2]
	print (A)
	half_tail_quicksort(A, 0, len(A)-1)
	print ('half_tail_quicksort sort', A)

if __name__=="__main__":
    main() 
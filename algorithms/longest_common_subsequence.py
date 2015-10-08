import numpy as np
import quicksort as qs

def lcs_length(X, Y):
	'''
	Computes the longest common subsequence of two vectors X and Y, keeping
	the size of those subsequences in a matrix c and the path to the longest
	subsequence in another matrix of same size b.
	We sum up 1 to m and n due to indexing of the original algorithm.
	
	The characters are:
	D - diagonal
	U - upper
	L - left

	Based on CLRS 2ed p353.
	'''
	m = len(X) + 1
	n = len(Y) + 1

	c = [[None for j in range(n)] for i in range(m)] # initializing the c matrix of size mxn
	b = [[None for j in range(n)] for i in range(m)] # initializing the b matrix of size mxn

	for i in range(1, m):
		c[i][0] = 0
	for j in range(0, n):
		c[0][j] = 0

	for i in range(1, m):
		for j in range(1, n):
			if X[i-1] == Y[j-1]: # once we use the the length m and n, we have to subtract 1 to get all values in X, Y vectors
				c[i][j] = c[i-1][j-1] + 1
				b[i][j] = 'D'
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i][j] = 'U'
			else:
				c[i][j] = c[i][j-1]
				b[i][j] = 'L'

	return c, b

def lcs_max_sum_length(X, Y):
	'''
	Computes the longest common subsequence of two vectors X and Y, keeping
	the size of those subsequences in a matrix c and the path to the longest
	subsequence in another matrix of same size b.
	We sum up 1 to m and n due to indexing of the original algorithm.
	
	The characters are:
	D - diagonal
	U - upper
	L - left

	Based on CLRS 2ed p353.
	'''
	m = len(X) + 1
	n = len(Y) + 1

	c = [[None for j in range(n)] for i in range(m)] # initializing the c matrix of size mxn
	b = [[None for j in range(n)] for i in range(m)] # initializing the b matrix of size mxn

	for i in range(1, m):
		c[i][0] = 0
	for j in range(0, n):
		c[0][j] = 0

	for i in range(1, m):
		for j in range(1, n):
			if X[i-1] == Y[j-1]: # once we use the the length m and n, we have to subtract 1 to get all values in X, Y vectors
				c[i][j] = c[i-1][j-1] + X[i-1]
				b[i][j] = 'D'
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i][j] = 'U'
			else:
				c[i][j] = c[i][j-1]
				b[i][j] = 'L'

	return c, b

def print_lcs(b, X, i, j):
	'''
	Prints out the longest common subsequence of X and Y in the proper, forward
	order, recursively.
	Pay attention in line 'print X[i-1]' where we had to subtract 1 due to 
	algorithm indexing.
	Based on CLRS 2ed p355.
	'''
	if i == 0 or j == 0:
		return
	if b[i][j] == 'D':
		print_lcs(b, X, i-1, j-1)
		print X[i-1],
	elif b[i][j] == 'U':
		print_lcs(b, X, i-1, j)
	else:
		print_lcs(b, X, i, j-1)

def build_longest_increasing_subsequence(v, n):
	'''
	Given a array v of integers, copies it in an auxiliary array u and
	sorts it using a comparison sort algorithm (n lg n).
	After that, it uses the LCS algorithm strategy to prints out the longest
	common subsequence between v and u (the original array v in increasing order).	
	'''
	u = [None] * n
	for i in range(n):
		u[i] = v[i]

	qs.quicksort(u, 0, len(u)-1)

	c, b = lcs_length(v, u)
	print_lcs(b, v, len(v), len(u))

def get_lcs_max_sum(X, m, n, b, max_length):
	'''
	Retrieve the longest common subsequence of maximum sum of X and Y in the proper, forward
	order, recursively.
	Pay attention in line 'print X[i-1]' where we had to subtract 1 due to 
	algorithm indexing.
	Based on CLRS 2ed p355.
	'''
	k = max_length
	i = m
	j = n
	Z = [None] * k
	l = 0
	print Z
	while i > 0 and j > 0:
		if b[i][j] == 'D':
			print X[i-1]
			print k
			Z[k-1] = X[i-1]
			k = k-1
			i = i-1
			j = j-1
			l = l+1
		elif b[i][j] == 'L':
			i = i-1
		else:
			j = j-1

	return Z, l

def build_max_sum_lcs(X, n):
	'''
	Given a array v of integers, copies it in an auxiliary array u and
	sorts it using a comparison sort algorithm (n lg n).
	After that, it uses the LCS algorithm strategy to prints out the longest
	common subsequence between v and u (the original array v in increasing order).	
	'''
	Y = [None] * n
	for i in range(n):
		Y[i] = X[i]

	qs.quicksort(Y, 0, len(Y)-1)

	c, b = lcs_max_sum_length(X, Y)
	print np.array(c)
	print np.array(b)

	print 'Length of the LCS max sum '
	print get_lcs_max_sum(X, len(X), len(Y), b, len(X))

def main():
	X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
	Y = ['B', 'D', 'C', 'A', 'B', 'A']
	c, b = lcs_length(X, Y)
	print '==============================================='
	print 'Longest Common Subsequence'
	print '==============================================='
	print 'X = ', X
	print 'Y = ', Y
	print 'c = '; print np.array(c)
	print 'b = '; print np.array(b)

	print_lcs(b, X, len(X), len(Y))


	X = [2,4,5,7,1,3,8,6,15]
	print
	print '==============================================='
	print 'Longest Common Subsequence'
	print '==============================================='
	print 'X = ', X
	build_longest_increasing_subsequence(X, len(X))

	#X = [42,4,5,7,1]
	X = [2,4,7,5,9]
	print
	print '==============================================='
	print 'Max Sum Longest Common Subsequence'
	print '==============================================='
	print 'X = ', X
	build_max_sum_lcs(X, len(X))

if __name__=="__main__":
    main() 
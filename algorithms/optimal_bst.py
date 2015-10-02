import numpy as np

def optimal_bst(e, n):
	'''
	Computes the optimal binary search tree with minimal cost, based
	on estimates of access through of each element given by the array e.
	n is the size of e array. We sum up 1 to this parameter to keep
	the algorithm like the original.
	Pay attention to the dimensions of the c matrix and some indices
	that differs from original.

	Algorithm by Cris Fernandes lectures - IME-USP
	'''
	n += 1 # we are gonna need one extra line/column
	c = [[None for j in range(n)] for i in range(n+1)] # initializing the c matrix of size n+1 x n
	s = [None] * (n) # keep the sum of acces at e[1..j]
	s[0] = 0

	for i in range(1, n):
		s[i] = s[i-1] + e[i-1]

	for i in range(1, n+1):
		c[i][i-1] = 0

	for l in range(1, n):
		for i in range(1, n-l+1):
			j = i+l-1
			c[i][j] = c[i+1][j]

			k = i+1
			while k <= j:
				x = c[i][k-1] + c[k+1][j]
				if x < c[i][j]:
					c[i][j] = x
				k += 1

			c[i][j] = c[i][j] + s[j] - s[i-1]
	
	return s, c

def main():
	e = [10,20,30,15,30]
	print
	print '==============================================='
	print 'Optimal binary search tree'
	print '==============================================='
	print 'e = ', e
	s, c = optimal_bst(e, len(e))
	print 's = ', s
	
	c = np.array(c)
	print 'c = '
	print c
	h,w = c.shape

	print 'Optimal BST has cost ', c[1][w-1]

if __name__=="__main__":
    main() 	
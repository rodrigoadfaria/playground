import numpy as np
import quicksort as qs

def lcs_length(X, Y):
	m = len(X)
	n = len(Y)

	c = [[None for j in range(n)] for i in range(m)] # initializing the c matrix of size mxn
	b = [[None for j in range(n)] for i in range(m)]

	for i in range(1, m):
		c[i][0] = 0
	for j in range(0, n):
		c[0][j] = 0

	for i in range(1, m):
		for j in range(1, n):
			if X[i] == Y[j]:
				c[i][j] = c[i-1][j-1] + 1
				b[i][j] = 'D'
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i][j] = 'U'
			else:
				c[i][j] = c[i][j-1]
				b[i][j] = 'L'

	return c, b

def print_lcs(b, X, i, j):
	if i == 0 or j == 0:
		return
	if b[i][j] == 'D':
		print_lcs(b, X, i-1, j-1)
		print X[i]
	elif b[i][j] == 'U':
		print_lcs(b, X, i-1, j)
	else:
		print_lcs(b, X, i, j-1)

def build_longest_increasing_subsequence(v, n):
	u = [None] * n
	for i in range(n):
		u[i] = v[i]

	print u
	qs.quicksort(u, 0, len(u)-1)
	print u

	c, b = lcs_length(v, u)
	print_lcs(b, v, len(v)-1, len(u)-1)

def main():
	X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
	Y = ['B', 'D', 'C', 'A', 'B', 'A']
	c, b = lcs_length(X, Y)
	print np.array(c)
	print np.array(b)

	print_lcs(b, X, len(X)-1, len(Y)-1)

	X = [2,4,5,7,1,3,8,6,15]
	build_longest_increasing_subsequence(X, len(X))

if __name__=="__main__":
    main() 
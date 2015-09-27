import numpy as np
import sys

def matrix_chain_order(p):
	n = len(p) - 1
	m = np.zeros((n, n)).astype(int)
	s = np.zeros((n, n)).astype(int)

	for l in range(2, n+1):
		for i in range(0, n-l+1):
			j = i + l - 1
			m[i, j] = sys.maxint
			for k in range(i, j):
				q = m[i, k] + m[k+1, j] + p[i] * p[k+1] * p[j+1]
				if q < m[i, j]:
					m[i, j] = q
					s[i, j] = k

	return (m, s)

def print_optimal_parens(s, i, j):
	if i == j:
		sys.stdout.write("A" + str(i+1))
	else:
		sys.stdout.write("(")
		print_optimal_parens(s,i,s[i, j])
		print_optimal_parens(s, s[i, j] + 1, j)
		sys.stdout.write(")")

def main():
	#p = [30, 35, 15, 5, 10, 20, 25]
	p = [5, 10, 3, 12, 5, 50, 6]
	(m, s) = matrix_chain_order(p)

	print "m =\n", m
	print "s =\n", s

	print_optimal_parens(s, 0, 5)
	print 

if __name__ == "__main__":
	main()
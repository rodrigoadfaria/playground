import numpy as np

def max_profit(t, p, d, n):
	'''
	Compute the maximum profit of a[n] jobs with t[n] times,
	p[n] profit and d[n] deadline each.
	This is a variation of the knapsack problem. We just order all vector
	in function of the relative order of d.
	'''
	order = np.array(d).argsort()
	t = np.array(t)[order]
	p = np.array(p)[order]
	d = np.array(d)[order]

	D = d[n-1]+1
	w = [[None for j in range(D)] for i in range(n+1)] # initializing the w matrix of size nxn

	for j in range(0, D):
		w[0][j] = 0

		for i in range(1, n+1):
			a = w[i-1][j]

			if t[i-1] > j:
				b = 0
			else:
				b = w[i-1][j-t[i-1]] + p[i-1]
			
			w[i][j] = max(a, b)

	s = get_schedule(w, t, D-1, n, order)
	
	return w, w[n-1][D-1], s

def get_schedule(w, t, D, n, order):
	'''
	Give the sequence of jobs we have to execute to get the maximum profit
	based on the w matrix, the times t[n] and the maximum deadline D.
	The order is the relative order of the d - the deadline array.
	'''
	j = D
	i = n
	s = [None] * (n)
	k = n-1

	for i in range(n, 0, -1):
		if w[i][j] != w[i-1][j]:
			s[k] = 'a' + str(order[i-1] + 1) # the +1 is just to the indexing fashion
			j = j-t[i-1]
			k = k - 1

	return s[k+1:n]

def main():
	#d = [2,4,11]
	#p = [10,22,12]
	#t = [1,2,3]
	d = [1,3,4,5,6,8,6]
	p = [1,2,3,4,2,2,12]
	t = [1,2,3,2,2,3,5]
	#d = [15,16]
	#p = [10,20]
	#t = [10,13]

	print
	print '==============================================='
	print 'Maximum profit productivity'
	print '==============================================='
	print 'p = ', p
	print 'd = ', d
	print 't = ', t
	
	w, mp, s = max_profit(t, p, d, len(d))
	print 'w = '
	print np.array(w)
	print
	print 'maximum profit 		= ', mp
	print 'best jobs schedule 	= ', s
	
if __name__=="__main__":
    main()
import numpy as np

def optimal_log_cutting(p, l):
	'''
	Analog Cutting Machinery - given an array p with cutting points p1, p2, ..., pk of
	an analog and l which is its length, computes the minimal cost based on the best
	cutting arrangement.
	'''
	p.insert(0, 0)
	p.insert(len(p), l)

	n = len(p)
	c = [[-1 for j in range(n)] for i in range(n)] # initializing the c matrix of size n+1 x n

	for i in range(0, n-1):
		c[i][i+1] = 0

	for k in range(1, n):
		for i in range(0, n-k-1):
			j = i+k+1
			c[i][j] = float('inf')

			m = i+1
			while m < j:
				aux = c[i][m] + c[m][j]	
				if aux < c[i][j]:
					c[i][j] = aux
				m += 1

			c[i][j] = c[i][j] + p[j] - p[i]	

	return c, c[0][n-1]

def main():
	#p = [25,50,75]
	#l = 100
	#p = [2,4,7]
	p = [4,5,7,8]
	l = 10
	print
	print '==============================================='
	print 'Analog cutting machinery'
	print '==============================================='
	print 'p = ', p
	print 'l = ', l
	c, cost = optimal_log_cutting(p, l)
	
	c = np.array(c)
	print 'c = '
	print c
	print 'The minimal cost is ', cost

if __name__=="__main__":
    main() 	
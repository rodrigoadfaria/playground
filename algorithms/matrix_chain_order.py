import numpy as np

def matrix_chain_order(p, n, debug=False):
    '''
    Compute a matrix m which keeps the minimal cost of a matrix
    chain multiplication. It's also maintain another matrix s 
    which tracks the sequence of the optimal solution.
    Pay attention in the indexing differences from the pseudocode.
    CLRS p336 - 2ed.
    '''
    m = [[float('inf') for x in range(n)] for x in range(n)] # initialize the matrix with +infinity
    s = [[0 for x in range(n)] for x in range(n)]             # initialize the matrix with 0

    for i in range (n): # fill the main diagonal with zeros
        m[i][i] = 0

    if debug == True:
        print 'l\ti\tn-l\tj\tk\tq = m[i, k] + m[k+1, j] + p[i]*p[k+1]*p[j+1]'
        print '==============================================='
    for l in range(1, n): # l is the chain length
        for i in range (n-l):
            j = i + l

            for k in range (i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]

                if debug:
                    print l, '\t', i,'\t', n-l, '\t', j, '\t', k, '\t', q
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
            
            if i < n-l-1 and debug == True:
                print '...............................................'
        if debug == True:
            print '==============================================='

    return m, s

def print_optimal_parens(s, i, j):
    '''
    Given the optimal sequence of k values in matrix s, and the indices i and j,
    it prints the optimal parenthesization of sequence Ai, Ai+1..Aj recursively.
    CLRS p338 - 2ed.
    '''
    if i == j:
        print 'A' + str(i),
    else:
        print '(',
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print ')',

def matrix_chain_multiply(A, s, i, j):
    '''
    Given the optimal sequence of k values in matrix s, and the indices i and j,
    and the matrices in A[a1, A2,..., An] it computes the optimal scalar multiplication
    of matrices sequence Ai, Ai+1..Aj recursively.
    The product is built in a divide and coquer manner.
    '''
    if i == j:
        return A[i]
    else:
        a = matrix_chain_multiply(A, s, i, s[i][j])
        b = matrix_chain_multiply(A, s, s[i][j] + 1, j)

    	return np.dot(a, b)

def main():
    #p = [30, 35, 15, 5, 10, 20, 25]
    p = [5, 10, 3, 12, 5, 50, 6]
    
    debug = True
    m, s = matrix_chain_order(p, len(p)-1, debug)

    if debug:
    	print "Optimal parenthesization"
    	print "==============================================="
    	print "m = "
        for i in range(len(m)):
            print m[i]

        print "s = "
        for i in range(len(s)):
            print s[i]

        print_optimal_parens(s, 0, 5)

    A = []
    for j in range(len(p)-1):
        A.append(np.matrix(np.random.randint(0,10, size=(p[j], p[j+1]))))

    result = matrix_chain_multiply(A, s, 0, 5)
    if debug:
    	print
    	print "==============================================="
    	print "Scalar product result"
    	print "==============================================="
    	print 'A = '
    	for k in range(len(A)):
    		print 'A' + str(A[k].shape[0]) + 'x' + str(A[k].shape[1])
    		print A[k]
    	print 'Scalar product = '
    	print result

if __name__=="__main__":
    main()     
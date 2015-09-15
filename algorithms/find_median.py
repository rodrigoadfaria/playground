from kway_merge import kway_merge

def find_median(X, Y, p, q, r, s):
    '''
    Find the median between two ordered arrays X[p..q] and Y[r..s].
    We know that the median of X and Y is at i = floor(q/2) and j = floor(s/2), respectively.
    Note that n = q + s is even, that's why we are using floor for convenience.
    If X[i] is greater than Y[j], means that the overall median resides at right of X[i]
    and left of Y[j]. If X[i] is less or equal than Y[j], we go through right of Y[j] and 
    left of X[i].
    We first check if p == q, which means that the overall median is
    within the X array. Otherwise, if r == s, it is into Y.

    Result of the exercise 9.3-8 CLRS 3ed.
    '''
    if p == q: # we have found the median between p, q and r
        return X[p]
    elif r == s: # we have found the median between q, r and s
        return Y[r]

    i = p + (q - p) / 2
    j = r + (s - r) / 2
    if X[i] > Y[j]: # go through right of X and left of Y
        q = i
        r = j
    else: # go through right of Y and left of X
        p = i
        s = j

    return find_median(X, Y, p, q, r, s)

def main():
    #test code    
    #X = [-2, 1, 5, 7, 8, 10, 26, 27, 37] # 10
    #Y = [2, 4, 9, 11, 22, 31, 32, 45, 48]
    
    #X = [4,9,12,28,42] # 42
    #Y = [63,67,82,85,94]
    
    #X = [1,2,3,4,5,6,7,8,9] # 5
    #Y = [1,2,3,4,5,6,7,8,9]

    #X = [1,1,1,1,2] # 1
    #Y = [-2,3,4,5,6]

    X = [1,5,7,9,11]
    Y = [4,6,15,20.25]
    Z = [X, Y]
    print X, Y
    print kway_merge([X, Y], len(Z))

    median = find_median(X, Y, 0, len(X)-1, 0, len(Y)-1)
    print ' Median is', median,'. Size of X and Y is 2n = ', len(X) + len(Y)

if __name__=="__main__":
    main()
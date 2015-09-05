
def merge(A, B, m, n):
    '''
    Merge two arrays A and B of size m and n, respectively
    '''
    C = [None] * (m + n)
    i = 0
    j = 0
    k = 0    
    while i < m and j < n:
        if A[i] <= B[j]: 
            C[k] = A[i]
            i = i+1
        else:                
            C[k] = B[j]
            j = j+1
            
        k = k+1
        
    while i < m:
        C[k] = A[i]
        k = k+1
        i = i+1            
    
    while j < n:
        C[k] = B[j]
        k = k+1
        j = j+1            
    
    return C

def kway_merge(arrays, k):
    # we have an empty array
    if k == 0:
        return []
    
    p = arrays[0]
    # if we have just one array (p in array[0]), we ended up with the merged arrays
    if (k >= 2):
        j = 0;
        q = (k / 2) + (k % 2)
        merged = [None] * q # initialize the merge array
        
        i = 0
        while i < k - 1:
            merged[j] = merge(arrays[i], arrays[i+1], len(arrays[i]), len(arrays[i+1]))
            j = j+1
            i = i+2
        
        if (k % 2) != 0: # we have an odd k lists, append the last one back
            merged[j] = arrays[i]
        
        p = kway_merge(merged, len(merged))
    
    return p

def main():
    #test code
    X_1 = [-2, 4, 5]
    X_2 = [1, 2, 7]
    X_3 = [1, 5]
    X_4 = [4, 10]
    X_5 = [1, 2, 3, 9]
    X_6 = [11, 13, 22, 92, 95]
    X_7 = [-7, -5, -2, 0]

    X_k = [X_1, X_2, X_3, X_4, X_5, X_6, X_7]
    result = kway_merge(X_k, int(len(X_k)))
    print 'X = ', X_k
    print 'k-way merge sort: ', result

if __name__=="__main__":
    main()
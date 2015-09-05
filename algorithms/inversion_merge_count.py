
def merge(A, p, q, r):
    '''
    A variation of the original merge sort (CLRS - 3ed, pg 31) which
    breaks the given array into two parts recursively, sort them 
    and merge at the end, counting the number of inversion of the elements.
    '''
    # r is the lenght of A. B is a helper array of 'r' size.
    B = [None] * (r + 1)
    # copy both parts into the helper array
    i = p
    while i <= q:
        B[i] = A[i]
        i = i+1
    
    j = q+1
    while j <= r:
        B[r + q + 1 - j] = A[j]
        j = j+1
    
    i = p
    j = r
    
    k = p
    count = 0
    while k <= r:
        if B[i] <= B[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = B[j]
            j = j - 1
            count = count + q - i + 1 # count the inversions
        
        k = k+1
    
    return count
    
def mergesort(A, p, r):
    if (p < r) : # we have to split
        q = p + (r - p) / 2

        # sort the left side of the array
        x1 = mergesort(A, p, q)
        # sort the right side of the array
        x2 = mergesort(A, q + 1, r)
        
        # combine the three parts again
        x3 = merge(A, p, q, r)
        return x1 + x2 + x3
    else:
        return 0

def main():
    #test code
    X_1 = []  #0
    X_2 = [1] #0
    X_3 = [1, 5]  #0
    X_4 = [4, 1] #1
    X_5 = [4, 1, 2, 3, 9] #3
    X_6 = [4, 1, 3, 2, 9, 5]  #5
    X_7 = [4, 1, 3, 2, 9, 1]  #8
    X_8 = [2, 4, 1, 3, 5] #3

    count = mergesort(X_1, 0, int(len(X_1)) - 1)
    print (count, ' inversions in ', X_1)

    count = mergesort(X_2, 0, int(len(X_2)) - 1)
    print (count, ' inversions in ', X_2)

    count = mergesort(X_3, 0, int(len(X_3)) - 1)
    print (count, ' inversions in ', X_3)

    count = mergesort(X_4, 0, int(len(X_4)) - 1)
    print (count, ' inversions in ', X_4)

    count = mergesort(X_5, 0, int(len(X_5)) - 1)
    print (count, ' inversions in ', X_5)

    count = mergesort(X_6, 0, int(len(X_6)) - 1)
    print (count, ' inversions in ', X_6)

    count = mergesort(X_7, 0, int(len(X_7)) - 1)
    print (count, ' inversions in ', X_7)

    count = mergesort(X_8, 0, int(len(X_8)) - 1)
    print (count, ' inversions in ', X_8)

if __name__=="__main__":
    main()
from merge_insertion_sort import merge
import math

def two_k_lists_sort(A, p, k):
    '''
    Copy the given subarrays from A within B auxiliary array
    and merge the content of B at the end using the power of 2 indexes.
    e.g.
    p=0     q=2^0       r=2^1
    p=0     q=2^1       r=2^2
    ...
    p=0     q=2^k-2     r=2^k-1
    '''
    n = int(math.pow(2, (k+1)) - 1)
    B = [None] * n       

    l = 0
    m = 0
    # copy the elements from each array A[l] into B aux array
    for i in range(p, n):
        B[i] = A[l][m]
        
        if m == len(A[l]) - 1: # elements at A[l] ended
            l += 1
            m = 0
        else:
            m += 1
    j = 0
    q = p
    # merge the content of B using the power of two indexes
    while j < k:
        r = int(math.pow(2, j+2)) - 1
        merge(B, p, q, r-1) # this r-1 is due to length of aux array copy in merge
        q = r-1

        j += 1

    return B


def main():
    #test code
    X_1 = [-2]
    X_2 = [7, 26]
    X_3 = [1, 5, 8, 10]
    X_4 = [4, 9, 11, 22, 31, 32, 45, 48]

    X_k = [X_1, X_2, X_3, X_4]

    print two_k_lists_sort(X_k, int(0), len(X_k) - 1)

if __name__=="__main__":
    main()
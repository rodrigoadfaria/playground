
def merge(A, p, q, r):
    '''
    A variation of the original merge sort (CLRS - 3ed, pg 31) given
    in the MAC5711 - Algorithms analysis.
    '''
    # r is the lenght of A. B is a helper array of 'r' size.
    B = [None] * (r + 1)
    # copy both parts into the helper array B
    i = p
    while i <= r:
        B[i] = A[i]
        i = i + 1

    j = q+1
    while j <= r:
        B[r + q + 1 - j] = A[j]
        j = j + 1
    
    i = p
    j = r
    
    k = p
    while k <= r:
        if B[i] <= B[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = B[j]
            j = j - 1

        k = k+1
    
def mergesort(A, p, r):
    if (p < r) : # we have to split
        q = p + (r - p) / 2

        # sort the left side of the array
        mergesort(A, p, q)
        # sort the right side of the array
        mergesort(A, q + 1, r)
        
        # combine the three parts again
        merge(A, p, q, r)

def insertion_sort(A):
    '''
    An implementation of the insertion sort from (CLRS - 3ed, pg 18).
    '''
    j = 1
    while j < len(A):
        key = A[j]
        i = j - 1
        
        # insert A[j] into the sorted sequence A[1..j-1]
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
            
        A[i + 1] = key
        
        j += 1

def main():
    A = [2,4,5,7,1,3,8,6,-2]
    print (A)
    p = 0
    r = int(len(A)) - 1
    mergesort(A, p, r)
    print ('merge sort ', A)


    A = [2,4,5,7,1,3,8,6,-2]
    print (A)
    insertion_sort(A)
    print ('insertion sort ', A)

if __name__=="__main__":
    main()
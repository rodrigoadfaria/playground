'''
    Solution to exercise 2.3-5 CLRS 3 ed
    Procedure BINARY-SEARCH takes a sorted array A, a value v, and a range
    [low..high] of the array, in which we search for the value v. The procedure compares
    v to the array entry at the midpoint of the range and decides to eliminate half
    the range from further consideration. We give both iterative and recursive versions,
    each of which returns either an index i such that A[i] == v, or NIL if no entry of
    A[low..high] contains the value v. The initial call to either version should have
    the parameters A, v, 1, n.
    Both procedures terminate the search unsuccessfully when the range is empty (i.e.,
    low > high) and terminate it successfully if the value v has been found. Based
    on the comparison of v to the middle element in the searched range, the search
    continues with the range halved. The recurrence for these procedures is therefore
    T(n) = T(n/2) + theta(1), whose solution is T(n) = theta(lg n).
'''
def iterative_binary_search(A, v, low, high):
    while low < high:
        mid = (low + high) // 2 # integer division-with-modulus operation
        if v == A[mid]:
            return mid
        elif v > A[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

def recursive_binary_search(A, v, low, high):
    if low > high:
        return None
    mid = (low + high) // 2 # integer division-with-modulus operation
    if v == A[mid]:
        return mid
    elif v > A[mid]:
        return recursive_binary_search(A, v, mid, high)
    else:
        return recursive_binary_search(A, v, low, mid - 1)

def main():
    A = [2,4,5,7,8,12,16,29]

    print (A)
    print ('iterative_binary_search 8 at ', iterative_binary_search(A, 8, 0, len(A)))
    print ('recursive_binary_search 29 at ', recursive_binary_search(A, 29, 0, len(A)))

if __name__=="__main__":
    main()
from merge_insertion_sort import merge

def mergesort(A, p, r):
    if (p < r) : # we have to split
        k = p + (r - p) / 3
        m = k+1 + (r - p) / 3

        # sort the left side of the array
        mergesort(A, p, k)
        # sort the center of the array
        mergesort(A, k + 1, m)
        # sort the right side of the array
        mergesort(A, m + 1, r)
        
        # combine the three parts again
        merge(A, p, k, m)
        merge(A, p, m, r)

def main():
    A = [2,4,5,7,1,3,8,6,-2]
    print (A)
    mergesort(A, int(0), int(len(A)) - 1)
    print ('3 way merge sort ', A)

if __name__=="__main__":
    main()
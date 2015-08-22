import math

class Sort:
    def __init__(self, A):
        self.A = A
        self.B = [None] * len(A)

    def merge(self, p, q, r):
        '''
        A variation of the original merge sort (CLRS - 3ed, pg 31) which
        breaks the given array into three parts recursively, sort them 
        and merge at the end.
        '''
        # copy both parts into the helper array
        i = p
        while i <= q:
            self.B[i] = self.A[i]
            i = i+1
        
        j = q+1
        while j <= r:
            self.B[r + q + 1 - j] = self.A[j]
            j += 1
        
        i = p
        j = r
        
        k = p
        while k <= r:
            if self.B[i] <= self.B[j]:
                self.A[k] = self.B[i]
                i = i + 1
            else:
                self.A[k] = self.B[j]
                j = j - 1
            
            k = k+1
        
    def mergesort(self, p, r):
        if (p < r) : # we have to split
            k = p + (r - p) / 3
            m = k+1 + (r - p) / 3

            # sort the left side of the array
            self.mergesort(p, k)
            # sort the center of the array
            self.mergesort(k + 1, m)
            # sort the right side of the array
            self.mergesort(m + 1, r)
            
            # combine the three parts again
            self.merge(p, k, m)
            self.merge(p, m, r)

    def insertion_sort(self):
        '''
        An implementation of the insertion sort from (CLRS - 3ed, pg 18)        
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

A = [2,4,5,7,1,3,8,6,-2]
sort = Sort(A)
sort.mergesort(int(0), int(len(A)) - 1)
print ('merge sort ', sort.A)


A = [2,4,5,7,1,3,8,6,-2]
A = [31, 41, 59, 26, 41, 58]
sort = Sort(A)
sort.insertion_sort()
print ('insertion sort ', sort.A)
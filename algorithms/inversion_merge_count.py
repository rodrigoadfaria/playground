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
        count = 0
        while k <= r:
            if self.B[i] <= self.B[j]:
                self.A[k] = self.B[i]
                i = i + 1
            else:
                self.A[k] = self.B[j]
                j = j - 1
                count += q - i + 1 # count the inversions
            
            k = k+1
        
        return count
        
    def mergesort(self, p, r):
        if (p < r) : # we have to split
            q = p + (r - p) / 2

            # sort the left side of the array
            x1 = self.mergesort(p, q)
            # sort the right side of the array
            x2 = self.mergesort(q + 1, r)
            
            # combine the three parts again
            x3 = self.merge(p, q, r)
            return x1 + x2 + x3
        else:
            return 0

#test code
X_1 = []  #0
X_2 = [1] #0
X_3 = [1, 5]  #0
X_4 = [4, 1] #1
X_5 = [4, 1, 2, 3, 9] #3
X_6 = [4, 1, 3, 2, 9, 5]  #5
X_7 = [4, 1, 3, 2, 9, 1]  #8

sort = Sort(X_1)
print sort.mergesort(int(0), int(len(sort.A)) - 1)

sort = Sort(X_2)
print sort.mergesort(int(0), int(len(sort.A)) - 1)

sort = Sort(X_3)
print sort.mergesort(int(0), int(len(sort.A)) - 1)

sort = Sort(X_4)
print sort.mergesort(int(0), int(len(sort.A)) - 1)

sort = Sort(X_5)
print sort.mergesort(int(0), int(len(sort.A)) - 1)

sort = Sort(X_6)
print sort.mergesort(int(0), int(len(sort.A)) - 1)

sort = Sort(X_7)
print sort.mergesort(int(0), int(len(sort.A)) - 1)
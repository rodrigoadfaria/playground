import random
import math

def selection_sort(A):
    '''
    Sort the given array using the selection sort strategy.
    Result of the exercise 2.2-3 CLRS 3ed.
    '''
   
    for i in range(0, len(A) - 1):
        min = i
        
        for j in range(i + 1, len(A)): # pay attention in this line when counting its running time
            if A[j] < A[min]:
                min = j
            
        aux = A[i]
        A[i] = A[min]
        A[min] = aux

A = [2,4,5,7,1,3,8,6,-2]
print (A)
selection_sort(A)
print (A)
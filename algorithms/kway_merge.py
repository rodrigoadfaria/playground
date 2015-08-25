import math

def merge(a, b):
    c = [None] * (len(a) + len(b))
    i=0
    j=0
    k=0
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: 
            c[k] = a[i]
            i = i+1
        else:                
            c[k] = b[j]
            j = j+1
            
        k = k+1
        
    while i < len(a):
        c[k] = a[i]
        k = k+1
        i = i+1            
    
    while j < len(b):
        c[k] = b[j]
        k = k+1
        j = j+1            
    
    return c

def kway_merge(arrays, k):
    if k == 0:
        return []
    
    p = arrays[0]
    if (k >= 2):
        j = 0;
        q = (k / 2) + (k % 2)
        merged = [None] * q # initialize the merge array
        
        i = 0;
        while i < k - 1:
            merged[j] = merge(arrays[i], arrays[i+1])
            j = j+1
            i = i+2
        
        if (k % 2) != 0: # we have an odd k lists, append the last one back
            merged[j] = arrays[i]
        
        p = kway_merge(merged, len(merged))
    
    return p

#test code
X_1 = [-2, 4, 5]
X_2 = [1, 2, 7]
X_3 = [1, 5]
X_4 = [4, 10]
X_5 = [1, 2, 3, 9]
X_6 = [11, 13, 22, 92, 95]
X_7 = [-7, -5, -2, 0]

X_k = [X_1, X_2, X_3, X_4, X_5, X_6, X_7]
print kway_merge(X_k, int(len(X_k)))

def order_letters(A, i, j):
    while i != j:
        if A[i] == 'B':
            aux = A[j]
            A[j] = A[i]
            A[i] = aux
            
            j = j - 1            
        elif A[j] == 'A':
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
            
            i = i + 1
        else:
            i = i + 1 # we already have an A in A[i] and a 'B' in A[j]

# tests    
X = ['A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'B', 'B']
print (X)
order_letters(X, 0, len(X) - 1)
print (X)
print ('\n')

X = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
print (X)
order_letters(X, 0, len(X) - 1)
print (X)
print ('\n')

X = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
print (X)
order_letters(X, 0, len(X) - 1)
print (X)
print ('\n')

X = ['B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
print (X)
order_letters(X, 0, len(X) - 1)
print (X)
print ('\n')

X = []
print (X)
order_letters(X, 0, len(X))
print (X)
print ('\n')

X = ['A', 'B']
print (X)
order_letters(X, 0, len(X) - 1)
print (X)
print ('\n')

X = ['B', 'A']
print (X)
order_letters(X, 0, len(X) - 1)
print (X)
import random
import math

def secmax(v, n):
    '''
    Find out the first and second max values in the given array
    '''
    max = 0
    secmax = 0
    i = 0;
    
    count_lines = 0
    
    while i < n:
        if v[i] > max:
            secmax = max
            count_lines = count_lines + 1 # count the number of executions of above line
            max = v[i]
        elif v[i] > secmax:
            secmax = v[i]
            count_lines = count_lines + 1 # count the number of executions of above line
        
        i = i + 1
        
    return count_lines
    
print('n\t\t\t E[X] \t\t\t 1 + 2ln n')

n_vector = [256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304]

i = 0
while i < len(n_vector):
    n = n_vector[i]

    v = []
    j = 0;
    num_samples = 10
    
    count_lines = 0 # sum of executions of line 5 and 8

    while j < num_samples:    
        
        k = 0
        while k < n:
            v.append(random.randint(1, n)) # generate a vector of size n[k]
            k = k + 1

        count_lines = count_lines + secmax(v, n)

        j = j + 1
    
    i = i + 1
    
    print n, '\t\t\t ', count_lines // num_samples, '\t\t\t ', 1 + 2 * math.log(n)

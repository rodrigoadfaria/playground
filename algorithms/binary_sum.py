def binary_sum(A, B, n):
    '''
    CLRS - 3 ed. Problem 2.1-4
    Add two n-bit binary integers, stored in two n-element arrays A and B
    '''
    C = [0]*(n+1)
    carry = 0
    # do the summation from the least significant to most significant bit
    for i in range(n-1, -1, -1):
        sum_ = A[i] + B[i] + carry
        C[i+1] = int(sum_ % 2)
        carry = int(sum_ / 2)
    
    C[0] = carry
    return C

def main():
    #A=[1,1,0] # 6
    #B=[0,1,0] # 2

    A=[0,1,1,0,1] # 13
    B=[1,0,1,1,1] # 23

    #A = [0,1,1,0,1,1,1,0] # 110
    #B = [0,0,0,1,0,1,1,1] #  23
    C = binary_sum(A, B, len(A))

    C_concat = ''
    A_concat = ''
    B_concat = ''

    for x in A:
        A_concat += str(x)
    for x in B:
        B_concat += str(x)
    for x in C:
        C_concat += str(x)

    # parse the arrays to int values for better seeing the summation
    A_ = int(A_concat, 2)
    B_ = int(B_concat, 2)
    C_ = int(C_concat, 2)

    print ('A = ', A, A_)
    print ('B = ', B, B_)

    print ('A + B = ', C, C_)

if __name__=="__main__":
    main()
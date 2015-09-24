def counting_sort_interval(A, k, a, b):
	'''
	Gives the number of appearence of k integer from the interval [a..b]
	within A[1..n].
	Resut of CLRS 8.2-4.
	'''
	n = len(A)
	C = [0] * (k + 1) # consider 0 as starting point
	
	for j in range(n):
		C[A[j]] = C[A[j]] + 1 # counting the k-number
	
	print C
	for i in range(1, k+1):
		C[i] = C[i] + C[i - 1] # cumulative counting the k-number
	print C

	aux = 0
	if a > 0:
		aux = C[a - 1]
	return C[b] - aux

def main():
    A = [2,5,3,0,2,3,0,3]
    print (A)

    k = 5
    a = 5
    b = 5
    count = counting_sort_interval(A, k, a, b)
    print ('counting sort interval of ', A, ' k=', k, ' a=', a, ' b=', b)
    print ('Count: ', count)

if __name__=="__main__":
    main() 
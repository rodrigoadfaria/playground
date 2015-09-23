#preprocessing function use intermediate countingsort step
#input a array A such that A[i] is in [1 .. k], its size n and k.
#ouput a array C to be used in the count_in_interval function
def preprocess_array(A, n, k):
	C = [0] * (k+1)
	
	for i in range(1, n):
		C[A[i]] = C[A[i]] + 1
	for i in range(2, k+1):
		C[i] = C[i] + C[i-1]
	
	return C
	
def count_in_interval(C, a, b):
	if a <= 1:
		a = 1
	else:
		a = C[a - 1] + 1
	
	return C[b] - a + 1
	
def test_answer(A, a, b, answer):
	count = 0
	
	for x in A:
		if a <= x and x <= b:
			count += 1
		
	assert answer == count, "you got wrong answer!"

def main():
	# make it similiar with class exercicise index 1 is ignored
	A = [-1, 2,2,3,7,6,3,8,6,2,4,8,10]
	k = 10
	n = len(A)
	
	C = preprocess_array(A, n, k)
	print "A = ", A[1:]
	print "C = ", C
	a = 1
	b = 5
	counting = count_in_interval(C, a, b)
	test_answer(A, a, b, counting)
	print("counting in interval [" + str(a) + " .. " + str(b) + "] is " + str(counting))
	
	a = 2
	b = 5
	counting = count_in_interval(C, a, b)
	test_answer(A, a, b, counting)
	print("counting in interval [" + str(a) + " .. " + str(b) + "] is " + str(counting))
	
	a = 2
	b = 10
	counting = count_in_interval(C, a, b)
	test_answer(A, a, b, counting)
	print("counting in interval [" + str(a) + " .. " + str(b) + "] is " + str(counting))
	
	
	a = 4 
	b = 8
	counting = count_in_interval(C, a, b)
	test_answer(A, a, b, counting)
	print("counting in interval [" + str(a) + " .. " + str(b) + "] is " + str(counting))
	
if __name__ == "__main__":
	main()

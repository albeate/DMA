import time 
start_time = time.clock()

A = [2,8,4,3,6]

def inversion(A):
	n = len(A)
	m = 0
	return sum([m+1 for i in range(n-1) for j in range(n-1) if A[i] > A[j] and i < j])
print "antallet af insertions:",inversion(A),"in",time.clock()-start_time,"seconds"

> antallet af insertions: 3 in 3.7e-05 seconds

import time 
start_time = time.clock()

A = [2,8,4,3,6]

def inversion(A):
	n = len(A)
	m = 0
	for i in range(n-1):
		for j in range(i+1,n-1):
			if A[i] > A[j]:
				m += 1
	return m

print "antallet af insertions:",inversion(A),"in",time.clock()-start_time,"seconds"
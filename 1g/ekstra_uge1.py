from __future__ import division 
import math

A = [1,5,6,10,15,16,17,23]
B = [5,10,17,6,23,15,16,1]

def exists(A,n,x):
	"""
	Checks wheter or not x exists 
	in the list before hi >= lo, 
	if yes then it'll return true 
	otherwise return false.
	"""
	lo = 0
	hi = n
	while hi >= lo:
		mid = int(math.floor((hi+lo)/2))
		print "\nmid: ",mid
		if x > A[mid]:
			lo = mid+1
		elif x < A[mid]:
			hi = mid-1
		else:
			return True
	return False

print "exists(A,8,17) returnerer: ",exists(A,8,17)
print "*"*20
print "exists(A,8,14) returnerer: ",exists(A,8,14)
print "*"*20
print "exists(A,4,16) returnerer: ",exists(A,4,16)
print "*"*20
print "exists(A,8,3) returnerer: ",exists(A,8,3) # mid 4, mid 1, mid 0
print "*"*20
print "exists(B) returnerer: ",exists(B,6,12) 
print "*"*20
print "exists(B,7,1) returnerer: ",exists(B,7,1)

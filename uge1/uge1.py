from __future__ import division 
import math

A = [1,5,6,10,15,16,17,23]
B = [23,5,6,10,15,16,17,1]
C = [11,1,2,3,4,5,6,5,8,16,10,0,12,13,7,15,13]

def exists(A,n,x):
	"""
	Checks wheter or not x exists 
	in the list before hi >= lo, 
	if yes then it'll return true 
	otherwise return false.
	"""
	lo = 0
	hi = (n-1)
	while hi >= lo:
		mid = int(math.floor((hi+lo)/2))
		print mid
		if x > A[mid]:
			lo = mid+1
		elif x < A[mid]:
			hi = mid-1
		else:
			return True
	return False
from __future__ import division
import random

star = '*'
n = 4

print star*15
print "n =", n


def A1():
	x = 1
	return x

def A2():
	x = 1
	x = x + 1
	return x

def A3(n):
	x = n
	return x

def A4(n):
	if n > 10: 
		return 1
	else: 
		return 0

def A5(n):
	x = 0
	i = 1
	for i in range(n):
		x = x + 2
	return x

print star*10
print star*10
print "A1:", A1()

print star*10
print "A2:", A2()

print star*10
print "A3:", A3(n)
# n = 4: 4, n = 10: 10, n = 100: 100

print star*10
print "A4:", A4(n)
# n = 4: 0, n = 10: 0, n = 100: 1

print star*10
print "A5:", A5(n)
# n = 4: 8, n = 10: 20, n = 100: 200



def B1(n):
	x = n
	x = x + x
	return 2*x

def B2(n):
	if n > 10:
		x = 1
	elif n == 10:
		x = 0
	else: x = -1
	return 2*x

def B3(n):
	x = n
	y = 2 * n
	x = 2*x + 3*y
	return 2*x

def B4(n):
	x = n
	y = 2 * x
	x = 2 * y
	return 2*x

def B5(n):
	return 2*(3*n)

print star*10
print star*10
print "B1:", B1(n)
# n = 4: 8, n = 10: 20, n = 100: 200

print star*10
print "B2:", B2(n)
# n = 4: -1, n = 10: 0, n = 100: 1

print star*10
print "B3:", B3(n)
# n = 4: 32, n = 10: 80, n = 100: 800

print star*10
print "B4:", B4(n)
# n = 4: 16, n = 10: 40, n = 100: 400

print star*10
print "B5:", B5(n)
# n = 4: 12, n = 10: 30, n = 100: 300


def loop0(n):
	x = 0
	i = 1
	for i in range(n):
		x = x + 2
	return x

def loop1(n):
	x = 0
	for i in range(1,n):
		for j in range(1,n):
			x = x + 1
	return x

def loop2(n):
	x = 0
	for i in range(1,n):
		x = x + 1
	for j in range(1,n):
		x = x + 1
	return x

def loop3(n):
	x = 0
	for i in range(1,n):
		if i >= n-1:
			for j in range(1,n):
				x = x + 1
	return x

print star*10
print star*10
print "loop0: ",loop0(n)
# n = 4: 8, n = 10: 20, n = 1000: 2000

print star*10
print "loop1: ",loop1(n)
# n = 4: 9, n = 10: 81, n = 1000: 998001

print star*10
print "loop2: ",loop2(n)
# n = 4: 6, n = 10: 18, n = 1000: 1998

print star*10
print "loop3: ",loop3(n)
# n = 4: 3, n = 10: 9, n = 1000: 999


def loop5(n):
	x = 0
	while n > 0:
		x = x + 1
		n = n - 1
	return x

print star*10
print "loop5: ",loop5(n)
# n = 4: 4, n = 10: 10, n = 1000: 1000

k = random.randint(1,10)
N = 2**k
def loop6(N):
	x = 0
	while N > 1:
		x = x + 1
		N = N / 2
	return x

def loop7(n):
	x = 1
	while n > 0:
		x = x * 2
		n = n - 1
	return x

print star*10
print star*10
print "loop6: ",loop6(N)
# constantly random because I made it so!

print star*10
print "loop7: ",loop7(n)
# n = 4: 16, n = 16: 65536


x = 8
y = 3
z = 1

def f1(x,y):
	return sum([x,y])

def f2(x,y):
	return int((sum([x,y]))/2)

def f3(x,y):
	return x**y

print star*10
print star*10
print "f1: ",f1(x,y)

print star*10
print "f2: ",f2(x,y)

print star*10
print "f3: ",f3(x,y)


def f4(x,y,z):
	if x + y == 3:
		return 1
	elif x + z == 3:
		return 1
	elif z + y == 3:
		return 1
	else:
		return 0

print star*10
print star*10
print "f4: ",f4(x,y,z)


def T1(A1,n):
	x = 0
	for i in range(n-1):
		x = x + A1[i]
	return x

def T2(A2,n,y):
	x = 0
	for i in range(n-1):
		if A2[i] == y:
			x = x + 1
	return x

def T3(A3,n):
	for i in range(n-2):
		if A3[i] > A3[i+1]:
			temp = A3[i+1]
			A3[i+1] = A3[i]
			A3[i] = temp
	return A3

A1 = [2,3,1,4,3] 
#A1 = [0,-1,1]
print star*15
print star*15
print "T1: ", T1(A1,5)
#print "T1: ", T1(A1,3)

#A2 = [2,3,4,2]
A2 = [2,3,4,2]
print star*15
#print "T2: ",T2(A2,4,2)
print "T2: ",T2(A2,4,3)

A3 = [7,10,12,2]
print star*15
print "T3: ",T3(A3,4)

A = [2,3,1,55,3,45,7]
def mindste(A,n):
	"""
	virker naesten.
	"""
	for j in range(0,n):
		x = A[j]
		i = j - 1
		while i > 0 and A[i] > x:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = x
	return A
print "mindste: ",mindste(A,7)

def sum100(A,n):
	for i in range(n):
		if A[i] + A[i+1] == 100:
			return A[i], A[i+1]
	return False
print "sum til 100: ",sum100(A,7)

Z = [34,6,7,32,4,1,100,2]
def maxZombie(Z):
	n = len(Z)
	zL = Z[0]
	for i in range(n-1):
		if zL < Z[i]:
			zL.insert(Z[i])
	return zL
print "zombie list: ",maxZombie(Z)
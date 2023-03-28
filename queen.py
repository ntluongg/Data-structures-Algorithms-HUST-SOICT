#An example for Back-tracking 

x = list() #global variables
n = 4

for i in range(n): #generating n-th array
	x+=[-1] 

def solution():
	#printing out the solution
	for i in range(len(x)):
		print(x[i],end=' ')
	print()

def check(v,k):
	for i in range(k):
		if x[i] == v:
			return False
		if x[i] + i == v + k:
			return False
		if x[i] - i == v - k:
			return False
	return True

def queen(k):
	for v in range(n):
		if check(v,k):
			x[k] = v
			if k == n - 1:
				solution()
			else:
				queen(k+1)

queen(0)


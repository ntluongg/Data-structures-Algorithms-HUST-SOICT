n = int(input())
m = [False for i in range(n)]
x = [0 for i in range(n)]

def solution():
	print(x)

def check(k,i): #implemented for discrete math
	if k==0:
		return True
	if x[k-1] + i == n:
		return False
	return True

def Try(k):
	for i in range(1,n+1):
		if (not m[i-1]) and check(k,i):
			x[k] = i
			m[i-1] = True
			if k == n-1:
				solution()
			else:
				Try(k+1)
			m[i-1] = False 

Try(0)
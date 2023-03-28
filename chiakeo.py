n,M = input().split()
n = int(n)
M = int(M)
x=[0 for i in range(n+1)]	
#count = 0
T = 0

def solution():
	print(' '.join(x[1:]))

def check(v,k):
	if k<n:
		return T + v <= M
	else:
		return T + v == M

def Try(k):
	global count
	global T
	#count = count + 1
	for v in range(1, M - T - (n-k) + 1):
		if check(v,k):
			x[k] = str(v)
			T += v
			if k == n:
				solution()
			else:
				Try(k+1)
			T += -v

Try(1)
#print(count)
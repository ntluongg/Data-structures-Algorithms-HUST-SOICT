from sys import stdin, stdout

n = int(stdin.readline())
c = [0 for i in range(n)]

for i in range(n):
	c[i]=[int(x)for x in stdin.readline().split()]

cmin = min([min(i) for i in c])

x = [0 for i in range(n)]
mark = [False for i in range(n)]
mark[0] = True
f = c[0][0]
fmin = 1e9

def solution():
	global fmin
	if f + c[x[n-1]][x[0]] < fmin:
		fmin = f + c[x[n-1]][x[0]]

def Try(k):
	global f
	global cmin
	for v in range(n):
		if not mark[v]:
			x[k] = v
			if k > 0:
				f = f + c[x[k-1]][x[k]]
			mark[v] = True
			if k == n-1:
				solution()
			else:
				if f + cmin*(n-k) < fmin:
					Try(k+1)
			mark[v] = False
			if k > 0:
				f = f - c[x[k-1]][x[k]]
Try(1)
print(fmin)

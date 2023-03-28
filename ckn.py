k,n = map(int,input().split())

c = [[0 for i in range(n+1)] for j in range(k+1)]

for i in range(k+1):
	for j in range(n+1):
		if i == j or i == 0:
			c[i][j] = 1
		elif i < j:
			c[i][j] = c[i-1][j-1] + c[i][j-1]

print(int(c[k][n])%(1000000007))
#print(c)
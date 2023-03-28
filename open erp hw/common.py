n,m = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
s = [[0 if x[i] != y[j] else 1 for j in range(m) ] for i in range(n)]

for i in range(1,n):
	for j in range(1,m):
		if x[i] == y[j]:
			s[i][j] = s[i-1][j-1] + 1
		elif s[i-1][j] > s[i][j-1]:
			s[i][j] = s[i-1][j]
		else:
			s[i][j] = s[i][j-1]

res = s[n-1][m-1]
print(res)
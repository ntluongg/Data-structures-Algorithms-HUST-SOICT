x = [1,2,3,4]
n = len(x)
y = [1,2,3,4,5]
m= len(y)
s = [[0 for j in range(m)] for i in range(n)]
trace = [[' ' for j in range(m)] for i in range(n)]

if x[0] == y[0]:
	s[0][0] = 1
	trace[0][0] = 'D'

for i in range(1,n):
	if x[i] == y[0]:
		s[i][0] = 1
		trace[i][0] = 'D'
	else:
		s[i][0] = s[i-1][0]
		trace[i][0] = 'U'

for j in range(1,m):
	if x[0] == y[j]:
		s[0][j] = 1
		trace[0][j] = 'D'
	else:
		s[0][j] = s[0][j-1]
		trace[0][j] = 'L'

for i in range(1,n):
	for j in range(1,m):
		if x[i] == y[j]:
			s[i][j] = s[i-1][j-1] + 1
			trace[i][j] = 'D' #diagonal
		elif s[i-1][j] > s[i][j-1]:
			s[i][j] = s[i-1][j]
			trace[i][j] = 'U' #up
		else:		
			s[i][j] = s[i][j-1]
			trace[i][j] = 'L' #left

res = s[n-1][m-1]
solution = []
i = n-1
j = m-1
while i>=0 and j>=0:
	if trace[i][j] == 'D':
		solution.append(x[i])
		i = i-1
		j = j-1
	elif trace[i][j] == 'L':
		j = j-1
	else:
		i = i-1
solution.reverse()
print(res)
print(solution)
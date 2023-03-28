#Back-tracking 

x = [[0 for i in range(9)] for j in range(9)]
markRow = [[False for v in range(10)] for r in range(9)]
markCol = [[False for v in range(10)] for c in range(9)]
markSquare = [[[False for v in range(10)] \
for c in range(3)] for r in range(3)]

def check(v,r,c):
	return (markRow[r][v] == False) and \
	(markCol[c][v] == False) and \
	(markSquare[r//3][c//3][v] == False)

def solution():
	for r in range(9):
		for c in range(9):
			print(x[r][c], end=' ')
		print(' ')
	print()

def Try(r,c):
	for v in range(1,10):
		if check(v,r,c):
			x[r][c] = v
			markRow[r][v] = True
			markCol[c][v] = True
			markSquare[r//3][c//3][v] = True
			if c == 8 and r == 8:
				solution()
			else:
				if c == 8:
					Try(r+1,0)
				else:
					Try(r,c+1)
			markRow[r][v] = False
			markCol[c][v] = False
			markSquare[r//3][c//3][v] = False

Try(0,0)
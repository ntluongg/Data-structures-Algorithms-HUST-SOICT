#the 2nd sudoku problem
import pickle

with open('test.inp','r') as f:
	x = list()
	for line in f:
		line.rstrip()
		x.append(line.split())
#print(x)

markRow = [[False for v in range(10)] for r in range(9)]
markCol = [[False for v in range(10)] for c in range(9)]
markSquare = [[[False for v in range(10)] \
for c in range(3)] for r in range(3)]

for r in range(9):
	for c in range(9):
		if x[r][c] != 0:
			markCol[c][x[r][c]] = True
			markRow[r][x[r][c]] = True
			markSquare[r//3][c//3][x[r][c]] = True

def check(v,r,c):
	return (markRow[r][v] == False) and \
	(markCol[c][v] == False) and \
	(markSquare[r//3][c//3][v] == False) and (x[r][c]!=0)

def solution():
	for r in range(9):
		for c in range(9):
			print(x[r][c], end=' ')
		print(' ')
	print()

def Try(r,c):
	if x[r][c] is not 0:
		
		if c == 8 and r == 8:
			solution()
		
		else:
			if c == 8:
				Try(r+1,0)
			else:
				Try(r,c+1)

	else:
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
				x[r][c] = 0

Try(0,0)
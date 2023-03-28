import sys
def input():
    [n, m] = [int(x) for x in sys.stdin.readline().split()]
    A = [[] for i in range(n+1)]
    for i in range(m):
        [u,v] = [int(x) for x in sys.stdin.readline().split()]
        A[u].append(v)
        A[v].append(u)
    return n,m,A

def DFS(u):
    c[u] = nbCC
    for v in A[u]:
        if c[v] == -1:
            DFS(v)

def DFSGraph():
    global nbCC
    for v in range(1,n+1):
        if c[v] == -1:
            nbCC += 1
            DFS(v)

def printConnectedComponents():
    for k in range(1, nbCC + 1):
        print('CC[',k,']:',end=' ')
        for v in range(1,n+1):
            if c[v] == k:
                print(v,end =' ')
    print()

n,m,A = input()

c = [-1 for v in range(n+1)]
nbCC = 0

DFSGraph()
printConnectedComponents()
'''
11 13
1 3
1 7
2 9
2 10
3 6
3 7
4 5 
4 7
4 8
5 8
5 11
6 7
9 10
'''
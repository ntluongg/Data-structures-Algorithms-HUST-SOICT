import sys
def input():
    [n, m] = [int(x) for x in sys.stdin.readline().split()]
    A = [[] for i in range(n+1)]
    for i in range(m):
        [u,v] = [int(x) for x in sys.stdin.readline().split()]
        A[u].append(v)
        A[v].append(u)
    return n,m,A

def BFS(u):
    Q = []
    Q.append(u)
    level[u] = 0
    while len(Q) > 0:
        v = Q.pop(0)
        for x in A[v]:
            if level[x] == -1:
                level[x] = level[v] + 1
                p[x] = v
                Q.append(x)

def getPath(u,v,p):
    x = v
    path = []
    while x != -1:
        path.append(x)
        x = p[x]
    path.reverse()
    return path

def BFSGraph():
    for v in range(1,n+1):
        if level[v] == -1:
            BFS(v)
    
    for v in range(1,n+1):
        print('level[',v,']=',level[v])

n,m,A = input()
level = [-1 for v in range(n+1)]
p = [-1 for v in range(n+1)]
BFSGraph()

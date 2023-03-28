import sys
def input():
    [n,m] = [int(x) for x in sys.stdin.readline().split()]
    A = [[] for v in range(n+1)]
    for i in range(m):
        [u,v,w] = [int(x) for x in sys.stdin.readline().split()]
        A[u].append([v,w])
        A[v].append([u,w])
    return n,m,A

def DeleteMin(S):
    minD = INF
    u = -1
    for x in S:
        if minD > d[x]:
            minD =d[x]
            u = x
    return u

def TracePath(s,t):
    path = []
    v = t
    while v != s:
        path.append(v)
        v = p[v]
    path.append(s)
    path.reverse()
    return path

def Dijkstra(s):
    #Initialization
    for [v,w] in A[s]:
        d[v] = w
        p[v] = s
    d[s] = 0

    S = set()
    for v in range(1,n+1):
        if v != s:
            S.add(v)
    count = 0
    while len(S) > 0:
        count+=1
        u = DeleteMin(S)
        S.remove(u)
        for [v,w] in A[u]:
            if v in S:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    p[v] = u

    for v in range(1,n+1):
        print('d[',v,']=',d[v],'path:',TracePath(s,v),end= ' ')

n,m,A = input()
INF = 1e9
d = [INF for v in range(n+1)]
p = [0 for v in range(n+1)]
Dijkstra(1)

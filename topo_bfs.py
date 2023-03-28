def input():
    with open('topo_sort.txt') as f:
        [n,m] = [int(x) for x in f.readline().split()]
        d = [0 for v in range(n+1)]
        A = [[] for v in range(n+1)]
    for i in range(m):
        [u,v] = [int(x) for x in f.readline().split()]
        d[v] = d[v] + 1
        A[u].append(v)
    
    return n,m,A,d

def TopoSort():
    Q = []
    L = []
    for v in range(1, n+1):
        if d[v] == 0:
            Q.append(v)
    while len(Q) > 0:
        v =Q.pop(0)
        L.append(v)
        for x in A[v]:
            d[x] = d[x] - 1
            if d[x] == 0:
                Q.append(x)
    print(L)

n,m,A,d = input()
TopoSort()

import sys

class PriorityQueue(object):
    def __init__(self, max_size):
        self.sz = max_size
        self.n = 0
        self.keys = [0 for i in range(self.sz + 1)]
        self.nodes = [0 for i in range(self.sz + 1)]
        self.idx = [-1 for i in range(self.sz + 1)]
    
    def Swap(self,i,j):
        tmp = self.nodes[i]
        self.nodes[i] = self.nodes[j]
        self.nodes[j] = tmp
        self.idx[self.nodes[i]] = i
        self.idx[self.nodes[j]] = j
    
    def Size(self):
        return self.n
    
    def UpHeap(self,i):
        if i == 0:
            return
        while i > 0:
            pi = (i-1)//2 #parent of i
            if self.keys[self.nodes[i]] < self.keys[self.nodes[pi]]:
                self.Swap(i,pi)
            else:
                break
            i = pi
    
    def DownHeap(self,i):
        L = 2*i + 1
        R = 2*i + 2
        minIdx = i
        if L < self.n and self.keys[self.nodes[L]] < self.keys[self.nodes[minIdx]]:
            minIdx = L
        if R < self.n and self.keys[self.nodes[R]] < self.keys[self.nodes[minIdx]]:
            minIdx = R
        if minIdx != i:
            self.Swap(i,minIdx)
            self.DownHeap(minIdx)

    def Insert(self,v,k):
        self.keys[v] = k
        self.nodes[self.n] = v
        self.idx[self.nodes[self.n]] = self.n 
        self.UpHeap(self.n)
        self.n = self.n + 1

    def InHeap(self, v):
        return self.idx[v] >= 0

    def UpdateKey(self,v,k):
        if self.keys[v] > k:
            self.keys[v] = k
            self.UpHeap(self.idx[v])
        else:
            self.keys[v] = k
            self.DownHeap(self.idx[v])

    def DeleteMin(self):
        sel_node = self.nodes[0]
        self.Swap(0,self.n -1)
        self.n = self.n - 1
        self.DownHeap(0)
        self.idx[sel_node] = -1
        return sel_node

    def getKey(self,v):
        return self.keys[v]

    def Print(self):
        for i in range(self.n):
            e = self.nodes[i]
            print('[',e,'idx',self.idx[e],',k',self.keys[e],']',end=' ')
        print('')

def Input():
    [n,m] = [int(x) for x in sys.stdin.readline().split()]
    A = [[] for v in range(n+1)]
    for i in range(m):
        [u,v,w] = [int(x) for x in sys.stdin.readline().split()]
        A[u].append([v,w])
    [s,t] = [int(x) for x in sys.stdin.readline().split()]
    return n,m,A,s,t

def DijkstraPriorityQueue(n,m,A,s,t):
    pq = PriorityQueue(n)
    pq.Insert(s,0)
    while pq.Size() > 0:
        u = pq.DeleteMin()
        if u == t:
            break
        du = pq.getKey(u)
        for [v,w] in A[u]:
            dv = du + w
            if pq.InHeap(v) == False:
                pq.Insert(v,dv)
            else:
                if pq.getKey(v) > dv:
                    pq.UpdateKey(v,dv)
    print(pq.getKey(t))

n,m,A,s,t = Input()
DijkstraPriorityQueue(n,m,A,s,t)
'''
5 7
2 5 87
1 2 97
4 5 78
3 1 72
1 4 19
2 3 63
5 1 18
1 5
'''

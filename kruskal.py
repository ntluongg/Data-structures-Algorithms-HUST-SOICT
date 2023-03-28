import sys

def input():
    [n,m] = [int(x) for x in sys.stdin.readline().split()]
    E = []
    for i in range(m):
        [u,v,w] = [int(x) for x in sys.stdin.readline().split()]
        E.append([u,v,w])
    return n,m,E

n,m,E = input()

E = sorted(E, key = lambda x: x[2])
p = [0 for i in range(n+1)]
r = [0 for i in range(n+1)]

def FindSet(x):
    if x != p[x]:
        p[x] = FindSet(p[x])
    return p[x]

def Unify(x,y):
    if r[x] > r[y]:
        p[y] = x # make y the child of x
    else:
        p[x] = y # make x the child of y
        if r[x] == r[y]:
            r[y] = r[y] + 1

def MakeSet(x):
    p[x] = x
    r[x] = 0

def Kruskal():
    for v in range(1,n+1):
        MakeSet(v)
    T = [] # solutions under construction
    for [u,v,w] in E:
        ru = FindSet(u)
        rv = FindSet(v)
        print('consider edge (',u,',',v,')')
        if ru != rv:
            print('accept edge (',u,',',v,')')
            Unify(ru,rv)
            T.append([u,v,w])
            if len(T) == n - 1:
                break
            else:
                print('ignore edge (',u,',',v,')')
    return T

MST = Kruskal()
print('MST is ',MST)
s = 0
for [u,v,w] in MST:
    s = s + w
print(s)
'''
5 8                  
1 2 1
1 3 4
1 5 1
2 4 2
2 5 1
3 4 3
3 5 3
4 5 2
'''
class State(object):
    def __init__(self,x,y,step):
        self.x = x
        self.y = y
        self.step = step

    def __str__(self):
        return '('+str(self.x)+', '+str(self.y)+')'

    def finalState(s):
        return (s.x == c) or (s.y == c)

def solve():
    if a%2==0 and b%2==0 and c%2==1:
        return None
    Q = []
    s0 = State(0,0,0)
    Q.append(s0)
    visited = [[False for i in range(1000)] for j in range(1000)]
    visited[0][0] = True
    while len(Q) > 0:
        s = Q.pop(0)
        #Fill jug 1:
        ns = State(a, s.y,s.step + 1)
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True

        #Fill jug 2:
        ns = State(s.x, b,s.step + 1)
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        #Empty jug 1
        ns = State(0, s.y,s.step + 1)
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        #Empty jug 2
        ns = State(s.x,0,s.step + 1)
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        #Pour jug 1 to jug 2
        if s.x + s.y <= b:
            ns = State(0, s.x + s.y, s.step + 1)
        else:
            ns = State(s.x + s.y - b, b, s.step + 1)
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True

        #Pour jug 2 to jug 1
        if s.x + s.y <= a:
            ns = State(s.x + s.y, 0, s.step + 1)
        else:
            ns = State(a, s.x + s.y - a, s.step + 1)
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
    
    return None

a,b,c = map(int,input().split())
solution = solve()

if solution == None:
    print(-1)
else:
    print(solution.step)
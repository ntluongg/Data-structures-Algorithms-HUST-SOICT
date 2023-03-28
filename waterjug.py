class State(object):
    def __init__(self,x,y,step,parent,action):
        self.x = x
        self.y = y
        self.step = step
        self.parent = parent
        self.action = action

    def __str__(self):
        return '('+str(self.x)+', '+str(self.y)+')'

    def finalState(s):
        return (s.x == c) or (s.y == c)

def solve():
    Q = []
    s0 = State(0,0,0,None,'')
    Q.append(s0)
    visited = [[False for i in range(1000)] for j in range(1000)]
    visited[0][0] = True
    while len(Q) > 0: #breadth-first-search
        s = Q.pop(0)
        #Fill jug 1:
        ns = State(a, s.y,s.step + 1, s,'Fill jug 1')
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True

        #Fill jug 2:
        ns = State(s.x, b,s.step + 1, s,'Fill jug 2')
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        #Empty jug 1
        ns = State(0, s.y,s.step + 1, s,'Empty jug 1')
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        #Empty jug 2
        ns = State(s.x,0,s.step + 1,s,'Empty jug 2')
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        #Pour jug 1 to jug 2
        if s.x + s.y <= b:
            ns = State(0, s.x + s.y, s.step + 1, s, 'Pour jug 1 to jug 2')
        else:
            ns = State(s.x + s.y - b, b, s.step + 1, s,'Pour jug 1 to jug 2')
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True

        #Pour jug 2 to jug 1
        if s.x + s.y <= a:
            ns = State(s.x + s.y, 0, s.step + 1, s,'Pour jug 2 to jug 1')
        else:
            ns = State(a, s.x + s.y - a, s.step + 1, s,'Pour jug 2 to jug 1')
        if ns.finalState():
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
    
    return None


a = 6
b = 8
c = 4
solution = solve()

if solution == None:
    print('Not found')
else:
    print('Number of steps is: ', solution.step)
    s = solution
    stack = []
    while s != None:
        stack.append(s)
        s = s.parent
    
    print('Intial state', end = ' ') 
    while len(stack) > 0:
        s = stack.pop()
        print(s.action,': ',s)

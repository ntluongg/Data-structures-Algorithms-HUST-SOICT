class Node(object):
    def __init__(self,coef = 0,exp = 0):
        self.coef = coef
        self.exp = exp
        self.next = None

def printpoly(id):
	p = d[id]
	while p != None:
		print(str(p.coef)+' '+str(p.exp),end=' ')
		p = p.next
	print()

def create(poly_id):
    global d
    if poly_id in d:
        return
    d[poly_id] = None

def find_nearest_exp(f,e):
    if f == None:
        return f
    p = f
    while p.next is not None:
        if p.next.exp <= e:
            break
        p = p.next
    return p

def addterm(poly_id, coef, exp):
    global d
    if poly_id not in d:
        create(poly_id)
    if d[poly_id] == None:
        d[poly_id] = Node(coef, exp)
        return

    first = d[poly_id]
    q = Node(coef, exp)
    
    if first.exp < exp:
        q.next = first
        d[poly_id] = q
        return
    if first.exp == exp:
        first.coef = first.coef + coef
        return

    p = find_nearest_exp(first, exp)
    if p.next == None:
        q.next = p.next
        p.next = q
        return

    if p.next.exp == exp:
        p.next.coef = p.next.coef + coef
        return

    q.next = p.next
    p.next = q
    return

def evaluate(id ,value):
    if d[id] == None:
        return 0
    sum = 0
    p = d[id]
    while p!= None:
        sum = sum + p.coef*(value**p.exp)
        p = p.next
    return sum

def addpoly(id1, id2, id3):
    create(id3)
    p = d[id1]
    while p != None:
        addterm(id3, p.coef, p.exp)
        p = p.next
    
    p = d[id2]
    while p != None:
        addterm(id3, p.coef, p.exp)
        p = p.next
    return

def destroy(id):
    global d
    del d[id]

d = dict()

while True:
    l = str(input())
    if l != '*':
        c = l.split()
        if c[0] == 'AddTerm':
            addterm(int(c[1]),int(c[2]),int(c[3]))
        elif c[0] == 'Create':
            create(int(c[1]))
        elif c[0] == 'AddPoly':
            addpoly(int(c[1]),int(c[2]),int(c[3]))
        elif c[0] == 'EvaluatePoly':
            s = evaluate(int(c[1]),int(c[2]))
            print(s)
        elif c[0] == 'PrintPoly':
            printpoly(int(c[1]))
        else:
            destroy(c[1])
    else:
        break

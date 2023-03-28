def match(o,c):
    if o == '(' and c==')':
        return True 
    if o == '[' and c==']':
        return True 
    if o == '{' and c=='}':
        return True 
    return False 

def checkParenthesis(I):
    s = []
    for o in I:
        if o=='(' or o=='[' or o=='{':
            s.append(o)
        else:
            if len(s) == 0:
                return False
            p = s.pop() 
            if match(p,o):
                continue
            else:
                return False
    return len(s) == 0

#L = '[]({}){}()((())))'
L = str(input())
if checkParenthesis(L):
    print(1)
else:
    print(0)
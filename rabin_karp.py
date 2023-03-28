def input(filename):
    with open(filename, 'r') as f:
        P = f.readline()
        T = f.readline()
        P = P.strip()
        T = T.strip()
        return P,T

def RabinKarp(P, T):
    cnt = 0
    N = len(T)
    M = len(P)
    e = Exp(d, M-1)
    codeP = h(P)
    codeT = h1(T, 0, M-1)
    for s in range(N-M+1):
        if codeP == codeT:
            ok = True
            for j in range(M):
                if P[j] != T[j+s]:
                    ok = False
                    break
            if ok:
                cnt +=1 
                print('found occurence at position',s)
        if s < N-M:
            codeT = (codeT - ord(T[s])*e)*d + ord(T[s+M])
            codeT = int(codeT%Q)
    return cnt

def h(P):
# return the hashCode of the key k 
    code = 0
    for i in range(len(P)):
        code = code*d + ord(P[i])
        code = code % Q
    return code

def h1(s, start, end):
    code = 0
    for i in range(start, end+1):
        code = code*d + ord(s[i])
        code = code % Q
    return code

def Exp(x,n): #compute x^n mod Q
    if n == 0:
        return 1
    if n == 1:
        return x % Q
    r = Exp(x, n//2)
    r = (r*r)%Q
    if n%2 == 1:
        return (r*x)%Q
    return r

P, T = input('string-matching.txt')
d = 256
Q = 1e9
print(RabinKarp(P,T))
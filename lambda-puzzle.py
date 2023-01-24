n = int(input())
D = [input().split() for _ in range(n)]
 
OP = {
    "ADD": (lambda x, y: x + y),
    "SUB": (lambda x, y: x - y),
    "MULT": (lambda x, y: x * y),
    "VALUE":( lambda x, y: x)
}
 
def s2int(D, s):
    if s == "_":
        return '_'
    if "$" not in s:
        return int(s)
    else:
        return val(D, int(s[1:]))
 
V=[None]*n
 
def val(D, i):
    if V[i] is not None:
        return V[i]
    op, u, v = D[i]
    x = s2int(D, u)
    y = s2int(D, v)
    V[i] = OP[op](x, y)
    return V[i]
 
for i in range(n):
    print(val(D,i)
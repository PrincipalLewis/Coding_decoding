def code(n):
    res = []
    ver = analys(n)
    q = [0]
    delt = [ver[0][1]/2]
    for i in range(1,len(ver)):
        q += [q[i-1]+ver[i-1][1]]
        delt += [q[i] + ver[i][1]/2]


    return delt,q


def analys(n):
    res = []
    x = len(n)
    while len(n) > 0:
        res = findplus(res,n[0])
        n = n[1:]
    return mdel(res,x)

def commul(n):
    res = []
    x = 0
    for i in range(0,len(n)):
        res += [n[i][1] + x]
        x += n[i][1]
    return res

def findplus(n,x):
    res = n
    i = 0
    while len(n) > 0:
        if n[0][0] == x:
            res[i][1] += 1
            return res
        n = n[1:]
        i += 1
    res += [[x,1]]
    return res

def mdel(n,x):
    for el in range(0,len(n)):
        n[el][1] = n[el][1]/x
    return n
print(code("aqqqqqqbbb"))
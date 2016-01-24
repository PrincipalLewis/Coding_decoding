from itertools import chain
def endcode(n):
    res = scode(n)
    res2 = []
    hel = (analys(n))
    x = len(commul(analys(n)))
    while len(res) != x:
        res = listmerge1(res)
    for el in range(0,x):
        res2 += [[hel[el][0],res[el]]]
    return res2

def code(n,x):
    if len(n) == 0:
        return []
    if len(n) == 1:
        return ["1"+x]
    if len(n) == 2:
        return ["1"+x,"0"+x]
    res = delpop(n)
    return [code(res[0],"1"+x),code(res[1],"0"+x)]

def scode(n):
    res = delpop(commul(analys(n)))
    return [code(res[0],"1"),code(res[1],"0")]

def analys(n):
    res = []
    x = len(n)
    while len(n) > 0:
        res = findplus(res,n[0])
        n = n[1:]
    return sorted(mdel(res,x),key = lambda x: x[1])

def listmerge1(lstlst):
    all=[]
    for el in range(0,len(lstlst)):
        if type(lstlst[el]) == list:
            for el2 in range(0,len(lstlst[el])):
                all += [lstlst[el][el2]]
        else:
            all += [lstlst[el]]
    return all

def delpop(n):
    x = mpop(n)
    res1 = []
    res2 = []
    for z in range(0,x):
        res1 += [n[z]]
    for i in range(x,len(n)):
        res2 += [n[i]]
    return [res1,res2]

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

def mpop(n):
    res = len(n)
    res1 = 0
    for i in range(0,len(n)):
        if abs(n[i] - (n[0]+n[-1])/2) < res:
            res1 = i
            res = abs(n[i] - (n[0]+n[-1])/2)
    return res1
def find(n,x):
    while len(n) > 0:
        if n[0][1] == x:
            return n[0][0]
        n = n[1:]
    return False
def decode(n,x):
    res = ""
    while len(x) > 0:
        flag = True
        i = 0
        while flag:
            if find(n,x[0:i]) != False:
                res += find(n,x[0:i])
                flag = False
            i += 1
        x = x[i-1:]
    return res

print(endcode("abc"))
print (decode(endcode("abc"),"11100000111000"))
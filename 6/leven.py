def bin2dec(n):
    i = 1
    res = 0
    while len(n) != 0:
        if n[-1] == "1":
            res += i
        i *= 2
        n = n[0:-1]
    return res

def bin(n,ind):
    if ind == 0:
        if n == 1:
            return "1"
        elif n == 0:
            return "0"
        else:
            return bin(n//2,0)+bin(n%2,0)
    else:
        return bin(n,0)[1:]

def repl(n,el):
    res = ""
    while n != 0:
        res += el
        n -= 1
    return res

def lev(n):
    x = iter(n)
    k = bin(n,1)
    m = len(k)
    while x != 0:
        k = bin(m,1) + k
        m = len(bin(m,1))
        x -= 1
    return repl(iter(n),"1") + "0" + k

def iter(n):
    i = 0
    while n != 0:
        n = len(bin(n,1))
        i += 1
    return i

def delev(n):
    c = findzero(n)
    if c == 0:
        return 0
    else:
        k = n[c+1:]
        c -= 1
        res = 1
        while c != 0:
            z = k[0:res]
            k = k[res:]
            z = "1"+z
            res = bin2dec(z)
            c -= 1
        return res

def findzero(n):
    i = 0
    while n[0] != "0":
        n = n[1:]
        i += 1
    return i


print(delev(lev(50012)))

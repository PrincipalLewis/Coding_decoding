def bin2dec(n):
    i = 1
    res = 0
    while len(n) != 0:
        if n[-1] == "1":
            res += i
        i *= 2
        n = n[0:-1]
    return res

def glev(n):
    k = bin(n)[::-1]
    res = ""
    f = True
    while len(k) != 1:
        if f :
            res += "0"
            f = False
        else:
            res += k[0]
            k = k[1:]
            f = True
    res += "1"
    return res


def bin(n):
    if n == 1:
        return "1"
    elif n == 0:
        return "0"
    else:
        return bin(n//2)+bin(n%2)


def deglev(n):
    f = True
    res = ""
    while len(n) != 0:
        if f:
            n = n[1:]
            f = False
        else:
            res += n[0]
            n = n[1:]
            f = True
    res += "1"
    res = res[::-1]
    return bin2dec(res)

print(deglev(glev(547)))

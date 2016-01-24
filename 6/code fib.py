def code (n):
    i = 0
    res = []
    res2 = []
    while n != 0:
        res += [fib(n)[1]]
        n -= fib(n)[0]
    i = 0
    while len(res) != 0:
        if res[-1:][0] == i+1:
            res2 += [1]
            res = res[0:-1]
        else:
            res2 += [0]
        i += 1
    return res2+[1]

def decod(n):
    i = 0
    i1 = 1
    i2 = 1
    i3 = 0
    res = 0
    n = n[0:-1]
    while len(n) != 0:
        if n[0] == 1:
           res += i2
        i3 = i2
        i2 = i1 + i2
        i1 = i3
        n = n[1:]
    return res


def fib(n):
    i1 = 1
    i2 = 2
    i3 = 0
    i = 1
    while n >= i2:
       i3 = i2
       i2 = i1 + i2
       i1 = i3
       i += 1
    return [i1,i]

print (decod(code(550)))
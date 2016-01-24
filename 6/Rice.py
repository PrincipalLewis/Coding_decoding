import math


def dec2un(n):
    if n == 0:
        return "0"
    else:
        return "1" + dec2un(n - 1)


def logupdown(arg, type):
    if type == 0:  # down
        return int(math.log(arg, 2) // 1)
    else:  # up
        return int(math.ceil(math.log(arg, 2)))


def bin(n):
    if n < 2:
        return str(n)
    else:
        return bin(n // 2) + bin(n % 2)


def replicate(el, length):
    retlst = ""
    while length > 0:
        retlst += el
        length -= 1
    return retlst


def golomb(n, m):
    if abs(math.log(m, 2)) % 1 < 0.00000001:
        dost = replicate("0", math.log(m, 2) - len(finderone(bin(n % m))))
        return dec2un(n // m) + dost + finderone(bin(n % m))
    else:
        r = n % m
        b = logupdown(m, 1)
        if r < (2 ** b - m):
            dost = replicate("0", b - 1 - len(bin(r)))
            # print("1", r,dost)
            return dec2un(n // m) +dost + bin(r)
        else:
            dost = replicate("0", b - len(bin(int(r + 2 ** b - m))))
            # print ("2", r + 2 ** b - m), b
            return dec2un(n // m) +dost + bin(int(r + 2 ** b - m))

def finderone(n):
    while len(n) != 0:
        if n[0] == "1":
            return n
        n = n[1:]
    return n

for l in range(0,17):
    print()
    for i in range(1,9):
        print(golomb(l, i),replicate(" ",17-len(golomb(l, i)))),


print(golomb(8,8))


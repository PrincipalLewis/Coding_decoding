import math


def dec2Bin(n):
    if n < 2:
        return str(n)
    else:
        return str(dec2Bin(n // 2)) + str(n % 2)


def dec2un(n):
    return str(replicate(n, '1') + '0')


def logupdown(arg, type):
    if type == 0:  # down
        return int(math.log(arg, 2) // 1)
    else:  # up
        return int(math.ceil(math.log(arg, 2)))


def replicate(length, char):
    string = "";
    for i in range(0, length):
        string += str(char)
    return string


def golExp(n, k):
    w = 1 + n // (2 ** k)
    f = logupdown((1 + n // (2 ** k)), 0)
    print(f)
    z1 = dec2un(f)
    z2 = (((dec2Bin(w))[::-1])[:f])[::-1]
    z = (dec2Bin(n))[::-1]
    if k < len(z):
        z3 = (z[:k])[::-1]
    else:
        z3 = replicate(k - len(z), '0') + (z[:k])[::-1]
    return z1 + "|" + z2 + "|" + z3


print(golExp(15, 2))

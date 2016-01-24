def dec2Bin(n):
    if n < 2:
        return n
    else:
        return str(dec2Bin(n // 2)) + str(dec2Bin(n % 2))


def bin2dec(binstr):
    if len(binstr) == 0:
        return 0
    else:
        return int(binstr[-1]) + 2 * bin2dec(binstr[:-1])


def omega(n):
    if n == 1:
        return ""
    else:
        return str(omega(len(dec2Bin(n)) - 1)) + str(dec2Bin(n))


def codeOmega(n):
    if n == 0:
        return "Bad Code"
    else:
        return omega(n) + "0"


def decOmega(string, n):
    if string[0] == "0":
        return n
    else:
        return decOmega(string[n + 1:], bin2dec(string[:n + 1]))


def decodeOmega(string):
    return decOmega(string, 1)


print(codeOmega(50), decodeOmega(codeOmega(50)))

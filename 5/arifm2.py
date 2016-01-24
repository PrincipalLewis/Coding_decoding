def filt(a, x):
    if len(a) == 0:
        return []
    elif a[0] < x:
        return [a[0]] + filt(a[1:], x)
    else:
        return filt(a[1:], x)


def dec(code, p, k):
    if k == 0:
        return []
    else:
        return [len(filt(p, code))] + dec(
            decode([p[-1 + len(filt(p, code))], p[len(filt(p, code))]], code), p,
            (k - 1))

def decq(code, p, k,l):
    if k == 0:
        print(l)
        return []
    else:
        return [len(filt(p, code))] + decq(
            decode([p[-1 + len(filt(p, code))], p[len(filt(p, code))]], code), p,
            (k - 1),(l+[code]))


def decl(code, p,l):
    if p[-1 + len(filt(p, code))] <= code < p[len(filt(p, code))]:
        return []
    else:
        return [len(filt(p, code))] + decl(
            decode([p[-1 + len(filt(p, code))], p[len(filt(p, code))]], code), p,
            (l+[decode]))


def decode(a, x):
    return (x - a[0]) / (a[1] - a[0])


def restore(a, x):
    if len(x) == 0:
        return ""
    else:
        return str(a[x[0]-1]) + restore(a, x[1:])

ar=['a','b','c','d']
print(decq(0.52, [0.0, 0.6, 0.9, 1.0],4,[]))
# print filt([['a', 0.6], ['b', 0.3], ['c', 0.1],['',0]],0.3)

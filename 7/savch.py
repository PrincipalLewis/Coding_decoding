def code(alp,word):
    res = []
    while len(word) != 0:
        res += [1 + alp.index(word[0])]
        alp = alp[-1:] + alp[0:-1]
        word = word[1:]
    return res

def decode(alp,code):
    res = ""
    while len(code) != 0:
        res += alp[code[0]-1]
        alp = alp[-1:] + alp[0:-1]
        code = code[1:]
    return res


print(decode(["a","b","d","k","r"],code(["a","b","d","k","r"],"abrakadabra")))
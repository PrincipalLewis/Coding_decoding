def code(list,word):
    res=[]
    while len(word) > 0:
        res.append(1+list.index(word[0]))
        list.remove(word[0])
        list = [word[0]]+list
        word = word[1:]
    return  res

def decode(list,code):
    res = ""
    while len(code) > 0:
        sym = list[code[0]-1]
        res = res + sym
        list.remove(sym)
        list = [sym]+list
        code = code[1:]
    return res

print (code(["a","b","d","k","r"],"abrakadabra"))
print (decode(["a","b","d","k","r"],[1, 2, 5, 3, 5, 2, 5, 2, 5, 5, 3]))
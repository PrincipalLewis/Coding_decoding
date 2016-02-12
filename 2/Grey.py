
aaaaa
# print 'insert value'
# a=n=int(raw_input())
a = n = 10
print(str(bin(a)))
intToBin = str(bin(n))[2:]
# intToBin='1110010' # 305str in LR-16
greyanswer = ''
greyanswer += intToBin[0]
for i in range(1, len(intToBin)):
    greyanswer += xorit(intToBin[i - 1], intToBin[i])

print(a, 'in bin=', intToBin, 'in grey=', greyanswer)

antigrey = ''
antigrey += greyanswer[0]
for i in range(1,len(greyanswer)):
    antigrey += xorit(antigrey[i-1],greyanswer[i])

print(greyanswer, 'in bin=', antigrey,'in 10=',int(antigrey, 2))

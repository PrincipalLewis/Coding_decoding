# print 'Insert value for Fib'
# a = currvalue = int(raw_input())
a = currvalue = 34
fiblist = [1, 1, 2]
i = 2
while fiblist[i] <= currvalue:
    i += 1
    fiblist.append(fiblist[i - 1] + fiblist[i - 2])

print(1, fiblist, len(fiblist))
print(2, i)
print(3, currvalue)
fibanswer = ''
for k in range(i - 1, 0, -1):
    if fiblist[k] <= currvalue:
        fibanswer += '1'
        currvalue -= fiblist[k]
    else:
        fibanswer += '0'

print('answer:', a, '=', fibanswer, 'F')

to10 = 0

for i in range(0, len(fibanswer)):
    print(len(fibanswer) - i, fiblist[len(fibanswer) - i], '*', int(fibanswer[i]))
    to10 += fiblist[len(fibanswer) - i] * int(fibanswer[i])

print(fibanswer, 'F=', to10)

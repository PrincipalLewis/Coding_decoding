# print 'insert value'
# a=n=int(raw_input())
a = n = 6
unarnanswer = ''
while n != 0:
    unarnanswer += '1'
    n -= 1
unarnanswer += '0'
print(a, 'in unarn system=',unarnanswer)

# print 'insert unarn value'
# unarnanswer=str(raw_input())
# unarnanswer='00'

if unarnanswer.count('0')!=1:
    print('Error ')
    exit(1)

print(unarnanswer,'in 10=',len(unarnanswer)-1)
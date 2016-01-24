import math

# print 'insert value'
# a= n=int(raw_input())
a = n = 59
k = 2
factanswer = ''
while True:
    print(n, k)
    factanswer = str(n % k) + factanswer
    n = (n - n % k) / k
    k += 1
    if k >= n:
        factanswer = str(n % k) + factanswer
        break

print(a, '=', factanswer)
k = 1
to10 = 0
# print 'insert factorial value'
# factanswer=str(raw_input())
for i in range(len(factanswer) - 1, -1, -1):
    to10 += int(factanswer[i]) * math.factorial(k)
    print(int(factanswer[i]), '*', math.factorial(k), '=', to10)
    k += 1

print(factanswer, '=', to10)

#WAP to calculate the sum of digits of a random three-digit number.
#Important to use "from random import random " because without it random() may not work.

from random import random

n= random()*1000
n = int(n)
print(n)

a = n//100
b = (n//10)%10
c = n%10
print(a+b+c)



#############################################################


lis1 = list(str(n))
# print(lis1)
a1=0
for i in lis1:
    a1 += int(i)
print(a1)
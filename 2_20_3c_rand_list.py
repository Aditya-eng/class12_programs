# WAP or function that fills a list with numbers.

from random import randint

def fill_list(lst,limit_num,low,high):
    for i in range(limit_num):
        lst.append(randint(low,high))
minimum = int(input("Min: "))
maximum = int(input("Max: "))
n = int(input("NUmber list: "))
a=[]

fill_list(a,n,minimum,maximum)
print(a)
def CountEvenOdd(mytuple) :
    counteven = 0
    countodd = 0
    for i in mytuple:
        if i % 2==0:
            counteven += 1
        else:
            countodd += 1
    return counteven, countodd  # return multiple values
mytuple=()
n = int(input("Enter how many numbers :"))
for i in range(n) :
    num = int(input("Enter any number :"))
    mytuple = mytuple + (num,)
eocount = CountEvenOdd(mytuple) #eocount will also be a tuple
print("Even Counts are :",eocount[0]," Odd Counts are :",eocount[1])
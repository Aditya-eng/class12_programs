#To input elements in a tuple and pass it to a function to determine the total
#number of even and odd number in it.

def countEvenOdd(tup):
    counteven = 0
    countodd = 0
    for i in tup:
        if i%2 == 0:
            counteven +=1
        else:
            countodd +=1
    return counteven,countodd

tup1 = ()
n = int(input("Enter the total elemnts in a tuple: "))
for i in range(n):
    num = int(input("enter the number: "))
    tup1 = tup1 + (num,)
count_stats = countEvenOdd(tup1)
print("Even numbers are:",count_stats[0])
print("Odd numbers are: ",count_stats[1])


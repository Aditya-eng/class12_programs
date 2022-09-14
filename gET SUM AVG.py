def GetSum_average(mylist):
    sum = 0
    for  i in mylist:
        sum+=1
    avg = sum/len(mylist)
    return sum,avg
mylist =[]
n = int(input("ENTER HOW MANY NUMBERS: "))
for i in range(n):
    num = int(input("ENTER ANY NUMBER: "))
    mylist.append(num)
print(mylist)
sumavg = GetSum_average(mylist)
print("Sum = ",sumavg[0],"average: ",sumavg[1])

#Passing a list to a fuctnion and just double each value
def DoubleIt(mylist):
    for i in range(len(mylist)):
        mylist[i]  = mylist[i]*2


mylist = [10,20,30,40,50,60,70,80,90]
DoubleIt(mylist)
print("Ouput list is kindly: ",mylist)

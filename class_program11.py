def check(num):
    print("********************************")
    print("value in function check() ",num)
    print("ID OF NUM IS: ",id(num))
    num+=10
    print("Value of function check() ",num)
    print("ID OF NUM: ",id(num))
    print("*****************************")

myvalue = 100
print("value in main functio nis: ",myvalue)
print("ID is :",id(myvalue))
check(myvalue)
print("value in main functio nis: ",myvalue)
print("ID is :",id(myvalue))
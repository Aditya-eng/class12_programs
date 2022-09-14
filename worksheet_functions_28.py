def Fun1(num1):
    num1*=2
    num1 = Fun2(num1)
    return num1
def Fun2(num1):
    num1 = num1 // 2
    return num1
n = 120
n = Fun1(n)
print(n)
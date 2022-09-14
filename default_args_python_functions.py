from calendar import c


def drawline(symb="$", times = 20):
	for x in range(times):
		print(symb,end="")

	print()

drawline()
drawline("@")
drawline("1dasdf",30)
print("-------------------------------------------------------")
drawline(times=3223,symb="whats up bro! ")
print("-------------------------------------------------------")


def convertbinoct(num,base=2):
	str1 = ''
	while num != 0:
		str1 = str1 + str(num%base)
		num = num//base
	str1 =str1 [::-1]
	print(str1)

num = int(input("Enter any number: "))
print("This is the decimal to binary----------")
convertbinoct(num)
print("------------------------------")
print("And this is decimal to octal._______----------------")
convertbinoct(num,8)

print("---------------------------")

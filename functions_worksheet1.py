# must be followed by
# 2 keyword is used to define a function
# 3 Function will perform its action only when it is
# 4 Write statement to call the function.
# def Add():
# X = 10 + 20
# print(X)
# #statement to call the above function
#
# 5 Write statement to call the function.
# def Add(X,Y):
# Z = X+Y
# print(Z)
# #statement to call the above function
#
# 6 Write statement to call the function.
# def Add(X,Y):
# Z = X+Y
# return Z
# #statement to call the above function
#
# print(“Total =”,C)
# 7 Which Line Number Code will never execute?
# def Check(num): #Line 1
# if num%2==0: #Line 2
# print("Hello") #Line 3
# return True #Line 4
# print("Bye") #Line 5
# else: #Line 6
# return False #Line 7
#
# C = Check(20)
# print(C)
# 8 What will be the output of following code?
# def Cube(n):
# print(n*n*n)
# Cube(n) # n is 10 here
# print(Cube(n))
# 9 What are the different types of actual arguments in function? Give example of any one
# of them.
# 10 What will be the output of following code:
# def Alter(x, y = 10, z=20):
# sum=x+y+z
# print(sum)
# Alter(10,20,30)
# Alter(20,30)
# Alter(100)
#
# 2 | P a g e
# 11 Ravi a python programmer is working on a project, for some requirement, he has to
# define a function with name CalculateInterest(), he defined it as:
# def CalculateInterest(Principal,Rate=.06,Time):
# # code
# But this code is not working, Can you help Ravi to identify the error in the above
# function and what is the solution.
# 12 Call the given function using KEYWORD ARGUMENT with values 100 and 200
# def Swap(num1,num2):
# num1,num2=num2,num1
# print(num1,num2)
# Swap( , )
# 13 Which line number of code(s) will not work and why?
# def Interest(P,R,T=7):
# I = (P*R*T)/100
# print(I)
# Interest(20000,.08,15) #Line 1
# Interest(T=10,20000,.075) #Line 2
# Interest(50000,.07) #Line 3
# Interest(P=10000,R=.06,Time=8) #Line 4
# Interest(80000,T=10) #Line 5
# 14 What will be the output of following code?
# def Calculate(A,B,C):
# return A*2, B*2, C*2
# val = Calculate(10,12,14)
# print(type(val))
# print(val)
# 15 What is Local Variable and Global Variables? Illustrate with example
# 16 What will be the output of following code?
# def check():
# num=50
# print(num)
# num=100
# print(num)
# check()
# print(num)
# 17 What will be the output of following code?
# def check():
# global num
# num=1000
# print(num)
# num=100
# print(num)
# check()
# print(num)
#
# 3 | P a g e
# 18 What will be the output of following code?
# print(“Welcome!”)
# print(“Iam “, name ) # is double underscore
# 19 Function can alter only Mutable data types? (True/False)
# 20 A Function can call another function or itself? (True/False)
# 21 What will be the output of following code?
# def display(s):
# l = len(s)
# m=""
# for i in range(0,l):
# if s[i].isupper():
# m=m+s[i].lower()
# elif s[i].isalpha():
# m=m+s[i].upper()
# elif s[i].isdigit():
# m=m+"$"
# else:
# m=m+"*"
#
# print(m)
# display("EXAM20@cbse.com")
# 22 What will be the output of following code?
#
# def Alter(M,N=50):
# M = M + N
# N = M - N
# print(M,"@",N)
# return M
# A=200
# B=100
# A = Alter(A,B)
# print(A,"#",B)
# B = Alter(B)
# print(A,’@’,B)
#
# 23 What will be the output of following code?
#
# def Total(Number=10):
# Sum=0
# for C in range(1,Number+1):
# if C%2==0:
# continue
# Sum+=C
# return Sum
# print(Total(4))
# print(Total(7))
# print(Total())
#
# 4 | P a g e
# 24 What will be the output of following code?
# X = 100
# def Change(P=10, Q=25):
# global X
# if P%6==0:
# X+=100
# else:
# X+=50
# Sum=P+Q+X
# print(P,'#',Q,'$',Sum)
# Change()
# Change(18,50)
# Change(30,100)
# 25 What will be the output of following code?
# a=100
# def show():
# global a
# a=200
# def invoke():
# global a
# a=500
# show()
# invoke()
# print(a)
# 26 What will be the output of following code?
# def drawline(char='$',time=5):
# print(char*time)
# drawline()
# drawline('@',10)
# drawline(65)
# drawline(chr(65))
# 27 What will be the output of following code?
# def Updater(A,B=5):
# A = A // B
# B = A % B
# print(A,'$',B)
# return A + B
# A=100
# B=30
# A = Updater(A,B)
# print(A,'#',B)
# B = Updater(B)
# print(A,'#',B)
# A = Updater(A)
# print(A,'$',B)
#
# 5 | P a g e
# 28 What will be the output of following code?
# def Fun1(num1):
# num1*=2
# num1 = Fun2(num1)
# return num1
# def Fun2(num1):
# num1 = num1 // 2
# return num1
# n = 120
# n = Fun1(n)
# print(n)
# 29 What will be the output of following code?
# X = 50
# def Alpha(num1):
# global X
# num1 += X
# X += 20
# num1 = Beta(num1)
# return num1
# def Beta(num1):
# global X
# num1 += X
# X += 10
# num1 = Gamma(num1)
# return num1
# def Gamma(num1):
# X = 200
# num1 += X
# return num1
# num = 100
# num = Alpha(num)
# print(num,X)
# 30 What will be the output of following code?
# def Fun1(mylist):
# for i in range(len(mylist)):
# if mylist[i]%2==0:
# mylist[i]/=2
# else:
# mylist[i]*=2
# list1 =[21,20,6,7,9,18,100,50,13]
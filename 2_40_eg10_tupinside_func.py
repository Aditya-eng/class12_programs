#Passing immutable tuple to a function

def funct(A):
    A = list(A)  #tupel converted to a list
    A[0] = A[0] + 2
    A[1] = A[1] + 10
    print("value inside the function: ",A)
tup=(100,200)
print(tup)


funct(tup)
print(tup)
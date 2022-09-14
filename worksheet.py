def Alter(M,N=50):
    M = M + N
    N = M - N
    print(M,"@",N)
    return M
A=200
B=100
A = Alter(A,B)
print(A)
print(A,"#",B)
B = Alter(B)
print(A,"@",B) 
def PrintDiagonal(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
                if i==j:
                    print(mylist[i][j],end = '\t')
                else:
                    print('\t',end = '')
        print()


mymatrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
PrintDiagonal(mymatrix)
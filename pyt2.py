#
# def Total(Number = 10):
#     Sum = 0
#     for c in range(1,Number+1):
#         if c%2==0:
#             continue
#         Sum +=c
#     return Sum
#
# print(Total(4))
# print(Total(7))



x=100
def Change(P = 10,Q =25):
    global x
    if P%6 ==0:
        x+=100
    else:
        x+=50
    sum = P+Q+x
    print(P,"#", Q,"$", sum)

Change()
Change(18,50)
Change(30,100)

# a=100
# def show():
#     global a
#     a=200
# def invoke():
#     global a
#     a=500
# show()
# invoke()
# print(a)
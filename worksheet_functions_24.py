#Find the output of the following code.
X = 100
def Change(P=10, Q=25):
    global X
    if P%6==0:
        X+=100
    else:
        X+=50
    Sum=P+Q+X
    print(P,'#',Q,'$',Sum)
Change()
Change(18,50)
Change(30,100)
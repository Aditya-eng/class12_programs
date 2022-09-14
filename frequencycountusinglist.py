#WAP to pass a dictionary with list and to store the value of
# list as key and its frequcny or no. of occurence as values
def frequencyCount(mylist,myd):
    for i in mylist:
            if i not in myd:
                myd[i] = 1
            else:
                myd[i] += 1
    return myd
mylist=[10,20,10,20,30,10,40,10,40]
d={}
frequencyCount(mylist,d)
print(d)
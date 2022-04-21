#WAP to perform binary search using randint()
#Binary search basically finds or searches for the object like we do in a dictionary,
# the algorithm first slices off the array in two halves
# then it searches for the object in one of the halves by comparing the first letter / type of object....
# it then ignores the half not with the
#element and repeats this slicing until it reaches the object.

from random import randint

def bin_search(lst,item):
    mid = len(lst)//2
    low = 0
    high = len(lst) -1
    while lst(mid) != item and low <= high:
        if item> lst(mid):
            low = mid+1
        else:
            high = mid-1
        mid = (low+high)//2
    if low>high:
        return None
    else:
        return mid

a=[]
for i in range(10):
    a.append(randint(1,20)) #list elements within the range gets automatically generated
a.sort() #sort() used to arrange the list elements in ascending order
print(a)

value = int(input("Enter the number to be searched: "))
#index = bin_search(a,value)
print("Elements found at the index: ",bin_search(a,value))
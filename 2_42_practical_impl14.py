#Program to pass a dictioaary to a function wiht list of elements as keys
#and frequency of its occurenece as value and return as a dictionary

def frequencyCount(list1,dict1):
    for  i in list1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] +=1
    return dict1

list1 = [4,5,6,5,10,6,5,5,40,30,2,4]
d={}
frequencyCount(list1,d)
print(d)

#passing a function into  a function
def countvowels(str1):
    count = 0
    vowels = ["a",'e','i','o','u']
    for s in str1:
        if s.lower() in vowels:
            count+=1
    return count
msg = input("Enter any string: ")
c = countvowels(msg)
print("total vowels in ",msg,'are/is',c)

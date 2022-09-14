#calculating all the details in string
def countvowels(str1):
    count = 0
    vowels = ["a",'e','i','o','u']
    for s in str1:
        if s.lower() in vowels:
            count+=1
    return count
def countdigits(str1):
    count = 0
    for s in str1:
        if s.isdigit():
            count+=1
    return count
def countspace(str1):
    count = 0
    for s in str1:
        if s == " ":
            count+=1
    return count

msg = input("Enter any string: ")
c = countvowels(msg)
d = countdigits(msg)
e = countspace(msg)
print("total vowels in ",msg,'are/is',c)
print("total digits in ",msg,'are/is',d)
print("total spaces in ",msg,'are/is',e)
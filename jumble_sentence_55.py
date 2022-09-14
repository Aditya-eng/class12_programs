#4-05-2022
#WAP to make all the specific characters in a string
def Jumble(str1):
    str2 = ""
    count = 0
    for i in range(len(str1)):
        if str1[i].islower():
            str2 = str2+str1[i].upper()
        elif str1[i].isupper():
            str2 = str2+str1[i].lower()
        elif str1[i].isdigit():
            str2 = str2 + "*"
        else:
            str2 = str2+ "@"
    return str2
msg = input("Enter Any string; ")
msg = Jumble(msg)
print("Jumbled object is",msg)
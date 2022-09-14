# data file handling program to read
# data file handling program to read
myfile = open("data.txt","r")
str1 = myfile.read(10)
str2 = myfile.read(5)
str3 = myfile.read()
print("Output of First read :")
print (str1)
print("Output of Second read :")
print(str2)
print("Output of Third read :")
print(str3)